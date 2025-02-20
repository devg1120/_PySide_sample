from PySide6.QtWidgets import (
    QApplication, QGraphicsTextItem, QGraphicsView, QGraphicsScene, QSlider,
    QVBoxLayout, QWidget, QLabel, QTableView, QGraphicsProxyWidget, QGraphicsItem, QAbstractItemView
)
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QStandardItemModel 
from resizableProxy import ResizableProxy
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

    def enterEvent(self, ev):
        print("EnterEvent")
    def leaveEvent(self, ev):
        print("LeaveEvent")
    def mouseMoveEvent(self, ev):
        print("mouseMoveEvent")
    #def eventFilter(self, object, event):
    #    print(event.type())
    #    return True
    #def mouseHoverEvent(self, ev):
    #    print("mouseHoverEvent")
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
        #self.setAttribute(Qt.WidgetAttribute.WA_Hover)
        #self.widget().setMouseTracking(True)
    #https://doc.qt.io/qtforpython-6/PySide6/QtCore/QEvent.html#PySide6.QtCore.QEvent.Type
    #https://doc.qt.io/qtforpython-6/PySide6/QtGui/QCursor.html

    """
    def eventFilter(self, object, event):
        #print(event.type())
        if event.type() == QEvent.Enter:
            print("enter")
            #self.widget().setMouseTracking(True)
            #self.widget().setCursor(Qt.CrossCursor)
            #self.widget().setCursor(Qt.SizeVerCursor)
            self.widget().setCursor(Qt.SizeHorCursor)
           # if ev.pos().x() > -2 and  ev.pos().x() < 2:

        elif event.type() == QEvent.Leave:
            print("leave")
            self.widget().setCursor(Qt.ArrowCursor)

        return super().eventFilter(object, event)
        #return True

    """
    
         #print(event)
         # <PySide6.QtCore.QEvent(QEvent::Leave)>
         # <PySide6.QtGui.QEnterEvent(QPointF(152,0))>
   
       

    #def eventFilter(self, object, event):
    #    print(event.type())
    def enterEvent(self, ev):
        print("mouseEnterEvent")
    def mouseEnterEvent(self, ev):
        print("mouseEnterEvent")
    def mousePressEvent(self, ev):
        print("mousePressEvent")
        #self.widget().setCursor(Qt.SizeHorCursor)
        #self.start_position = ev.pos()
        if ev.pos().x() > -2 and  ev.pos().x() < 2:
            print("resize x")
            x = self.x()
            y = self.y()
            size = self.size()
            w = size.width()
            h = size.height()
            self.setGeometry(x -10,y,w+10,h)
            return
        if ev.pos().y() > -1 and  ev.pos().y() < 1:
            print("resize y")
            x = self.x()
            y = self.y()
            size = self.size()
            w = size.width()
            h = size.height()
            self.setGeometry(x ,y -10 ,w,h+10)
            return
        if ev.pos().x() > 10 and ev.pos().y() > 10:
           super().mousePressEvent(ev)
           return
        #print("Proxy Press")
        if ev.button() == Qt.LeftButton:
            self.start_position = ev.pos()

    #def mouseReleaseEvent(self, ev):
    #    print("mouseReleaseEvent")
    def mouseMoveEvent(self, ev):
        print("mouseMoveEvent")
        if ev.pos().x() > 10 and ev.pos().y() > 10:
          super().mouseMoveEvent(ev)
          return
        #print("Proxy Move")
        if ev.buttons() == Qt.LeftButton:
            delta = ev.pos() - self.start_position
            new_position = self.pos() + delta
            self.setPos(new_position)
            #label_parameters = int(self.pos().x()), int(self.pos().y())
            #print(label_parameters)

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.graphical_window = QGraphicsView()
        self.scene = QGraphicsScene()
        self.graphical_window.setScene(self.scene)

        self.movable_item = MovableItem()
        self.movable_item.setTransformOriginPoint(self.movable_item.boundingRect().center())
        self.scene.addItem(self.movable_item)


        table_widget = MovableTable()
        #table_widget = QTableView()
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


app = QApplication(sys.argv)
window = Widget()
window.show()

if __name__ == '__main__':
    app.exec()

