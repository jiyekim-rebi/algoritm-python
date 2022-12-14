#bubble sort algoritm
import random
import time


def bubble_sort(random_list):
    for start_index in range(len(random_list)-1):
        for index in range(1, len(random_list) - start_index):
            if random_list[index-1] > random_list[index]:
                temp = random_list[index-1]
                random_list[index-1] = random_list[index]
                random_list[index] = temp

if __name__=="__main__":
    list = []
    input_n = input("정렬할 데이터의 수: ")
    for i in range(int(input_n)):
        list.append(random.randint(1, int(input_n)))
    print("<정렬 전>")
    print(list)

    start_time = time.time()
    bubble_sort(list)
    running_time = time.time() - start_time

    print("<정렬 후>")
    print(list)

    print("실행시간 : {}".format(running_time))