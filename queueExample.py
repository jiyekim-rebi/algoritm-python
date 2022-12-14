# FIFO(First In First Out)

def put(item):
    queue.append(item)

def get():
    return queue.pop()

if __name__ == "__main__":
    queue = []
    put(1)
    put(2)
    put(3)
    put(4)

    print("현재 queue의 모습")
    print(queue)

    while queue:
        print("pop > {}".format(get()))