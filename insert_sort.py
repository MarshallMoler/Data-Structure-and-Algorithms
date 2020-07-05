#coding:utf-8
def insert_sort(alist):
    '''插入排序'''
    n = len(alist)
    for i in range(1,n):
        j = i
        while j > 0:
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
            j -= 1
        print(f'第{i}次排序的结果为{alist}')
    

if __name__ == "__main__":
    alist = [55,23,87,62,16]
    insert_sort(alist)
