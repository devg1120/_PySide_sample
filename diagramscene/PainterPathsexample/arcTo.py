


from PySide6.QtWidgets import (QApplication, QWidget, QLabel,
                               QComboBox, QSpinBox, QGridLayout, QHBoxLayout,QVBoxLayout, QPushButton, QFontDialog,
                               QSizePolicy)
from PySide6.QtGui import QPainterPath, QLinearGradient, QColor,QPen, QFont, QPalette, QPainter
from PySide6.QtCore import Qt, QSize, QSizeF, QPoint, QPointF, QLineF, QRectF
#from PySide6.QtMath import  qDegreesToRadians, qRadiansToDegrees, qAtan2, qSin, qCos
import math, sys


#
# https://doc.qt.io/qt-6/qtwidgets-painting-painterpaths-example.html
#

class Window(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        #p = self.palette()
        #p.setColor(self.backgroundRole(), Qt.white)
        #self.setPalette(p)
        self.setStyleSheet('background-color: white; color: black;')

        #self.font = QFont("Helvetica [Cronyx]", 10)
        #self.font = QFont("Courier")
        #self.font = QFont("MSゴシック")
        #self.font.setPointSize(6)
        #self.font.setItalic(False)
        #self.font.setBold(False)
        #self.font.setFixedPitch(True)
        #self.font.setKerning(True)
        #self.font.setLetterSpacing(QFont.AbsoluteSpacing, 0)

        self.renderAreas = []     

        # https://stackoverflow.com/questions/40010114/how-are-angles-on-qpainterpatharcto-interpreted
        #

        r = QRectF(20.0, 20.0, 60.0, 60.0)
        piePath = QPainterPath()
        #piePath.moveTo(50.0, 50.0)
        piePath.arcMoveTo(r, 45)
        piePath.arcTo(r, 45.0, 270.0)
        #piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 60 arc 45 270",result = ""  )) 

        r = QRectF(20.0, 30.0, 60.0, 40.0)
        piePath = QPainterPath()
        #piePath.moveTo(50.0, 50.0)
        piePath.arcMoveTo(r, 45)
        piePath.arcTo(r, 45.0, 270.0)
        #piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 40 arc 45 270",result = ""  )) 



        title = "60 x 40 arc intersect cut"
        r = QRectF(20.0, 30.0, 60.0, 40.0)
        cr = QRectF(r.center()-QPointF(2,2)  , QSizeF(4,4))
        L1 = QPointF(20,80)
        L2 = QPointF(80,30)

        testpath1 = QPainterPath()
        testpath1.arcMoveTo(r, 0.0)
        testpath1.arcTo(r, 0.0, 360.0)

        testpath2 = QPainterPath()
        testpath2.moveTo(L1)
        testpath2.lineTo(L2)

        points = self.intersectPathPoints(testpath1, testpath2)
        center = r.center()
        p0 = QRectF(points[0]-QPointF(2,2)  , QSizeF(4,4))
        p1 = QRectF(points[1]-QPointF(2,2)  , QSizeF(4,4))

        #*******************************************************
        angle1 = QLineF(center,points[0]).angle()
        angle2 = QLineF(center,points[1]).angle()
        radius1 = r.width()/2
        radius2 = r.height()/2
        angleRad1 = math.radians(angle1)
        angle1 = math.degrees(math.atan2(radius1 * math.sin(angleRad1),
                                             radius2 * math.cos(angleRad1)))

        angleRad2 = math.radians(angle2)
        angle2 =  math.degrees(math.atan2(radius1 * math.sin(angleRad2),
                                             radius2 * math.cos(angleRad2)))
        angle2 = angle2 +360
        #*******************************************************
        testpath1 = QPainterPath()
        testpath1.arcMoveTo(r, angle1 )
        testpath1.arcTo(r, angle1, angle2 - angle1)

        testpath3 = QPainterPath()   # center point
        testpath3.arcMoveTo(cr, 0.0)
        testpath3.arcTo(cr, 0.0, 360.0)
        testpath3.arcMoveTo(p0, 0.0)
        testpath3.arcTo(p0, 0.0, 360.0)
        testpath3.arcMoveTo(p1, 0.0)
        testpath3.arcTo(p1, 0.0, 360.0)

        self.renderAreas.append(RenderArea([testpath1,testpath2, testpath3] ,title,result = "ipn:" + str(len(points)) ))

        """
        startAngle  =45
        endAngle = 270
        
        #radius1 = 60 #X-axis
        #radius2 = 40 #Y-axis
        
        radius1 = 30 #X-axis
        radius2 = 20 #Y-axis
        center = QPointF(50,50)
        #boundingRect = QRectF(center.x() - radius1, center.y() - radius2, radius1*2, radius2*2)
        #r  = QRectF(20.0, 30.0, 60.0, 40.0)
        r = QRectF(center.x() - radius1, center.y() - radius2, radius1*2, radius2*2)
        
        #if (!qFuzzyIsNull(endAngle) &&
        #        !VFuzzyComparePossibleNulls(endAngle, 90) &&
        #        !VFuzzyComparePossibleNulls(endAngle, 180) &&
        #        !VFuzzyComparePossibleNulls(endAngle, 270) &&
        #        !VFuzzyComparePossibleNulls(endAngle, 360))
        #{
        #  // Calculating correct end angle
        #  qreal endAngleRad = qDegreesToRadians(endAngle);
        #  endAngle = qRadiansToDegrees(qAtan2(radius1 * qSin(endAngleRad),
        #                                      radius2 * qCos(endAngleRad)));
        #}
        
        #endAngleRad = qDegreesToRadians(endAngle)
        #endAngle = qRadiansToDegrees(qAtan2(radius1 * qSin(endAngleRad),
        #                                     radius2 * qCos(endAngleRad)))

        endAngleRad = math.radians(endAngle)
        endAngle = math.degrees(math.atan2(radius1 * math.sin(endAngleRad),
                                             radius2 * math.cos(endAngleRad)))

        startLine = QLineF(center.x(), center.y(), center.x() + radius1, center.y())
        endLine = startLine
        
        startLine.setAngle(startAngle)
        endLine.setAngle(endAngle)
        sweepLength = startLine.angleTo(endLine)
        
        myPath = QPainterPath()
        #myPath.arcTo(boundingRect, startAngle, sweepLength)
        myPath.arcMoveTo(r, startAngle)
        myPath.arcTo(r, startAngle, sweepLength)
        #myPath.arcMoveTo(r, 45)
        #myPath.arcTo(r, 45, 270)
        self.renderAreas.append(RenderArea([myPath] ,"60 x 40 arc 45 270",result = ""  )) 
        """

        """
        r = QRectF(20.0, 20.0, 60.0, 40.0)
        piePath = QPainterPath()
        piePath.arcMoveTo(r,  60.0)
        piePath.arcTo(r, 60.0, 240.0)
        #piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 40 arc 2",result = ""  )) 
        """




        ##################################################################################

        #self.button1 = QPushButton('Select Font')
        #self.button1.clicked.connect(self.selectFont)

        self.fillRuleComboBox = QComboBox()
        self.fillRuleComboBox.addItem(self.tr("Odd Even"))
        self.fillRuleComboBox.addItem(self.tr("Winding"))
   
        self.fillRuleLabel = QLabel(self.tr("Fill &Rule:"))
        self.fillRuleLabel.setBuddy(self.fillRuleComboBox)
        
        
        self.fillColor1ComboBox = QComboBox()
        self.populateWithColors(self.fillColor1ComboBox)
        #self.fillColor1ComboBox.setCurrentIndex(self.fillColor1ComboBox.findText("mediumslateblue"))
        self.fillColor1ComboBox.setCurrentIndex(self.fillColor1ComboBox.findText("limegreen"))

        self.fillColor2ComboBox = QComboBox()
        self.populateWithColors(self.fillColor2ComboBox)
        self.fillColor2ComboBox.setCurrentIndex(self.fillColor2ComboBox.findText("cornsilk"))

        self.fillGradientLabel = QLabel(self.tr("&Fill Gradient"))
        self.fillGradientLabel.setBuddy(self.fillColor1ComboBox)

        self.fillToLabel = QLabel(self.tr("to"))
        self.fillToLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        self.penWidthSpinBox = QSpinBox(minimum=0, maximum=20)

        self.penWidthLabel = QLabel(self.tr("&Pen"))
        self.penWidthLabel.setBuddy(self.penWidthSpinBox)
        
        self.penColorComboBox = QComboBox()
        self.populateWithColors(self.penColorComboBox)
        #self.penColorComboBox.setCurrentIndex(self.penColorComboBox.findText("darkslateblue"))
        self.penColorComboBox.setCurrentIndex(self.penColorComboBox.findText("green"))

        self.penColorLabel = QLabel()
        self.penColorLabel.setBuddy(self.penColorComboBox)

        self.fillRuleComboBox.activated.connect(self.fillRuleChanged)
        self.fillColor1ComboBox.activated.connect(self.fillGradientChanged)
        self.fillColor2ComboBox.activated.connect(self.fillGradientChanged)
        self.penColorComboBox.activated.connect(self.penColorChanged)

            
        topLayout = QGridLayout()
        
        
        self.rotationAngleSpinBox = QSpinBox(maximum=359)
        
        self.rotationAngleSpinBox.setWrapping(True)
        self.rotationAngleSpinBox.setSuffix("\xB0")
        
        self.rotationAngleLabel = QLabel(self.tr("&Rotation Angle"))
        self.rotationAngleLabel.setBuddy(self.rotationAngleSpinBox)

        for area in self.renderAreas:
            self.penWidthSpinBox.valueChanged.connect(area.setPenWidth)
            self.rotationAngleSpinBox.valueChanged.connect(area.setRotationAngle)
        
        cloumn = 2
        for num, area in enumerate(self.renderAreas):
            topLayout.addWidget(area, int(num/cloumn), num%cloumn)

        panelLayout = QGridLayout()
        panelLayout.addWidget(self.fillRuleLabel         , 0, 0)
        panelLayout.addWidget(self.fillRuleComboBox      , 0, 1, 1, 3)
        panelLayout.addWidget(self.fillGradientLabel     , 1, 0)
        panelLayout.addWidget(self.fillColor1ComboBox    , 1, 1)
        #panelLayout.addWidget(self.fillToLabel           , 2, 1)
        panelLayout.addWidget(self.fillColor2ComboBox    , 2, 1)
        panelLayout.addWidget(self.penWidthLabel         , 3, 0)
        panelLayout.addWidget(self.penWidthSpinBox       , 3, 1, 1, 3)
        panelLayout.addWidget(self.penColorLabel         , 4, 0)
        panelLayout.addWidget(self.penColorComboBox      , 4, 1, 1, 3)
        panelLayout.addWidget(self.rotationAngleLabel    , 5, 0)
        panelLayout.addWidget(self.rotationAngleSpinBox  , 5, 1, 1, 3)


        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 5, 5)
        mainLayout.addLayout(panelLayout, 0, 5, 1, 1)
        self.setLayout(mainLayout)

        #mainLayout = QHBoxLayout()
        #mainLayout.addLayout(topLayout, stretch=6)
        #mainLayout.addLayout(panelLayout, stretch =1)
        #self.setLayout(mainLayout)

        self.fillRuleChanged()
        self.fillGradientChanged()
        self.penColorChanged()
        self.penWidthSpinBox.setValue(0)

        self.setWindowTitle("Painter Paths")
       
    def intersectPathPoints(self, path1, path2):
        #polygon = self.mapToScene(_polygon)
        #c_path = path1
        intersection_points = []
        if not path1.intersects(path2):
            print("  not  intersects")
            return intersection_points
        c_polygon = path1.toFillPolygon()
        polygon   = path2.toFillPolygon()
        #print(c_polygon)
        #print(polygon)
        for i in range(0, c_polygon.size() - 2):
            #print("polygon i:",i )
            c_polyline = QLineF(c_polygon[i], c_polygon[i + 1])
            for j in range(0, polygon.size() - 2):
                #print("  polygon j:",j )
                line = QLineF(polygon[j], polygon[j + 1])
                _type , _point =  c_polyline.intersects(line)
                if _type  == QLineF.BoundedIntersection:
                    #print("    intersectConnectorPoints:",i,j )
                    #print("BoundedIntersection")
                    intersection_points.append(_point)
                elif _type  == QLineF.UnboundedIntersection:
                    #print("UnboundedIntersection")
                    pass
                elif _type  == QLineF.NoIntersection:
                    #print("NoIntersection")
                    pass
        return intersection_points

   
    def fillRuleChanged(self):

        rule = self.currentItemData(self.fillRuleComboBox)

        for area in self.renderAreas:
            area.setFillRule(rule)
            
            

    def fillGradientChanged(self):

        color1 = self.currentItemData(self.fillColor1ComboBox)
        color2 = self.currentItemData(self.fillColor2ComboBox)

        for area in self.renderAreas:
            area.setFillGradient(color1, color2)

    def penColorChanged(self):

        color = self.currentItemData(self.penColorComboBox)

        for area in self.renderAreas:
            area.setPenColor(color)
            

    def populateWithColors(self, comboBox):

        colorNames = QColor.colorNames()

        for name in colorNames:
            comboBox.addItem(name, QColor(name))
            

    def currentItemData(self, comboBox):
        from PySide6.QtCore import QModelIndex
        model = comboBox.model()
        index = model.index(comboBox.currentIndex(), 0)
        data = comboBox.model().data(index)
        if comboBox is self.fillRuleComboBox:
            data = Qt.FillRule(comboBox.currentIndex())
        
        return data

    #def selectFont(self):
    #    ok, self.font = QFontDialog.getFont(QFont(), self, "Select font")       
    #    print("selecrFont:",self.font.family())
    
            

