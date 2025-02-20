#!/usr/bin/env python

# This is only needed for Python v2 but is harmless for Python v3.
#import sip
#sip.setapi('QString', 2)

import math

from PySide6 import QtCore, QtGui, QtWidgets
#from resizableItem import ResizableItem

from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtGui import QBrush, QPainterPath, QPainter, QColor, QPen, QPixmap
from PySide6.QtWidgets import QGraphicsRectItem, QApplication, QMainWindow,  QGraphicsView, QGraphicsScene, QGraphicsItem


#import diagramscene_rc
#from resizableItem2 import ResizableRectItem


class DiagramItem(QtWidgets.QGraphicsPolygonItem):
    Step, Conditional, StartEnd, Io , Ellipse , Hexagon = range(6)


    handleTopLeft = 1
    handleTopMiddle = 2
    handleTopRight = 3
    handleMiddleLeft = 4
    handleMiddleRight = 5
    handleBottomLeft = 6
    handleBottomMiddle = 7
    handleBottomRight = 8

    handleSize = +8.0
    handleSpace = -4.0

    handleCursors = {
        handleTopLeft: Qt.SizeFDiagCursor,
        handleTopMiddle: Qt.SizeVerCursor,
        handleTopRight: Qt.SizeBDiagCursor,
        handleMiddleLeft: Qt.SizeHorCursor,
        handleMiddleRight: Qt.SizeHorCursor,
        handleBottomLeft: Qt.SizeBDiagCursor,
        handleBottomMiddle: Qt.SizeVerCursor,
        handleBottomRight: Qt.SizeFDiagCursor,
    }

    def __init__(self, diagramType, contextMenu, parent=None, scene=None):
        super(DiagramItem, self).__init__(parent, scene)

        self._x = 0
        self._y = 0
        self._width = 100
        self._height = 60

        self.arrows = []

        self.diagramType = diagramType
        self.myContextMenu = contextMenu

        self.handles = {}
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)

        #self.updateHandlesPos()

        self.myPolygon = self.update_Polygon()
        self.setPolygon(self.myPolygon)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)

    def shape(self):
        path = QtGui.QPainterPath()
        path.moveTo(self._x , self._y)                 
        path.lineTo(self._x + self._width  , self._y )  
        path.lineTo(self._x + self._width, self._y + self._height  )  
        path.lineTo(self._x                , self._y + self._height)  
        path.lineTo(self._x  , self._y                  ) 
        return path

    def removeArrow(self, arrow):
        try:
            self.arrows.remove(arrow)
        except ValueError:
            pass

    def removeArrows(self):
        for arrow in self.arrows[:]:
            arrow.startItem().removeArrow(arrow)
            arrow.endItem().removeArrow(arrow)
            self.scene().removeItem(arrow)

    def addArrow(self, arrow):
        self.arrows.append(arrow)

    def image(self):
        pixmap = QtGui.QPixmap(250, 250)
        pixmap.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(pixmap)
        painter.setPen(QtGui.QPen(QtCore.Qt.white, 3))
        #painter.translate(125, 125)
        painter.translate(7, 55)
        painter.scale(2.3,2.3)
        painter.drawPolyline(self.myPolygon)
        return pixmap

    def contextMenuEvent(self, event):
        self.scene().clearSelection()
        self.setSelected(False)
        self.myContextMenu.exec_(event.screenPos())

    def itemChange(self, change, value):
        if change == QtWidgets.QGraphicsItem.ItemPositionChange:
            for arrow in self.arrows:
                arrow.updatePosition()

        return value

    ####################################################################
   
    def handleAt(self, point):
        for k, v, in self.handles.items():
            if v.contains(point):
                return k
        return None

    def hoverMoveEvent(self, moveEvent):
        if self.isSelected():
            handle = self.handleAt(moveEvent.pos())
            cursor = Qt.ArrowCursor if handle is None else self.handleCursors[handle]
            self.setCursor(cursor)
        super().hoverMoveEvent(moveEvent)

    def hoverLeaveEvent(self, moveEvent):
        self.setCursor(Qt.ArrowCursor)
        super().hoverLeaveEvent(moveEvent)

    def mousePressEvent(self, mouseEvent):
        #self.setSelected(True)
        self.updateHandlesPos()
        self.handleSelected = self.handleAt(mouseEvent.pos())
        #self.handleSelected = None
        if self.handleSelected:
            self.mousePressPos = mouseEvent.pos()
            self.mousePressRect = self.boundingRect()
        super().mousePressEvent(mouseEvent)

    def mouseMoveEvent(self, mouseEvent):
        if self.handleSelected is not None:
            self.interactiveResize(mouseEvent.pos())
        else:
            super().mouseMoveEvent(mouseEvent)

    def mouseReleaseEvent(self, mouseEvent):
        super().mouseReleaseEvent(mouseEvent)
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.update()
    
    def boundingRect(self):
        o = self.handleSize + self.handleSpace
        return self.rect().adjusted(-o, -o, o, o)
    
    def rect(self):
        return QRectF(self._x, self._y, self._width, self._height)
    
    def setRect(self, rect):
        self._x = rect.x()
        self._y = rect.y()
        self._width = rect.width()
        self._height = rect.height()

    def updateHandlesPos(self):
        if not self.isSelected():
            return
        s = self.handleSize
        b = self.boundingRect()
        self.handles[self.handleTopLeft] = QRectF(b.left(), b.top(), s, s)
        self.handles[self.handleTopMiddle] = QRectF(b.center().x() - s / 2, b.top(), s, s)
        self.handles[self.handleTopRight] = QRectF(b.right() - s, b.top(), s, s)
        self.handles[self.handleMiddleLeft] = QRectF(b.left(), b.center().y() - s / 2, s, s)
        self.handles[self.handleMiddleRight] = QRectF(b.right() - s, b.center().y() - s / 2, s, s)
        self.handles[self.handleBottomLeft] = QRectF(b.left(), b.bottom() - s, s, s)
        self.handles[self.handleBottomMiddle] = QRectF(b.center().x() - s / 2, b.bottom() - s, s, s)
        self.handles[self.handleBottomRight] = QRectF(b.right() - s, b.bottom() - s, s, s)
    
        self.myPolygon = self.update_Polygon()
        self.setPolygon(self.myPolygon)
        for arrow in self.arrows:
            arrow.updatePosition()
   
    def interactiveResize(self, mousePos):
        offset = self.handleSize + self.handleSpace
        boundingRect = self.boundingRect()
        rect = self.rect()
        diff = QPointF(0, 0)

        self.prepareGeometryChange()

        if self.handleSelected == self.handleTopLeft:

            fromX = self.mousePressRect.left()
            fromY = self.mousePressRect.top()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setLeft(toX)
            boundingRect.setTop(toY)
            rect.setLeft(boundingRect.left() + offset)
            rect.setTop(boundingRect.top() + offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleTopMiddle:

            fromY = self.mousePressRect.top()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setY(toY - fromY)
            boundingRect.setTop(toY)
            rect.setTop(boundingRect.top() + offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleTopRight:

            fromX = self.mousePressRect.right()
            fromY = self.mousePressRect.top()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setRight(toX)
            boundingRect.setTop(toY)
            rect.setRight(boundingRect.right() - offset)
            rect.setTop(boundingRect.top() + offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleMiddleLeft:

            fromX = self.mousePressRect.left()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            diff.setX(toX - fromX)
            boundingRect.setLeft(toX)
            rect.setLeft(boundingRect.left() + offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleMiddleRight:
            fromX = self.mousePressRect.right()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            diff.setX(toX - fromX)
            boundingRect.setRight(toX)
            rect.setRight(boundingRect.right() - offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleBottomLeft:

            fromX = self.mousePressRect.left()
            fromY = self.mousePressRect.bottom()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setLeft(toX)
            boundingRect.setBottom(toY)
            rect.setLeft(boundingRect.left() + offset)
            rect.setBottom(boundingRect.bottom() - offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleBottomMiddle:

            fromY = self.mousePressRect.bottom()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setY(toY - fromY)
            boundingRect.setBottom(toY)
            rect.setBottom(boundingRect.bottom() - offset)
            self.setRect(rect)


        elif self.handleSelected == self.handleBottomRight:

            fromX = self.mousePressRect.right()
            fromY = self.mousePressRect.bottom()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setRight(toX)
            boundingRect.setBottom(toY)
            rect.setRight(boundingRect.right() - offset)
            rect.setBottom(boundingRect.bottom() - offset)
            self.setRect(rect)

        self.updateHandlesPos()
        #self.myPolygon = self.update_Polygon()
        #self.setPolygon(self.myPolygon)
        #for arrow in self.arrows:
        #    arrow.updatePosition()

    def paint(self, painter, option, widget=None):
        """
        Paint the node in the graphic view.
        """
        super(DiagramItem, self).paint(painter, option, widget)

        if not self.isSelected():
            return
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(51, 153, 255, 255)))
        painter.setPen(QPen(QColor(51,153,255, 255), 1.0, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        for handle, rect in self.handles.items():
            if self.handleSelected is None or handle == self.handleSelected:
                painter.drawEllipse(rect)


    def update_Polygon(self):
        #print("update_Polygon: ",self.diagramType)

        myPolygon = None
        path = QtGui.QPainterPath()
        if self.diagramType == self.StartEnd:
            #print("StartEnd")

            myPolygon = QtGui.QPolygonF([
                    QtCore.QPointF(self._x , self._y), 
                    QtCore.QPointF(self._x + self._width  , self._y ),
                    QtCore.QPointF(self._x + self._width, self._y + self._height  ),
                    QtCore.QPointF(self._x                , self._y + self._height),
                    QtCore.QPointF(self._x  , self._y                  )
                    ])

        elif self.diagramType == self.Conditional:
            #print("Conditional")
            myPolygon = QtGui.QPolygonF([
                    QtCore.QPointF(self._x + self._width/2, self._y), 
                    QtCore.QPointF(self._x + self._width  , self._y + self._height/2),
                    QtCore.QPointF(self._x + self._width/2, self._y + self._height  ),
                    QtCore.QPointF(self._x                , self._y + self._height/2),
                    QtCore.QPointF(self._x + self._width/2 , self._y                  )
                    ])

        elif self.diagramType == self.Step:
            #print("Step")
            #myPolygon = QtGui.QPolygonF([
            #        QtCore.QPointF(-100, -100), QtCore.QPointF(100, -100),
            #        QtCore.QPointF(100, 100), QtCore.QPointF(-100, 100),
            #        QtCore.QPointF(-100, -100)])
            myPolygon = QtGui.QPolygonF([
                    QtCore.QPointF(self._x , self._y), 
                    QtCore.QPointF(self._x + self._width  , self._y ),
                    QtCore.QPointF(self._x + self._width, self._y + self._height  ),
                    QtCore.QPointF(self._x                , self._y + self._height),
                    QtCore.QPointF(self._x  , self._y                  )
                    ])
        elif self.diagramType == self.Io:
            #print("Io")
            myPolygon = QtGui.QPolygonF([
                    QtCore.QPointF(self._x                    , self._y), 
                    QtCore.QPointF(self._x + self._width -20  , self._y), 
                    QtCore.QPointF(self._x + self._width  , self._y + self._height),
                    QtCore.QPointF(self._x + 20           , self._y + self._height),
                    QtCore.QPointF(self._x                    , self._y), 

                    ])
        

        elif self.diagramType == self.Ellipse:
            boundingRectangle = QRectF(self._x, self._y, self._width, self._height)
            path.addEllipse(boundingRectangle)
            myPolygon = path.toFillPolygon()

        elif self.diagramType == self.Hexagon:

            #print("Ellipse")
            g = 12
            path.moveTo(self._x + g               , self._y )
            path.lineTo(self._x + self._width - g , self._y )
            path.lineTo(self._x + self._width     , self._y  + g )
            path.lineTo(self._x + self._width     , self._y  + self._height - g)
            path.lineTo(self._x + self._width - g , self._y  + self._height)
            path.lineTo(self._x + g               , self._y  + self._height)
            path.lineTo(self._x                   , self._y  + self._height - g)
            path.lineTo(self._x                   , self._y  + g )
            path.lineTo(self._x + g               , self._y )

            myPolygon = path.toFillPolygon()

        return myPolygon
