n = int(input("Enter value of n: "))

for i in range(n):
    if i ==0 or i == n-1:
        print("*"*n)
    else:
        print(" "*(n-i-1)+"*")
