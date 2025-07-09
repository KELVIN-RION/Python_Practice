def RightangledTriangle(n):
    for i in range (1,n+1):
        print("*" * i)

def InverseRightangledTriangle(n):
    for i in range (n , 0, -1):
        print("*" *i)

def OutlineSquare(n):
    for i in range(n):
        if i ==0 or i == n-1:
            print("*" *n)
        else:
            print("*"+ " " * (n-2) + "*")

def Square(n):
    for _ in range(n):
        print("*" * n)

def Diamond(n):
    for i in range(1, n+1, 2):
        print(" " * ((n-i)//2) + "*" * i)
    for i in range(n-2, 0, -2):
        print(" " * ((n-i)//2) + "*" * i)

def InverseEquilateralTriangle(n):
    for i in range(n, 0, -2):
        print(" " * ((n - i)//2) + "*" * i)

def EquilateralTriangle(n):
    for i in range (n, n+1, 2):
        print(" " * ((n-i)//2) +  "*" * i )

def LeftsidebaseTriangle(n):
    for i in range(1, n+1):
        print("*" * i)
    for i in range(n-1, 0, -1):
        print("*" * i)

def OutlineEquilateralTriangle(n):
    for i in range(1, n, 2):
        spaces = (n - i) // 2
        if i == 1:
            print(" " * spaces + "*")
        else:
            print(" " * spaces + "*" + " " * (i - 2) + "*")
    print("*" * n)


def X_pattern(n):
    for i in range(n):
        line=""
        for j in range(n):
            if j == i or  j==n-i-1:
                line += "*"
            else:
                line += " "
        print(line)

def Heart(n):
    if n % 2 != 0:
        n += 1
    for i in range(n//2, n + 1, 2):
        print(" " * ((n - i)//2) + "*" * i + " " * (n - i) + "*" * i)
    for i in range(n, 0, -2):
        print(" " * ((n - i)//2) + "*" * i)



n = 5  # or any desired odd/even number

RightangledTriangle(n)
print()
InverseRightangledTriangle(n)
print()
OutlineSquare(n)
print()
Square(n)
print()
Diamond(9)
print()
InverseEquilateralTriangle(9)
print()
EquilateralTriangle(9)
print()
LeftsidebaseTriangle(n)
print()
OutlineEquilateralTriangle(9)
print()
X_pattern(5)
print()
Heart(11)




    
    
