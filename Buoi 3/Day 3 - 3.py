import random
def loopex1():
    for i in range(1, 11):
        print(i)
def loopex2():
    n = int(input("Nhập số n: "))
    tong = 0
    for i in range(1, n + 1):
        tong += i
    print("Tổng từ 1 đến", n, "là:", tong)
def loopex3():
    """Write a program to calculate the sum of even (/odd) numbers in a range from
1 to n (n is entered from the keyboard)"""
    n = int(input("Enter a nuber= "))
    even = 0
    odd = 0
    start =0
    while start <= n:
        if start % 2 == 0:
            even = even + start
        else:
            odd = odd + start
        start = start + 1
    print("sum of odd to n =",odd)
    print("sum of even to n =",even)
def loopex4():
    chuoi = input("Nhập chuỗi: ")
    nguyen_am = "aeiouAEIOU"
    dem = 0
    for ky_tu in chuoi:
        if ky_tu in nguyen_am:
            dem += 1
    print("Số nguyên âm trong chuỗi là:", dem)
def loopex5():
    cau = input("Nhập một câu: ")
    tu = cau.split()  # Tách câu thành các từ dựa theo khoảng trắng
    so_tu = len(tu)
    print("Số từ trong câu là:", so_tu)
def loopex6():
    x = random.randrange(1,100)
    limit = 0
    diff = input("Choose difficult: Easy: 10 times, Medium: 5 times, Hard: 3 times")
    if diff.lower() == "hard":
        limit = 3
    elif diff.lower() == "medium":
        limit = 5
    elif diff.lower() == "easy":
        limit = 10
    a = 0
    while a < limit:
        y = int(input("Guess the number:"))
        if y == x:
            print(f"You right! The number is {y}")
            return
        else:
            if y > x:
                print("Smaller!")
            else:
                print("Larger!")
        a += 1
    print("You failed!")
if __name__ == '__main__':
    loopex6()