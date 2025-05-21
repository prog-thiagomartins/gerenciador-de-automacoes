import sys
from PyQt6.QtWidgets import QMainWindow, QListWidgetItem, QWidget
from PyQt6.QtGui import QPixmap,QIcon
from PyQt6.QtCore import Qt, QSize
from ui.ui_main_window import Ui_MainWindow
from config.side_menu_config import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # initialize the UI from the generated 'main_ui' class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Set window properties
        self.setWindowIcon(QIcon(LOGO_ICON_PATH))
        self.setWindowTitle("APP DE AUTOMAÇÃO - EM DESENVOLVIMENTO")
        
        # Initialize UI Elements
        self.title_label = self.ui.title_label
        self.title_label.setText("Automatize")
        
        self.title_icon = self.ui.title_icon
        self.title_icon.setText("")
        self.title_icon.setPixmap(QPixmap(LOGO_ICON_PATH))
        self.title_icon.setFixedSize(32, 32)
        self.title_icon.setScaledContents(True)
        
        self.side_menu = self.ui.side_menu
        self.side_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        self.side_menu_icon_only = self.ui.side_menu_icon_only
        self.side_menu_icon_only.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon_only.hide()
        
        self.menu_btn = self.ui.menu_btn
        self.menu_btn.setText("")
        self.menu_btn.setIcon(QIcon(CLOSE_SIDE_MENU_ICON))
        self.menu_btn.setIconSize(QSize(30, 30))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setChecked(False)
        
        
        self.main_content = self.ui.stackedWidget

        # Define a list of menu items with names and icons
        self.menu_list = MENU_CONFIG
        
        # Initialize the UI elements and slots
        self.init_list_widget()
        self.init_stacked_widget()
        self.init_signal_slot()
               
    def init_signal_slot(self):
        # connect signals and slots for menu button and side menu
        self.menu_btn.toggled["bool"].connect(self.side_menu.setHidden)
        self.menu_btn.toggled["bool"].connect(self.title_label.setHidden)
        self.menu_btn.toggled["bool"].connect(self.title_icon.setHidden)
        self.menu_btn.toggled["bool"].connect(self.side_menu_icon_only.setVisible)
        self.menu_btn.toggled.connect(self.button_icon_change)
        
        # Connect signals and slots for swiching between menu items
        self.side_menu.currentRowChanged["int"].connect(self.main_content.setCurrentIndex)
        self.side_menu_icon_only.currentRowChanged["int"].connect(self.main_content.setCurrentIndex)
        
        self.side_menu.currentRowChanged["int"].connect(self.side_menu_icon_only.setCurrentRow)
        self.side_menu_icon_only.currentRowChanged["int"].connect(self.side_menu.setCurrentRow)
               
    def init_list_widget(self):
        # Initialize the side menu and side menu with icons only
        self.side_menu.clear()
        self.side_menu_icon_only.clear()
        
        for menu in self.menu_list:
            # Set items for the side menu with icons only
            item = QListWidgetItem()
            item.setIcon(QIcon(menu.get("icon")))
            item.setSizeHint(QSize(40,40))
            self.side_menu_icon_only.addItem(item)
            
            
            # Set items for the side menu with icons and text
            item_new = QListWidgetItem()
            item_new.setIcon(QIcon(menu.get("icon")))
            item_new.setText(menu.get("name"))
            self.side_menu.addItem(item_new)
        
        self.side_menu.setCurrentRow(0)
        self.side_menu_icon_only.setCurrentRow(0)
        
    def init_stacked_widget(self):
        # Limpa widgets existentes
        widget_list = self.main_content.findChildren(QWidget)
        for widget in widget_list:
            self.main_content.removeWidget(widget)

        for menu in self.menu_list:
            PageClass = menu.get("page")
            if PageClass:
                page_instance = PageClass()
                self.main_content.addWidget(page_instance)
        
        self.main_content.setCurrentIndex(0)
   
    def button_icon_change(self, status):
        # Change the menu button icon based on its status
        if status:
            self.menu_btn.setIcon(QIcon(OPEN_SIDE_MENU_ICON))
        else:
            self.menu_btn.setIcon(QIcon(CLOSE_SIDE_MENU_ICON))