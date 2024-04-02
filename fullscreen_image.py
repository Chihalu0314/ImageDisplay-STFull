import schedule
import time
import cv2
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from screeninfo import get_monitors

print("スクリプトが起動しました！")

def job():
    image_path = 'img.png'  # 画像のパスを指定
    img = cv2.imread(image_path)
    
    for m in get_monitors():
        window_name = f'image_{m}'
        cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
        cv2.moveWindow(window_name, m.x, m.y)
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(window_name, img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtWidgets.QMenu(parent)
        exit_action = menu.addAction("Exit")
        exit_action.triggered.connect(lambda: sys.exit())
        self.setContextMenu(menu)

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
tray_icon = SystemTrayIcon(QtGui.QIcon("icon.jpeg"), w)  # アイコンのパスを指定
tray_icon.show()

schedule.every().day.at("10:30").do(job)  # 時間を指定

while True:
    schedule.run_pending()
    time.sleep(1)
