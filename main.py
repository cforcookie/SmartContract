from eth_utils.decorators import combomethod
from toolz.itertoolz import take
from web3.main import Web3
from PyQt5 import QtWidgets
import sys
import json
import interface
from web3._utils import personal
import time
import random
from datetime import datetime

class Main(interface.Ui_Form, QtWidgets.QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)

        global contract, web3
        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        web3.isConnected
        address = "0xEFEa7853451E07876Ad368327Fa33cb14709514f"
        abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"admins","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"chanle_transfer","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"code","type":"uint256"}],"name":"clime_transfer","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"confirm_admin","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"id_transfer","type":"uint256"},{"internalType":"address","name":"admin","type":"address"},{"internalType":"bool","name":"status_admin","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"confirm_transfer","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"}],"name":"create_shablon","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"shablon_id","type":"uint256"},{"internalType":"string","name":"catigory","type":"string"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"create_shablon_category","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"taker","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"code","type":"uint256"},{"internalType":"string","name":"catigory","type":"string"},{"internalType":"string","name":"dyscription","type":"string"}],"name":"create_transfer","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"taker","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"code","type":"uint256"},{"internalType":"string","name":"catigory","type":"string"},{"internalType":"string","name":"dyscription","type":"string"},{"internalType":"address","name":"admin","type":"address"}],"name":"create_transfer_safe","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"create_vote","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"info_id","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"info_used","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"register","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"search_voter","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"shablon_info","outputs":[{"internalType":"string","name":"catigory","type":"string"},{"internalType":"uint256","name":"value","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"shablon_name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"transfers","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"giver","type":"address"},{"internalType":"address","name":"taker","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"code","type":"uint256"},{"internalType":"string","name":"catigory","type":"string"},{"internalType":"string","name":"dyscription","type":"string"},{"internalType":"uint256","name":"time","type":"uint256"},{"internalType":"bool","name":"status","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"user","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"user_rule","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"view_admins_length","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"view_categores_length","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"view_confirm_admin_length","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"view_shablons_length","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"view_transactios_length","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"view_votes_length","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"vote_no","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"vote_yes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"votes","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"from","type":"address"},{"internalType":"bool","name":"status","type":"bool"}],"stateMutability":"view","type":"function"}]'
        contract = web3.eth.contract(abi = abi, address= address)
        
        for i in range (len(web3.eth.get_accounts())):
            web3.parity.personal.unlockAccount(web3.eth.accounts[i], "", 0)
            
        self.stackedWidget.setCurrentWidget(self.loginPage)
        self.add_list_start()
        
        for i in ("День", "Неделя", "Месяц", "Год"):
            self.comboBox_11.addItem(i)
            
        self.pushButton.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.to_transfer)
        self.pushButton_4.clicked.connect(self.to_transfer_shablon)
        self.pushButton_5.clicked.connect(self.to_history)
        self.pushButton_6.clicked.connect(self.to_createPage)
        self.pushButton_21.clicked.connect(self.to_addPage)
        self.pushButton_7.clicked.connect(self.to_votePage)
        self.pushButton_16.clicked.connect(self.create_vote_user)
        
        self.pushButton_9.clicked.connect(self.create_transfer)
        self.pushButton_10.clicked.connect(self.create_transfer_with)
        self.pushButton_14.clicked.connect(self.create_transfer2)
        self.pushButton_12.clicked.connect(self.create_transfer_with2)
        
        self.pushButton_8.clicked.connect(self.to_login)
        self.pushButton_11.clicked.connect(self.to_main)
        self.pushButton_13.clicked.connect(self.to_main)
        self.pushButton_19.clicked.connect(self.to_main)
        self.pushButton_20.clicked.connect(self.to_main)
        self.pushButton_23.clicked.connect(self.to_main)
        self.pushButton_25.clicked.connect(self.to_main)
        
        self.pushButton_2.clicked.connect(self.confirm_shablon)
        self.pushButton_29.clicked.connect(self.confirm_catefory)
        
        self.pushButton_15.clicked.connect(self.view_transfer)
        self.pushButton_18.clicked.connect(self.chanle_transfer)
        self.pushButton_17.clicked.connect(self.clime_transfer)
        self.pushButton_22.clicked.connect(self.create_shablon)
        self.pushButton_24.clicked.connect(self.add_category)
        self.pushButton_28.clicked.connect(self.choose_vote)
        
        self.pushButton_26.clicked.connect(self.vote_yes)
        self.pushButton_27.clicked.connect(self.vote_no)
        self.pushButton_30.clicked.connect(self.to_register)
        self.pushButton_32.clicked.connect(self.go_back)
        self.pushButton_31.clicked.connect(self.register_user)
        self.pushButton_33.clicked.connect(self.to_safe_transfer)
        self.pushButton_36.clicked.connect(self.to_main)
        self.pushButton_35.clicked.connect(self.show_info)
        self.pushButton_34.clicked.connect(self.accept_admin)
        self.pushButton_37.clicked.connect(self.to_history_date)
    
    def accept_admin(self):
        data = str(self.comboBox_10.currentText())
        j = 0
        index = "0"
        while data[j] != ":":
            index += data[j]
            j += 1
        contract.functions.confirm_transfer(int(index)).transact({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
        time.sleep(15)
        self.to_safe_transfer()
    
    def to_safe_transfer(self):
        self.textBrowser_3.clear()
        self.comboBox_10.clear()
        self.label_44.clear()
        self.frame_11.setVisible(False)
        for i in range(contract.functions.view_confirm_admin_length().call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})):
            data = contract.functions.confirm_admin(i).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            value = contract.functions.transfers(data[1]).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            if (data[2] == self.comboBox.currentText()) & (value[1] != self.comboBox.currentText()) & (data[3] == False):
                self.comboBox_10.addItem(str(i) + ": " + "От " + value[1])
        self.stackedWidget.setCurrentWidget(self.safePage)
        
    def show_info(self):
        try:
            data = str(self.comboBox_10.currentText())
            j = 0
            index = "0"
            while data[j] != ":":
                index += data[j]
                j += 1
            data = contract.functions.confirm_admin(int(index)).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            value = contract.functions.transfers(data[1]).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            self.textBrowser_3.setText("От: " + value[1] + "\n" + "Для: " + value[2] + "\n" + "Сумма: " + str(int(value[3])/10**18))
            self.frame_11.setVisible(True)
        except :
            self.label_44.setText("ПУСТОЕ ПОЛЕ")
    
    def add_list_start(self):
        self.comboBox.clear()
        for i in web3.eth.accounts:
            if contract.functions.user(i).call({"from" : i}) == True:
                self.comboBox.addItem(i)
    
    def to_register(self):
        self.stackedWidget.setCurrentWidget(self.registerPage)
        self.comboBox_8.clear()
        self.label_45.clear()
        for i in web3.eth.accounts:
            if contract.functions.user(i).call({"from" : i}) == False:
                self.comboBox_8.addItem(i)
                
    def register_user(self):
        try:
            account = self.comboBox_8.currentText()
            contract.functions.register().transact({"from" : account})
            time.sleep(15)
            self.stackedWidget.setCurrentWidget(self.loginPage)
            self.add_list_start()
        except :
            self.label_45.setText("НЕТ АККАУНТОВ")   
        
    def go_back(self):
        self.add_list_start()
        self.stackedWidget.setCurrentWidget(self.loginPage)
        
    def to_login(self):
        self.add_list_start()
        self.stackedWidget.setCurrentWidget(self.loginPage)
        
    def to_main(self):
        self.stackedWidget.setCurrentWidget(self.mainPage)
        self.textBrowser.clear()
        self.comboBox_6.clear()
        self.get_balance()
        
    def to_transfer(self):
        self.stackedWidget.setCurrentWidget(self.page)
        self.comboBox_2.clear()
        self.label_47.clear()
        for i in web3.eth.accounts:
            if i != self.comboBox.currentText():
                self.comboBox_2.addItem(i)
        
    def to_transfer_shablon(self):
        self.stackedWidget.setCurrentWidget(self.shablonPage)
        self.frame_8.setVisible(False)
        self.frame_9.setVisible(False)
        self.label_46.clear()
        for i in range(int(contract.functions.view_shablons_length().call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())}))):
            data = contract.functions.shablon_name(i).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            self.comboBox_4.addItem(str(i) + ": " + str(data))
        for i in web3.eth.accounts:
            if i != self.comboBox.currentText():
                self.comboBox_3.addItem(i)
    
    def to_history(self):
        self.stackedWidget.setCurrentWidget(self.historyPage)
        for i in range (contract.functions.view_transactios_length().call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})):
            data = contract.functions.transfers(i).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            if str(data[1]) == self.comboBox.currentText():
                self.comboBox_6.addItem(str(i) + ": Для " + str(data[2]))
            elif str(data[2]) == self.comboBox.currentText():
                self.comboBox_6.addItem(str(i) + ": От " + str(data[1]))
        self.frame_2.setVisible(False)
        self.frame_3.setVisible(False)
        self.frame_10.setVisible(False)
        self.label_36.clear()
        
    def to_history_date(self):
        self.comboBox_6.clear()
        now = datetime.now().timestamp()
        if self.comboBox_11.currentText() == "День":
            for i in range (contract.functions.view_transactios_length().call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})):
                data = contract.functions.transfers(i).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
                if (str(data[1]) == self.comboBox.currentText()) & (datetime.fromtimestamp(data[7]).strftime("%d") == datetime.fromtimestamp(now).strftime("%d")):
                    self.comboBox_6.addItem(str(i) + ": Для " + str(data[2]))
                elif (str(data[2]) == self.comboBox.currentText()) & (datetime.fromtimestamp(data[7]).strftime("%d") == datetime.fromtimestamp(now).strftime("%d")):
                    self.comboBox_6.addItem(str(i) + ": От " + str(data[1]))
                
        elif self.comboBox_11.currentText() == "Неделя":
            for i in range (contract.functions.view_transactios_length().call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})):
                data = contract.functions.transfers(i).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
                if (str(data[1]) == self.comboBox.currentText()) & (datetime.fromtimestamp(data[7]).strftime("%V") == datetime.fromtimestamp(now).strftime("%V")):
                    self.comboBox_6.addItem(str(i) + ": Для " + str(data[2]))
                elif (str(data[2]) == self.comboBox.currentText()) & (datetime.fromtimestamp(data[7]).strftime("%V") == datetime.fromtimestamp(now).strftime("%V")):
                    self.comboBox_6.addItem(str(i) + ": От " + str(data[1]))
                
        elif self.comboBox_11.currentText() == "Месяц":
            for i in range (contract.functions.view_transactios_length().call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})):
                data = contract.functions.transfers(i).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
                if (str(data[1]) == self.comboBox.currentText()) & (datetime.fromtimestamp(data[7]).strftime("%B") == datetime.fromtimestamp(now).strftime("%B")):
                    self.comboBox_6.addItem(str(i) + ": Для " + str(data[2]))
                elif (str(data[2]) == self.comboBox.currentText()) & (datetime.fromtimestamp(data[7]).strftime("%B") == datetime.fromtimestamp(now).strftime("%B")):
                    self.comboBox_6.addItem(str(i) + ": От " + str(data[1]))
                
        elif self.comboBox_11.currentText() == "Год":
            for i in range (contract.functions.view_transactios_length().call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})):
                data = contract.functions.transfers(i).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
                if (str(data[1]) == self.comboBox.currentText()) & (datetime.fromtimestamp(data[7]).strftime("%Y") == datetime.fromtimestamp(now).strftime("%Y")):
                    self.comboBox_6.addItem(str(i) + ": Для " + str(data[2]))
                elif (str(data[2]) == self.comboBox.currentText()) & (datetime.fromtimestamp(data[7]).strftime("%Y") == datetime.fromtimestamp(now).strftime("%Y")):
                    self.comboBox_6.addItem(str(i) + ": От " + str(data[1]))
    def view_transfer(self):
        try:
            data = str(self.comboBox_6.currentText())
            j = 0
            index = "0"
            while data[j] != ":":
                index += data[j]
                j += 1
            data = contract.functions.transfers(int(index)).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            if data[8] == False:
                self.textBrowser.setText("От: " + str(data[1]) + "\n" + "Для: " + str(data[2]) + "\n" + "Сумму: " + str(int(data[3])/10**18) + " ETH" + "\n" + "Статус: Активен" + "\n\n" + str(datetime.fromtimestamp(data[7]).strftime("%d.%B.%Y")))
                if (str(data[1]) == self.comboBox.currentText()) & (data[8] == False):
                    self.frame_2.setVisible(True)
                    self.frame_3.setVisible(False)
                    self.frame_10.setVisible(False)
                else:
                    self.frame_2.setVisible(False)
                    self.frame_3.setVisible(True)
                    self.frame_10.setVisible(True)
            else: 
                self.textBrowser.setText("От: " + str(data[1]) + "\n" + "Для: " + str(data[2]) + "\n" + "Сумму: " + str(int(data[3])/10**18) + " ETH" + "\n" + "Статус: Завершен" + "\n\n" + str(datetime.fromtimestamp(data[7]).strftime("%d.%B.%Y")))
                self.frame_2.setVisible(False)
                self.frame_3.setVisible(False)
                self.frame_10.setVisible(False)
            
            if contract.functions.info_used(int(index)).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())}) == True :
                id = contract.functions.info_id(int(index)).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
                info = contract.functions.confirm_admin(id).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
                if info[3] == False: 
                    self.textBrowser.setText("От: " + str(data[1]) + "\n" + "Для: " + str(data[2]) + "\n" + "Сумму: " + str(int(data[3])/10**18) + " ETH" + "\n" + "Статус: Активен" + "\n" + "БЕЗОПАСНЫЙ ПЕРЕВОД" + "\n" + "Админ: " + str(info[2]) + "\n" + "Не подтвержден админом"  + "\n\n" + str(datetime.fromtimestamp(data[7]).strftime("%d.%B.%Y")))
                    if (str(data[1]) == self.comboBox.currentText()) & (data[8] == False):
                        self.frame_2.setVisible(True)
                        self.frame_3.setVisible(False)
                        self.frame_10.setVisible(False)
                    else:
                        self.frame_2.setVisible(False)
                        self.frame_3.setVisible(False)
                        self.frame_10.setVisible(False)
                else:
                    self.textBrowser.setText("От: " + str(data[1]) + "\n" + "Для: " + str(data[2]) + "\n" + "Сумму: " + str(int(data[3])/10**18) + " ETH" + "\n" + "Статус: Завершен" + "\n" + "БЕЗОПАСНЫЙ ПЕРЕВОД" + "\n" + "Админ: " + str(info[2]) + "\n" + "Подтвержден админом"  + "\n\n" + str(datetime.fromtimestamp(data[7]).strftime("%d.%B.%Y")))
                    self.frame_2.setVisible(False)
                    self.frame_3.setVisible(True)
                    self.frame_10.setVisible(True)
            self.label_36.clear()
        except:
            self.label_36.setText("ИСТОРИЯ ПУСТА")
        
    def chanle_transfer(self):
        data = str(self.comboBox_6.currentText())
        j = 0
        index = "0"
        while data[j] != ":":
            index += data[j]
            j += 1
        contract.functions.chanle_transfer(int(index)).transact({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
        time.sleep(15)
        self.view_transfer()
        
    def clime_transfer(self):
        data = str(self.comboBox_6.currentText())
        j = 0
        index = "0"
        while data[j] != ":":
            index += data[j]
            j += 1
        code = self.spinBox_5.text()
        try:
            contract.functions.clime_transfer(int(index), code).transact({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            time.sleep(15)
            self.label_36.clear()
            self.view_transfer()
        except:
            self.label_36.setText("НЕВЕРНЫЙ КОД")
    
    
    def to_createPage(self):
        self.lineEdit_4.clear()
        self.stackedWidget.setCurrentWidget(self.createPage)
        
    def to_addPage(self):
        self.comboBox_7.clear()
        self.stackedWidget.setCurrentWidget(self.addPage)
        for i in range(contract.functions.view_shablons_length().call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})):
            item = contract.functions.shablon_name(i).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            self.comboBox_7.addItem(str(i) + ": " + str(item))
        
    def to_votePage(self):
        self.stackedWidget.setCurrentWidget(self.votePage)
        self.comboBox_9.clear()
        self.textBrowser_2.clear()
        self.label_37.clear()
        self.frame_5.setVisible(False)
        self.frame_4.setVisible(False)
        for i in range(contract.functions.view_votes_length().call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})):
            data = contract.functions.votes(i).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            self.comboBox_9.addItem(str(i) + ": " + str(data[1]))
        
    
    def get_balance(self):
        balance = int(web3.eth.get_balance(Web3.toChecksumAddress(self.comboBox.currentText())))/10**18
        self.label_9.setText(str(balance) + " ETH")
    
    def login(self):
        self.label_8.setText(self.comboBox.currentText())
        self.get_balance()
        if contract.functions.user_rule(self.comboBox.currentText()).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())}) == True:
            self.label_10.setText("Админ")
            self.frame_6.setVisible(True)
            self.frame.setVisible(False)
        else:
            self.label_10.setText("Пользователь")
            self.frame_6.setVisible(False)
            self.frame.setVisible(True)
            
        self.stackedWidget.setCurrentWidget(self.mainPage)
                    
    def create_vote_user(self):
        contract.functions.create_vote().transact({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
        time.sleep(15)
        self.get_balance()
        
        
    def create_transfer(self):
        try:
            taker = Web3.toChecksumAddress(self.comboBox_2.currentText())
            summ = int(self.spinBox_2.text())
            code = int(self.spinBox.text())
            catigory = str(self.lineEdit.text())
            dyscription = str(self.lineEdit_2.text())
            contract.functions.create_transfer(taker, summ * 10**18, code, catigory, dyscription).transact({"from" : Web3.toChecksumAddress(self.comboBox.currentText()), "value" : Web3.toWei(summ, "ether")})
            time.sleep(15)
            self.spinBox_2.clear()
            self.spinBox.clear()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.get_balance()
        except:
            self.label_47.setText("НЕ КОРРЕКТНЫЕ ДАННЫЕ")
            
        
    def create_transfer_with(self):
        try:
            taker = Web3.toChecksumAddress(self.comboBox_2.currentText())
            summ = int(self.spinBox_2.text())
            code = int(self.spinBox.text())
            catigory = str(self.lineEdit.text())
            dyscription = str(self.lineEdit_2.text())
            admin = contract.functions.view_admins_length().call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            admin = Web3.toChecksumAddress(contract.functions.admins(random.randrange(0, admin)).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())}))
            contract.functions.create_transfer_safe(taker, summ * 10**18, code, catigory, dyscription, admin).transact({"from" : Web3.toChecksumAddress(self.comboBox.currentText()), "value" : Web3.toWei(summ, "ether")})
            time.sleep(15)
            self.spinBox_2.clear()
            self.spinBox.clear()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.get_balance()
        except :
            self.label_46.setText("НЕ КОРРЕКТНЫЕ ДАННЫЕ")
        
    def confirm_shablon(self):
        data = str(self.comboBox_4.currentText())
        j = 0
        index = "0"
        while data[j] != ":":
            index += data[j]
            j += 1
        value = contract.functions.view_categores_length(int(index)).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
        for i in range(value):
            data = contract.functions.shablon_info(int(index), i).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            self.comboBox_5.addItem(str(i) + ": " + str(data[0]) + " " + str(data[1]))
        self.frame_8.setVisible(True)
        self.get_balance()
        
    def confirm_catefory(self):
        data = str(self.comboBox_4.currentText())
        j = 0
        index = "0"
        while data[j] != ":":
            index += data[j]
            j += 1
        data1 = str(self.comboBox_5.currentText())
        j = 0
        index1 = "0"
        while data[j] != ":":
            index1 += data1[j]
            j += 1
        data = contract.functions.shablon_info(int(index), int(index1)).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
        self.label_24.setText(str(data[1]))
        self.frame_9.setVisible(True)
        self.get_balance()
        
        
    def create_transfer2(self):
        data = str(self.comboBox_4.currentText())
        j = 0
        index = "0"
        while data[j] != ":":
            index += data[j]
            j += 1
        data1 = str(self.comboBox_5.currentText())
        j = 0
        index1 = "0"
        while data[j] != ":":
            index1 += data1[j]
            j += 1
        data = contract.functions.shablon_info(int(index), int(index1)).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
        taker = Web3.toChecksumAddress(self.comboBox_3.currentText())
        summ = int(self.label_24.text())
        code = int(self.spinBox_3.text())
        catigory = str(data[0])
        dyscription = str(self.lineEdit_3.text())
        contract.functions.create_transfer(taker, summ * 10**18, code, catigory, dyscription).transact({"from" : Web3.toChecksumAddress(self.comboBox.currentText()), "value" : Web3.toWei(summ, "ether")})
        time.sleep(15)
        self.frame_8.setVisible(False)
        self.frame_9.setVisible(False)
        self.get_balance()
        
    def create_transfer_with2(self):
        data = str(self.comboBox_4.currentText())
        j = 0
        index = "0"
        while data[j] != ":":
            index += data[j]
            j += 1
        data1 = str(self.comboBox_5.currentText())
        j = 0
        index1 = "0"
        while data[j] != ":":
            index1 += data1[j]
            j += 1
        data = contract.functions.shablon_info(int(index), int(index1)).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
        taker = Web3.toChecksumAddress(self.comboBox_3.currentText())
        summ = int(self.label_24.text())
        code = int(self.spinBox_3.text())
        catigory = str(data[0])
        dyscription = str(self.lineEdit_3.text())
        admin = contract.functions.view_admins_length().call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
        admin = Web3.toChecksumAddress(contract.functions.admins(random.randrange(0, admin)).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())}))
        contract.functions.create_transfer_safe(taker, summ * 10**18, code, catigory, dyscription, admin).transact({"from" : Web3.toChecksumAddress(self.comboBox.currentText()), "value" : Web3.toWei(summ, "ether")})
        time.sleep(15)
        self.frame_8.setVisible(False)
        self.frame_9.setVisible(False)
        self.get_balance()
        
    def create_shablon(self):
        name = str(self.lineEdit_4.text())
        contract.functions.create_shablon(name).transact({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
        time.sleep(15)
        
    def add_category(self):
        data = str(self.comboBox_7.currentText())
        j = 0
        index = "0"
        while data[j] != ":":
            index += data[j]
            j += 1
        name = str(self.lineEdit_5.text())
        summ = int(self.spinBox_4.text())
        contract.functions.create_shablon_category(int(index), name, summ).transact({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
        time.sleep(15)
        self.lineEdit_5.clear()
        self.spinBox_4.clear()
        
    def choose_vote(self):
        try:
            data = str(self.comboBox_9.currentText())
            j = 0
            index = "0"
            while data[j] != ":":
                index += data[j]
                j += 1
            data = contract.functions.votes(int(index)).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            if data[2] == True:
                self.textBrowser_2.setText("Подал заявку: " + str(data[1]) + "\n" + "Статус голосования: Активно")
            else:
                self.textBrowser_2.setText("Подал заявку: " + str(data[1]) + "\n" + "Статус голосования: Завершено")
            if contract.functions.search_voter(int(index)).call({"from" : Web3.toChecksumAddress(self.comboBox.currentText())}) == True:
                self.frame_5.setVisible(True)
                self.frame_4.setVisible(True)
            else:
                self.frame_5.setVisible(False)
                self.frame_4.setVisible(False)
            self.label_37.clear()
        except:
            self.label_37.setText("ИСТОРИЯ ГОЛОСОВАНИЙ ПУСТА")
    
    def vote_yes(self):
        try:
            data = str(self.comboBox_9.currentText())
            j = 0
            index = "0"
            while data[j] != ":":
                index += data[j]
                j += 1
            data = contract.functions.vote_yes(int(index)).transact({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            time.sleep(15)
            self.choose_vote()
        except:
            self.label_37.setText("ВЫ УЖЕ ПРОГОЛОСОВАЛИ")
            
    def vote_no(self):
        try:
            data = str(self.comboBox_9.currentText())
            j = 0
            index = "0"
            while data[j] != ":":
                index += data[j]
                j += 1
            data = contract.functions.vote_no(int(index)).transact({"from" : Web3.toChecksumAddress(self.comboBox.currentText())})
            time.sleep(15)
            self.choose_vote()
        except:
            self.label_37.setText("ВЫ УЖЕ ПРОГОЛОСОВАЛИ")
        
            
            
            
def App():
    app = QtWidgets.QApplication(sys.argv)
    web_contract = Main()
    web_contract.show()
    app.exec_()

if __name__ == "__main__":
    App()