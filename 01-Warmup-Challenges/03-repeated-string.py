#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    a_in_s = s.count('a')
    len_rep_str = n // len(s)
    len_of_remainder = n % len(s)
    a_in_remainder = s[:len_of_remainder].count('a')
    total_a = (a_in_s * len_rep_str) + a_in_remainder
    return total_a
    


s = input()

n = int(input().strip())

result = repeatedString(s, n)

print(result)