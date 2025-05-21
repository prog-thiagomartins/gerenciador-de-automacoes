import sys
import os
from PyQt6.QtWidgets import  QApplication
from pages.main_window import MainWindow

# Define o diretório raiz do projeto como o CWD
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Load style file
    with open("assets/styles.qss") as f:
        style_str = f.read()
    app.setStyleSheet(style_str)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())