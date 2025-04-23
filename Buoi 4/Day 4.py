import random

def game_engine():
    money = 100_000  # Số tiền ban đầu
    bet_amount = 10_000  # Số tiền cược mỗi lần
    print("=== Trò chơi Tài Xỉu mở rộng ===")
    print("Bạn bắt đầu với 100,000 VND. Mỗi lượt chơi đặt 10,000 VND.")
    print("1. Tài (Tổng > 5), 2. Xỉu (Tổng <= 5)")
    print("3. Cược số 5 (nếu tổng xúc xắc = 5 thì x3)")

    while money >= bet_amount:
        print(f"\nSố tiền hiện tại: {money} VND")

        try:
            bet_type = int(input("Chọn kiểu cược (1-Tài, 2-Xỉu, 3-Cược số 5): "))
            if bet_type not in [1, 2, 3]:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
                continue
        except ValueError:
            print("Vui lòng nhập số.")
            continue

        # Tài/Xỉu
        if bet_type in [1, 2]:
            user_select = bet_type
            die_1 = random.randint(1, 6)
            die_2 = random.randint(1, 6)
            sum_dice = die_1 + die_2
            print(f"Xúc xắc: {die_1} + {die_2} = {sum_dice}")

            if (sum_dice > 5 and user_select == 1) or (sum_dice <= 5 and user_select == 2):
                print("Bạn thắng!")
                money += bet_amount
            else:
                print("Bạn thua!")
                money -= bet_amount

        # Cược số 5
        elif bet_type == 3:
            die_1 = random.randint(1, 6)
            die_2 = random.randint(1, 6)
            sum_dice = die_1 + die_2
            print(f"Xúc xắc: {die_1} + {die_2} = {sum_dice}")
            if sum_dice == 5:
                print("Bạn đoán đúng tổng là 5! Nhận x3 số tiền!")
                money += bet_amount * 3
            else:
                print("Không trúng tổng là 5.")
                money -= bet_amount

        if money < bet_amount:
            print("\nBạn không còn đủ tiền để chơi tiếp.")
            break

        cont = input("Bạn có muốn chơi tiếp không? (y/n): ")
        if cont.lower() != 'y':
            break

    print(f"\nTrò chơi kết thúc. Số tiền còn lại: {money} VND")

if __name__ == '__main__':
    game_engine()
