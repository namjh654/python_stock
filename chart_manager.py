import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PyQt5.QtWidgets import QVBoxLayout, QWidget


class RealTimeChart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.figure, self.ax = plt.subplots()
        layout.addWidget(QWidget.createWindowContainer(self.figure.canvas))

        self.animation = FuncAnimation(self.figure, self.update_chart, interval=1000)

    def update_data(self, new_price):
        self.data.append(new_price)
        if len(self.data) > 100:
            self.data.pop(0)

    def update_chart(self, _):
        self.ax.clear()
        self.ax.plot(self.data, label="Price")
        self.ax.legend()
