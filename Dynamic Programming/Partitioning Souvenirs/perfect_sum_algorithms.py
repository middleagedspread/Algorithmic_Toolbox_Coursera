# Python code to find the number of
# possible subset with given sum
def f(pat, i, currSum):
    global cnt, n, sum
    if (currSum == sum):
        cnt += 1
        return
    if (currSum < sum and i < n):
        f(pat, i + 1, currSum + pat[i])
        f(pat, i + 1, currSum)

# driver code
cnt = 0
n = 6
sum = 10

pat = [2, 3, 5, 6, 8, 10]
f(pat, 0, 0)

print(cnt)
