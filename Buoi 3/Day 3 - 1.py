def ifex1():
    age = int(input("Nhập tuổi đi: "))

    if age >= 18:
        print("Bạn hợp pháp để bầu cử")
    else:
        print("Bạn ko hợp pháp để bầu cư")
def ifex2():
    x = int(input("enter a number:"))
    if x / 2 == 0:
        print(f"{x} is an even number")
    else:
        print(f"{x} is an odd number")
def ifex3():
    number = int(input("Nhập số đi: "))

    if number % 7 == 0:
        print(f"{number} is divisible by 7.")
    else:
        print(f"{number} is not divisible by 7.")
def ifex4():
    number = int(input("Nhập số đi "))

    last_digit = number % 10

    if last_digit % 3 == 0:
        print(f"The last digit of {number} is {last_digit} and it is divisible by 3.")
    else:
        print(f"The last digit of {number} is {last_digit} and it is not divisible by 3.")
def ifex5():
    x = random.randrange(1,9)
    a = 0
    while a < 5:
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
def ifex6():
    x = int(input("day of week = "))
    if x == 2:
        print("Monday")
    elif x == 3:
        print("Tuesday")
    elif x == 4:
        print("Wednesday")
    elif x == 5:
        print("Thursday")
    elif x == 6:
            print("Friday")
    elif x == 7:
            print("Saturday")
    elif x == 1:
        print("Sunday")
    else:
        print ("Out of range!!!!!!!!!!")
if __name__ == '__main__':
    ifex4()