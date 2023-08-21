def solution(arr):
    answer = []
    answer.append(arr[0])
    for index in range(1, len(arr)):
        if answer[-1] != arr[index]:
            answer.append(arr[index])

    return answer