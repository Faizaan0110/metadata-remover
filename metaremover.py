import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QMessageBox, QTextEdit
from PyQt5.QtCore import Qt
from PIL import Image, ExifTags
import datetime
import os


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Metadata Cleaner')
        self.setGeometry(300, 300, 400, 300)
        self.setStyleSheet("background-color: black; color: white;")
        
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file_dialog)
        file_menu.addAction(open_action)
        clear_metadata_action = QAction('Clear Metadata', self)
        clear_metadata_action.triggered.connect(self.clear_metadata)
        menubar.addAction(clear_metadata_action)
        
        self.metadata_display = QTextEdit(self)
        self.metadata_display.setGeometry(0, 100, 400, 200)
        self.metadata_display.setStyleSheet("background-color: black; color: white;")
        self.metadata_display.setReadOnly(True)
        
        self.file_path = None
        self.show()
