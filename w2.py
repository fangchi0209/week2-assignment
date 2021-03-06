
#要求一:函式與流程控制
#完成以下函式，在函式中​使用迴圈​計算最小值到最大值之間，所有整數的總和。

def calculate(min, max): # 請用你的程式補完這個函式的區塊
    sum=0
    for i in range (min, max+1):
        sum=sum+i
    print(sum)




calculate(1, 3) # 你的程式要能夠計算 1+2+3
calculate(4, 8) #​# 你的程式要能夠計算 4+5+6+7+8，最後印出 30


#要求二:Python 字典與列表、JavaScript 物件與陣列
#完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。

def avg(data):
# 請用你的程式補完這個函式的區塊 
    s=0
    for j in range(0,data["count"]):
        s = s + data["employees"][j]["salary"]

    print(s/data["count"])
        
avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
})


# avg({
#     "count":3,
#     "employees":[
#         {
#             "name":"John",
#             "salary":30000},
#         {
#             "name":"Bob",
#             "salary":60000},
#         {
#             "name":"Jenny",
#             "salary":50000}
#     ]
# })​
# 呼叫 avg 函式


#要求三:演算法
#找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。

def maxProduct(nums): # 請用你的程式補完這個函式的區塊
    sum=0
    l=[]
    for k in range(0, len(nums)):
        for m in range(k+1, len(nums)):
            sum=nums[k]*nums[m]
            l.append(sum)
    print(max(l))

maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])

# maxProduct([5, 20, 2, 6])​ # 得到 120 因為 20 和 6 相乘得到最大值
# maxProduct([10, -20, 0, 3])​ # 得到 30 因為 10 和 3 相乘得到最大值


#要求四 ( 請閱讀英文 ):演算法
#Given an array of integers, show indices of the two numbers such that 
# they add up to a specific target. You can assume that each input 
# would have exactly one solution, and you can not use the same element twice.

def twoSum(nums, target):
# your code here
    c=0
    for t in range(0, len(nums)):
        for u in range(t+1, len(nums)):
            c=nums[t]+nums[u]
            if c==target:
                return [t, u]

result=twoSum([2, 11, 7, 15], 9)
print(result) #show[0, 2] because nums[0]+nums[2] is 9

# result=twoSum([2, 11, 7, 15], 9)
# print(result) ​# show [0, 2] because nums[0]+nums[2] is 9



def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
    b=0
    r=0
    for x in range(0, len(nums)):
        if nums[x]==0:
            b=b+1
            r=max(r,b)
        else:
            b=0
    print(r)

maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])



# maxZeros([0, 1, 0, 0])​ # 得到 2
# maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])​ # 得到 4
# maxZeros([1, 1, 1, 1, 1])​ # 得到 0





