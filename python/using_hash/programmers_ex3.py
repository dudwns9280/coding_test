def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    for index in range(len(phone_book)-1):
        next_number = phone_book[index+1]
        if next_number[:len(phone_book[index])] == phone_book[index]:
            return False
    return True


print(solution(['118', '119', '1181', '1191', '115']))
