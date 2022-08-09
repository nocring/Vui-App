import pyautogui, time
from pynput.keyboard import Controller

def spam(num, ls = ["Spam Text"]):
    print("\n--------------- Tiến hành spam ---------------\n")
    while num > 0 or num == -1:
        if num != -1:
            print("\t (!) Còn lại %d lần!\n" %num)
            num -= 1
        for word in ls:
            keyboard = Controller()
            keyboard.type(word)
            pyautogui.press ("enter")    
            time.sleep(1)

def delay(second = 5):
    for i in range(second, 0, -1):
        print("Còn %ds" %i)
        time.sleep(1)


def main():
    print("\n Được viết bởi Vui Vẻ.")
    print("\n Ghé thăm tôi tại: https://www.facebook.com/profile.php?id=100076426310765\n")
    ls = input(" - Nhập chuỗi (cách nhau bởi 3 dấu cách): ").split("   ")
    num = 0
    sec = 0
    try:
        num = int(input(" - Số lần spam (nhập -1 để spam vô hạn): "))
        sec = int(input(" - Thời gian đợi: "))
    except ValueError:
        print("Số lần không hợp lệ")
        input()
        exit(-1)

    delay(sec)

    try:
        spam(num, ls)
    except:
        print("-------------------------- Kết thúc spam! --------------------------")

if __name__ == "__main__":
    main()
