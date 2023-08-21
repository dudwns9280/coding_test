def solution(prices):
    answer = []

    for index in range(len(prices)):
        down_count = 0
        for compare_index in range(index+1, len(prices)):
            if prices[index] <= prices[compare_index]:
                down_count+=1
            else:
                down_count+=1
                break
        answer.append(down_count)
    return answer