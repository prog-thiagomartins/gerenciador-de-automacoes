from pages.catalog_page import CatalogPage
from pages.my_automations_page import MyAutomationsPage
from pages.settings_page import SettingsPage

MENU_CONFIG = [
    {"name": "Catálogo", "icon": "assets/icons/catalog.svg", "page": CatalogPage},
    {"name": "Minhas automações", "icon": "assets/icons/smart_toy.svg", "page": MyAutomationsPage},
    {"name": "Configurações", "icon": "assets/icons/settings.svg", "page": SettingsPage},
]

LOGO_ICON_PATH = "assets/icons/logo.png"
CLOSE_SIDE_MENU_ICON = "assets/icons/close_side_menu.svg"
OPEN_SIDE_MENU_ICON = "assets/icons/open_side_menu.svg"