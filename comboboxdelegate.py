# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ComboBoxDelegate(QtWidgets.QStyledItemDelegate):
	def createEditor(self, parent, option, index):
		cb = QtWidgets.QComboBox(parent)
		cb.addItem("Charge")
		cb.addItem("Pause")
		return cb

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