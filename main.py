import sys
from counter import Counter
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])

root = QWidget()

root.resize(540, 240)
root.setWindowTitle("Stack counter")
root.setLayout(Counter())
root.show()

sys.exit(app.exec_())