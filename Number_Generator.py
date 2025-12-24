import sys
import random
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.calc = Calculation(self)
        self.title = QLabel("Random number generator",self)
        self.label_number = QLabel("0", self)
        self.enter_min_range = QLabel("Minimum")
        self.enter_range = QLineEdit(self)
        self.enter_max_range = QLabel("Maximum")
        self.enter_range1 = QLineEdit(self)
        self.generate = QPushButton("Generate", self)
        self.check_num = QLabel("Range: 0 — 100", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Number generator")

        vbox = QVBoxLayout()
        vbox.addWidget(self.title)
        vbox.addWidget(self.label_number)
        vbox.addWidget(self.enter_min_range)
        vbox.addWidget(self.enter_range)
        vbox.addWidget(self.enter_max_range)
        vbox.addWidget(self.enter_range1)
        vbox.addWidget(self.generate)
        vbox.addWidget(self.check_num)

        self.setLayout(vbox)

        self.title.setObjectName("title")
        self.label_number.setObjectName("num")
        self.enter_min_range.setObjectName("min")
        self.enter_range.setObjectName("range")
        self.enter_max_range.setObjectName("max")
        self.enter_range1.setObjectName("range1")
        self.check_num.setObjectName("check_num")

        self.setStyleSheet("""
            QWidget{
            background-color: black;
            }
            QLabel#title{
                font-size: 20px;
                color: white;
            }
            QLabel#num{
                font-size: 60px;
                font-weight: bold;
                color: white;
            }
            
            QLabel#min{
                color: white;
            }
            
            QLabel#max{
                color: white;
            }
            
            QLineEdit{
                font-size: 32px;
                border-radius: 4px;
                color: white;
                background-color: black;
                border: 2px solid #3d3d3d;
            }
            
            QPushButton{
                font-size: 20px;
                font-weight: bold;
                border-radius: 4px;
                padding-top: 8px;
                padding-bottom: 8px;
                color: white;
                background-color: #3d3d3d;
            }
            QLabel#check_num{
                color: white;
            }
        """)

        self.generate.clicked.connect(self.send)

    def send(self):
        try:
            num = int(self.enter_range.text())
            num2 = int(self.enter_range1.text())
            if num > num2:
                num = 0
                num2 = 100
                self.enter_min_range.setText("Minimum (this number must be lower)")
                self.enter_max_range.setText("Minimum (than this one)")
            else:
                self.enter_min_range.setText("Minimum")
                self.enter_max_range.setText("Maximum")

        except ValueError:
            num = 0
            num2 = 100
            self.enter_min_range.setText("Minimum (enter a number)")
            self.enter_max_range.setText("Maximum (enter a number)")

        finally:
            self.calc.get_the_number(num, num2)
            self.check_num.setText(f"Range: {num} — {num2}")


    def get_num(self, num):
        self.label_number.setText(str(num))



class Calculation:
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

    def get_the_number(self, num, num2):
        final_number = random.randint(num, num2)
        self.ui.get_num(final_number)


if __name__ == "__main__":
    run = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(run.exec_())

