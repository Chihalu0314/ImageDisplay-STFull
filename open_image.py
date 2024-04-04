import os
import time
from datetime import datetime
import subprocess
import pyautogui
import getpass

# 画像のパスと開きたい時間を指定します
image_path = "img.png"
open_time = "21:51"  # 24時間形式で指定します

# 正しいパスワードを設定します
correct_password = "p"

while True:
    # 現在の時間を取得します
    now = datetime.now().strftime("%H:%M")
    
    # 現在の時間が指定した時間と一致したら画像を開きます
    if now == open_time:
        os.startfile(image_path)  # Windows標準のPhotoアプリで画像を開きます
        time.sleep(1)  # Photoアプリが開くのを待ちます
        pyautogui.press('f11')  # フルスクリーン表示に切り替えます

        # パスワードが正しく入力されるまでマウスを動かせないようにします
        while True:
            password = getpass.getpass("Enter the password to unlock the mouse: ")
            if password == correct_password:
                break
            pyautogui.moveTo(100, 100, duration=0.1)  # マウスを特定の位置に移動します

        break

    # 1秒ごとに時間をチェックします
    time.sleep(1)
