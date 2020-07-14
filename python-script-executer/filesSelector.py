import os
import sys
from pathlib import Path
from PySide2.QtWidgets import QWidget,QTreeView, QAction, QPushButton, QMainWindow, QListView
from PySide2.QtWidgets import QFileDialog, QFileSystemModel, QWidget, QVBoxLayout, QGridLayout, QHBoxLayout
from PySide2.QtCore import QFile, qApp, QDir, Qt
from PySide2.QtGui import QStandardItem, QStandardItemModel

class filesSelector(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(filesSelector, self).__init__(*args, **kwargs)
        self.directory_browse =  QWidget()
        self.directory_browse_layout = QVBoxLayout()
        self.directory_browse.setLayout(self.directory_browse_layout)

        self.file_list_view = QListView()
        self.file_list_view.setObjectName("treeView")
        self.directory_browse_layout.addWidget(self.file_list_view)

        self.file_option_widget =  QWidget()
        self.file_option_widget_layout = QHBoxLayout()
        self.file_option_widget.setLayout(self.file_option_widget_layout)
        self.directory_browse_layout.addWidget(self.file_option_widget)

        self.select_folder_button = QPushButton()
        self.select_folder_button.setObjectName("browseButton")
        self.select_folder_button.setText("Select Folder")
        self.file_option_widget_layout.addWidget(self.select_folder_button)

        self.select_file_button = QPushButton()
        self.select_file_button.setObjectName("browseButton")
        self.select_file_button.setText("Select File")
        self.file_option_widget_layout.addWidget(self.select_file_button)

        


        self.file_model = QStandardItemModel()
        

    def select_folder(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly)

        self.directoryUrl = dialog.getExistingDirectoryUrl()

        directory_model = QFileSystemModel()
        #directory_model.setRootPath(QDir.currentPath()) 
        directory_model.setRootPath(QDir.currentPath())
        #directory_model.directoryLoaded(self.directoryUrl.toDisplayString())
        self.selected_folder = self.directoryUrl.toDisplayString()[7:]
        self.nameFileArray = [f for f in os.listdir(self.selected_folder) if os.path.isfile(os.path.join(self.selected_folder, f))]
        
        item = QStandardItem("All")
        item.setCheckState(Qt.Checked)
        item.setCheckable(True)
        self.file_model.appendRow(item)
        for name in self.nameFileArray:
            item = QStandardItem(name)
            item.setCheckState(Qt.Checked)
            item.setCheckable(True)
            self.file_model.appendRow(item)
        self.file_list_view.setModel(self.file_model)
        #self.treeView.setModel(directory_model)
        #self.treeView.setRootIndex(directory_model.index(self.directoryUrl.toDisplayString()))