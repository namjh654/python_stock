from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextEdit, QWidget
from api_manager import KiwoomAPI
from strategy import Strategy
from chart_manager import RealTimeChart


class StockAutoTrader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.api = KiwoomAPI()
        self.strategy = Strategy(initial_balance=1000000)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Stock Auto Trader")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Start button
        self.start_button = QPushButton("Start Trading")
        self.start_button.clicked.connect(self.start_trading)
        layout.addWidget(self.start_button)

        # Log display
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        layout.addWidget(self.log_display)

        # Real-time chart
        self.chart = RealTimeChart(self)
        layout.addWidget(self.chart)

    def start_trading(self):
        ticker = "005930"  # Example: 삼성전자
        self.log_message("Starting trading...")
        self.api.login()
        price = self.api.get_stock_price(ticker)
        self.chart.update_data(float(price))

    def log_message(self, message):
        self.log_display.append(message)
        self.log_display.verticalScrollBar().setValue(
            self.log_display.verticalScrollBar().maximum()
        )


if __name__ == "__main__":
    app = QApplication([])
    window = StockAutoTrader()
    window.show()
    app.exec_()
