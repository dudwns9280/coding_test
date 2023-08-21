def solution(priorities, location):
    excute_count = 0

    while True:
        cur_data = priorities.pop(0)
        last_index = len(priorities)

        if priorities and cur_data < max(priorities):
            priorities.append(cur_data)
        else:
            excute_count += 1
            if location == 0:
                break

        if location == 0:
            location = last_index
        else:
            location -= 1
    return excute_count

