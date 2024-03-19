
# def hourglassSum(arr):
#     # Write your code here
#     summ = []
#     flat = []
#     for i in arr:
#         for j in i:
#             flat.append(j)
    
#     for i, item in enumerate(flat):
#         if i >= 24 or i ==4 or i==5 or i==10 or i==11 or i==16 or i==17 or i==22 or i==23:
#             continue
#         else:
#             hourglass_sum = sum(flat[i:i+3]) + sum(flat[i+7:i+8]) + sum(flat[i+12:i+15])
#             summ.append(hourglass_sum)
#     return max(summ)


# arr = []

# for _ in range(6):
#     arr.append(list(map(int, input().rstrip().split())))

# result = hourglassSum(arr)

# print(result)











# def minimumBribes(q):
#     # Write your code here
#     bribeCount = 0
#     bc = []
#     flag = True
#     originalPos = list(range(1, (len(q)+1)))
#     for i in q:
#         for j in originalPos:
#             diff = i - j
#             if diff <= 0:
#                 continue
#             elif diff >= 3:
#                 flag = False
#                 # break
#             else:
#                 bribeCount += diff
#                 bc.append(diff)
                
#     # if flag == False:
#     #     print('Too chaotic')
#     # else:
#     #     print(bribeCount)
#     print(bc)
#     print(bribeCount)
                
        
# q = [2, 1, 5, 3, 4]        
# minimumBribes(q)

















from collections import Counter
def makeAnagram(a, b):
    # Write your code here
    chrCount = 0
    x = Counter(a)
    y = Counter(b)
    for i in x.keys():
        if i in y.keys():
            if x[i] == y[i]:
                continue
            else:
                chrCount += abs(x[i] - y[i])
        else:
            chrCount += x[i]

    for i in y.keys():
        if i in x.keys():
            if y[i] == x[i]:
                continue
            else:
                chrCount += abs(y[i] - x[i])
        else:
            chrCount += y[i]
            
    
    
    return x,y

if __name__ == '__main__':


    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)