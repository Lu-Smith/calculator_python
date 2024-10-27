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
    
    #styling
    self.display.setStyleSheet("""
      QLineEdit {
        background-color: #f5f5f5;
        font-size: 24px;
        padding: 10px;
        border: 1px solid #d9d9d9;
        border-radius: 5px;
        color: #333;
      }
    """)
    
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
      if btn_text == '=':
        button.setObjectName("equalsButton")
      elif btn_text == 'C':
        button.setObjectName("clearButton")
      elif btn_text in {'+', '-', '*', '/'}:
        button.setObjectName("operatorButton")
      else: 
        button.setObjectName("numberButton")
      
      button.clicked.connect(self.on_button_clicked)
      layout.addWidget(button, pos[0], pos[1])
      
    self.setStyleSheet("""
        QPushButton {
          background-color: rgb(1, 28, 24);
          font-size: 18px;
          border: 1px solid #bfbfbf;
          border-radius: 5px;
          padding: 15px;
        }
        QPushButton:hover {
          background-color: rgb(17, 79, 70);
        }
        QPushButton:pressed {
          background-color: rbg(17, 79, 70);
        }
      QPushButton#equalsButton {
        color: rgb(115, 230, 213);
      }
      QPushButton#clearButton {
        color: rgb(242, 10, 68);
      }
      QPushButton#numberButton {
        color: white;
      }
      QPushButton#operatorButton {
        color: rgb(115, 230, 213);
      }
    """)
    
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
  