# to create a tuple of numbers and print one item.
#  to unpack a tuple into several variables.
#  to add an item to a tuple.
#  to find the index of an item in a tuple.
#  to find the repeated items of a tuple

def tuple1():
    tupOfNum = (1,2,3,4,9,8,7,6)
    print (tupOfNum[2])
def tuple2():
    tupOfText = ('Cay tao','Trai tao','Toyota')
    (cay,doAn,xe) = tupOfText
    print (cay,doAn,xe)
def tuple3():
    tupOfNum = (1,2,3,4)
    newTup = (6,7,8,9)
    tupOfNum += newTup
    print (tupOfNum)
def tuple4():
    tupOfNum = (1,2,3,4)
    print (tupOfNum)
    x = int(input('Nhap gia tri trong tuple de tim ra vi tri(index): '))
    indexOfTup = tupOfNum.index(x)
    print (f'Gia tri {x} nam o vi tri {indexOfTup}')
def tuple5():
    tupOfNum = (7,3,5,5,6,0,8)
    dupNum = []
    for x in tupOfNum:
        if tupOfNum.count(x) > 1:
            dupNum.append(x)
    print(dupNum)
def set1():
    setOfNum = {1,2,4,5,6,2}
    print("Maximum value:", max(setOfNum))
    print("Minimum value:",min(setOfNum))
def set2():
    inputValue = int(input('Nhap gia tri can tim trong set:'))
    setOfNum = {1,2,4,5,6,2}
    check = False
    for x in setOfNum:
        if inputValue == x:
            check = True
    if check:
        print (f"Gia tri {inputValue} co xuat hien trong set")
    else:
        print(f"Gia tri {inputValue} khong xuat hien trong set")
def set3():
    setOfNum1 = {1,2,4,5,6,2}
    setOfNum2 = {3,4,1,5,8,9}

    if setOfNum1.intersection(setOfNum2):
        print ("2 set nay co gia tri giong nhau, gia tri do la:",setOfNum1.intersection(setOfNum2))
    else:
        print ("2 set nay khong co gia tri giong nhau")
def set4():
    setOfNum = {1,2,4,5,6,2,4,1,5,8,9}
    count = {}
    for x in setOfNum:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    print(count)
def set5():
    setOfNum1 = {1,2,4,5,6,2}
    setOfNum2 = {3,4,1,5,8,9}
    print("Set 2 thieu gia tri tu set 1:",setOfNum1.difference(setOfNum2))
    print("Set 1 thieu gia tri tu set 2:",setOfNum2.difference(setOfNum1))
def dict1():
    keys = ['name', 'age', 'city']
    values = ['Alice', 25, 'Hanoi']
    result = dict(zip(keys, values))
    print("Dictionary từ 2 list:", result)

def dict2():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged = {**dict1, **dict2}
    print("Dict sau khi merge:", merged)

def dict3():
    sample_dict = {
        "class": {
            "student": {
                "name": "John",
                "marks": {
                    "math": 90,
                    "history": 85
                }
            }
        }
    }
    print("Giá trị của key 'history':", sample_dict["class"]["student"]["marks"]["history"])

def dict4():
    employees = ['Alice', 'Bob', 'Charlie']
    default_value = {'designation': 'Developer', 'salary': 5000}
    result = dict.fromkeys(employees, default_value)
    print("Dict với giá trị mặc định:", result)

def dict5():
    original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    keys = ['a', 'c']
    new_dict = {k: original[k] for k in keys}
    print("Dict với các key được trích:", new_dict)

def dict6():
    data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    keys_to_remove = ['a', 'd']
    for key in keys_to_remove:
        data.pop(key, None)
    print("Dict sau khi xóa keys:", data)

def dict7():
    data = {'a': 1, 'b': 2, 'c': 3}
    value = 2
    exists = value in data.values()
    print(f"Giá trị {value} {'tồn tại' if exists else 'không tồn tại'} trong dict.")

def dict8():
    data = {'name': 'Alice', 'age': 25}
    data['first_name'] = data.pop('name')
    print("Dict sau khi đổi tên key:", data)

def dict9():
    scores = {'Alice': 88, 'Bob': 70, 'Charlie': 95}
    min_key = min(scores, key=scores.get)
    print("Key có giá trị nhỏ nhất là:", min_key)

def dict10():
    student = {'name': 'John', 'details': {'age': 20, 'city': 'Hanoi'}}
    student['details']['city'] = 'Saigon'
    print("Dict sau khi đổi giá trị lồng:", student)

def dict11():
    text = "hello world"
    count = {}
    for char in text:
        if char != ' ':
            count[char] = count.get(char, 0) + 1
    print("Tần suất xuất hiện của ký tự:", count)

def dict12():
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    n = 20
    primes = [x for x in range(2, n) if is_prime(x)]
    result = {i + 1: primes[i] for i in range(len(primes))}
    print(f"Dict chứa số nguyên tố < {n}:", result)

if __name__ == '__main__':
    dict1()
