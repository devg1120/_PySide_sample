from PySide6.QtWidgets import (
    QApplication, QGraphicsTextItem, QGraphicsView, QGraphicsScene, QSlider,
    QVBoxLayout, QWidget, QLabel, QTableView, QGraphicsProxyWidget, QGraphicsItem, QAbstractItemView
)
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QStandardItemModel 
#from resizableProxy import ResizableProxy
import sys

class MovableItem(QGraphicsTextItem):
    def __init__(self):
        super().__init__()
        self.setPlainText("Stack Overflow")

    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.start_position = ev.pos()

    def mouseMoveEvent(self, ev):
        if ev.buttons() == Qt.LeftButton:
            delta = ev.pos() - self.start_position
            new_position = self.pos() + delta
            self.setPos(new_position)
            label_parameters = int(self.pos().x()), int(self.pos().y())
            print(label_parameters)

class MovableTable(QTableView):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover)
        self.prev_cursor = self.cursor()
    
    

    def enterEvent(self, ev):
        return
        print("EnterEvent")
        self.prev_cursor = self.cursor()
        _x = ev.position().x()
        _y = ev.position().y()
        if _y > -2 and  _y < 2\
            and _x > -2 and  _x < 2:
           self.setCursor(Qt.OpenHandCursor)
        elif _y > -2 and  _y < 2:
           self.setCursor(Qt.SizeVerCursor)
        elif _x  > -2 and  _x < 2:
           self.setCursor(Qt.SizeHorCursor)
        #else:
        #   self.setCursor(self.prev_cursor)
        return super().enterEvent(ev)

    def leaveEvent(self, ev):
        print("LeaveEvent")
        self.setCursor(self.prev_cursor)
        return super().leaveEvent(ev)

    def mouseMoveEvent(self, ev):
        return
        #print("mouseMoveEvent")
        self.setCursor(Qt.ArrowCursor)
        _x = ev.position().x()
        _y = ev.position().y()
        if _y > -2 and  _y < 2\
            and _x > -2 and  _x < 2:
           pass
           #self.setCursor(Qt.OpenHandCursor)
        elif _y > -2 and  _y < 2:
           pass
           #self.setCursor(Qt.SizeVerCursor)
        elif _x > -2 and  _x < 2:
           pass
           #self.setCursor(Qt.SizeHorCursor)
        else:
           #self.setCursor(self.prev_cursor)
           self.setCursor(Qt.ArrowCursor)
           print("self.prev_cursor")
        #return super().mouseMoveEvent(ev)
    
    """
    def mousePressEvent(self, ev):
        print("Press")
        if ev.button() == Qt.LeftButton:
            self.start_position = ev.pos()

    def mouseMoveEvent(self, ev):
        print("Move")
        if ev.buttons() == Qt.LeftButton:
            delta = ev.pos() - self.start_position
            new_position = self.pos() + delta
            self.setPos(new_position)
            label_parameters = int(self.pos().x()), int(self.pos().y())
            print(label_parameters)
    """


