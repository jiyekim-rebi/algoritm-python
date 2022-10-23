from numpy.ma import stack

def push(item):
    stack.append(item)

def pop():
    return stack.pop()


if __name__=="__main__":
    stack=[]

    push(1)
    push(2)
    push(3)
    print(stack)

    pop()
    print(stack)
