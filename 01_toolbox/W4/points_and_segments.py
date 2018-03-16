# Uses python3
import sys
import collections

# Uses python3
import sys
import collections

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    points_dict = collections.defaultdict(set)

    open_label, target_label, close_label = 1, 2, 3 

    swept_points = []
    for point in starts:
        swept_points.append((point, open_label))
    for point in ends:
        swept_points.append((point, close_label))
    for i in range(len(points)):
        point = points[i]
        swept_points.append((point, target_label))
        points_dict[point].add(i)
    swept_points.sort(key=lambda x: (x[0], x[1]))

    segments = 0
    for i in swept_points:
        if i[1] == open_label:
            segments += 1
        elif i[1] == close_label:
            segments -= 1
        else:
            p = i[0]
            for x in points_dict[p]:
                cnt[x] = segments

    return cnt



def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
