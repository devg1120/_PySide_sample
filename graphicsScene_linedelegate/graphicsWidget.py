import sys

import PySide6
from PySide6.QtGui import Qt, QCursor
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsItem, QGraphicsWidget
from PySide6.QtCore import QRect, QPointF


class MyItem(QGraphicsWidget):
   def __init__(self, node_item):
       super().__init__(parent=None)
       self.setAcceptHoverEvents(True)
       self.setFlag(QGraphicsItem.ItemIsMovable, False)
       self.setFlag(QGraphicsWidget.ItemIsMovable, True)
       self.setFlag(QGraphicsWidget.ItemIsSelectable, True)
   
       self.offset : QPointF = None
   
   def boundingRect(self) -> PySide6.QtCore.QRectF:
       return QRect(0,0,30,30)
   
   def paint(self, painter: PySide6.QtGui.QPainter, option: PySide6.QtWidgets.QStyleOptionGraphicsItem, widget) -> None:
       r = QRect(0, 0, 30, 30)
       painter.drawRect(r)
   
   
   def mouseMoveEvent(self, event):
       self.setCursor(QCursor(Qt.ClosedHandCursor))
       print(event.pos().x() - self.offset.x(), event.pos().y() - self.offset.y())
       self.moveBy(event.pos().x() - self.offset.x(), event.pos().y() - self.offset.y())
   
   
   
   def mousePressEvent(self, event: PySide6.QtWidgets.QGraphicsSceneMouseEvent) -> None:
   
       self.setSelected(True)
       scene.update(self.boundingRect())
       #self.offset = QPointF(event.pos()-self.pos())
       self.offset = QPointF(event.pos())
   
   def mouseReleaseEvent(self, event: PySide6.QtWidgets.QGraphicsSceneMouseEvent) -> None:
       self.setSelected(False)
       self.update(self.boundingRect())
   
   def grabMouseEvent(self, event: PySide6.QtCore.QEvent) -> None:
       print("object grabbed")




app = QApplication()

scene = QGraphicsScene()
item = MyItem(scene)
scene.addItem(item)

view = QGraphicsView(scene)

scene.setSceneRect(0, 0 ,1000, 1000)

view.geometry().setHeight(500)
view.geometry().setWidth(500)

view.show()

sys.exit(app.exec())

