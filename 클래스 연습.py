
class Class1:
    def __init__(self):
        global n
        n = int(input())

    def fun(self, n):
        global ans
        ans = 0
        for i in range(100, n + 1):
            x = str(i)
            a = int(x[1]) - int(x[0])
            b = int(x[2]) - int(x[1])
            if a == b:
                ans = ans + 1
            else:
                continue
        return ans


c1 = Class1()
if n < 100:
    print(n)
elif 100 <= n <= 1000:
    print(c1.fun(n) + 99)
