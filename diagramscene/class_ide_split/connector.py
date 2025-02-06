#!/usr/bin/env python

import math

from PySide6 import QtCore, QtGui, QtWidgets

class ConnectorContactSurface:
    Top, TopRight, Right, BottomRight, Bottom, BottomLeft, Left, TopLeft = range(8)

class ConnectorPainterPathOrder:
    MoveTo, LineTo, ArcTo, AddText = range(4)

class Connector(QtWidgets.QGraphicsPathItem):
    def __init__(self, startItem, endItem, parent=None, scene=None):
        super(Connector, self).__init__(parent, scene)
        self._scene = scene
        self.arrowHead = QtGui.QPolygonF()

        self.myStartItem = startItem
        self.myEndItem = endItem
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.myColor = QtCore.Qt.white
        self.setPen(QtGui.QPen(self.myColor, 2, QtCore.Qt.SolidLine,
                QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))

    def setColor(self, color):
        self.myColor = color

    def startItem(self):
        return self.myStartItem

    def endItem(self):
        return self.myEndItem

    #def boundingRect(self):
    #    extra = (self.pen().width() + 20) / 2.0
    #    p1 = self.line().p1()
    #    p2 = self.line().p2()
    #    p1 = self.path().p1()
    #    p2 = self.path().p2()
    #    return QtCore.QRectF(p1, QtCore.QSizeF(p2.x() - p1.x(), p2.y() - p1.y())).normalized().adjusted(-extra, -extra, extra, extra)

    def shape(self):
        path = super(Connector, self).shape()
        path.addPolygon(self.arrowHead)
        return path

    def intersectItemPoints(self, polygon, line):
        #polygon = self.mapToScene(_polygon)
        intersection_points = []
        for i in range(0, polygon.size() - 1):
            #print("polygon:",i, end =" " )
            polyline = QtCore.QLineF(polygon[i], polygon[i + 1])
            _type , _point =  polyline.intersects(line)
            if _type  == QtCore.QLineF.BoundedIntersection:
                #print("polygon:",i, end =" " )
                #print("BoundedIntersection")
                intersection_points.append(_point)
            elif _type  == QtCore.QLineF.UnboundedIntersection:
                #print("UnboundedIntersection")
                pass
            elif _type  == QtCore.QLineF.NoIntersection:
                #print("NoIntersection")
                pass
        return intersection_points

    def intersectConnectorPoints(self, connector, path):
        #polygon = self.mapToScene(_polygon)
        c_path = connector.path()
        intersection_points = []
        if not c_path.intersects(path):
            print("  not  intersects")
            return intersection_points
        c_polygon = c_path.toFillPolygon()
        polygon   = path.toFillPolygon()
        #print(c_polygon)
        #print(polygon)
        for i in range(0, c_polygon.size() - 2):
            #print("polygon i:",i )
            c_polyline = QtCore.QLineF(c_polygon[i], c_polygon[i + 1])
            for j in range(0, polygon.size() - 2):
                #print("  polygon j:",j )
                line = QtCore.QLineF(polygon[j], polygon[j + 1])
                _type , _point =  c_polyline.intersects(line)
                if _type  == QtCore.QLineF.BoundedIntersection:
                    #print("    intersectConnectorPoints:",i,j )
                    #print("BoundedIntersection")
                    intersection_points.append(_point)
                elif _type  == QtCore.QLineF.UnboundedIntersection:
                    #print("UnboundedIntersection")
                    pass
                elif _type  == QtCore.QLineF.NoIntersection:
                    #print("NoIntersection")
                    pass
        return intersection_points

    def intersectConnectors(self, path):
        intersectPoints = []
        items = self._scene.items(path, mode = QtCore.Qt.IntersectsItemShape)
        for item in items:
            #print(str(type(item)))
            if isinstance(item, Connector):
                if item == self:
                    continue
                #print("--intersect Connecor")
                intersectPoint = self.intersectConnectorPoints(item, path)
                #print("intersectPoint:", len(intersectPoint), intersectPoint)
                intersectPoints.append( intersectPoint )
        return intersectPoints 

    def updatePosition(self):

        Start_suf = ConnectorContactSurface.Right
        End_suf   = ConnectorContactSurface.Left
        Start_pos_ratio = 0.2
        End_pos_ratio = 0.2

        sx = self.myStartItem.x() + self.myStartItem._x 
        sy = self.myStartItem.y() + self.myStartItem._y 
        sw = self.myStartItem._width
        sh = self.myStartItem._height

        ex = self.myEndItem.x() + self.myEndItem._x 
        ey = self.myEndItem.y() + self.myEndItem._y 
        ew = self.myEndItem._width
        eh = self.myEndItem._height

        points = []

        if   Start_suf == ConnectorContactSurface.Top:
            pass
        elif Start_suf == ConnectorContactSurface.TopRight:
            pass
        elif Start_suf == ConnectorContactSurface.Right:
            pass
            #points.append((ConnectorPainterPathOrder.MoveTo,QtCore.QPointF(sx , sy + sh*End_pos_ratio)))
            points.append((ConnectorPainterPathOrder.MoveTo,QtCore.QPointF(sx+sw/2 , sy + sh*End_pos_ratio)))

            #line = QtCore.QLineF(
            #                     QtCore.QPointF(sw/2  ,   sh*Start_pos_ratio),
            #                     QtCore.QPointF(sw    ,   sh*Start_pos_ratio))
            #i_points = self.intersectItemPoints(self.myStartItem.myPolygon,line)
            #if  len(i_points) == 0:
            #    return
            #points.append((ConnectorPainterPathOrder.MoveTo, (QtCore.QPointF(sx + i_points[0].x(), sy + i_points[0].y()))))

        elif Start_suf == ConnectorContactSurface.BottomRight:
            pass
        elif Start_suf == ConnectorContactSurface.Bottom:
            pass
        elif Start_suf == ConnectorContactSurface.BottomLeft:
            pass
        elif Start_suf == ConnectorContactSurface.Left:
            pass
        elif Start_suf == ConnectorContactSurface.TopLeft:
            pass

        if True:
            # Right Angle  直角
            mx = (ex -(sx + sw))/2
            points.append((ConnectorPainterPathOrder.LineTo,QtCore.QPointF( sx + sw  + mx , sy + sh*Start_pos_ratio )))
            points.append((ConnectorPainterPathOrder.LineTo,QtCore.QPointF( sx + sw  + mx , ey + eh*End_pos_ratio   )))

        if False:
            # Right Angle  直角 斜角
            mx = (ex -(sx + sw))/2
            points.append((ConnectorPainterPathOrder.LineTo,QtCore.QPointF( sx + sw  + mx  -10 , sy + sh*Start_pos_ratio )))
            points.append((ConnectorPainterPathOrder.LineTo,QtCore.QPointF( sx + sw  + mx , sy + sh*Start_pos_ratio  +10 )))
            points.append((ConnectorPainterPathOrder.LineTo,QtCore.QPointF( sx + sw  + mx , ey + sh*Start_pos_ratio   -10)))
            points.append((ConnectorPainterPathOrder.LineTo,QtCore.QPointF( sx + sw  + mx + 10 , ey + eh*End_pos_ratio   )))

        if False:
            # Right Angle  直角 丸角
            mx = (ex -(sx + sw))/2
            g = 20
            points.append((ConnectorPainterPathOrder.LineTo,QtCore.QPointF( sx + sw  + mx  -g , sy + sh*Start_pos_ratio )))

            points.append((ConnectorPainterPathOrder.MoveTo, QtCore.QPointF(sx + sw  + mx  , sy + sh*Start_pos_ratio + g )))
            points.append((ConnectorPainterPathOrder.ArcTo, sx + sw  + mx  -g*2 , sy + sh*Start_pos_ratio ,g*2,g*2,0,90))

            points.append((ConnectorPainterPathOrder.MoveTo,QtCore.QPointF( sx + sw  + mx , sy + sh*Start_pos_ratio  +g )))
            points.append((ConnectorPainterPathOrder.LineTo,QtCore.QPointF( sx + sw  + mx , ey + sh*Start_pos_ratio   -g)))

            points.append((ConnectorPainterPathOrder.MoveTo, QtCore.QPointF(sx + sw  + mx  , ey + eh*Start_pos_ratio - g*2 )))
            points.append((ConnectorPainterPathOrder.ArcTo, sx + sw  + mx   , ey + eh*Start_pos_ratio -g*2 ,g*2,g*2,180,90))

            points.append((ConnectorPainterPathOrder.MoveTo,QtCore.QPointF( sx + sw  + mx + g , ey + eh*End_pos_ratio   )))

            timesFont = QtGui.QFont("Times", 12);
            timesFont.setStyleStrategy(QtGui.QFont.ForceOutline);
            points.append((ConnectorPainterPathOrder.MoveTo,QtCore.QPointF( 50,50 )))
            points.append((ConnectorPainterPathOrder.AddText, 250, 50, timesFont, "QtText"  ))

            poiints.append((ConnectorPainterPathOrder.MoveTo,QtCore.QPointF( sx + sw  + mx + g , ey + eh*End_pos_ratio   )))

        if False:
            # Slant 傾斜
            top = 15
            points.append((ConnectorPainterPathOrder.LineTo,QtCore.QPointF( sx + sw  + top , sy + sh*Start_pos_ratio )))
            points.append((ConnectorPainterPathOrder.LineTo,QtCore.QPointF( ex       - top , ey + eh*End_pos_ratio   )))

        if False:
            # Curve カーブ
            pass

        if   End_suf == ConnectorContactSurface.Top:
            pass
        elif End_suf == ConnectorContactSurface.TopRight:
            pass
        elif End_suf == ConnectorContactSurface.Right:
            pass
        elif End_suf == ConnectorContactSurface.BottomRight:
            pass
        elif End_suf == ConnectorContactSurface.Bottom:
            pass
        elif End_suf == ConnectorContactSurface.BottomLeft:
            pass
        elif End_suf == ConnectorContactSurface.Left:
            pass
            #points.append((ConnectorPainterPathOrder.LineTo,QtCore.QPointF(ex , ey + eh*End_pos_ratio)))
            points.append((ConnectorPainterPathOrder.LineTo,QtCore.QPointF(ex+ew/2 , ey + eh*End_pos_ratio)))
            
            #line = QtCore.QLineF(
            #                     QtCore.QPointF(0     ,   eh*End_pos_ratio),
            #                     QtCore.QPointF(ew/2  ,   eh*End_pos_ratio))
            #i_points = self.intersectItemPoints(self.myEndItem.myPolygon,line)
            #if  len(i_points) == 0:
            #    return
            #points.append((ConnectorPainterPathOrder.LineTo,QtCore.QPointF(ex + i_points[0].x(), ey + i_points[0].y())))

        elif End_suf == ConnectorContactSurface.TopLeft:
            pass


        path = QtGui.QPainterPath()
        #path.moveTo( points[0])
        #for point in points[1:]:
        #    path.lineTo( point )

        for order in points:
            #print("#",order)
            if order[0] == ConnectorPainterPathOrder.MoveTo:
                path.moveTo( order[1])
            elif order[0] == ConnectorPainterPathOrder.LineTo:
                path.lineTo( order[1])
            elif order[0] == ConnectorPainterPathOrder.ArcTo:
                #print(order[1])
                #print(order[2])
                #print(order[3])
                #print(order[4])
                #print(order[5])
                #print(order[6])
                x = order[1]
                y = order[2]
                w = order[3]
                h = order[4]
                sa = order[5]
                sl = order[6]
                #path.arcTo( order[1], order[2],order[3].order[4],order[5], order[6])
                path.arcTo( x, y, w, h, sa, sl)
                pass
            elif order[0] == ConnectorPainterPathOrder.AddText:
                x = order[1]
                y = order[2]
                font = order[3]
                text = order[4]
                path.addText( x, y, font, text)
                pass

        #path.closeSubpath()
        
        intersectPoints = self.intersectConnectors(path)
        if len(intersectPoints) > 0:
            #print(intersectPoints)
            s =20
            path.moveTo( intersectPoints[0][0].x()+s/2, intersectPoints[0][0].y())
            path.arcTo(  intersectPoints[0][0].x()-s/2, intersectPoints[0][0].y()-s/2, s,s,0, 360)

       
        self.setPath(path)

    def updatePosition_OLD(self):

        Start_suf = ConnectorContactSurface.Right
        End_suf   = ConnectorContactSurface.Left
        Start_pos_ratio = 0.2
        End_pos_ratio = 0.2

        sx = self.myStartItem.x() + self.myStartItem._x 
        sy = self.myStartItem.y() + self.myStartItem._y 
        sw = self.myStartItem._width
        sh = self.myStartItem._height

        ex = self.myEndItem.x() + self.myEndItem._x 
        ey = self.myEndItem.y() + self.myEndItem._y 
        ew = self.myEndItem._width
        eh = self.myEndItem._height

        points = []

        if   Start_suf == ConnectorContactSurface.Top:
            pass
        elif Start_suf == ConnectorContactSurface.TopRight:
            pass
        elif Start_suf == ConnectorContactSurface.Right:
            points.append(QtCore.QPointF(sx  + sw, sy + sh*Start_pos_ratio))

        elif Start_suf == ConnectorContactSurface.BottomRight:
            pass
        elif Start_suf == ConnectorContactSurface.Bottom:
            pass
        elif Start_suf == ConnectorContactSurface.BottomLeft:
            pass
        elif Start_suf == ConnectorContactSurface.Left:
            pass
        elif Start_suf == ConnectorContactSurface.TopLeft:
            pass


        mx = (ex -(sx + sw))/2
        points.append(QtCore.QPointF( sx + sw  + mx , sy + sh*Start_pos_ratio ))
        points.append(QtCore.QPointF( sx + sw  + mx , ey + eh*End_pos_ratio   ))


        if   End_suf == ConnectorContactSurface.Top:
            pass
        elif End_suf == ConnectorContactSurface.TopRight:
            pass
        elif End_suf == ConnectorContactSurface.Right:
            pass
        elif End_suf == ConnectorContactSurface.BottomRight:
            pass
        elif End_suf == ConnectorContactSurface.Bottom:
            pass
        elif End_suf == ConnectorContactSurface.BottomLeft:
            pass
        elif End_suf == ConnectorContactSurface.Left:
            points.append(QtCore.QPointF(ex , ey + eh*End_pos_ratio))

        elif End_suf == ConnectorContactSurface.TopLeft:
            pass


        path = QtGui.QPainterPath()
        path.moveTo( points[0])
        for point in points[1:]:
            path.lineTo( point )

        self.setPath(path)

    def updatePosition_BASIC(self):
        path = QtGui.QPainterPath()

        sx = self.myStartItem.x() + self.myStartItem._x 
        sy = self.myStartItem.y() + self.myStartItem._y 
        sw = self.myStartItem._width
        sh = self.myStartItem._height

        ex = self.myEndItem.x() + self.myEndItem._x 
        ey = self.myEndItem.y() + self.myEndItem._y 
        ew = self.myEndItem._width
        eh = self.myEndItem._height

        mx = (ex -(sx + sw))/2

        # L => R
        xd = self.myEndItem.x() - self.myStartItem.x()
        path.moveTo( sx + sw , sy )
        path.lineTo( sx + sw  + mx , sy )
        path.lineTo( sx + sw  + mx , ey )
        path.lineTo( ex            , ey )

        self.setPath(path)




    """
    def paint(self, painter, option, widget=None):
        if (self.myStartItem.collidesWithItem(self.myEndItem)):
            return

        myStartItem = self.myStartItem
        myEndItem = self.myEndItem
        myColor = self.myColor
        myPen = self.pen()
        myPen.setColor(self.myColor)
        arrowSize = 20.0
        painter.setPen(myPen)
        painter.setBrush(self.myColor)

        centerLine = QtCore.QLineF(myStartItem.pos(), myEndItem.pos())
        endPolygon = myEndItem.polygon()
        p1 = endPolygon.at(0) + myEndItem.pos()

        intersectPoint = QtCore.QPointF()
        for i in endPolygon:
            p2 = i + myEndItem.pos()
            polyLine = QtCore.QLineF(p1, p2)
            #intersectType, intersectPoint = polyLine.intersect(centerLine)
            intersectType, intersectPoint = polyLine.intersects(centerLine)
            if intersectType == QtCore.QLineF.BoundedIntersection:
                break
            p1 = p2

        self.setLine(QtCore.QLineF(intersectPoint, myStartItem.pos()))
        line = self.line()

        angle = math.acos(line.dx() / line.length())
        if line.dy() >= 0:
            angle = (math.pi * 2.0) - angle

        arrowP1 = line.p1() + QtCore.QPointF(math.sin(angle + math.pi / 3.0) * arrowSize,
                                        math.cos(angle + math.pi / 3) * arrowSize)
        arrowP2 = line.p1() + QtCore.QPointF(math.sin(angle + math.pi - math.pi / 3.0) * arrowSize,
                                        math.cos(angle + math.pi - math.pi / 3.0) * arrowSize)

        self.arrowHead.clear()
        for point in [line.p1(), arrowP1, arrowP2]:
            self.arrowHead.append(point)

        painter.drawLine(line)
        painter.drawPolygon(self.arrowHead)
        if self.isSelected():
            painter.setPen(QtGui.QPen(myColor, 1, QtCore.Qt.DashLine))
            myLine = QtCore.QLineF(line)
            myLine.translate(0, 4.0)
            painter.drawLine(myLine)
            myLine.translate(0,-8.0)
            painter.drawLine(myLine)


    """
