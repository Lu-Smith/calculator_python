import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QDesktopWidget, 
                             QGridLayout, QLineEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Calculator(QWidget):
  def __init__(self):
    super().__init__()
    self.time_label = QLabel("I am a calculator", self)
    self.display = QLineEdit(self)
    self.display.setReadOnly(True)
    self.display.setFixedHeight(50)
    self.display.setAlignment(Qt.AlignRight)
    self.display.setText("0")
    self.initUI()
    
  def initUI(self):
    self.setWindowTitle("Stopwatch")
    self.resize(400, 600)
    self.setWindowIcon(QIcon("calculator.png"))
    

    
    self.center()
    
  def center(self):
    screen = QDesktopWidget().availableGeometry().center()
    frame = self.frameGeometry()
    frame.moveCenter(screen)

def main():
  app =QApplication(sys.argv)
  calculator = Calculator()
  calculator.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()
  