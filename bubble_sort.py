#coding:utf8
def bubble_sort(alist):
    '''冒泡排序'''
    n = len(alist)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
        print(f'第{i+1}次排序后的的数据为{alist}')


if __name__ == '__main__':
    alist = [16,25,39,27,12,8,45,63]
    bubble_sort(alist)
