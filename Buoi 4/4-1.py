import random

def play_game():
    wins = 0
    losses = 0

    print("Chào mừng đến với trò chơi Đoán số từ 1 đến 100!")

    while True:
        print("\nChọn cấp độ:")
        print("1. Dễ (9 lần đoán)")
        print("2. Vừa (6 lần đoán)")
        print("3. Khó (4 lần đoán)")

        try:
            level = int(input("Nhập cấp độ (1/2/3): "))
            if level == 1:
                max_attempts = 9
            elif level == 2:
                max_attempts = 6
            elif level == 3:
                max_attempts = 4
            else:
                print("Cấp độ không hợp lệ. Chọn lại.")
                continue
        except ValueError:
            print("Vui lòng nhập số.")
            continue

        target = random.randint(1, 100)
        attempts = 0
        success = False

        print(f"\nĐã chọn một số từ 1 đến 100. Bạn có {max_attempts} lần đoán.")

        while attempts < max_attempts:
            try:
                guess = int(input(f"Lần đoán thứ {attempts + 1}: "))
                attempts += 1

                if guess < 1 or guess > 100:
                    print("Số đoán phải trong khoảng 1 đến 100.")
                    continue

                if guess == target:
                    print("Chính xác! Bạn đã đoán đúng.")
                    wins += 1
                    success = True
                    break
                elif guess < target:
                    print("Số bạn đoán nhỏ hơn.")
                else:
                    print("Số bạn đoán lớn hơn.")
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")

        if not success:
            print(f"Bạn đã thua. Số đúng là {target}.")
            losses += 1

        again = input("Bạn có muốn chơi tiếp? (y/n): ").lower()
        if again != 'y':
            break

    print("\nThống kê:")
    print(f"Số lần thắng: {wins}")
    print(f"Số lần thua: {losses}")
    print("Cảm ơn bạn đã chơi!")

if __name__ == '__main__':
    play_game()
