def solution(s):
    check_stack = list()

    for index in range(len(s)):
        if s[index] == '(':
            check_stack.append(s[index])
        elif s[index] == ')'and check_stack and check_stack[-1]=='(':
            check_stack.pop(len(check_stack)-1)
        else:
            return False
    if len(check_stack) > 0:
        return False
    else:
        return True


print(solution(")()("))
