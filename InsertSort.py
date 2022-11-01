# insert sort algoritm
# 순차적으로 정렬하면서 현재의 값을 정렬된 값과 비교하여 위치 삽입

import random
import time

compare_counter = 0
swap_counter = 0

def insertion_sort(my_list):
    global compare_counter, swap_counter
    my_list.insert(0, -1) #정렬할 데이터가 0보다 같거나 양수 기준으로 정렬
    for idx in range(2, len(my_list)): #첫 데이터부터 마지막 데이터까지 비교작업
        temp = my_list[idx]
        ins_idx = idx #현재 index를 변수에 별도 저장
        compare_counter += 1
        while my_list[ins_idx-1] > temp: #현재 temp값 보다 클 경우 리스트를 한칸 뒤로 이동
            swap_counter += 1
            my_list[ins_idx] = my_list[ins_idx-1]
            ins_idx = ins_idx-1

        my_list[ins_idx] = temp #temp데이터 위치 지정
    del my_list[0]

if __name__ == "__main__":
    list = []
    input_n = input("정렬할 데이터의 수 : ")
    for i in range(int(input_n)):
        list.append(random.randint(1, int(input_n)))

    print("<정렬 전>")
    print(list)

    start_time = time.time()
    insertion_sort(list)
    running_time = time.time() - start_time

    print("<정렬 후>")
    print(list)

    print("비교횟수 : {}".format(compare_counter))
    print("교환횟수 : {}".format(swap_counter))
    print("실행시간 : {}".format(running_time))