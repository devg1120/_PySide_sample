


from PySide6.QtWidgets import (QApplication, QWidget, QLabel,
                               QComboBox, QSpinBox, QGridLayout, QHBoxLayout,QVBoxLayout, QPushButton, QFontDialog,
                               QSizePolicy)
from PySide6.QtGui import QPainterPath, QLinearGradient, QColor,QPen, QFont, QPalette, QPainter
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

        r = QRectF(20.0, 30.0, 60.0, 40.0)
        piePath = QPainterPath()
        piePath.moveTo(50.0, 50.0)
        piePath.arcTo(r, 60.0, 240.0)
        piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 40 arc 1",result = ""  )) 

        piePath = QPainterPath()
        piePath.arcMoveTo(r,  60.0)
        piePath.arcTo(r, 60.0, 240.0)
        #piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 40 arc 2",result = ""  )) 

        piePath = QPainterPath()
        piePath.moveTo(50.0, 50.0)
        piePath.arcTo(r, 45.0, 270.0)
        piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 40 arc 3",result = ""  )) 

        piePath = QPainterPath()
        piePath.arcMoveTo(r,  45.0)
        piePath.arcTo(r, 45.0, 270.0)
        #piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 40 arc 4",result = ""  )) 

        #################################################################
        r = QRectF(20.0, 30.0, 60.0, 60.0)

        piePath = QPainterPath()
        piePath.moveTo(50.0, 60.0)
        piePath.arcTo(r, 60.0, 240.0)
        piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 60 arc 1",result = ""  )) 

        piePath = QPainterPath()
        piePath.arcMoveTo(r,  60.0)
        piePath.arcTo(r, 60.0, 240.0)
        #piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 60 arc 2",result = ""  )) 

        piePath = QPainterPath()
        piePath.moveTo(50.0, 60.0)
        piePath.arcTo(r, 45.0, 270.0)
        piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 60 arc 3",result = ""  )) 

        piePath = QPainterPath()
        piePath.arcMoveTo(r,  45.0)
        piePath.arcTo(r, 45.0, 270.0)
        #piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 60 arc 4",result = ""  )) 

        #################################################################
        r = QRectF(20.0, 30.0, 60.0, 80.0)

        piePath = QPainterPath()
        piePath.moveTo(50.0, 70.0)
        piePath.arcTo(r, 60.0, 240.0)
        piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 80 arc 1",result = ""  )) 

        piePath = QPainterPath()
        piePath.arcMoveTo(r,  60.0)
        piePath.arcTo(r, 60.0, 240.0)
        #piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 80 arc 2",result = ""  )) 

        piePath = QPainterPath()
        piePath.moveTo(50.0, 70.0)
        piePath.arcTo(r, 45.0, 270.0)
        piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 80 arc 3",result = ""  )) 

        piePath = QPainterPath()
        piePath.arcMoveTo(r,  45.0)
        piePath.arcTo(r, 45.0, 270.0)
        #piePath.closeSubpath()

        self.renderAreas.append(RenderArea([piePath] ,"60 x 80 arc 4",result = ""  )) 

        self.renderAreas.append(RenderArea([] ,"BLANK")) 
        self.renderAreas.append(RenderArea([] ,"BLANK")) 
        self.renderAreas.append(RenderArea([] ,"BLANK")) 
        self.renderAreas.append(RenderArea([] ,"BLANK")) 





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
        
        cloumn = 4
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
        painter.scale(self.width()/150.0, self.height()/150.0)
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
    

    

