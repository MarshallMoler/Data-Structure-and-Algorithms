#coding:utf8
def select_sort(alist):
    n = len(alist)
    for i in range(0,n-1):
        min_index = i
        for j in range(i+1,n):
            if alist[min_index]>alist[j]:
                min_index = j
        alist[i],alist[min_index] = alist[min_index],alist[i]
        print(f'第{i+1}次排序后的结果为:{alist}')


if __name__ == "__main__":
    alist = [16,25,39,27,12,8,45,63]
    select_sort(alist)
