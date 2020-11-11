# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class SpinBoxDelegate(QtWidgets.QStyledItemDelegate):
	def __init__(self,parent=None):
		super(SpinBoxDelegate, self).__init__()
		self.parent = parent
	
	def createEditor(self, parent, option, index):
		editor = QtWidgets.QDoubleSpinBox(parent)
		editor.setFrame(False)
		editor.setDecimals(1)
		editor.setMinimum(0.0)
		editor.setMaximum(25)
		return editor

	def setEditorData(self, spinbox, index):
		value = index.model().data(index,QtCore.Qt.EditRole)
		if value !='-':
			spinbox.setValue(value)

	def setModelData(self,spinbox,model,index):
		spinbox.interpretText()
		value = spinbox.value()
		model.setData(index,value,QtCore.Qt.EditRole)
