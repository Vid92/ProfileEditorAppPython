# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ComboBoxTime(QtWidgets.QStyledItemDelegate):
	def __init__(self,parent=None):
		super(ComboBoxTime, self).__init__()
		self.parent = parent

	def createEditor(self, parent, option, index):
		cbt = QtWidgets.QComboBox(parent)
		x = self.parent.tableWidget.currentRow()
		opt = self.parent.tableWidget.item(x,0).text()
		#print("opt:",opt)
		if opt == "Charge":
			cbt.addItem("AH")
			cbt.addItem("H")
		elif opt == "Pause":
			cbt.addItem("H")
			
		return cbt

	def setEditorData(self, editor, index):
		cbIndex = index.model().data(index,QtCore.Qt.EditRole)
		if cbIndex!='-':
			editor.setCurrentText(cbIndex)

	def setModelData(self,editor,model,index):
		model.setData(index,editor.currentText(),QtCore.Qt.EditRole)

'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
'''