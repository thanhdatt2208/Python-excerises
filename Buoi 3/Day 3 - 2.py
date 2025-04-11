import math
import random

def ex1():
    print ('Câu 1')
    base = float(6)
    height = float(8)
    area = 0.5 * base * height
    print (f'Area of triangle with bae {base} and height {height } is {area}')   
def ex2():
    a = float(input())
    b = float(input())
    c =  float(input())
    chuvi = a + b + c
    print (f'Chu vi {chuvi}')
def ex3():
    pi = 3.14
    r = 6
    dientich = pi * r * r
    chuvi = 2 * pi * r
    print (f'Dien tich va chu vi cua duong tron lan luot la {dientich}, {chuvi}')
def ex5():
    slope = 2  
    y_intercept = -2  

    x_intercept = 2 / 2 
    
    print(f"Slope: {slope}")
    print(f"X-Intercept: {x_intercept}")
    print(f"Y-Intercept: {y_intercept}")    
def ex6():
    x1,y1,x2,y2 =  2,2,6,10
    slope = (y2-y1)/(x2-x1)
    print (slope)
    euclidean = math.sqrt((x1-x2)**2+(y1-y)**2)
    print (euclidean)
def ex5():
    x = (int(input("x= ")))
    #y = 2*x - 2 # x = y
    #x = 2*y - 2
    #2*y = x + 2
    y = x/2 + 1
    print ("y =",y)
def ex8():
    x = int(input("x= "))
    a,b,c = 1,6,9
    y = a*x**2 +b*x + c 
    print("y=",y)
    y = 0
    print("for y = 0, x must be at:",(y-b)/2)
def ex9():
    chuoi1 = "python"
    chuoi2 = "dragon"

    do_dai_chuoi1 = len(chuoi1)
    do_dai_chuoi2 = len(chuoi2)

    print("Độ dài của chuỗi 'python':", do_dai_chuoi1)
    print("Độ dài của chuỗi 'dragon':", do_dai_chuoi2)

    so_sanh = do_dai_chuoi1 > do_dai_chuoi2  # Đây là sai vì cả hai đều dài 6 ký tự
    print("So sánh sai (python > dragon):", so_sanh)
def ex10():
    ket_qua = 'on' in 'python' and 'on' in 'dragon'
    print("Chuỗi 'on' có trong cả 'python' và 'dragon':", ket_qua)
def ex11():
    cau = "I hope this course is not full of jargon"
    ket_qua = "jargon" in cau
    print("Từ 'jargon' có trong câu không?:", ket_qua)
def ex13():
    chuoi = "python"
    do_dai = len(chuoi)          
    dang_float = float(do_dai)    
    dang_chuoi = str(dang_float) 

    print("Độ dài:", do_dai)
    print("Dạng float:", dang_float)
    print("Dạng chuỗi:", dang_chuoi)
def ex14():
    so = 10
    la_so_chan = so % 2 == 0
    print("Số", so, "là số chẵn?", la_so_chan)
def ex15():
    gio = input("Nhập số giờ làm việc: ")
    luong_moi_gio = input("Nhập mức lương mỗi giờ: ")
    gio = float(gio)
    luong_moi_gio = float(luong_moi_gio)
    tong_luong = gio * luong_moi_gio
    print("Tổng lương của bạn là:", tong_luong)
def ex16():
    so_nam = input("Nhập số năm bạn muốn tính (tối đa 100 năm): ")
    so_nam = int(so_nam)
    if so_nam > 100:
        print("Giả sử một người chỉ sống tối đa 100 năm. Vui lòng nhập lại.")
    else:
        so_giay = so_nam * 365 * 24 * 60 * 60
        print("Số giây bạn có thể sống trong", so_nam, "năm là:", so_giay)
if __name__ == '__main__':
    ex1()