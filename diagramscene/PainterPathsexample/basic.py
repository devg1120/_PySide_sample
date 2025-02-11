


from PySide6.QtWidgets import (QApplication, QWidget, QLabel,
                               QComboBox, QSpinBox, QGridLayout, QHBoxLayout,QVBoxLayout, QPushButton, QFontDialog,
                               QSizePolicy)
from PySide6.QtGui import QPainterPath, QLinearGradient, QColor,QPen, QFont, QPalette, QPainter, QPolygon
from PySide6.QtCore import Qt, QSize, QSizeF, QPoint, QPointF, QLineF, QRectF
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

        rectPath = QPainterPath()
        rectPath.moveTo(20.0, 30.0)
        rectPath.lineTo(80.0, 30.0)
        rectPath.lineTo(80.0, 70.0)
        rectPath.lineTo(20.0, 70.0)
        rectPath.closeSubpath()
        self.renderAreas.append(RenderArea([rectPath]     ,"rectPath"))

        rectPath = QPainterPath()
        rectPath.moveTo(20.0, 30.0)
        rectPath.lineTo(80.0, 30.0)
        rectPath.lineTo(80.0, 70.0)
        rectPath.lineTo(20.0, 70.0)
        rectPath.closeSubpath()

        rectPath2 = QPainterPath()
        rectPath2.moveTo(30.0, 40.0)
        rectPath2.lineTo(60.0, 40.0)
        rectPath2.lineTo(60.0, 50.0)
        rectPath2.lineTo(30.0, 50.0)
        rectPath2.closeSubpath()

        #clip_path = rectPath.subtracted(rectPath2)
        #self.renderAreas.append(RenderArea([rectPath ]     ,"clipPath",clippath = clip_path))
        self.renderAreas.append(RenderArea([ rectPath - rectPath2 ]     ,"clipPath"))


        #pathE = QPainterPath()
        #pathE.addEllipse(-100,-100,200,200)
        #pathR = QPainterPath()
        #pathR.addRect(0,0,100,100)

        #pathE = QPainterPath()
        #pathE.addEllipse(-50,-50,100,100)
        #pathR = QPainterPath()
        #pathR.addRect(0,0,50,50)

        pathE = QPainterPath()
        pathE.addEllipse(-40,-30,100,100)
        pathR = QPainterPath()
        pathR.addRect(10,20,50,50)
        self.renderAreas.append(RenderArea([ pathR - pathE ]     ,"clipPath"))



        roundRectPath = QPainterPath()
        roundRectPath.moveTo(80.0, 35.0)
        roundRectPath.arcTo(70.0, 35.0, 10.0, 10.0, 0.0, 90.0)
        roundRectPath.lineTo(25.0, 30.0)
        roundRectPath.arcTo(20.0, 30.0, 10.0, 10.0, 90.0, 90.0)
        roundRectPath.lineTo(20.0, 65.0)
        roundRectPath.arcTo(20.0, 60.0, 10.0, 10.0, 180.0, 90.0)
        roundRectPath.lineTo(75.0, 70.0)
        roundRectPath.arcTo(70.0, 60.0, 10.0, 10.0, 270.0, 90.0)
        #roundRectPath.addText(20,20, self.font, "roundRectPath")
        roundRectPath.closeSubpath()

        ellipsePath = QPainterPath()
        ellipsePath.moveTo(80.0, 50.0)
        ellipsePath.arcTo(20.0, 30.0, 60.0, 40.0, 0.0, 360.0)
        
        piePath = QPainterPath()
        piePath.moveTo(50.0, 50.0)
        piePath.arcTo(20.0, 30.0, 60.0, 40.0, 60.0, 240.0)
        piePath.closeSubpath()

        polygonPath = QPainterPath()
        polygonPath.moveTo(10.0, 80.0)
        polygonPath.lineTo(20.0, 10.0)
        polygonPath.lineTo(80.0, 30.0)
        polygonPath.lineTo(90.0, 70.0)
        polygonPath.closeSubpath()

        groupPath = QPainterPath()
        groupPath.moveTo(60.0, 40.0)
        groupPath.arcTo(20.0, 20.0, 40.0, 40.0, 0.0, 360.0)
        groupPath.moveTo(40.0, 40.0)
        groupPath.lineTo(40.0, 80.0)
        groupPath.lineTo(80.0, 80.0)
        groupPath.lineTo(80.0, 40.0)
        groupPath.closeSubpath()

        textPath = QPainterPath()
        timesFont = QFont("Times", 50)
        timesFont.setStyleStrategy(QFont.ForceOutline)
        textPath.addText(10, 70, timesFont, self.tr("Qt"))

        bezierPath = QPainterPath()
        bezierPath.moveTo(20, 30)
        bezierPath.cubicTo(80, 0, 50, 50, 80, 80)

        starPath = QPainterPath()
        starPath.moveTo(90, 50)
        for i in range(5):
            starPath.lineTo(50 + 40*math.cos(0.8*i*math.pi),
                            50 + 40*math.sin(0.8*i*math.pi))

        starPath.closeSubpath()

        #self.renderAreas.append(RenderArea([rectPath]     ,"rectPath"))
        self.renderAreas.append(RenderArea([roundRectPath],"roundRectPath"))
        self.renderAreas.append(RenderArea([ellipsePath]  ,"ellipsePath"))
        self.renderAreas.append(RenderArea([piePath]      ,"piePath"))
        self.renderAreas.append(RenderArea([polygonPath]  ,"polygonPath"))
        self.renderAreas.append(RenderArea([groupPath]    ,"groupPath"))
        self.renderAreas.append(RenderArea([textPath]     ,"textPath"))
        self.renderAreas.append(RenderArea([bezierPath]   ,"bezierPath"))
        self.renderAreas.append(RenderArea([starPath]     ,"starPath")) 


        # http://blog.livedoor.jp/take_z_ultima/archives/52550736.html
        testpath1 = QPainterPath()
        testpath1.moveTo(30,25)
        testpath1.lineTo(10,40)
        testpath1.lineTo(60,45)
        testpath1.moveTo(30,55)
        testpath1.lineTo(10,70)
        testpath1.lineTo(60,75)
        testpath1.closeSubpath()

        self.renderAreas.append(RenderArea([testpath1]    ,"testpath1")) 

        testpath2 = QPainterPath()
        testpath2.moveTo(30,25)
        testpath2.lineTo(10,40)
        testpath2.lineTo(60,45)
        testpath2.lineTo(30,25)
        testpath2.moveTo(30,55)
        testpath2.lineTo(10,70)
        testpath2.lineTo(60,75)
        testpath2.closeSubpath()

        self.renderAreas.append(RenderArea([testpath2]    ,"testpath2")) 

        testpath1 = QPainterPath()
        testpath1.moveTo(90,25)
        testpath1.lineTo(10,60)
        testpath1.lineTo(90,75)
        testpath2 = QPainterPath()
        testpath2.moveTo(50,20)
        testpath2.lineTo(50,90)
        points = self.intersectPathPoints(testpath1, testpath2)
        self.renderAreas.append(RenderArea([testpath1,testpath2] ,"intesect at 2",result = "ipn:" + str(len(points)) )) 

        testpath1 = QPainterPath()
        testpath1.moveTo(30,25)
        testpath1.lineTo(10,60)
        testpath1.lineTo(90,75)
        testpath2 = QPainterPath()
        testpath2.moveTo(50,20)
        testpath2.lineTo(50,90)
        points = self.intersectPathPoints(testpath1, testpath2)
        self.renderAreas.append(RenderArea([testpath1,testpath2] ,"intesect at 1",result = "ipn:" + str(len(points)) )) 

        testpath1 = QPainterPath()
        #testpath1.moveTo(80.0, 50.0)
        testpath1.arcMoveTo(20.0, 30.0, 60.0, 40.0, 0.0)
        testpath1.arcTo(20.0, 30.0, 60.0, 40.0, 0.0, 360.0)
        testpath2 = QPainterPath()
        testpath2.moveTo(40,80)
        testpath2.lineTo(80,30)
        points = self.intersectPathPoints(testpath1, testpath2)
        self.renderAreas.append(RenderArea([testpath1,testpath2] ,"intesect angle",result = "ipn:" + str(len(points)) )) 

        testpath1 = QPainterPath()
        #testpath1.moveTo(80.0, 50.0)
        testpath1.arcMoveTo(20.0, 30.0, 60.0, 40.0, 0.0)
        testpath1.arcTo(20.0, 30.0, 60.0, 40.0, 0.0, 360.0)
        testpath2 = QPainterPath()
        testpath2.moveTo(20,80)
        testpath2.lineTo(60,40)
        points = self.intersectPathPoints(testpath1, testpath2)
        self.renderAreas.append(RenderArea([testpath1,testpath2] ,"intesect slice",result = "ipn:" + str(len(points)) )) 


        path = QPainterPath()
        #path.moveTo(5, 5)
        #path.cubicTo(20, 5, 5, 35, 35, 35)
        path.moveTo(10, 30)
        path.cubicTo(60, 30, 20, 70, 70, 70)
        timesFont = QFont("Times", 10)
        timesFont.setStyleStrategy(QFont.ForceOutline)
        path.addText(55, 50, timesFont, self.tr("Qt"))
        self.renderAreas.append(RenderArea([path] ,"cubicTo",result = "" ) )

        path = QPainterPath()
        #path.moveTo(5, 5)
        #path.cubicTo(20, 5, 5, 35, 35, 35)
        #path.moveTo(10, 30)
        path.moveTo(10, 30)
        path.cubicTo(60, 30, 20, 70, 70, 70)
        timesFont = QFont("Times", 10)
        timesFont.setStyleStrategy(QFont.ForceOutline)
        path.addText(55, 50, timesFont, self.tr("Qt"))
        self.renderAreas.append(RenderArea([path] ,"cubicTo rotate 90",rotate =15 , result = "" ) )

        path = QPainterPath()
        path.moveTo(30,30);
        path.quadTo(30,80,60,60);
        point = path.pointAtPercent(0.7)
        cr = QRectF(point-QPointF(2,2)  , QSizeF(4,4))
        testpath3 = QPainterPath()   # center point
        testpath3.arcMoveTo(cr, 0.0)
        testpath3.arcTo(cr, 0.0, 360.0)
        self.renderAreas.append(RenderArea([path, testpath3] ,"quadTo", result = "" ) )


        points = [
            QPoint(10,40),
            QPoint(10,80),
            QPoint(80,40),
            QPoint(80,80)
            ]
        poly = QPolygon(points)
        self.renderAreas.append(RenderArea([poly] ,"draw polygon", result = "" ) )

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
        
        cloumn = 5
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
        intersection_points = []
        if not path1.intersects(path2):
            print("  not  intersects")
            return intersection_points
        c_polygon = path1.toFillPolygon()
        polygon   = path2.toFillPolygon()
        for i in range(0, c_polygon.size() - 2):
            c_polyline = QLineF(c_polygon[i], c_polygon[i + 1])
            for j in range(0, polygon.size() - 2):
                line = QLineF(polygon[j], polygon[j + 1])
                _type , _point =  c_polyline.intersects(line)
                if _type  == QLineF.BoundedIntersection:
                    intersection_points.append(_point)
                elif _type  == QLineF.UnboundedIntersection:
                    pass
                elif _type  == QLineF.NoIntersection:
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

    def __init__(self, elements, name, parent=None, rotate=None, clippath=None, result=None):
        super().__init__(parent)

        #self.paths = paths
        self.elements = elements
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
        self.rotate = rotate
        self.clippath = clippath

    def minimumSizeHint(self):
        
        return QSize(50, 50)

    def sizeHint(self):

        return QSize(100, 100)

    def setFillRule(self, rule):

        for element in self.elements:
           if type(element) == QPainterPath:
             element.setFillRule(rule)
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
        if self.clippath:
            painter.setClipPath(self.clippath)

        #painter.translate(50.0, 50.0)
        #painter.translate(-50.0, -50.0)
        if self.rotate :
           painter.rotate(self.rotate)
        else:
           painter.rotate(-self.rotationAngle)
        painter.translate(50.0, 50.0)
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

        for element in self.elements:
            if type(element) == QPolygon:
                print("drawPolygon")
                painter.drawPolygon(element)
            elif type(element) == QPainterPath:
                painter.drawPath(element)

        pen = painter.pen()
        pen.setColor(QColor("blue"))
        painter.setPen(pen)
        painter.drawText(QPoint(0,20),self.name)

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
    

    

