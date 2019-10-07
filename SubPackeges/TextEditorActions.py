from PyQt5.Qt import QFileInfo
from SubPackeges.TextEditorUi import window
from PyQt5.QtWidgets import QFontDialog,QColorDialog,QFileDialog,QMessageBox,QDialog,QApplication,QWidget
from PyQt5.QtPrintSupport import QPrinter,QPrintPreviewDialog,QPrintDialog
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import Qt
from SubPackeges.keyboard import Ui_clavier
import datetime
import calendar
import sys

class Window(window):
    def __init__(self):
        super().__init__()
        self.font = QFont()
        self.cpt = 1
        self.cpti = 1
        self.cptu = 1
        self.copyaction.triggered.connect(self.copyfunction)
        self.cutaction.triggered.connect(self.cutfunction)
        self.pastaction.triggered.connect(self.pasteaction)
        self.deleteaction.triggered.connect(self.deletefunction)
        self.selectall.triggered.connect(self.selectfunction)
        self.redoaction.triggered.connect(self.textedit.redo)
        self.undoaction.triggered.connect(self.textedit.undo)
        self.printaction.triggered.connect(self.printfunction)
        self.printpreviewaction.triggered.connect(self.printpreviewDialog)
        self.exportaction.triggered.connect(self.exportPDF)
        self.openaction.triggered.connect(self.openfunction)
        self.newaction.triggered.connect(self.newfunction)
        self.saveaction.triggered.connect(self.savefunction)
        self.exitaction.triggered.connect(self.close)
        self.fontaction.triggered.connect(self.fontfunction)
        self.coloraction.triggered.connect(self.colorfunction)
        self.boldaction.triggered.connect(self.boldfunction)
        self.italicaction.triggered.connect(self.italicfunction)
        self.leftaction.triggered.connect(self.leftfunction)
        self.rightaction.triggered.connect(self.rightfunction)
        self.centeraction.triggered.connect(self.centerfunction)
        self.justifyaction.triggered.connect(self.justifyfunction)
        self.blue.triggered.connect(lambda:self.colorrfunction('blue'))
        self.grey.triggered.connect(lambda:self.colorrfunction('grey'))
        self.green.triggered.connect(lambda:self.colorrfunction('green'))
        self.white.triggered.connect(lambda: self.colorrfunction(''))
        self.bluetype.triggered.connect(lambda:self.typefunction('blue'))
        self.greentype.triggered.connect(lambda :self.typefunction('green'))
        self.rosetype.triggered.connect(lambda :self.typefunction('rose'))
        self.yellowtype.triggered.connect(lambda:self.typefunction('yellow'))
        self.simpletype.triggered.connect(lambda:self.typefunction('black'))
        self.aboutaction.triggered.connect(self.aboutfunction)
        self.contactaction.triggered.connect(self.contactfunction)
        self.keyboardaction.triggered.connect(self.keyboard)
        self.dateaction.triggered.connect(lambda:self.function('date'))
        self.timeaction.triggered.connect(lambda:self.function('time'))

    def copyfunction(self):
        self.textedit.copy()
    def cutfunction(self):
        self.textedit.cut()
    def pasteaction(self):
        self.textedit.paste()
    def deletefunction(self):
        text=self.textedit.clear()
    def selectfunction(self):
        self.textedit.selectAll()
    def printfunction(self):
        printer=QPrinter(QPrinter.HighResolution)
        dialog=QPrintDialog(printer,self)
        if dialog.exec_()==QPrintDialog.Accepted:
            self.textedit.print_(printer)
    def printpreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.print)
        previewDialog.exec_()
    def print(self,printer):
            self.textedit.print_(printer)
    def exportPDF(self):
        file,_=QFileDialog.getSaveFileName(self, 'Export PDF', None, 'PDF files (.pdf);;All Files()')
        if file!="":
            if QFileInfo(file).suffix()=="":file+= '.pdf'
            printer=QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(file)
            self.textedit.document().print_(printer)
    def openfunction(self):
        file=QFileDialog.getOpenFileName(self,'Open File','/home')
        if file[0]:
            f=open(file[0],'r')
            with f:
                data=f.read()
                self.textedit.setText(data)
    def savefunction(self):
        filename=QFileDialog.getSaveFileName(self,'Save File',None,'text Files (*.txt) ;; All Files()')
        if filename[0]:
            file=open(filename[0],'w')
            with file:
                text = self.textedit.toPlainText()
                file.write(text)

    def newfunction(self):
        message = QMessageBox.question(self, "Save File", "Do You Want To Save File",
                                       QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel , QMessageBox.No)
        if message == QMessageBox.Yes:
            self.savefunction()
        else:
            self.textedit.clear()
    def fontfunction(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.textedit.setFont(font)
    def colorfunction(self):
        color=QColorDialog.getColor()
        self.textedit.setTextColor(color)

    def boldfunction(self):
        self.cpt += 1

        if self.cpt%2==0:

            self.font.setBold(True)
            self.textedit.setCurrentFont(self.font)

        else :

            self.font.setBold(False)
            self.textedit.setCurrentFont(self.font)

    def italicfunction(self):
        self.cpt+= 1
        if self.cpt%2==0:

            self.font.setItalic(True)
            self.textedit.setCurrentFont(self.font)
        else :

            self.font.setItalic(False)
            self.textedit.setCurrentFont(self.font)
    def underline(self):
        self.cpt += 1
        if self.cpt % 2 == 0:

            self.font.setUnderline(True)
            self.textedit.setCurrentFont(self.font)
        else:

            self.font.setUnderline(False)
            self.textedit.setCurrentFont(self.font)
    def leftfunction(self):
        self.textedit.setAlignment(Qt.AlignLeft)
    def rightfunction(self):
        self.textedit.setAlignment(Qt.AlignRight)
    def centerfunction(self):
        self.textedit.setAlignment(Qt.AlignCenter)
    def justifyfunction(self):
        self.textedit.setAlignment(Qt.AlignJustify)
    def colorrfunction(self,color):

        self.setStyleSheet('background-color:{}'.format(color))
        self.textedit.setStyleSheet('background-color:white')
    def aboutfunction(self):
        message=QMessageBox.about(self,'about TeEditor','if you have probelem report in our web site')
    def contactfunction(self):
        message=QMessageBox.about(self,'Contact us','TeEditor Create By Khireddine Belkhiri\n Email: khireddinekhirou123@gmail.com\n Fb: khireddine belkhiri \n github: khireddine belkhiri')
    def typefunction(self,color):
        if color=='black':
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
        else:
            ####  File Actions Icon's ####
            self.newaction.setIcon(QIcon('Icons/{}/open-file.ico'.format(color)))
            self.openaction.setIcon(QIcon('Icons/{}/file.ico'.format(color)))
            self.saveaction.setIcon(QIcon('Icons/{}/save.ico'.format(color)))
            self.printaction.setIcon(QIcon('Icons/{}/printer.ico'.format(color)))
            self.printpreviewaction.setIcon(QIcon('Icons/{}/preview.ico'.format(color)))
            self.exportaction.setIcon(QIcon('Icons/{}/pdf.png'.format(color)))
            self.exitaction.setIcon(QIcon('Icons/{}/exit.ico'.format(color)))

            ####        Edit Actions  Icon's      ####
            self.copyaction.setIcon(QIcon('Icons/{}/copy.ico'.format(color)))
            self.cutaction.setIcon(QIcon('Icons/{}/cut.ico'.format(color)))
            self.pastaction.setIcon(QIcon('Icons/{}/paste.ico'.format(color)))
            self.undoaction.setIcon(QIcon('Icons/{}/undo.ico'.format(color)))
            self.redoaction.setIcon(QIcon('Icons/{}/redo.ico'.format(color)))
            self.selectall.setIcon(QIcon('Icons/{}/selectall.png'.format(color)))
            self.deleteaction.setIcon(QIcon('Icons/{}/delete.png'.format(color)))
            ####        Format Actions Icon's      ####
            self.fontaction.setIcon(QIcon('Icons/{}/font.ico'.format(color)))
            self.coloraction.setIcon(QIcon('Icons/{}/color.png'.format(color)))
            self.keyboardaction.setIcon(QIcon('Icons/{}/keyboard.png'.format(color)))
            ####        Style Actions  Icon's     ####
            self.boldaction.setIcon(QIcon('Icons/{}/bold.ico'.format(color)))
            self.italicaction.setIcon(QIcon('Icons/{}/italic.ico'.format(color)))
            self.underlinaction.setIcon(QIcon('Icons/{}/underline.ico'.format(color)))
            self.leftaction.setIcon(QIcon('Icons/{}/left-alignment.ico'.format(color)))
            self.rightaction.setIcon(QIcon('Icons/{}/right-alignment.ico'.format(color)))
            self.centeraction.setIcon(QIcon('Icons/{}/center-alignment.ico'.format(color)))
            self.justifyaction.setIcon(QIcon('Icons/{}/justify-align.ico'.format(color)))
            ####        Time and Date Actions Icon's ####
            self.timeaction.setIcon(QIcon('Icons/{}/time.png'.format(color)))
            self.dateaction.setIcon(QIcon('Icons/{}/date.png'.format(color)))
            ####        Options Actions   Icon's  ####
            self.windowcolor.setIcon(QIcon('Icons/{}/windowcolor.png'.format(color)))
            self.windowtype.setIcon(QIcon('Icons/{}/windowtype.png'.format(color)))
            ####        Help Actions Icon's   ####
            self.aboutaction.setIcon(QIcon('Icons/{}/about.png'.format(color)))
            self.contactaction.setIcon(QIcon('Icons/{}/contact.png'.format(color)))
    def keyboard(self):
        mydialog = QDialog(self)
        self.ui=Ui_clavier()
        self.ui.setupUi(mydialog)
        mydialog.show()
    def function(self,type):
        dt = datetime.datetime.now()
        if type=='date':
            year=dt.year
            month=dt.month
            day=dt.day
            nameday=dt.strftime('%A')
            date='today is {}'.format(nameday)+'\n'+'Corresponding {}-{}-{}'.format(year,month,day)
            self.textedit.setText(date)
        elif type=='time':
            hour=dt.hour
            minute=dt.minute
            second=dt.second
            time='{}:{}:{}'.format(hour,minute,second)
            self.textedit.setText(time)
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

