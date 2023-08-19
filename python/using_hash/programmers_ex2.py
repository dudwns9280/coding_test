import collections


# 효율성 테스트 실패.
def solution1(participant, completion):
    for man in completion:
        participant.remove(man)
    return participant[0]


def solution2(participant, completion):
    participant.sort()
    completion.sort()

    for index in range(len(completion)):
        if participant[index] != completion[index]:
            return participant[index]
    return participant[-1]


def solution_by_counter(participant, completion):
    participant_count = collections.Counter(participant)
    completion_count = collections.Counter(completion)
    answer_dict = participant_count - completion_count
    return answer_dict.keys()[0]

