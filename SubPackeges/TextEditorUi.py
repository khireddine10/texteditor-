from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import sys


class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'TeEditor'
        self.icon = 'Icons/TextEditorIcon.ico'
        self.width = 700
        self.height = 500
        self.CreatWindow()

    def CreatWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))
        self.resize(self.width, self.height)
        self.components()
        # self.setStyleSheet('background-color:red')
        self.show()

    def components(self):
        self.toolbar = self.addToolBar('toolbar')
        self.menubar()
        self.textedit = QTextEdit()
        self.setCentralWidget(self.textedit)
        self.actions()
        self.icons()

    def menubar(self):
        menubar = self.menuBar()
        self.file = menubar.addMenu('File')
        self.edit = menubar.addMenu('Edit')
        self.format = menubar.addMenu('Format')
        self.style = menubar.addMenu('Style')
        self.date = menubar.addMenu('Time and Date')
        self.options = menubar.addMenu('Options')
        self.help = menubar.addMenu('Help')

    def toolbar(self):
        pass

    def actions(self):
        ####        File Actions         ####
        self.newaction = QAction('New')
        self.openaction = QAction('Open')
        self.saveaction = QAction('Save')
        self.printaction = QAction('Print')
        self.printpreviewaction = QAction('PrintPreviw')
        self.exportaction = QAction('Export PDF')
        self.exitaction = QAction('Exit')
        self.file.addAction(self.newaction)
        self.file.addAction(self.openaction)
        self.file.addAction(self.saveaction)
        self.file.addAction(self.printaction)
        self.file.addAction(self.printpreviewaction)
        self.file.addAction(self.exportaction)
        self.file.addAction(self.exitaction)

        ####        Edit Actions        ####
        self.copyaction = QAction('Copy')
        self.cutaction = QAction('Cut')
        self.pastaction = QAction('paste')
        self.deleteaction = QAction('Delete')
        self.selectall = QAction('Select All')
        self.undoaction = QAction('Undo')
        self.redoaction = QAction('Rudo')

        self.edit.addAction(self.copyaction)
        self.edit.addAction(self.cutaction)
        self.edit.addAction(self.pastaction)
        self.edit.addAction(self.deleteaction)
        self.edit.addAction(self.selectall)
        self.edit.addAction(self.undoaction)
        self.edit.addAction(self.redoaction)
        self.toolbar.addAction(self.copyaction)
        self.toolbar.addAction(self.cutaction)
        self.toolbar.addAction(self.pastaction)
        self.toolbar.addAction(self.deleteaction)
        self.toolbar.addAction(self.selectall)
        self.toolbar.addAction(self.undoaction)
        self.toolbar.addAction(self.redoaction)
        self.toolbar.addAction(self.printaction)
        self.toolbar.addAction(self.printpreviewaction)
        self.toolbar.addAction(self.exportaction)

        ####        Format Actions      ####
        self.fontaction = QAction('Font')
        self.coloraction = QAction('FontColor')
        self.keyboardaction = QAction('Keyboard')
        self.format.addAction(self.keyboardaction)
        self.format.addAction(self.fontaction)
        self.format.addAction(self.coloraction)
        self.toolbar.addAction(self.fontaction)
        self.toolbar.addAction(self.coloraction)
        self.toolbar.addAction(self.keyboardaction)

        ####        Style Actions       ####
        self.boldaction = QAction('Bold')
        self.italicaction = QAction('Italic')
        self.underlinaction = QAction('Underline')
        self.leftaction = QAction('Left')
        self.rightaction = QAction('Right')
        self.centeraction = QAction('Center')
        self.justifyaction = QAction('Justify')
        self.style.addAction(self.boldaction)
        self.style.addAction(self.italicaction)
        self.style.addAction(self.underlinaction)
        self.style.addAction(self.leftaction)
        self.style.addAction(self.rightaction)
        self.style.addAction(self.centeraction)
        self.style.addAction(self.justifyaction)
        self.toolbar.addAction(self.boldaction)
        self.toolbar.addAction(self.italicaction)
        self.toolbar.addAction(self.underlinaction)
        self.toolbar.addAction(self.leftaction)
        self.toolbar.addAction(self.rightaction)
        self.toolbar.addAction(self.centeraction)
        self.toolbar.addAction(self.justifyaction)

        ####        Time and Date Actions ####
        self.timeaction = QAction('Time')
        self.dateaction = QAction('Date')
        self.date.addAction(self.timeaction)
        self.date.addAction(self.dateaction)
        # self.date.addAction(self.dateaction)

        ####        Options Actions     ####
        self.windowcolor = self.options.addMenu('Window Color')
        self.grey = QAction(QIcon('Icons/grey.png'), 'Grey', self)
        self.blue = QAction(QIcon('Icons/blue.png'), 'Blue', self)
        self.green = QAction(QIcon('Icons/green.png'), 'Green', self)
        self.white = QAction(QIcon('Icons/white.png'), 'Simple', self)
        self.windowcolor.addAction(self.grey)
        self.windowcolor.addAction(self.green)
        self.windowcolor.addAction(self.blue)
        self.windowcolor.addAction(self.white)
        self.windowtype = self.options.addMenu('Window Options')
        self.greentype = QAction(QIcon('Icons/green.png'), 'green Type', self)
        self.rosetype = QAction(QIcon('Icons/rose.png'), 'Rose Type', self)
        self.bluetype = QAction(QIcon('Icons/blue.png'), 'Blue Type', self)
        self.yellowtype = QAction(QIcon('Icons/yellow.png'), 'Yellow Type', self)
        self.simpletype = QAction(QIcon('Icons/black.png'), 'Simple Type', self)
        self.windowtype.addAction(self.greentype)
        self.windowtype.addAction(self.rosetype)
        self.windowtype.addAction(self.bluetype)
        self.windowtype.addAction(self.yellowtype)
        self.windowtype.addAction(self.simpletype)

        ####        Help Actions    ####
        self.aboutaction = QAction('About')
        self.contactaction = QAction('Contact')
        self.help.addAction(self.aboutaction)
        self.help.addAction(self.contactaction)

    def icons(self):
        ####  File Actions Icon's ####
        self.newaction.setIcon(QIcon('Icons/black/open-file.ico'))
        self.openaction.setIcon(QIcon('Icons/black/file.ico'))
        self.saveaction.setIcon(QIcon('Icons/black/save.ico'))
        self.printaction.setIcon(QIcon('Icons/black/printer.ico'))
        self.printpreviewaction.setIcon(QIcon('Icons/black/preview.ico'))
        self.exportaction.setIcon(QIcon('Icons/black/pdf.png'))
        self.exitaction.setIcon(QIcon('Icons/black/exit.ico'))

        ####        Edit Actions  Icon's      ####
        self.copyaction.setIcon(QIcon('Icons/black/copy.ico'))
        self.cutaction.setIcon(QIcon('Icons/black/cut.png'))
        self.pastaction.setIcon(QIcon('Icons/black/paste.ico'))
        self.undoaction.setIcon(QIcon('Icons/black/undo.png'))
        self.redoaction.setIcon(QIcon('Icons/black/redo.png'))
        self.selectall.setIcon(QIcon('Icons/black/selectall.png'))
        self.deleteaction.setIcon(QIcon('Icons/black/delete.png'))
        ####        Format Actions Icon's      ####
        self.fontaction.setIcon(QIcon('Icons/black/font.ico'))
        self.coloraction.setIcon(QIcon('Icons/black/colorr.ico'))
        self.keyboardaction.setIcon(QIcon('Icons/black/keyboard.png'))
        ####        Style Actions  Icon's     ####
        self.boldaction.setIcon(QIcon('Icons/black/bold.ico'))
        self.italicaction.setIcon(QIcon('Icons/black/italic.ico'))
        self.underlinaction.setIcon(QIcon('Icons/black/underline.ico'))
        self.leftaction.setIcon(QIcon('Icons/black/left-alignment.ico'))
        self.rightaction.setIcon(QIcon('Icons/black/align-right.ico'))
        self.centeraction.setIcon(QIcon('Icons/black/center-alignment.ico'))
        self.justifyaction.setIcon(QIcon('Icons/black/justify.ico'))
        ####        Time and Date Actions Icon's ####
        self.timeaction.setIcon(QIcon('Icons/black/time.png'))
        self.dateaction.setIcon(QIcon('Icons/black/date.png'))
        ####        Options Actions   Icon's  ####
        self.windowcolor.setIcon(QIcon('Icons/black/windowcolor.png'))
        self.windowtype.setIcon(QIcon('Icons/black/windowtype.png'))
        ####        Help Actions Icon's   ####
        self.aboutaction.setIcon(QIcon('Icons/black/about.png'))
        self.contactaction.setIcon(QIcon('Icons/black/contact.png'))






