from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit,QPushButton,QVBoxLayout
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion
from PyQt6.QtCore import Qt
import time
import datetime
import sys
import os
 
image_folder_path = 'C:\\Users\\besro\\Documents\\code\\camera_date_reader\\images'
 
class PhotoWindow(QWidget):
    def __init__(self, photo_name:str):
        super().__init__()
 
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Python QLabel")
        self.setWindowIcon(QIcon('qt.png'))
 
 
        label = QLabel(self)
        pixmap = QPixmap(photo_name)
        label.setPixmap(pixmap)

class TextWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(1000, 200, 200, 100)
        self.setWindowTitle("Python QLabel")
        self.setWindowIcon(QIcon('qt.png'))
        self._date_entered = False
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Input field for year value
        self.year_input = QLineEdit()
        self.year_input.setFixedWidth(150)
        layout.addWidget(self.year_input)
        # Input field for month value
        self.month_input = QLineEdit()
        self.month_input.setFixedWidth(150)
        layout.addWidget(self.month_input)
        # Input field for day value
        self.day_input = QLineEdit()
        self.day_input.setFixedWidth(150)
        layout.addWidget(self.day_input)
        # Input field for hour value
        self.hour_input = QLineEdit()
        self.hour_input.setFixedWidth(150)
        layout.addWidget(self.hour_input)
        # Input field for minute value
        self.minute_input = QLineEdit()
        self.minute_input.setFixedWidth(150)
        layout.addWidget(self.minute_input)

        button_go = QPushButton("Get Text")
        button_go.clicked.connect(self.get)
        layout.addWidget(button_go)
 
        button_clear = QPushButton("Clear Text")
        # would be nice to put these in a function, see line 78
        button_clear.clicked.connect(self.year_input.clear)
        button_clear.clicked.connect(self.month_input.clear)
        button_clear.clicked.connect(self.day_input.clear)
        button_clear.clicked.connect(self.hour_input.clear)
        button_clear.clicked.connect(self.minute_input.clear)
        layout.addWidget(button_clear)
 
    def get(self):
        year = int(self.year_input.text())
        month = int(self.month_input.text())
        day = int(self.day_input.text())
        hour = int(self.hour_input.text())
        minute = int(self.minute_input.text())
        date_time = datetime.datetime(year, month, day, hour, minute)
        unix_time = time.mktime(date_time.timetuple())
        self._date_entered = True
        print(date_time)
        print(unix_time)
    # WOULD BE NICE TO ADD BUT DOESNT WORK WHEN CALLED THE SAME WAY AS THE GET ONE
    # def clear(self):
    #     print("Clear")
    #     self.year_input.clear
    #     self.month_input.clear
    #     self.day_input.clear
    #     self.hour_input.clear
    #     self.minute_input.clear
 
app = QApplication(sys.argv)

text_window = TextWindow()
text_window.show()
image_folder = os.listdir(image_folder_path)
for image in image_folder:
    photo_window = PhotoWindow('image')
    photo_window.show()
    # while(text_window._date_entered is False):
    #     time.sleep(5)


sys.exit(app.exec())