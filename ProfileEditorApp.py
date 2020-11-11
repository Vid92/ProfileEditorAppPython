# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from comboboxdelegate import ComboBoxDelegate
from spinboxdelegate import SpinBoxDelegate
from comboboxtime import ComboBoxTime
from timedelegate import TimeDelegate
from spinboxtemp import SpinBoxTemp

class Ui_ProfileEditor(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setFixedSize(1530, 923) #1280 923
		self.centralWidget = QtWidgets.QWidget(MainWindow)
		self.centralWidget.setObjectName("centralWidget")
		self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
		self.tableWidget.setGeometry(QtCore.QRect(195, 10, 825, 474))
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(6)
	#	self.tableWidget.setRowCount(0)
		#self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
		self.tableWidget.horizontalHeader().setHighlightSections(True)

		self.treeWidget = QtWidgets.QTreeWidget(self.centralWidget)
		self.treeWidget.setGeometry(QtCore.QRect(10, 10, 180, 740))
		self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.treeWidget.setObjectName("treeWidget")
		self.treeWidget.headerItem().setText(0, "1")
		self.treeWidget.setHeaderLabel("Programs")
		self.treeWidget.header().setDefaultAlignment(QtCore.Qt.AlignCenter)
		MainWindow.setCentralWidget(self.centralWidget)
		self.mainToolBar = QtWidgets.QToolBar(MainWindow)
		self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.mainToolBar.setObjectName("mainToolBar")
		MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
		self.statusBar = QtWidgets.QStatusBar(MainWindow)
		self.statusBar.setObjectName("statusBar")
		MainWindow.setStatusBar(self.statusBar)
		self.menuBar = QtWidgets.QMenuBar(MainWindow)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 616, 22))
		self.menuBar.setObjectName("menuBar")
		MainWindow.setMenuBar(self.menuBar)
		self.actionNuevo = QtWidgets.QAction(QtGui.QIcon('/opt/Ditsa/ProfileEditor/image/nuevo.png'),'New',MainWindow)
		self.actionGuardar = QtWidgets.QAction(QtGui.QIcon('/opt/Ditsa/ProfileEditor/image/guardar.png'),'Save',MainWindow)
		self.actionRenombrar = QtWidgets.QAction(QtGui.QIcon('/opt/Ditsa/ProfileEditor/image/renombrar.png'),'Rename',MainWindow)
		self.actionBorrar = QtWidgets.QAction(QtGui.QIcon('/opt/Ditsa/ProfileEditor/image/borrar.png'),'Delete',MainWindow)
		self.actionSalir = QtWidgets.QAction(QtGui.QIcon('/opt/Ditsa/ProfileEditor/image/salir.png'),'Exit',MainWindow)
		self.actionAgregar_Renglon = QtWidgets.QAction(QtGui.QIcon('/opt/Ditsa/ProfileEditor/image/agregarRenglon.png'),'AddRow',MainWindow)
		self.actionBorrar_Renglon = QtWidgets.QAction(QtGui.QIcon('/opt/Ditsa/ProfileEditor/image/borrarRenglon.png'),'DeleteRow',MainWindow)
		
		self.mainToolBar.addAction(self.actionNuevo)
		self.mainToolBar.addAction(self.actionGuardar)
		self.mainToolBar.addAction(self.actionRenombrar)
		self.mainToolBar.addAction(self.actionBorrar)
		self.mainToolBar.addAction(self.actionAgregar_Renglon)
		self.mainToolBar.addAction(self.actionBorrar_Renglon)
		self.mainToolBar.addAction(self.actionSalir)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		tableTitles = ['Operation Mode','Nominal Value','Termino','t/AH','Temp Max','Temp Min']
		self.tableWidget.setHorizontalHeaderLabels(tableTitles)

		MainWindow.showEvent = self.showEvent
		MainWindow.closeEvent = self.closeEvent
		#MainWindow.resizeEvent = self.resizeEvent

		self.filex = QtCore.QFile()
		self.programData = list() 
		self.tmpData = list()

		self.m_cProgramIndex = 0

		self.t = False			#flags
		self.save = False
		self.flagExit = False
		self.wmin = False
		self.flagText = False

		self.actionNuevo.triggered.connect(self.on_actionNew)
		self.actionGuardar.triggered.connect(self.on_actionSave)
		self.actionRenombrar.triggered.connect(self.on_actionRename)
		self.actionBorrar.triggered.connect(self.on_actionDelete)
		self.actionSalir.triggered.connect(self.on_actionExit)
		self.actionAgregar_Renglon.triggered.connect(self.on_actionAddRow)
		self.actionBorrar_Renglon.triggered.connect(self.on_actionDeleteRow)

		self.treeWidget.itemClicked.connect(self.on_treeItemClicked)
		self.treeWidget.itemDoubleClicked.connect(self.doubleClickedTree)
		self.treeWidget.itemChanged.connect(self.treeChanged)

		self.tableWidget.cellChanged.connect(self.tableCellCh)
	#	self.tableWidget.itemChanged.connect(self.tableItemCh)
		self.tableWidget.itemClicked.connect(self.on_tableItemClicked)
		
	#	MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowMinimizeButtonHint)

		self.MainWindow = MainWindow

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Profile Editor"))
		#MainWindow.setWindowIcon(QtGui.QIcon('/opt/Ditsa'))
		MainWindow.setWindowIcon(QtGui.QIcon('/opt/Ditsa/ProfileEditor/editorprograma1.png'))
		self.tableWidget.setColumnWidth(0,150)
		self.tableWidget.setColumnWidth(1,150)
		self.tableWidget.setColumnWidth(2,125)
		self.tableWidget.setColumnWidth(3,125)
		self.tableWidget.setColumnWidth(4,125)
		self.tableWidget.setColumnWidth(5,125)


	def showEvent(self,event): 
		print("ShowEvent")
		if self.wmin != True:
			self.loadSettings()
			self.populateTree()
			self.wmin = True

	def closeEvent(self,event):
		print("closeEvent")
		if self.t != False and self.save != True:
			if self.flagExit != True:
				msg = QtWidgets.QMessageBox()
				returnExit = msg.warning(self.MainWindow,'Warning',"Do you want to save changes in this file?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Cancel)

				if returnExit == msg.Yes:
					self.saveTable()
					if self.save != True:
						self.saveSettings()
						self.jsonTable()
						MainWindow.close()
					else:
						self.mssage_Information()

				elif returnExit == msg.No:
					MainWindow.close()
				elif returnExit == msg.Cancel:
					event.ignore()

		else:
			MainWindow.close()

	def resizeEvent(self,event):
		print("resizeEvent")

	def on_actionNew(self):
		print("on_actionNew")
		
		if self.t != True:
			if self.treeWidget.topLevelItemCount() + 1 < 11: 
				self.addTree()
			else:
				msg = QtWidgets.QMessageBox()
				msg.critical(self.MainWindow,'Error',"Invalid number of programs (1-10)")

		else:
			msg = QtWidgets.QMessageBox()
			quest = msg.question(self.MainWindow,'Warning',"Do you want to save changes you made?")

			if quest == msg.Yes:
				self.on_actionSave()

				if self.save != True:
					if self.treeWidget.topLevelItemCount() + 1 < 11: 
						self.addTree()
						self.t = False
					else:
						msg = QtWidgets.QMessageBox()
						msg.critical(self.MainWindow,'Error',"Invalid number of programs (1-10)")

			elif quest == msg.No:
				print("NO ITEM NEW")
				self.t = False
				print("pIdx0:",self.m_cProgramIndex)
				self.programData.clear()
				self.treeWidget.takeTopLevelItem(self.m_cProgramIndex-1)
				self.loadSettings()

				if len(self.programData) != 0:
					self.m_cProgramIndex = self.treeWidget.currentIndex().row() + 1
					print("pIdx:",self.m_cProgramIndex)
					itemTree = self.treeWidget.topLevelItem(self.m_cProgramIndex)
					itemTree.setSelected(True)
					self.populateTable(self.m_cProgramIndex)

	def addTree(self):
		print("addTree")
		topLevel = QtWidgets.QTreeWidgetItem()
		self.m_cProgramIndex = self.treeWidget.topLevelItemCount() + 1
		idx = str(self.m_cProgramIndex)
		print("idx:", self.m_cProgramIndex)

		#-------------------- Add Top Level (tree)-------------------#
		topLevel.setText(0,str(idx)+"-SGL")
		self.treeWidget.addTopLevelItem(topLevel)
		self.programData.append([idx+"-SGL","-,-,-,-,-,-"])

		#------------------------ Add Row 1 -------------------------#
		print("idx2:", self.m_cProgramIndex)
		self.treeWidget.setCurrentIndex(QtCore.QModelIndex().siblingAtRow(self.m_cProgramIndex-1))
		
		itemTree = self.treeWidget.topLevelItem(self.m_cProgramIndex-1)
		itemTree.setSelected(True)

		self.t = True
		
		self.populateTable(self.m_cProgramIndex)

	def on_actionSave(self):
		print("save")
		if self.treeWidget.currentItem()!= 0:
			self.saveTable()

			if self.save != True:
				self.saveSettings()
				self.jsonTable()
				self.t = False
				if self.flagText != False:
					#remove txt
					self.filex.remove("/home/ditsa/DitsaNet/ProfileEditorPrograms/"+self.txt+".txt")

			else:
				self.mssage_Information()
		else:
			self.mssage_Information()

	
	def on_actionRename(self):
		print("rename")
		item = self.treeWidget.topLevelItem(self.m_cProgramIndex-1)
		#item = self.treeWidget.currentItem()
		item.setFlags(QtCore.Qt.ItemIsEnabled| QtCore.Qt.ItemIsEditable |QtCore.Qt.ItemIsSelectable)
		self.treeWidget.editItem(item,0)
	
	def on_actionDelete(self):
		print("delete")

		tmp = self.programData[self.m_cProgramIndex-1][0]
		msg = QtWidgets.QMessageBox()
		rDelete = msg.critical(self.MainWindow,'Warning',"Are you sure you want to delete program "+tmp+"?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
		
		if rDelete == msg.Yes: #corregir con respecto a cerrar pregunta guardar
			if self.treeWidget.currentItem()!= 0: #talvez esta linea no hace falta
				self.t = True
				self.programData.pop(self.m_cProgramIndex-1)
				self.tableWidget.clearContents()
				self.tableWidget.setRowCount(0)
				self.treeWidget.takeTopLevelItem(self.m_cProgramIndex-1)
				self.on_treeItemClicked()

				self.saveTable()
				self.saveSettings()
				self.filex.remove("/home/ditsa/DitsaNet/ProfileEditorPrograms/"+tmp+".txt")
				self.t = False

	def on_actionExit(self):
		print("Exit")

		if self.t != False:
			msg = QtWidgets.QMessageBox()
			returnExit = msg.warning(self.MainWindow,'Warning',"Do you want to save changes in this file?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Cancel)

			if returnExit == msg.Yes:
				self.saveTable()
				if self.save != True:
					self.saveSettings()
					self.jsonTable()
					self.t = False
					MainWindow.close()
				else:
					self.mssage_Information()
				
			elif returnExit == msg.No:
				self.flagExit = True
				MainWindow.close()
		else:
			MainWindow.close()

	def on_actionAddRow(self):
		print("addRow")
		if self.treeWidget.currentItem()!=0:
			if len(self.programData[self.m_cProgramIndex-1]) < 16: #limite 15 steps
				self.programData[self.m_cProgramIndex-1].append("-,-,-,-,-,-")
				self.populateTable(self.m_cProgramIndex)
			else:
				msg = QtWidgets.QMessageBox()
				msg.critical(self.MainWindow,'Error',"Invalid number of steps (1-15)")


	def on_actionDeleteRow(self):
		print("deleteRow")
		if self.treeWidget.currentItem()!=0:
			print(self.programData)
			print(self.programData[self.m_cProgramIndex-1])
			print(len(self.programData[self.m_cProgramIndex-1])-1)

			if len(self.programData[self.m_cProgramIndex-1])-1 > 1: 
				self.programData[self.m_cProgramIndex-1].pop(len(self.programData[self.m_cProgramIndex-1])-1)
				self.tableWidget.setRowCount(len(self.programData[self.m_cProgramIndex-1])-1)
				self.populateTable(self.m_cProgramIndex)
			else:
				print("DELTE ELSE")
				self.tableWidget.clearContents()
				self.tableWidget.setRowCount(1)
				self.programData[self.m_cProgramIndex-1].pop(1)
				self.programData[self.m_cProgramIndex-1].append("-,-,-,-,-,-")
				print(self.programData)
				self.populateTable(self.m_cProgramIndex)
			#self.t = True
 
	def saveTable(self):
		print("saveTable")
		itabtext = []
		itabtext.clear()

		self.t = False
		self.save = True

		if len(self.programData)!= 0:

			for j in range(len(self.programData[self.m_cProgramIndex-1])-1):
				itabtext.clear()
				for i in range(6):
					itab = self.tableWidget.item(j,i)
					itabtext.append(itab.text())
					#print("itabtext:",itabtext)

				if itabtext[0] == "-" and itabtext[1] == "-" and itabtext[2] == "-" and itabtext[3] == "-" and itabtext[4] == "-" and itabtext[5] == "-":
					self.save = True
					#print("entra a todo vacio")
					break
				
				if itabtext[0] == "-":
					self.save = True
					#print("no se puede guardar")
					break

				if itabtext[0] == "Charge":
					if itabtext[1] == "-" or itabtext[2] == "-" or itabtext[3] == "-":
						self.save = True
						#print("no se puede guardar")
						break
					
					else:
						#print("si se puede guardarC")
						self.save = False
						self.t = True
						text = itabtext[0]+","+itabtext[1]+","+itabtext[2]+","+itabtext[3]+","+itabtext[4]+","+itabtext[5]
						self.programData[self.m_cProgramIndex-1][j+1] = text

				else:
					if itabtext[2] == "-" or itabtext[3] == "-":
						self.save = True
						#print("no se puede guardar")
						break
					
					else:
						#print("si se puede guardar")
						self.save = False
						self.t = True
						text = itabtext[0]+","+itabtext[1]+","+itabtext[2]+","+itabtext[3]+","+itabtext[4]+","+itabtext[5]
						self.programData[self.m_cProgramIndex-1][j+1] = text


	def saveSettings(self):
		print("saveSettings") ##checar si esta completo o incompleto
		settings = QtCore.QSettings("/home/ditsa/DitsaNet/Settings/archivo_ProfEdi.ini",QtCore.QSettings.NativeFormat)
		settings.setValue("programData",self.programData)
		#print("data:",self.programData)

	def jsonTable(self):
		print("jsonTable")
		
		for j in range(len(self.programData)):
			name = self.programData[j][0]

			self.filex.remove("/home/ditsa/DitsaNet/ProfileEditorPrograms/"+name+".txt")
			self.filex.setFileName("/home/ditsa/DitsaNet/ProfileEditorPrograms/"+name+".txt")

			if self.filex.open(QtCore.QIODevice.ReadWrite):
				stream = QtCore.QTextStream(self.filex) #&file
				stream<<"[{\"Type\":\"Begin\"},"
			
				for i in range(1,len(self.programData[j])):
					list1 = [self.programData[j][i]]

					#print("list1:",list1)
					list3 = []
					stepCount = [len(list1)]

					list2 = list1[:]
					list3 = list2[0].split(',')
				
					#print("list3:",list3)
					temp0 = list3[0]
					temp1 = list3[1]
					temp2 = list3[2] 
					temp3 = list3[3]
					temp4 = list3[4]
					temp5 = list3[5]

					if temp3 == "AH":
						valTime = "AH"

					else:
						#val = float(list3[2]) * 3600 #dejar en horas 
						#temp2 = str(val)
						valTime = "Time"

					if temp0 == "Charge":
						stepCount = ["{\"Type\":\""+temp0+"\",\"Current\":\""+temp1+"\",\""+valTime+"\":\""+temp2+"\",\"MaxTemp\":\""+temp4+"\",\"MinTemp\":\""+temp5+"\"}"]
						step = [stepCount[0].replace("-","0.0")]
						#print("step:",step)
		
					else: 
						step = ["{\"Type\":\""+temp0+"\",\"Time\":\""+temp2+"\"}"]
				
					stepTotal = [step[0] +","]
				
					#print("stepTotal:",stepTotal[0])
					stream<<stepTotal[0]

				stream<<"{\"Type\":\"End\"}]"

	def mssage_Information(self):
		print("mssage_inf")
		msg = QtWidgets.QMessageBox()
		msg.critical(self.MainWindow,'Error',"Cannot save program empty or incomplete")


	def loadSettings(self):
		print("loadSettings")
		settings = QtCore.QSettings("/home/ditsa/DitsaNet/Settings/archivo_ProfEdi.ini",QtCore.QSettings.NativeFormat)
		self.tmpData = settings.value("programData")
		print(self.tmpData)
		if self.tmpData != None:
			self.programData = self.tmpData[:]
		
	def populateTree(self):
		print("populateTree") 
		if len(self.programData) != 0:
			for i in range(len(self.programData)):
				topLevel = QtWidgets.QTreeWidgetItem()
				topLevel.setText(0,self.programData[i][0])
				self.treeWidget.addTopLevelItem(topLevel)

				#self.m_cProgramIndex = self.treeWidget.currentIndex().row()
				self.m_cProgramIndex = 1
				x = self.treeWidget.topLevelItem(0)
				x.setSelected(True)
				self.populateTable(self.m_cProgramIndex)
				
				self.t = False #verificar!!


	def populateTable(self,pgmIdx):
		print("populateTable")
		print("pgmIdx:",pgmIdx)
		#print("m_cProgramIndex:",self.m_cProgramIndex)
		#print(self.programData)
	
		for nstep in range(len(self.programData[pgmIdx-1])-1):
			stringTosplit = self.programData[pgmIdx-1][nstep+1]
			
			self.tableWidget.setRowCount(len(self.programData[pgmIdx-1])-1)
			query = stringTosplit.split(',')

			for j in range(6):
				item = QtWidgets.QTableWidgetItem(query[j])
				self.tableWidget.setItem(nstep,j,item)

				if query[j] == "-":
					self.tableWidget.item(nstep,j).setBackground(QtCore.Qt.lightGray)
				else:
					self.tableWidget.item(nstep,j).setBackground(QtCore.Qt.white)

		self.tableItemCh()

	def on_treeItemClicked(self):
		print("on_treeItemCliked")
		print("indice:",self.m_cProgramIndex)
	
		if self.t != True:
			self.m_cProgramIndex = self.treeWidget.currentIndex().row() + 1
			self.populateTable(self.m_cProgramIndex)
		else:
			msgq = QtWidgets.QMessageBox()
			quest = msgq.question(self.MainWindow,'Warning',"Do you want to save changes you made?")

			if quest == msgq.Yes:
				self.on_actionSave()

				if self.save != True:
					self.m_cProgramIndex = self.treeWidget.currentIndex().row() + 1
					print("pIdx:",self.m_cProgramIndex)
					self.populateTable(self.m_cProgramIndex)
					self.t = False
				
				else:
					print("elseTree")
					print("self.t:",self.t)
					prub = self.treeWidget.topLevelItem(self.treeWidget.currentIndex().row())
					prub.setSelected(False)
	
					itemTree = self.treeWidget.topLevelItem(self.m_cProgramIndex-1)
					itemTree.setSelected(True)

			elif quest == msgq.No:
				self.t = False
				self.treeWidget.takeTopLevelItem(self.m_cProgramIndex-1)
				self.programData.clear()
				self.loadSettings()

				if len(self.programData) != 0:
					for i in range(len(self.programData)):
						self.m_cProgramIndex = self.treeWidget.currentIndex().row() + 1
						self.populateTable(self.m_cProgramIndex)

	def doubleClickedTree(self,item,column):
		print("doubleClickedTree")
		item.setFlags(item.flags()|QtCore.Qt.ItemIsEditable)
		self.treeWidget.editItem(item,column)

	def treeChanged(self,item,column):
		print("treeChanged")
		d = item.text(column)
		self.txt = self.programData[self.m_cProgramIndex-1][0]

	#	self.filex.remove("/home/ditsa/DitsaNet/ProfileEditorPrograms/"+tmp+".txt")
		self.programData[self.m_cProgramIndex-1][0] = d
		self.t = True
		self.flagText = True

	def tableCellCh(self,row,column):
		#print("tableCellCh")
		#self.t = True
		stringToSplit = self.programData[self.m_cProgramIndex-1][row+1]
		query = stringToSplit.split(",")
		query[column] = self.tableWidget.item(row,column).text()
		self.programData[self.m_cProgramIndex-1][row+1] = query[0]+","+query[1]+","+query[2]+","+query[3]+","+query[4]+","+query[5]
		#print("PgD:",self.programData)

	def tableItemCh(self):
		#print("tableItemCh")
		self.cbid = ComboBoxDelegate()
		self.tableWidget.setItemDelegateForColumn(0,self.cbid)

		self.sbd = SpinBoxDelegate()
		self.tableWidget.setItemDelegateForColumn(1,self.sbd)

		self.editime = TimeDelegate()
		self.tableWidget.setItemDelegateForColumn(2,self.editime)

		self.cbtime = ComboBoxTime(self)
		self.tableWidget.setItemDelegateForColumn(3,self.cbtime)

		self.sbtmx = SpinBoxTemp()
		self.tableWidget.setItemDelegateForColumn(4,self.sbtmx)

		self.sbtmin = SpinBoxTemp()
		self.tableWidget.setItemDelegateForColumn(5,self.sbtmin)
		

	def on_tableItemClicked(self):
		print("on_tableItemCliked")

		row = self.tableWidget.currentRow()
		column = self.tableWidget.currentColumn()
		itab = self.tableWidget.item(row,0)
		itabtext = itab.text()
		item = QtWidgets.QTableWidgetItem("-")

		if itabtext == "Charge":
			item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
			self.t = True

		elif itabtext == "Pause":
			item.setFlags(item.flags()& ~QtCore.Qt.ItemIsEditable)
			self.t = True
			if column==1 or column==4 or column==5:
				self.tableWidget.setItem(row,column,item)

		for k in range(self.tableWidget.rowCount()):
			for j in range(6):
				if self.tableWidget.item(k,j).text() == "-":
					self.tableWidget.item(k,j).setBackground(QtCore.Qt.lightGray)
				else:
					self.tableWidget.item(k,j).setBackground(QtCore.Qt.white)


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_ProfileEditor()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
