import os
import sys
from pathlib import Path
from PySide2.QtWidgets import QWidget,QTreeView, QAction, QPushButton, QMainWindow, QListView, QComboBox
from PySide2.QtWidgets import QFileDialog, QFileSystemModel, QWidget, QVBoxLayout, QGridLayout, QHBoxLayout
from PySide2.QtCore import QFile, qApp, QDir, Qt
from PySide2.QtGui import QStandardItem, QStandardItemModel
from fliletypes import *

class filesSelector(QWidget):
    def __init__(self, *args, **kwargs):
        #super(filesSelector, self).__init__(*args, **kwargs)

        #Widget for displaying all the options for adding files to the view
        self.directory_browse =  QWidget()
        self.directory_browse_layout = QVBoxLayout()
        self.directory_browse.setLayout(self.directory_browse_layout)

        #List View for displaying the files which have been selected for processing
        self.file_list_view = QListView()
        self.file_list_view.setObjectName("treeView")
        self.directory_browse_layout.addWidget(self.file_list_view)
        
        #The widget within the Directory_Browse widget which will contain all the options for loading files
        self.file_option_widget =  QWidget()
        self.file_option_widget_layout = QHBoxLayout()
        self.file_option_widget.setLayout(self.file_option_widget_layout)
        self.directory_browse_layout.addWidget(self.file_option_widget)

        #The button for browsing to the folder which needs to be added
        self.select_folder_button = QPushButton()
        self.select_folder_button.setObjectName("browseButton")
        self.select_folder_button.setText("Select Folder")
        self.file_option_widget_layout.addWidget(self.select_folder_button)

        #The button for adding selected files from a directory
        self.select_file_button = QPushButton()
        self.select_file_button.setObjectName("browseButton")
        self.select_file_button.setText("Select File")
        self.file_option_widget_layout.addWidget(self.select_file_button)

        #The widget which will contain the list of all the extensions which are to be added
        # self.file_extension_widget = QWidget()
        # self.file_extension_widget.setObjectName("fileExtensionWidget")
        # self.file_extension_widget_layout = QHBoxLayout()
        # self.file_extension_widget.setLayout(self.file_option_widget_layout)
        # self.file_option_widget_layout.addWidget(self.file_extension_widget)

        #What happens when we click the browse directory button?
        self.select_folder_button.clicked.connect(self.select_folder)

        #Custom model to hold the names of the all the files which are selected
        self.file_model = QStandardItemModel()
        

    def select_folder(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly)

        self.directoryUrl = dialog.getExistingDirectoryUrl()

        self.selected_folder = self.directoryUrl.toDisplayString()[7:]
        self.nameFileArray = [f for f in os.listdir(self.selected_folder) if os.path.isfile(os.path.join(self.selected_folder, f))]
        

        # item = QStandardItem("All")
        # item.setCheckState(Qt.Checked)
        # item.setCheckable(True)
        #self.file_model.appendRow(item)
        
        #self.file_model, self.file_option_listview = self.create_checkBoxes(self.nameFileArray, self.file_model, self.file_option_listview)

        self.file_model = self.create_checkBoxes(self.nameFileArray, self.file_model, self.file_list_view)
        for name in self.nameFileArray:
            self.file_model.appendRow(self.append_checkbox(name, self.file_model, Qt.Checked))
        self.file_list_view.setModel(self.file_model)

        #self.file_model, self.file_option_listview = self.create_checkBoxes(self.nameFileArray, self.file_model, self.file_option_listview)

    def create_checkBoxes(self, array, model, view):
        model.appendRow(self.append_checkbox("All", model, Qt.Checked))
        # for item in array:
        #     model = self.append_checkbox(item, model, Qt.Checked)
        # view.setModel(model)
        return model

    def append_checkbox(self, item, model, checkdStatus):
        item = QStandardItem(item)
        item.setCheckState(checkdStatus)
        item.setCheckable(True)
        #model.appendRow(item)

        return item

