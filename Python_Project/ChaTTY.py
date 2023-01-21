import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.Qt import QColor,QIcon

class Chatty(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChaTTY")
        self.setWindowIcon(QIcon("logo.png"))

        self.setFixedSize(610,480)
        
        self.received_data_text_edit = QtWidgets.QTextEdit(self)
        self.received_data_text_edit.setReadOnly(True)
        self.received_data_text_edit.move(310, 50)
        self.received_data_text_edit.resize(290, 380)
        font = QtGui.QFont("Courier")
        self.received_data_text_edit.setFont(font)
        color = QColor('white')
        self.received_data_text_edit.setTextColor(color)
        self.received_data_text_edit.setStyleSheet("background-color:black;")

        self.sent_data_text_edit = QtWidgets.QTextEdit(self)
        self.sent_data_text_edit.setReadOnly(False)
        self.sent_data_text_edit.move(10, 50)
        self.sent_data_text_edit.resize(290, 380)
        self.sent_data_text_edit.setCursorWidth(0)
        font = QtGui.QFont("Courier")
        self.sent_data_text_edit.setFont(font)
        self.sent_data_text_edit.setTextColor(color)
        self.sent_data_text_edit.setStyleSheet("background-color:black;")


        self.send_button = QtWidgets.QPushButton("Send", self)
        self.send_button.move(10, 430)
        self.send_button.resize(290,47)
        self.send_button.clicked.connect(self.send_data)
        
        self.format_combo_box = QtWidgets.QComboBox()
        self.format_combo_box.addItems(["Characters", "Hexadecimal"])
        self.format_combo_box.currentIndexChanged.connect(self.on_format_changed)
        self.format_combo_box.setParent(self)
        self.format_combo_box.setGeometry(310, 432, 290, 44)
            
        self.config_button = QtWidgets.QPushButton("Configure", self)
        self.config_button.move(10, 10)
        self.config_button.resize(590,30)
        self.config_button.clicked.connect(self.on_config_button_clicked)

        self.serial = QSerialPort()

        self.show()

    def on_config_button_clicked(self):
        ports = []
        for info in QSerialPortInfo.availablePorts():
            ports.append(info.portName())
        port, ok = QtWidgets.QInputDialog.getItem(self, "Serial Port", "Select the serial port:", ports, 0, False)
        if ok:
            self.serial.setPortName(port)
            baud_rates = ["4800", "9600", "19200", "38400", "57600", "115200"]
            baud_rate, ok = QtWidgets.QInputDialog.getItem(self, "Baud Rate", "Select the baud rate:", baud_rates, 5, False)
            
            if ok:
                self.serial.setBaudRate(int(baud_rate))
                data_bits = ["5", "6", "7", "8"]
                data_bit, ok = QtWidgets.QInputDialog.getItem(self, "Data Bits", "Select the data bits:", data_bits, 3, False)
                if ok:
                    if data_bit == "5":
                        self.serial.setDataBits(QSerialPort.Data5)
                    elif data_bit == "6":
                        self.serial.setDataBits(QSerialPort.Data6)
                    elif data_bit == "7":
                        self.serial.setDataBits(QSerialPort.Data7)
                    elif data_bit == "8":
                        self.serial.setDataBits(QSerialPort.Data8)
                    parity = ["None", "Even", "Odd"]
                    parity, ok = QtWidgets.QInputDialog.getItem(self, "Parity", "Select the parity:", parity, 0, False)
                    if ok:
                        if parity == "None":
                            self.serial.setParity(QSerialPort.NoParity)
                        elif parity == "Even":
                            self.serial.setParity(QSerialPort.EvenParity)
                        elif parity == "Odd":
                            self.serial.setParity(QSerialPort.OddParity)
                        stop_bits = ["1", "2"]
                        stop_bit, ok = QtWidgets.QInputDialog.getItem(self, "Stop Bits", "Select the stop bits:", stop_bits, 0, False)
                        if ok:
                            if stop_bit == "1":
                                self.serial.setStopBits(QSerialPort.OneStop)
                            elif stop_bit == "2":
                                self.serial.setStopBits(QSerialPort.TwoStop)
                            flow_control = ["None", "Hardware", "Software"]
                            flow_control, ok = QtWidgets.QInputDialog.getItem(self, "Flow Control", "Select the flow control:", flow_control, 0, False)
                            if ok:
                                if flow_control == "None":
                                    self.serial.setFlowControl(QSerialPort.NoFlowControl)
                                elif flow_control == "Hardware":
                                    self.serial.setFlowControl(QSerialPort.HardwareControl)
                                elif flow_control == "Software":
                                    self.serial.setFlowControl(QSerialPort.SoftwareControl)
                                
                            
        self.serial.readyRead.connect(self.on_format_changed)
        self.serial.error.connect(self.handleError)
        self.serial.open(QtCore.QIODevice.ReadWrite)
               
    def send_data(self):
        if self.serial.isOpen():
            data = self.sent_data_text_edit.toPlainText()
            self.serial.write(data.encode())
            self.sent_data_text_edit.clear()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Serial Port is not open")
    def on_format_changed(self):
        data = self.serial.readAll()
        if self.format_combo_box.currentText() == "Characters":
            self.received_data_text_edit.setPlainText(self.received_data_text_edit.toPlainText() + data.data().decode())
        elif self.format_combo_box.currentText() == "Hexadecimal":
            hex_data = " ".join("{:02x}".format(c) for c in data.data())
            self.received_data_text_edit.setPlainText(self.received_data_text_edit.toPlainText() + hex_data)
        
            
       
        
    def handleError(self, error):
        if error == QSerialPort.NoError:
            return
        elif error == QSerialPort.DeviceNotFoundError:
            QtWidgets.QMessageBox.critical(self, "Device Not Found Error", "Device not found or unavailable")
        elif error == QSerialPort.PermissionError:
            QtWidgets.QMessageBox.critical(self, "Permission Error", "Permission denied")
        elif error == QSerialPort.OpenError:
            QtWidgets.QMessageBox.critical(self, "Open Error", "Error opening the device")
        elif error == QSerialPort.ParityError:
            QtWidgets.QMessageBox.critical(self, "Parity Error", "Parity error detected")
        elif error == QSerialPort.FramingError:
            QtWidgets.QMessageBox.critical(self, "Framing Error", "Framing error detected")
        elif error == QSerialPort.BreakConditionError:
            QtWidgets.QMessageBox.critical(self, "Break Condition Error", "Break condition detected")
        elif error == QSerialPort.WriteError:
            QtWidgets.QMessageBox.critical(self, "Write Error", "An I/O error occurred while writing the data")
        elif error == QSerialPort.ReadError:
            QtWidgets.QMessageBox.critical(self, "Read Error", "An I/O error occurred while reading the data")
        elif error == QSerialPort.ResourceError:
            QtWidgets.QMessageBox.critical(self, "Resource Error", "Device was unexpectedly removed")
        elif error == QSerialPort.UnsupportedOperationError:
            QtWidgets.QMessageBox.critical(self, "Unsupported Operation Error", "Operation not supported or unimplemented")
        elif error == QSerialPort.UnknownError:
            QtWidgets.QMessageBox.critical(self, "Unknown Error", "An unknown error has occurred")
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "An error has occurred")
    
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    chatty = Chatty()
    sys.exit(app.exec_())
                            