class RenderArea(QWidget):

    def __init__(self, paths, name, parent=None, result=None):
        super().__init__(parent)

        self.paths = paths
        self.fillColor1 = QColor()
        self.fillColor2 = QColor()
        self.penWidth = 1
        self.penColor = QColor()
        self.rotationAngle = 0
        self.setBackgroundRole(QPalette.Base)        
        self.name = name
        #self.setFont(QFont("Courier",9))
        self.setFont(QFont("Helvetica",6))
        self.result = result


    def minimumSizeHint(self):
        
        return QSize(180, 180)

    def sizeHint(self):

        return QSize(100, 100)

    def setFillRule(self, rule):

        #self.paths[0].setFillRule(rule)
        for path in self.paths:
           path.setFillRule(rule)
        self.update()

    def setFillGradient(self, color1, color2):
        self.fillColor1 = color1
        self.fillColor2 = color2
        self.update()
        

    def setPenWidth(self, width):
        self.penWidth = width
        self.update()
        

    def setPenColor(self, color):
        self.penColor = color
        self.update()
        

    def setRotationAngle(self, degrees):
        self.rotationAngle = degrees
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.scale(self.width()/100.0, self.height()/100.0)
        painter.translate(50.0, 50.0)
        painter.rotate(-self.rotationAngle)
        painter.translate(-50.0, -50.0)

        pen = painter.pen()
        pen.setColor(self.penColor)
        pen.setWidth(self.penWidth)
        pen.setStyle(Qt.SolidLine)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        
        painter.setPen(pen)
        gradient = QLinearGradient(0, 0, 0, 100)
        gradient.setColorAt(0.0, self.fillColor1)
        gradient.setColorAt(1.0, self.fillColor2)
        
        painter.setBrush(gradient)
        #painter.drawPath(self.paths[0])
        for path in self.paths:
           painter.drawPath(path)

        pen = painter.pen()
        pen.setColor(QColor("blue"))
        painter.setPen(pen)
        painter.drawText(QPoint(0,7),self.name)
        pen.setWidth(0.5)
        #pen.setStyle(Qt.SolidLine)
        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(0,  0,100,  0)
        painter.drawLine(0, 10,100, 10)
        painter.drawLine(0, 20,100, 20)
        painter.drawLine(0, 30,100, 30)
        painter.drawLine(0, 40,100, 40)
        painter.drawLine(0, 50,100, 50)
        painter.drawLine(0, 60,100, 60)
        painter.drawLine(0, 70,100, 70)
        painter.drawLine(0, 80,100, 80)
        painter.drawLine(0, 90,100, 90)
        painter.drawLine(0,100,100,100)

        painter.drawLine(  0, 0,  0, 100)
        painter.drawLine( 10, 0, 10, 100)
        painter.drawLine( 20, 0, 20, 100)
        painter.drawLine( 30, 0, 30, 100)
        painter.drawLine( 40, 0, 40, 100)
        painter.drawLine( 50, 0, 50, 100)
        painter.drawLine( 60, 0, 60, 100)
        painter.drawLine( 70, 0, 70, 100)
        painter.drawLine( 80, 0, 80, 100)
        painter.drawLine( 90, 0, 90, 100)
        painter.drawLine(100, 0,100, 100)

        pen.setColor(QColor("red"))
        pen.setWidth(0.7)
        pen.setStyle(Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawLine(0,0,100,100)
        painter.drawLine(0,100,100,0)

        pen = painter.pen()
        pen.setColor(QColor("blue"))
        painter.setPen(pen)
        painter.drawText(QPoint(0,7),self.name)

        pen = painter.pen()
        pen.setColor(QColor("red"))
        painter.setPen(pen)
        if self.result != None:
            painter.drawText(QPoint(10,98),self.result)


def main():

    windowWidth =  1200
    windowHeight = 500 

    app = QApplication()
    window = Window()
    window.resize(windowWidth, windowHeight)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    

    

