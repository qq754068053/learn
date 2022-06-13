import sys
import PySide6.QtWidgets


def GetApp():

    app = PySide6.QtWidgets.QApplication(sys.argv)
    w = PySide6.QtWidgets.QWidget()
    w.setWindowTitle('Simple')
    btn = PySide6.QtWidgets.QPushButton('Hello PyQt6!', w)
    btn.move(50, 50)
    w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    GetApp()
