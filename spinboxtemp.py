# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class SpinBoxTemp(QtWidgets.QStyledItemDelegate):
	def createEditor(self, parent, option, index):
		editor = QtWidgets.QDoubleSpinBox(parent)
		editor.setFrame(False)
		editor.setDecimals(1)
		editor.setMinimum(0.0)
		editor.setMaximum(80)

		return editor

	def setEditorData(self,spintemp , index):
		value = index.model().data(index,QtCore.Qt.EditRole)
		if value !='-':
			spintemp.setValue(value)

	def setModelData(self,spintemp,model,index):
		spintemp.interpretText()
		value = spintemp.value()
		model.setData(index,value,QtCore.Qt.EditRole)

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