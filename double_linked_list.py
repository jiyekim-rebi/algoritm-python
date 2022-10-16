class DLinkedList:
    
    class Node:
        def __init__(self, v, n=None, p=None):
            self.value = v    # 저장데이터
            self.next = n     # 다음노드
            self.prev = p     # 이전노드
        
    def __init__(self):
        self.head = None
        self.tail = None

    # head로 삽입하는 경우
    def insertNodeBefore(self, v):
        if self.head is None:
            self.head = self.Node(v)
            self.tail = self.head #같은 노드를 가리킴
        else:
            self.head.prev = self.Node(v, n=self.head)   #기존 노드를 이전 노드로 설정
            self.head = self.head.prev                   #새 노드를 헤드로 설정
        
            
    # tail로 삽입하는 경우
    def insertNodeAfter(self, v):
        #데이터가 없을때
        if self.tail is None:
            self.tail = self.Node(v)
            self.head = self.tail #같은 노드를 가리킴
        else:
            self.tail.next = self.Node(v, p=self.tail)
            self.tail = self.tail.next

    #head로 삭제
    def deleteNodeBefore(self):
        if self.head is None:
            print('삭제할 노드가 없습니다')
            return
        else:
            self.head = self.head.next
            self.head.prev = None

    #tail로 삭제
    def deleteNodeAfter(self):
        if self.tail is None:
            print('삭제할 노드가 없습니다')
            return
        else:
            self.tail = self.tail.prev
            self.tail.next = None


    def printNodeBefore(self):
        if self.head is None:
            print('저장된 데이터가 없음')
            return
        else:
            print('<현재 리스트 구조>', end='\t')
            link = self.head

            while link:
                print(link.value, '<->', end = ' ')
                link = link.next
            print()

    def printNodeAfter(self):
        if self.tail is None:
            print('저장된 데이터가 없음')
            return
        else:
            print('<현재 리스트 구조>', end='\t')
            link = self.tail

            while link:
                print(link.value, '<->', end = ' ')
                link = link.prev
            print()

    #head로 검색했을 때
    def searchNodeBefore(self, v):
        if self.head is None:
            print('저장된 데이터가 없음')
            return
        else:
            link = self.head
            index = 0
            while link:
                if v == link.value:
                    return index
                else:
                    link = link.next
                    index += 1
                    
    #tail로 검색했을 때
    def searchNodeAfter(self, v):
        if self.tail is None:
            print('저장된 데이터가 없음')
            return
        else:
            link = self.tail
            index = 0
            while link:
                if v == link.value:
                    return index
                else:
                    link = link.prev
                    index -= 1 #위치값 1감소: 역행해야 함

if __name__=="__main__":
    dl = DLinkedList()
    dl.insertNodeBefore('1stF')
    dl.insertNodeAfter('1stB')
    dl.insertNodeBefore('2ndF')
    dl.insertNodeAfter('2ndB')
    dl.printNodeBefore()
    dl.deleteNodeBefore() #head 삭제
    dl.printNodeBefore()
    dl.deleteNodeAfter() #tail 삭제
    dl.printNodeAfter()