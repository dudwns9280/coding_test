def solution(progresses, speeds):
    answer = []
    deploy_index_list = list()
    deploy_count = 0
    while len(progresses) > 0:
        length = len(progresses)
        for index in range(length):
            progresses[index] += speeds[index]

        for index in range(length):
            if progresses[index] >= 100:
                deploy_index_list.append(index)
                deploy_count += 1
            else:
                break
        if deploy_count > 0:
            answer.append(deploy_count)
            deploy_count = 0

        if deploy_index_list:
            for deploy_index in sorted(deploy_index_list, reverse=True):
                progresses.pop(deploy_index)
                speeds.pop(deploy_index)
            deploy_index_list = list()

    return answer

print(solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]))