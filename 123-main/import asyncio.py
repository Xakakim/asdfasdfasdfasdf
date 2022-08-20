import asyncio
from login import Ui_MainWindow
from pyrogram import Client
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QInputDialog
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from main import Ui_Form
import sys




class Worker(QThread, Ui_MainWindow):
    def __init__(self, parent):
        super().__init__(parent)
    
    def run(self):
        async def main():
            api_id = int(self.Api.text())
            api_hash = self.Hash.text()
            phone_number = self.Phone.text()
            client = Client("my_account", api_id, api_hash)
            await client.connect()
            sent_code_info = await client.send_code(phone_number)
            (phone_code, ) = input(QInputDialog.getText(self , 'Input Dialog' , 'Enter your Code:'))
            await client.sign_in(phone_number, sent_code_info.phone_code_hash, phone_code)
        asyncio.run(main())


class first(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


    def loginChk(self):
        self.worker = Worker()
        self.worker.start()


app = QtWidgets.QApplication(sys.argv)
ex = first()
sys.exit(app.exec_())
