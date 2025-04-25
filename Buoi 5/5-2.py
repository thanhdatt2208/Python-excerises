#▸Tạo 1 danh sách (list) ngẫu nhiên N phần tử (N nhập từ bàn phím) có giá trị từ 1 đến 100 sau đó tạo 1 menu cho phép thực hiện các công việc sau:
# In ra danh sách vừa tạo.
# In đảo ngược danh sách.
# Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).
# tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
# đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện
# # In ra vị trí các phần tử là số nguyên tố.
# tìm các số duy nhất (không trùng lặp) trong danh sách.
# liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.
# In ra các đoạn con trong danh sách giảm liên tiếp.

import random
def phanTuN():
    n = (int(input(print("Nhap N: "))))
    return n 
def randomList(n):
    listOfNum = []
    for x in range(n):
            x = random.randint(1,100)
            listOfNum.append(x)
    return listOfNum

def printList(listOfNum):
    print (listOfNum)

def printRevList (listOfNum):
    print (listOfNum[::-1])

def largestNum (listOfNum):
    largestNum = max(listOfNum)
    index = listOfNum.index(largestNum)
    print ("Largest number =", largestNum,"Index =", index)

def dupNum (n,listOfNum):
    indexOfDupNum = []
    for x in range(len(listOfNum)):
        if listOfNum[x] == n:
            indexOfDupNum.append(x)
    print(indexOfDupNum)

def isPrime(listOfNum):
    primeNumbers = []
    for x in listOfNum:
        if x < 2:
            continue
        isThisNumPrime = True
        for n in range(2,x):
            if x % n == 0:
                isThisNumPrime = False
                break
        if isThisNumPrime:
                primeNumbers.append(x)
    print (primeNumbers)

def sortedList(listOfNum):
    sortedList = sorted(listOfNum)
    print (sortedList)

def uniqueNumbers(listOfNum):
    unique = []
    for x in listOfNum:
        if listOfNum.count(x) == 1:
            unique.append(x)
    print(unique)

def countOccurrences(listOfNum):
    
    counted = {}
    for x in listOfNum:
        if x in counted:
            counted[x] += 1
        else:
            counted[x] = 1
    for key, value in counted.items():
        print(f"{key}: xuất hiện {value} lần")

def decreasingSubsequences(listOfNum):
    result = []
    sub = []

    for i in range(len(listOfNum)):
        if not sub or listOfNum[i] < sub[-1]:
            sub.append(listOfNum[i])
        else:
            if len(sub) > 1:
                result.append(sub)
            sub = [listOfNum[i]]
    
    if len(sub) > 1:
        result.append(sub)

    for seq in result:
        print(seq)

def menu(n,listOfNum):
    if n == 1:
        printList(listOfNum)
    if n == 2:
        printRevList(listOfNum)
    if n == 3:
        sortedList(listOfNum)
    if n == 4:
        largestNum(listOfNum)
    if n == 5:
        dupNumber = phanTuN()
        dupNum(dupNumber,listOfNum)
    if n == 6:
        isPrime(listOfNum)
    if n == 7:
        uniqueNumbers(listOfNum)
    if n == 8:
        countOccurrences(listOfNum)
    if n == 9:
        decreasingSubsequences(listOfNum)
    if n == 10:
        return True
def choiceMenu():
    choice = int(input("Nhap so de su dung tinh nang: "))
    return choice

if __name__ == '__main__':
    n = phanTuN()
    listOfNum = randomList(n)
    while True:
        choice = choiceMenu()
        menu(choice,listOfNum)
    
