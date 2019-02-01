# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = float(input())
X = input()

X = X.split(' ')
X = [int(x) for x in X]

mean = sum(X) / n

num = 0
for x in X:
    num = num + (x - mean)**2
    
std_dev = math.sqrt(num / n)
print(std_dev)

