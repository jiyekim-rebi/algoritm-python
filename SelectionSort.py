# selection sort algoritm

import random

def selected_sort(random_list):
    for sel in range(len(random_list)-1):
        #해당 값이 최소값이라고 가정하고 backup
        min = random_list[sel]
        minindex = sel

        #최소값 찾기
        for step in range(sel+1, len(random_list)):
            #backup한 값보다 작은 값을 발견했다면 저장
            if min > random_list[step]:
                min = random_list[step]
                minindex = step

        #Swap
        random_list[minindex] = random_list[sel]
        random_list[sel] = min

if __name__ == "__main__":
    list = []
    for i in range(10):
        list.append(random.randint(1, 10))
    print("Before")
    print(list)
    selected_sort(list)
    print("After")
    print(list)