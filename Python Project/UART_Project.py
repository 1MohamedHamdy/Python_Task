import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import serial

class UART_Emulator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial('COM6', baudrate=9600, timeout=1)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

        self.send_button = QtWidgets.QPushButton('Send', self)
        self.send_button.clicked.connect(self.send_data)
        self.send_text = QtWidgets.QLineEdit(self)

        self.receive_text = QtWidgets.QTextEdit(self)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.send_text)
        layout.addWidget(self.send_button)
        layout.addWidget(self.receive_text)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.receive_data)
        self.timer.start(100)

    def send_data(self):
        data = self.send_text.text()
        self.ser.write(data.encode())
        self.receive_text.append("Sent: " + data)
        self.send_text.clear()

    def receive_data(self):
        received_data = self.ser.readline().decode()
        if received_data:
            self.receive_text.append("Received: " + received_data)

    def closeEvent(self, event):
        self.ser.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    uart_emulator = UART_Emulator()
    uart_emulator.show()
    sys.exit(app.exec_())
