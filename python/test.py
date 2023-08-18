def solution(arrayA, arrayB):
    answer = 0
    arrayA_dict = dict()
    arrayA_length = len(arrayA)
    for element in arrayA:
        number_list = list()
        for number in range(1, element//2 -1):
            if element % number == 0 and number not in number_list:
                number_list.append(number)
                number_list.append(int(element/number))
                
        # for number in number_list:
        #     arrayA_dict.update(number= arrayA_dict.get(number, 0) + 1)
    arrayA_dict.pop(1)
    print(arrayA_dict)
    max_number = 0
    for key, value in arrayA_dict.items():
        if value == arrayA_length and max_number < key:
            max_number = key
    print(max_number)
        
    return answer

## 공약수를 먼저 구해야함.
## 어캐구함? 1~14까지 돌려서 근데 반까지만 하면됨.
## 최대 공약수 구하기 A 리스트와 B리스트에서 각각
## 그 후 A 리스트의 최대 공약수로 B리스트 전체나눠서 나눌수 없는지 판단 해야함
## B리스트도 마찬가지
## 둘중 더 큰 값을 return함.