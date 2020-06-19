import sys

n = input()
min = sys.maxsize
while True:
    if n == "Stop":
        break
    num = int(n)
    if num < min:
        min = num
    n = input()
print(min)
