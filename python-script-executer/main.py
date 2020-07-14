from PySide2.QtWidgets import QApplication
from app import MainWindow
import sys

if __name__ == "__main__":
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show() # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec_()


    # Your application won't reach here until you exit and the event 
    # loop has stopped.