class MovableTableProxy(QGraphicsProxyWidget):
    def __init__(self):
        super().__init__()
        #self.CTRL = True
        self.SHIFT = False
        #self.SHIFT = True
        self.drag_mode = None
        #self.setAttribute(Qt.WidgetAttribute.WA_Hover)
        #self.widget().setMouseTracking(True)
        #https://doc.qt.io/qtforpython-6/PySide6/QtCore/QEvent.html#PySide6.QtCore.QEvent.Type
        #https://doc.qt.io/qtforpython-6/PySide6/QtGui/QCursor.html

    def setShift(self, value):
        self.SHIFT = value

    def enterEvent(self, ev):
        print("*** mouseEnterEvent")
        return super().enterEvent(ev)
    def mouseEnterEvent(self, ev):
        print("*** mouseEnterEvent")
        return super().mouseEnterEvent(ev)
    def mouseReleaseEvent(self, ev):
        print("*** mouseReleaseEvent")
        self.drag_mode = None
        return super().mouseReleaseEvent(ev)
    def mousePressEvent(self, ev):
        print("*** mousePressEvent")
        if self.SHIFT:
           #self.widget().setCursor(Qt.SizeHorCursor)
           _x = ev.pos().x()
           _y = ev.pos().y()
           #print(_x, _y)
           size = self.size()
           w = size.width()
           h = size.height()
           #print(w, h)
           g = 10
           if _x > w -g and _x < w \
                   and _y > h -g and _y < h:
                       print("LEFT_BOTTOM_CONNER")
                       self.drag_mode = "LEFT_BOTTOM_CONER"
           elif _x > w -g and _x < w :
                       print("LEFT_EDGE")
                       self.drag_mode = "LEFT_EDGE"
           elif _y > h -g and _y < h:
                       print("BOTTOM_EDGE")
                       self.drag_mode = "BOTTOM_EDGE"

           #print("Proxy Press")
           if ev.button() == Qt.LeftButton:
               self.start_position = ev.pos()
        return super().mousePressEvent(ev)
    def mouseMoveEvent(self, ev):
        if self.SHIFT:
           if ev.buttons() != Qt.LeftButton:
               return
           if self.drag_mode == None:
               delta = ev.pos() - self.start_position
               new_position = self.pos() + delta
               self.setPos(new_position)
               #label_parameters = int(self.pos().x()), int(self.pos().y())
               #print(label_parameters)
           elif self.drag_mode == "LEFT_EDGE":
               delta = ev.pos() - self.start_position
               geo = self.geometry()
               #print(geo.x() ,geo.y() , geo.w()+2  , geo.h())
               self.setGeometry(geo.x() ,geo.y() , geo.width()+delta.x()  , geo.height())
               self.start_position = ev.pos()

           elif self.drag_mode == "BOTTOM_EDGE":
               delta = ev.pos() - self.start_position
               geo = self.geometry()
               #print(geo.x() ,geo.y() , geo.w()+2  , geo.h())
               self.setGeometry(geo.x() ,geo.y() , geo.width()  , geo.height()+delta.y())
               self.start_position = ev.pos()

           elif self.drag_mode == "LEFT_BOTTOM_CONER":
               delta = ev.pos() - self.start_position
               geo = self.geometry()
               #print(geo.x() ,geo.y() , geo.w()+2  , geo.h())
               self.setGeometry(geo.x() ,geo.y() , geo.width()+delta.x()  , geo.height()+delta.y())
               self.start_position = ev.pos()
        return super().mouseMoveEvent(ev)
       

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 800)
        self.graphical_window = QGraphicsView()
        self.scene = QGraphicsScene()
        self.graphical_window.setScene(self.scene)

        self.movable_item = MovableItem()
        self.movable_item.setZValue(100)
        self.movable_item.setPos(-90,-20)
        self.movable_item.setTransformOriginPoint(self.movable_item.boundingRect().center())
        self.scene.addItem(self.movable_item)


        #table_widget = MovableTable()
        table_widget = QTableView()
        table_widget.setMouseTracking(True)
        table_widget.setEditTriggers(QAbstractItemView.DoubleClicked
                                     | QAbstractItemView.SelectedClicked)
        table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        rowsCount = 100
        columnsCount = 30
        model = QStandardItemModel()
        for row in range(rowsCount):
             model.insertRow(row)
             for column in range(columnsCount):
                 if model.columnCount() < columnsCount:
                    model.insertColumn(column)
                 id = model.index(row, column)
                 model.setData(id, f"[{str(row + 1)}x{str(column + 1)}]")

        table_widget.setModel(model)
        #proxyWidget = self.scene.addWidget(table_widget)
        #proxyWidget.setPos(50,50)

        tableProxy = MovableTableProxy()
        self.tableProxy = tableProxy
        #tableProxy = ResizableProxy()
        tableProxy.setFlag(QGraphicsItem.ItemIsMovable, True)
        tableProxy.setFlag(QGraphicsItem.ItemIsSelectable, True)
        tableProxy.setWidget(table_widget);
        self.scene.addItem(tableProxy);


        #table_widget2 = MovableTable()
        table_widget2 = QTableView()
        table_widget2.setModel(model)
        proxyWidget = self.scene.addWidget(table_widget2)
        proxyWidget.setPos(-190,-220)

        
        self.slider = QSlider(Qt.Horizontal, minimum=0, maximum=359)
        self.slider.valueChanged.connect(self.movable_item.setRotation)

        self.label_rotation = QLabel('{}'.format(self.slider.value()), alignment=Qt.AlignCenter)
        self.slider.valueChanged.connect(lambda value: self.label_rotation.setText('{}'.format(self.slider.value())))


        main_layout = QVBoxLayout()
        main_layout.addWidget(self.graphical_window)
        main_layout.addWidget(self.label_rotation)
        main_layout.addWidget(self.slider)
        self.setLayout(main_layout)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Shift:
            print("keyPressEvent: Shift")
            self.shift_key = True
            self.tableProxy.setShift(True)
        event.accept()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Shift:
            print("keyReleaseEvent: Shift")
            self.shift_key = False
            self.tableProxy.setShift(False)
        event.accept()

app = QApplication(sys.argv)
window = Widget()
window.show()

if __name__ == '__main__':
    app.exec()

