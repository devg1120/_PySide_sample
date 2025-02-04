#!/usr/bin/env python

from PySide6 import QtCore, QtGui, QtWidgets

from diagramItem import DiagramItem
from diagramScene import DiagramScene
from resizableRectItem import ResizableRectItem

import diagramscene_rc

class MainWindow(QtWidgets.QMainWindow):
    InsertTextButton = 6

    def __init__(self):
        super(MainWindow, self).__init__()

        self.createActions()
        self.createMenus()
        self.createToolBox()

        self.scene = DiagramScene(self.itemMenu)
        self.scene_size = 1000
        s = self.scene_size

        self.scene.setSceneRect(QtCore.QRectF(0, 0, s, s))
        #self.scene.setAlignment(Qt.AlignTop|Qt.AlignLeft)

        self.scene.itemInserted.connect(self.itemInserted)
        self.scene.textInserted.connect(self.textInserted)
        self.scene.itemSelected.connect(self.itemSelected)

        self.createToolbars()

        ###################################################
        """
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.toolBox)

        self.view1 = QtWidgets.QGraphicsView(self.scene)
        self.view1.setSceneRect(QtCore.QRectF(0, 0, 200, 200))
        self.view1.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        layout.addWidget(self.view1)

        self.view2 = QtWidgets.QGraphicsView(self.scene)
        self.view2.setSceneRect(QtCore.QRectF(0, 0, 200, 200))
        self.view2.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignRight)
        layout.addWidget(self.view2)

        self.view3 = QtWidgets.QGraphicsView(self.scene)
        self.view3.setSceneRect(QtCore.QRectF(0, 0, 200, 200))
        self.view3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeft)
        layout.addWidget(self.view3)

        self.view4 = QtWidgets.QGraphicsView(self.scene)
        self.view4.setSceneRect(QtCore.QRectF(0, 0, 200, 200))
        self.view4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight)
        layout.addWidget(self.view4)

        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)
        """
        ###################################################
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.toolBox)

        self.h_splitter1 = QtWidgets.QSplitter()
        self.h_splitter2 = QtWidgets.QSplitter()
        self.v_splitter  = QtWidgets.QSplitter()
        self.v_splitter.setOrientation(QtCore.Qt.Orientation.Vertical)

        self.view1 = QtWidgets.QGraphicsView(self.scene)
        self.view1.setSceneRect(QtCore.QRectF(0, 0, s, s))
        self.view1.centerOn(QtCore.QPointF(0,0))

        self.view2 = QtWidgets.QGraphicsView(self.scene)
        self.view2.setSceneRect(QtCore.QRectF(0, 0, s, s))
        self.view2.centerOn(QtCore.QPointF(0,0))

        self.view3 = QtWidgets.QGraphicsView(self.scene)
        self.view3.setSceneRect(QtCore.QRectF(0, 0, s, s))
        self.view3.centerOn(QtCore.QPointF(0,0))

        self.view4 = QtWidgets.QGraphicsView(self.scene)
        self.view4.setSceneRect(QtCore.QRectF(0, 0, s, s))
        self.view4.centerOn(QtCore.QPointF(0,0))

        self.h_splitter1.addWidget(self.view1)
        self.h_splitter1.addWidget(self.view2)
        self.h_splitter2.addWidget(self.view3)
        self.h_splitter2.addWidget(self.view4)
        self.v_splitter.addWidget(self.h_splitter1)
        self.v_splitter.addWidget(self.h_splitter2)

        self.h_splitter1.moveSplitter(0,0)
        self.h_splitter2.moveSplitter(0,0)
        self.v_splitter.moveSplitter(0,0)

        #self.setCentralWidget(self.v_splitter)
        layout.addWidget(self.v_splitter)

        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)

        self.setWindowTitle("Diagramscene")
        

        css = """
        QSplitter { background: gray;  }
        """

        self.setStyleSheet(css)

        """
        table_widget = QtWidgets.QTableView()
        table_widget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked
                                     | QtWidgets.QAbstractItemView.SelectedClicked)
        table_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        rowsCount = 100
        columnsCount = 30
        model = QtGui.QStandardItemModel()
        for row in range(rowsCount):
             model.insertRow(row)
             for column in range(columnsCount):
                 if model.columnCount() < columnsCount:
                    model.insertColumn(column)
                 id = model.index(row, column)
                 model.setData(id, f"[{str(row + 1)}x{str(column + 1)}]")

        table_widget.setModel(model)
        table_widget.resizeColumnsToContents()
        table_widget.resize(600, 300)

        proxyWidget = self.scene.addWidget(table_widget) 
        proxyWidget.setPos(50,50)
        
        button = QtWidgets.QPushButton("Download")
        proxyWidget2 = self.scene.addWidget(button) 
        """

        rectItem = ResizableRectItem(100, 100, 50, 50)
        self.scene.addItem(rectItem)


    def backgroundButtonGroupClicked(self, button):
        buttons = self.backgroundButtonGroup.buttons()
        for myButton in buttons:
            if myButton != button:
                button.setChecked(False)

        text = button.text()
        if text == "Blue Grid":
            self.scene.setBackgroundBrush(QtGui.QBrush(QtGui.QPixmap(':/images/background1.png')))
        elif text == "White Grid":
            self.scene.setBackgroundBrush(QtGui.QBrush(QtGui.QPixmap(':/images/background2.png')))
        elif text == "Gray Grid":
            self.scene.setBackgroundBrush(QtGui.QBrush(QtGui.QPixmap(':/images/background3.png')))
        else:
            self.scene.setBackgroundBrush(QtGui.QBrush(QtGui.QPixmap(':/images/background4.png')))

        self.scene.update()
        self.view.update()

    def buttonGroupClicked(self, cbutton):
        buttons = self.buttonGroup.buttons()
        id = 1
        tid = 0
        for button in buttons:
            tid += 1
            if cbutton == button:
                id = tid
            else:
                button.setChecked(False)

        #print("TextButton:",self.InsertTextButton, id)
        #if cbutton == self.InsertTextButton:
        #print("id", id)
        #print("cbutton", type(cbutton))

        #if id == 6:                                              # GUSA GS
        if id == self.InsertTextButton:
            print("InsertText")
            self.scene.setMode(DiagramScene.InsertText)
        else:
            self.scene.setItemType(id)
            self.scene.setMode(DiagramScene.InsertItem)

    def buttonGroupClicked_(self, id):
        buttons = self.buttonGroup.buttons()
        for button in buttons:
            if self.buttonGroup.button(id) != button:
                button.setChecked(False)

        if id == self.InsertTextButton:
            self.scene.setMode(DiagramScene.InsertText)
        else:
            self.scene.setItemType(id)
            self.scene.setMode(DiagramScene.InsertItem)

    def deleteItem(self):
        for item in self.scene.selectedItems():
            if isinstance(item, DiagramItem):
                item.removeArrows()
            self.scene.removeItem(item)

    def pointerGroupClicked(self, i):
        self.scene.setMode(self.pointerTypeGroup.checkedId())

    def bringToFront(self):
        if not self.scene.selectedItems():
            return

        selectedItem = self.scene.selectedItems()[0]
        overlapItems = selectedItem.collidingItems()

        zValue = 0
        for item in overlapItems:
            if (item.zValue() >= zValue and isinstance(item, DiagramItem)):
                zValue = item.zValue() + 0.1
        selectedItem.setZValue(zValue)

    def sendToBack(self):
        if not self.scene.selectedItems():
            return

        selectedItem = self.scene.selectedItems()[0]
        overlapItems = selectedItem.collidingItems()

        zValue = 0
        for item in overlapItems:
            if (item.zValue() <= zValue and isinstance(item, DiagramItem)):
                zValue = item.zValue() - 0.1
        selectedItem.setZValue(zValue)

    def itemInserted(self, item):
        self.pointerTypeGroup.button(DiagramScene.MoveItem).setChecked(True)
        self.scene.setMode(self.pointerTypeGroup.checkedId())
        #GUSA self.buttonGroup.button(item.diagramType).setChecked(False)

    def textInserted(self, item):
        self.buttonGroup.button(self.InsertTextButton).setChecked(False)
        self.scene.setMode(self.pointerTypeGroup.checkedId())

    def currentFontChanged(self, font):
        self.handleFontChange()

    def fontSizeChanged(self, font):
        self.handleFontChange()

    def sceneScaleChanged(self, scale):
        print(type(scale))
        print(scale)
        #newScale = int(scale[:-1]) / 100.0
        scale_p = self.scale_list[scale]
        newScale = int(scale_p[:-1]) / 100.0
        #oldMatrix = self.view1.matrix()
        #self.view1.resetMatrix()
        #self.view1.translate(oldMatrix.dx(), oldMatrix.dy())
        self.view1.scale(newScale, newScale)

    def textColorChanged(self):
        self.textAction = self.sender()
        self.fontColorToolButton.setIcon(self.createColorToolButtonIcon(
                    ':/images/textpointer.png',
                    QtGui.QColor(self.textAction.data())))
        self.textButtonTriggered()

    def itemColorChanged(self):
        self.fillAction = self.sender()
        self.fillColorToolButton.setIcon(self.createColorToolButtonIcon(
                    ':/images/floodfill.png',
                    QtGui.QColor(self.fillAction.data())))
        self.fillButtonTriggered()

    def lineColorChanged(self):
        self.lineAction = self.sender()
        self.lineColorToolButton.setIcon(self.createColorToolButtonIcon(
                    ':/images/linecolor.png',
                    QtGui.QColor(self.lineAction.data())))
        self.lineButtonTriggered()

    def textButtonTriggered(self):
        self.scene.setTextColor(QtGui.QColor(self.textAction.data()))

    def fillButtonTriggered(self):
        self.scene.setItemColor(QtGui.QColor(self.fillAction.data()))

    def lineButtonTriggered(self):
        self.scene.setLineColor(QtGui.QColor(self.lineAction.data()))

    def handleFontChange(self):
        font = self.fontCombo.currentFont()
        font.setPointSize(int(self.fontSizeCombo.currentText()))
        if self.boldAction.isChecked():
            font.setWeight(QtGui.QFont.Bold)
        else:
            font.setWeight(QtGui.QFont.Normal)
        font.setItalic(self.italicAction.isChecked())
        font.setUnderline(self.underlineAction.isChecked())

        self.scene.setFont(font)

    def itemSelected(self, item):
        font = item.font()
        color = item.defaultTextColor()
        self.fontCombo.setCurrentFont(font)
        self.fontSizeCombo.setEditText(str(font.pointSize()))
        self.boldAction.setChecked(font.weight() == QtGui.QFont.Bold)
        self.italicAction.setChecked(font.italic())
        self.underlineAction.setChecked(font.underline())

    def about(self):
        QtGui.QMessageBox.about(self, "About Diagram Scene",
                "The <b>Diagram Scene</b> example shows use of the graphics framework.")

    def createToolBox(self):
        self.buttonGroup = QtWidgets.QButtonGroup()
        self.buttonGroup.setExclusive(False)
        #self.buttonGroup.buttonClicked[int].connect(self.buttonGroupClicked)
        self.buttonGroup.buttonClicked.connect(self.buttonGroupClicked)
  
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.createCellWidget("Conditional", DiagramItem.Conditional),
                0, 0)
        layout.addWidget(self.createCellWidget("Process", DiagramItem.Step),
                0, 1)
        layout.addWidget(self.createCellWidget("Input/Output", DiagramItem.Io),
                1, 0)
        layout.addWidget(self.createCellWidget("Ellipse", DiagramItem.Ellipse),
                1, 1)
        layout.addWidget(self.createCellWidget("Hexagon", DiagramItem.Hexagon),
                2, 0)

        textButton = QtWidgets.QToolButton()
        textButton.setCheckable(True)
        self.buttonGroup.addButton(textButton, self.InsertTextButton)
        textButton.setIcon(QtGui.QIcon(QtGui.QPixmap(':/images/textpointer.png')
                            .scaled(30, 30)))
        textButton.setIconSize(QtCore.QSize(50, 50))

        textLayout = QtWidgets.QGridLayout()
        textLayout.addWidget(textButton, 0, 0, QtCore.Qt.AlignHCenter)
        textLayout.addWidget(QtWidgets.QLabel("Text"), 1, 0,
                QtCore.Qt.AlignCenter)
        textWidget = QtWidgets.QWidget()
        textWidget.setLayout(textLayout)
        layout.addWidget(textWidget, 2, 1)

        layout.setRowStretch(3, 10)
        layout.setColumnStretch(2, 10)

        itemWidget = QtWidgets.QWidget()
        itemWidget.setLayout(layout)

        self.backgroundButtonGroup = QtWidgets.QButtonGroup()
        self.backgroundButtonGroup.buttonClicked.connect(self.backgroundButtonGroupClicked)

        backgroundLayout = QtWidgets.QGridLayout()
        backgroundLayout.addWidget(self.createBackgroundCellWidget("Blue Grid",
                ':/images/background1.png'), 0, 0)
        backgroundLayout.addWidget(self.createBackgroundCellWidget("White Grid",
                ':/images/background2.png'), 0, 1)
        backgroundLayout.addWidget(self.createBackgroundCellWidget("Gray Grid",
                ':/images/background3.png'), 1, 0)
        backgroundLayout.addWidget(self.createBackgroundCellWidget("No Grid",
                ':/images/background4.png'), 1, 1)

        backgroundLayout.setRowStretch(2, 10)
        backgroundLayout.setColumnStretch(2, 10)

        backgroundWidget = QtWidgets.QWidget()
        backgroundWidget.setLayout(backgroundLayout)

        self.toolBox = QtWidgets.QToolBox()
        self.toolBox.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored))
        self.toolBox.setMinimumWidth(itemWidget.sizeHint().width())
        self.toolBox.addItem(itemWidget, "Basic Flowchart Shapes")
        self.toolBox.addItem(backgroundWidget, "Backgrounds")

    def createActions(self):
        self.toFrontAction = QtGui.QAction(
                QtGui.QIcon(':/images/bringtofront.png'), "Bring to &Front",
                self, shortcut="Ctrl+F", statusTip="Bring item to front",
                triggered=self.bringToFront)

        self.sendBackAction = QtGui.QAction(
                QtGui.QIcon(':/images/sendtoback.png'), "Send to &Back", self,
                shortcut="Ctrl+B", statusTip="Send item to back",
                triggered=self.sendToBack)

        self.deleteAction = QtGui.QAction(QtGui.QIcon(':/images/delete.png'),
                "&Delete", self, shortcut="Delete",
                statusTip="Delete item from diagram",
                triggered=self.deleteItem)

        self.exitAction = QtGui.QAction("E&xit", self, shortcut="Ctrl+X",
                statusTip="Quit Scenediagram example", triggered=self.close)

        self.boldAction = QtGui.QAction(QtGui.QIcon(':/images/bold.png'),
                "Bold", self, checkable=True, shortcut="Ctrl+B",
                triggered=self.handleFontChange)

        self.italicAction = QtGui.QAction(QtGui.QIcon(':/images/italic.png'),
                "Italic", self, checkable=True, shortcut="Ctrl+I",
                triggered=self.handleFontChange)

        self.underlineAction = QtGui.QAction(
                QtGui.QIcon(':/images/underline.png'), "Underline", self,
                checkable=True, shortcut="Ctrl+U",
                triggered=self.handleFontChange)

        self.aboutAction = QtGui.QAction("A&bout", self, shortcut="Ctrl+B",
                triggered=self.about)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.exitAction)

        self.itemMenu = self.menuBar().addMenu("&Item")
        self.itemMenu.addAction(self.deleteAction)
        self.itemMenu.addSeparator()
        self.itemMenu.addAction(self.toFrontAction)
        self.itemMenu.addAction(self.sendBackAction)

        self.aboutMenu = self.menuBar().addMenu("&Help")
        self.aboutMenu.addAction(self.aboutAction)

    def createToolbars(self):
        self.editToolBar = self.addToolBar("Edit")
        self.editToolBar.addAction(self.deleteAction)
        self.editToolBar.addAction(self.toFrontAction)
        self.editToolBar.addAction(self.sendBackAction)

        self.fontCombo = QtWidgets.QFontComboBox()
        self.fontCombo.currentFontChanged.connect(self.currentFontChanged)

        self.fontSizeCombo = QtWidgets.QComboBox()
        self.fontSizeCombo.setEditable(True)
        for i in range(8, 30, 2):
            self.fontSizeCombo.addItem(str(i))
        validator = QtGui.QIntValidator(2, 64, self)
        self.fontSizeCombo.setValidator(validator)
        self.fontSizeCombo.currentIndexChanged.connect(self.fontSizeChanged)

        self.fontColorToolButton = QtWidgets.QToolButton()
        self.fontColorToolButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.fontColorToolButton.setMenu(
                self.createColorMenu(self.textColorChanged, QtCore.Qt.black))
        self.textAction = self.fontColorToolButton.menu().defaultAction()
        self.fontColorToolButton.setIcon(
                self.createColorToolButtonIcon(':/images/textpointer.png',
                        QtCore.Qt.white))
        self.fontColorToolButton.setAutoFillBackground(True)
        self.fontColorToolButton.clicked.connect(self.textButtonTriggered)

        self.fillColorToolButton = QtWidgets.QToolButton()
        self.fillColorToolButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.fillColorToolButton.setMenu(
                self.createColorMenu(self.itemColorChanged, QtCore.Qt.white))
        self.fillAction = self.fillColorToolButton.menu().defaultAction()
        self.fillColorToolButton.setIcon(
                self.createColorToolButtonIcon(':/images/floodfill.png',
                        QtCore.Qt.white))
        self.fillColorToolButton.clicked.connect(self.fillButtonTriggered)

        self.lineColorToolButton = QtWidgets.QToolButton()
        self.lineColorToolButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.lineColorToolButton.setMenu(
                self.createColorMenu(self.lineColorChanged, QtCore.Qt.white))
        self.lineAction = self.lineColorToolButton.menu().defaultAction()
        self.lineColorToolButton.setIcon(
                self.createColorToolButtonIcon(':/images/linecolor.png',
                        QtCore.Qt.white))
        self.lineColorToolButton.clicked.connect(self.lineButtonTriggered)

        self.textToolBar = self.addToolBar("Font")
        self.textToolBar.addWidget(self.fontCombo)
        self.textToolBar.addWidget(self.fontSizeCombo)
        self.textToolBar.addAction(self.boldAction)
        self.textToolBar.addAction(self.italicAction)
        self.textToolBar.addAction(self.underlineAction)

        self.colorToolBar = self.addToolBar("Color")
        self.colorToolBar.addWidget(self.fontColorToolButton)
        self.colorToolBar.addWidget(self.fillColorToolButton)
        self.colorToolBar.addWidget(self.lineColorToolButton)

        pointerButton = QtWidgets.QToolButton()
        pointerButton.setCheckable(True)
        pointerButton.setChecked(True)
        pointerButton.setIcon(QtGui.QIcon(':/images/pointer.png'))
        linePointerButton = QtWidgets.QToolButton()
        linePointerButton.setCheckable(True)
        linePointerButton.setIcon(QtGui.QIcon(':/images/linepointer.png'))

        connectorPointerButton = QtWidgets.QToolButton()
        connectorPointerButton.setCheckable(True)
        connectorPointerButton.setIcon(QtGui.QIcon(':/images/linepointer.png'))

        self.pointerTypeGroup = QtWidgets.QButtonGroup()
        self.pointerTypeGroup.addButton(pointerButton, DiagramScene.MoveItem)
        self.pointerTypeGroup.addButton(linePointerButton,
                DiagramScene.InsertLine)
        self.pointerTypeGroup.addButton(connectorPointerButton,
                DiagramScene.InsertConnector)

        #self.pointerTypeGroup.buttonClicked[int].connect(self.pointerGroupClicked)
        self.pointerTypeGroup.buttonClicked.connect(self.pointerGroupClicked)

        self.sceneScaleCombo = QtWidgets.QComboBox()
        #self.sceneScaleCombo.addItems(["50%", "75%", "100%", "125%", "150%"])
        self.scale_list = ["50%", "75%", "100%", "125%", "150%"]
        self.sceneScaleCombo.addItems(self.scale_list)
        self.sceneScaleCombo.setCurrentIndex(2)
        #self.sceneScaleCombo.currentIndexChanged[str].connect(self.sceneScaleChanged)
        self.sceneScaleCombo.currentIndexChanged.connect(self.sceneScaleChanged)

        self.pointerToolbar = self.addToolBar("Pointer type")
        self.pointerToolbar.addWidget(pointerButton)
        self.pointerToolbar.addWidget(linePointerButton)
        self.pointerToolbar.addWidget(connectorPointerButton)
        self.pointerToolbar.addWidget(self.sceneScaleCombo)

    def createBackgroundCellWidget(self, text, image):
        button = QtWidgets.QToolButton()
        button.setText(text)
        button.setIcon(QtGui.QIcon(image))
        button.setIconSize(QtCore.QSize(50, 50))
        button.setCheckable(True)
        self.backgroundButtonGroup.addButton(button)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(button, 0, 0, QtCore.Qt.AlignHCenter)
        layout.addWidget(QtWidgets.QLabel(text), 1, 0, QtCore.Qt.AlignCenter)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)

        return widget

    def createCellWidget(self, text, diagramType):
        item = DiagramItem(diagramType, self.itemMenu)
        icon = QtGui.QIcon(item.image())

        button = QtWidgets.QToolButton()
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(50, 50))
        button.setCheckable(True)
        self.buttonGroup.addButton(button, diagramType)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(button, 0, 0, QtCore.Qt.AlignHCenter)
        layout.addWidget(QtWidgets.QLabel(text), 1, 0, QtCore.Qt.AlignCenter)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)

        return widget

    def createColorMenu(self, slot, defaultColor):
        colors = [QtCore.Qt.black, QtCore.Qt.white, QtCore.Qt.red, QtCore.Qt.blue, QtCore.Qt.yellow]
        names = ["black", "white", "red", "blue", "yellow"]

        colorMenu = QtWidgets.QMenu(self)
        for color, name in zip(colors, names):
            action = QtGui.QAction(self.createColorIcon(color), name, self,
                    triggered=slot)
            action.setData(QtGui.QColor(color))
            colorMenu.addAction(action)
            if color == defaultColor:
                colorMenu.setDefaultAction(action)
        return colorMenu

    def createColorToolButtonIcon(self, imageFile, color):
        pixmap = QtGui.QPixmap(50, 80)
        pixmap.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(pixmap)
        image = QtGui.QPixmap(imageFile)
        target = QtCore.QRect(0, 0, 50, 60)
        source = QtCore.QRect(0, 0, 42, 42)
        painter.fillRect(QtCore.QRect(0, 60, 50, 80), color)
        painter.drawPixmap(target, image, source)
        painter.end()

        return QtGui.QIcon(pixmap)

    def createColorIcon(self, color):
        pixmap = QtGui.QPixmap(20, 20)
        painter = QtGui.QPainter(pixmap)
        painter.setPen(QtCore.Qt.NoPen)
        painter.fillRect(QtCore.QRect(0, 0, 20, 20), color)
        painter.end()

        return QtGui.QIcon(pixmap)


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.setGeometry(100, 100, 800, 500)
    mainWindow.show()

    sys.exit(app.exec())
