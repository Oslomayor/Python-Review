# 出现1次的数字的和
# 给定一个数组里面有一串数字，其中有2个数字只出现了1次，
# 剩下的数字出现2次！要求返回只出现1次的数字的和
# 比如repeats([4,5,7,5,4,8]) = 15，因为7和8数字出现1次，它的和为15
# 8:39PM, Feb 1st, 2018 @ dormitory 627
# to do:
# 1.解法一和二不健壮，出现重复多次的数字，怎么解决
import time

# 解法一
# Done
def new_sum1(nums):
    buffer=[]
    s = 0
    for num in nums:
        if num in buffer:
            s -= num
        else:
            s += num
            buffer.append(num)
    return s

# 解法二
# Done
def new_sum2(nums):
    buffer=[]
    s = 0
    for num in nums:
        if num in buffer:
            buffer.remove(num)
        else:
            buffer.append(num)
    return sum(buffer)

# 解法三
# Done
def new_sum3(nums):
    s = 0
    for num in nums:
        if nums.count(num) == 1:
            s += num
    return s
# 解法四
# Done
def new_sum4(nums):
    return sum([num for num in nums if nums.count(num) == 1])

def main():
    temp = list(input().split())
    nums=[]
    for num in temp:
        nums.append(int(num))
    time1 = time.time()
    print(new_sum1(nums))
    print(time.time()-time1)
if __name__ == '__main__':
    main()





