from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtCore import QEventLoop


class KiwoomAPI:
    def __init__(self):
        self.api = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.api_event_loop = QEventLoop()

    def login(self):
        self.api.dynamicCall("CommConnect()")
        self.api.OnEventConnect.connect(self.on_login)
        self.api_event_loop.exec_()

    def on_login(self, err_code):
        if err_code == 0:
            print("Login successful")
        else:
            print(f"Login failed. Error code: {err_code}")
        self.api_event_loop.exit()

    def get_stock_price(self, ticker):
        self.api.dynamicCall("SetInputValue(QString, QString)", "종목코드", ticker)
        self.api.dynamicCall("CommRqData(QString, QString, int, QString)", "req", "opt10001", 0, "0101")
        self.api.OnReceiveTrData.connect(self.on_receive_tr_data)
        self.api_event_loop.exec_()

    def on_receive_tr_data(self, screen_no, rqname, trcode, recordname, prev_next):
        price = self.api.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, 0, "현재가")
        print(f"Current price: {price.strip()}")
        self.api_event_loop.exit()
        return price.strip()
