# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class TimeDelegate(QtWidgets.QStyledItemDelegate):
	def createEditor(self, parent, option, index):
		timeEdit = QtWidgets.QDoubleSpinBox(parent)
		timeEdit.setFrame(False)
		timeEdit.setDecimals(4)
		timeEdit.setMinimum(0.0000)
		timeEdit.setMaximum(1000)

		return timeEdit

	def setEditorData(self, editor, index):
		value = index.model().data(index,QtCore.Qt.DisplayRole)
		if value !='-':
			editor.setValue(value)

	def setModelData(self,editor,model,index):
		editor.interpretText()
		value = editor.value()
		model.setData(index,value,QtCore.Qt.EditRole)
