import sys
from PyQt5.QtWidgets import QApplication
from SubPackeges.TextEditorActions import Window

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())
