# coding:utf-8
class Queue(object):
    '''双端队列'''
    def __init__(self):
        self.__list = []

    def enqueue(self,elem):
        '''进栈'''
        self.__list.append(elem)

    def dequeue(self):
        '''出栈'''
        self.__list.pop(0)

    def is_empty(self):
        '''判空'''
        return self.__list == []

    def size(self):
        '''返回队列大小'''
        return len(self.__list)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(8)
    q.enqueue(5)
    q.dequeue()
    a=q.size()
    print(a)

        

