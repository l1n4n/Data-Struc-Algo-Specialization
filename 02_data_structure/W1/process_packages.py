# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        # pop from the front of finish_time all the packets which are already processed by the time new packet arrives
        while self.finish_time_ != [] and self.finish_time_[0] <= request.arrival_time:
            self.finish_time_.pop(0)

        # If the buffer is full (there are already s finish times in finish_time), the packet is dropped.
        if len(self.finish_time_) >= self.size:
            return Response(True, -1)
        
        elif len(self.finish_time_) == 0:
            # process it immediately if buffer is empty
            self.finish_time_.append(request.arrival_time + request.process_time)
            return Response(False, request.arrival_time)
        else:
            # If there are other requests being processed, then wait till the one before it finished.
            # the start time would be the last one's finish time
            last_finish = self.finish_time_[-1]
            self.finish_time_.append(last_finish + request.process_time)
            return Response(False, last_finish)
            

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
