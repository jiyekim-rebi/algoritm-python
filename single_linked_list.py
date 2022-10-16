class SLinkedList:

    class Node:
        def __init__(self, v, n = None):
            self.value = v #저장된 데이터
            self.next = n #다음 노드를 가리키는 변수

    def __init__(self):
        self.head = None #노드가 처음 생성된다면 내부에 데이터가 없음

    #노드 신규 삽입
    def insertNode(self, v):
        #처음 노드일 경우
        if self.head is None:
            self.head = self.Node(v)
        else: #기존에 노드가 있었다면
            self.head = self.Node(v, self.head)

    #노드 삭제
    def deleteNode(self):
        #노드가 없으면 건너뛴다
        if self.head is None:
            print("삭제할 노드가 없음")
            return
        else:
            #head를 다음 노드의 데이터로 변경
            self.head = self.head.next

    #노드 조회
    def searchNode(self, v):
        #데이터가 없으면
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            link = self.head
            index = 0
            while link:
                #찾는 노드를 발견하면 인덱스 값을 리턴
                if v == link.value:
                    return index
                else:
                    link = link.next
                    index += 1

    def printNode(self):
        #데이터가 없으면
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            print("<현재 리스트 구조>")
            print()
            #처음은 헤드를 지정하고 이후부턴 현 노드의 next를 지정
            link = self.head
            while link:
                print(link.value, '->', end = ' ')
                link = link.next
            print()

if __name__=="__main__":
    sl = SLinkedList()
    sl.insertNode('1st')
    sl.insertNode('2nd')
    sl.insertNode('3rd')

    # 탐색
    print("<위치 탐색>")
    result = sl.searchNode('1st')
    print("1st의 위치: {}".format(result))

    result = sl.searchNode('555')
    print("555의 위치: {}".format(result))