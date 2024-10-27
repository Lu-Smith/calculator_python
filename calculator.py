import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QDesktopWidget, 
                             QGridLayout, QLineEdit, QPushButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Calculator(QWidget):
  def __init__(self):
    super().__init__()
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
    
    #layout
    layout = QGridLayout()
    layout.addWidget(self.display, 0, 0, 1, 4)
    
    buttons = {
      '7': (1, 0), '8': (1, 1), '9': (1, 2), '/': (1, 3),
      '4': (2, 0), '5': (2, 1), '6': (2, 2), '*': (2, 3),
      '1': (3, 0), '2': (3, 1), '3': (3, 2), '-': (3, 3),
      '0': (4, 0), '.': (4, 1), 'C': (4, 2), '+': (4, 3),
      '=': (5, 3),
    }
    
    for btn_text, pos in buttons.items():
      button = QPushButton(btn_text)
      button.clicked.connect(self.on_button_clicked)
      layout.addWidget(button, pos[0], pos[1])
    
    self.setLayout(layout)
    
    self.center()
    
  def on_button_clicked(self):
    sender = self.sender().text()
    
    if sender == '=':
      try:
        result = str(eval(self.display.text()))
        self.display.setText(result)
      except Exception:
        self.display.setText("Error")
    elif sender == 'C':
      self.display.clear()
      self.display.setText("0")
    else:
      current_text = self.display.text()
      if current_text == "0":
          self.display.setText(sender)
      else:
          self.display.setText(current_text + sender)
    
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
  