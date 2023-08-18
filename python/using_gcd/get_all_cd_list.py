import datetime


def get_cd_list_using_1(number):
    cd_list = list()
    for num in range(1, number + 1):
        if number % num == 0 and num not in cd_list:
            cd_list.append(num)
    return cd_list


def get_cd_list_using_2(number):
    cd_list = list()
    for num in range(1, number//2-1):
        if number % num == 0 and num not in cd_list:
            cd_list.append(num)
            cd_list.append(int(number/num))
    return sorted(cd_list)


def get_cd_list_using_3(number):
    cd_list = list()
    for num in range(1, int(number**(1/2)) + 1):
        if number % num == 0:
            cd_list.append(num)
            if num ** 2 != number:
                cd_list.append(int(number/num))
    return sorted(cd_list)

print("1번 방법 실행")
start_date_time = datetime.datetime.now()
print(get_cd_list_using_1(100000))
print(datetime.datetime.now() - start_date_time)
print("1번 방법 종료")
print("2번 방법 실행")
start_date_time = datetime.datetime.now()
print(get_cd_list_using_2(100000))
print(datetime.datetime.now() - start_date_time)
print("2번 방법 종료")
print("3번 방법 실행")
start_date_time = datetime.datetime.now()
print(get_cd_list_using_3(100000))
print(datetime.datetime.now() - start_date_time)
print("3번 방법 종료")
