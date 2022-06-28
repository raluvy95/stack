import math
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QLabel, QPushButton, QHBoxLayout, QFileDialog, QTextEdit


class Counter(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.list = []

        self.addLayout(self.left())
        self.addLayout(self.right())

    def left(self):
        leftbox = QVBoxLayout()
        self.i = self.prompt("Number:")
        self.i2 = self.prompt("Item:")
        self.i["input"].textChanged.connect(self.change)
        self.i2["input"].textChanged.connect(self.change)

        self.info = QLabel()

        leftbox.addLayout(self.i["layout"])
        leftbox.addLayout(self.i2["layout"])
        leftbox.addLayout(self.buttons())
        leftbox.addWidget(self.info)
        return leftbox

    def right(self):
        rightbox = QVBoxLayout()

        self.log = QTextEdit()
        self.log.setReadOnly(True)

        rightbox.addWidget(self.log)
        return rightbox

    def prompt(self, inpu: str):
        inputs = QHBoxLayout()
        lineedit = QLineEdit()
        linetext = QLabel()
        linetext.setText(inpu)

        inputs.addWidget(linetext)
        inputs.addWidget(lineedit)

        return {
            "layout": inputs,
            "input": lineedit
        }

    def change(self) -> None:
        num = self.i["input"].text()
        name = self.i2["input"].text()

        try:
            num = int(num)
        except:
            self.info.setText("Must be a number")
            return
        stacks = math.floor(num/64)
        leftovers = num-(stacks*64)

        self.info.setText(f"{stacks} stacks and {leftovers} {name.lower()}")

    def buttons(self):
        layout = QHBoxLayout()
        button = QPushButton()
        button.setText("Save to file")
        button.clicked.connect(self.save_to_file)

        button1 = QPushButton()
        button1.setText("Add to list")
        button1.clicked.connect(self.add_to_list)

        layout.addWidget(button1)
        layout.addWidget(button)

        return layout

    def add_to_list(self):
        current_text = self.info.text()
        if(current_text not in self.list):
            self.list.append(current_text)
        self.log.setPlainText("\n".join(self.list))

    def save_to_file(self):
        name = QFileDialog().getSaveFileName(
            caption='Save File', filter="Text Files (*.txt)")
        if not name[0]:
            return
        file = open(name[0], 'w')
        text = self.log.toPlainText()
        file.write(text)
        file.close()