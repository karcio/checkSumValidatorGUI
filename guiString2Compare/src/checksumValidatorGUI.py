#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2 Jan 2015

@author: crystal
'''
import sys

from PyQt4 import QtGui, QtCore


class CheckSum(QtGui.QWidget):
    
    def __init__(self):
        super(CheckSum, self).__init__()
        self.initUI()

        
    def initUI(self):        
        
        
        self.stringLabel1 = QtGui.QLabel('First  string ')
        self.stringLabel2 = QtGui.QLabel('Second string')
        self.stringLabel3 = QtGui.QLabel('Result')
        self.stringLabel4 = QtGui.QLabel()   
        
        self.stringLineEdit1 = QtGui.QLineEdit()
        self.stringLineEdit1.setMaximumWidth(250)
        self.stringLineEdit1.setMaxLength(32)
        
        self.stringLineEdit2 = QtGui.QLineEdit()
        self.stringLineEdit2.setMaximumWidth(250)
        self.stringLineEdit2.setMaxLength(32)
        
        self.stringLineEdit3 = QtGui.QLineEdit()
        
        self.button1 = QtGui.QPushButton('validate')
       
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.stringLabel1, 0, 0)
        grid.addWidget(self.stringLineEdit1, 0, 1)

        grid.addWidget(self.stringLabel2, 1, 0)
        grid.addWidget(self.stringLineEdit2, 1, 1)
        
        grid.addWidget(self.stringLabel3, 2, 0)
        grid.addWidget(self.stringLabel4, 2, 1)
        
        grid.addWidget(self.button1, 3, 1)
        
        self.button1.clicked.connect(self.handleButton)
        
        self.setLayout(grid) 
        self.resize(400, 100)
        self.center()  
        self.setWindowTitle('Checksum Validator v.0.1')    
        self.show()
    
    
    def handleButton(self):
                  
        text1 = self.stringLineEdit1.text()
        text2 = self.stringLineEdit2.text()
               
        if text1 == text2:
            result = "True"
            
        else:
            result = "False"
           
        self.stringLabel4.setText(repr(result))
         
   
    def center(self):
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())    
   
        
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
    
    
    def keyPressEvent(self, e):
        
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
    
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = CheckSum()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
