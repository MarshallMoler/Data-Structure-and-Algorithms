# coding:utf-8
class Stack(object):
    '''栈'''
    def __init__(self):
        self.__list=[]

    def push(self,elem):
        self.__list.append(elem)

    def pop(self):
        '''出栈'''
        return self.__list.pop(-1)

    def peek(self):
        '''返回栈顶元素'''
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        '''判空'''
        return self.__list == []

    def size(self):
        '''返回栈的元素个数'''
        return len(self.__list)


if __name__ == "__main__":
    s = Stack()
    s.push(0)
    s.push(5)
    s.push(10)
    s.push(6)
    s.push(8)
    a =  s.peek()
    print(a)
