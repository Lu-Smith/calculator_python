import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel)
from PyQt5.QtGui import QIcon

class Calculator(QWidget):
  def __init__(self):
    super().__init__()
    self.time_label = QLabel("I am a calculator", self)
    self.initUI()
    
  def initUI(self):
    self.setWindowTitle("Stopwatch")
    self.resize(400, 600)
    self.setWindowIcon(QIcon("calculator.png"))


def main():
  app =QApplication(sys.argv)
  calculator = Calculator()
  calculator.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()
  