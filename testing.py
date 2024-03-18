
def hourglassSum(arr):
    # Write your code here
    summ = []
    flat = []
    for i in arr:
        for j in i:
            flat.append(j)
    
    for i, item in enumerate(flat):
        if i >= 24 or i ==4 or i==5 or i==10 or i==11 or i==16 or i==17 or i==22 or i==23:
            continue
        else:
            hourglass_sum = sum(flat[i:i+3]) + sum(flat[i+7:i+8]) + sum(flat[i+12:i+15])
            summ.append(hourglass_sum)
    return max(summ)


arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)

print(result)