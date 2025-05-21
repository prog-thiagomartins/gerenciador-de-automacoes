import sys
from PyQt6.QtWidgets import  QApplication
from pages.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Load style file
    with open("assets/styles.qss") as f:
        style_str = f.read()
    app.setStyleSheet(style_str)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())