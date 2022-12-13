# 스택을 이용한 큐 구현
# https://leetcode.com/problems/implement-queue-using-stacks

# 두개의 스택을 활용한 구현
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # output이 없으면 모두 재입력처리
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]