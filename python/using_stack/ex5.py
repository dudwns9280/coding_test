def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for _ in range(bridge_length)]
    sum_weight = 0
    while truck_weights:
        sum_weight -= bridge.pop(0)
        if weight >= sum_weight+truck_weights[0]:
            sum_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

        time += 1
    time += bridge_length

    return time