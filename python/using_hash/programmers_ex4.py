def solution(clothes):
    cloth_dict = dict()
    for cloth in clothes:
        cloth_dict[cloth[1]] = cloth_dict.get(cloth[1], 0)
        cloth_dict[cloth[1]] += 1

    total_count = 1
    for kind, count in cloth_dict.items():
        total_count *= (count+1)
    total_count -= 1
    return total_count
