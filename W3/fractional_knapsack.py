# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    W = capacity
    
    unit_weights = [values[i] / weights[i] for i in range(n)]
    unit_weights.sort()
    #print(unit_weights)
    unit_dict = {values[i] / weights[i] : weights[i] for i in range(n)}
    #print(unit_dict)

    for i in range(n):
        if W == 0:
            return value
        current_max_unit = unit_weights.pop()
        #print(current_max_unit)
        fill_volume = min(unit_dict[current_max_unit], W)
        #print(fill_volume)
        value += fill_volume * current_max_unit
        unit_dict[current_max_unit] -= fill_volume
        W -= fill_volume
        #print(W)

    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
