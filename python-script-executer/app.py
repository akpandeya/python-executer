# This Python file uses the following encoding: utf-8
import os
import sys
from pathlib import Path
from PySide2.QtWidgets import QWidget,QTreeView, QAction, QPushButton, QMainWindow, QListView
from PySide2.QtWidgets import QFileDialog, QFileSystemModel, QWidget, QVBoxLayout, QGridLayout, QHBoxLayout
from PySide2.QtCore import QFile, qApp, QDir, Qt
from PySide2.QtGui import QStandardItem, QStandardItemModel

from filesSelector import filesSelector

class MainWindow(QMainWindow,filesSelector ):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self,*args, **kwargs)
        filesSelector.__init__(self)
        
        self.setWindowTitle("Python Script Executer")
        self.page_layout = QGridLayout()
        self.page = QWidget()
        self.page.setLayout(self.page_layout)
        self.setCentralWidget(self.page)
        self.page_layout.addWidget(self.directory_browse,0,0)