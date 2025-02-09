


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

        testpath1 = QPainterPath()
        #testpath1.moveTo(20 + 60 , 30 + 60//2)
        testpath1.arcMoveTo(20, 30, 60.0, 60.0, 0 )
        testpath1.arcTo(20, 30, 60.0, 60.0, 0, 270.0 )
        testpath2 = QPainterPath()
        testpath2.moveTo(40,80)
        testpath2.lineTo(80,30)
        points = self.intersectPathPoints(testpath1, testpath2)
        #print("intersects:",len(points))
        self.renderAreas.append(RenderArea([testpath1,testpath2] ,"intesect angle",result = "ipn:" + str(len(points)) )) 
        
        testpath1 = QPainterPath()
        #testpath1.moveTo(20 + 60//2 , 30)
        testpath1.arcMoveTo(20, 30, 60.0, 60.0, 90)
        testpath1.arcTo(20, 30, 60.0, 60.0, 90, 180)
        testpath2 = QPainterPath()
        testpath2.moveTo(40,80)
        testpath2.lineTo(80,30)
        points = self.intersectPathPoints(testpath1, testpath2)
        self.renderAreas.append(RenderArea([testpath1,testpath2] ,"intesect angle",result = "ipn:" + str(len(points)) )) 
        
        testpath1 = QPainterPath()
        #testpath1.moveTo(20 + 60//2 , 30)
        testpath1.arcMoveTo(20, 30, 60.0, 60.0, 45)
        testpath1.arcTo(20, 30, 60.0, 60.0, 45, 180)
        testpath2 = QPainterPath()
        testpath2.moveTo(40,80)
        testpath2.lineTo(80,30)
        points = self.intersectPathPoints(testpath1, testpath2)
        self.renderAreas.append(RenderArea([testpath1,testpath2] ,"intesect angle",result = "ipn:" + str(len(points)) )) 

        #-------------------------------------------------
        self.renderAreas.append(RenderArea([] ,"BLANK")) 
        #-------------------------------------------------
        #############################################################
        #            x
        #          
        # y          +
        #
        #-------------------------------------------------
        r = QRectF(20.0, 30.0, 60.0, 40.0)
        #r = QRectF(20.0, 30.0, 40.0, 40.0)
        cr = QRectF(r.center()-QPointF(2,2)  , QSizeF(4,4))

        testpath1 = QPainterPath()
        testpath1.arcMoveTo(r, 0.0)
        testpath1.arcTo(r, 0.0, 360.0)
        testpath2 = QPainterPath()
        testpath2.moveTo(40,80)
        testpath2.lineTo(40,10)

        points = self.intersectPathPoints(testpath1, testpath2)
        print("intersects:",len(points))
        print("intersects 0:",points[0])
        print("intersects 1:",points[1])
        center = r.center()
        base   = QPointF(100, 50)
        offset = QLineF(r.center(),base) 
        #angle1 = offset.angleTo(QLineF(r.center(),points[0])) 
        #angle2 = offset.angleTo(QLineF(r.center(),points[1]))  
        points[0].setX(points[0].x() +3)
        points[1].setX(points[1].x() +3)
        angle1 = QLineF(center,points[0]).angle() 
        angle2 = QLineF(center,points[1]).angle() 

        print("angle:", angle1, angle2)

        testpath1 = QPainterPath()
        testpath1.arcMoveTo(r, angle1 )
        testpath1.arcTo(r, angle1, angle2 - angle1 )

        testpath3 = QPainterPath()   # center point
        testpath3.arcMoveTo(cr, 0.0)
        testpath3.arcTo(cr, 0.0, 360.0)

        self.renderAreas.append(RenderArea([testpath1,testpath2, testpath3] ,"intesect angle cut",result = "ipn:" + str(len(points)) )) 

        #-------------------------------------------------
        r = QRectF(20.0, 30.0, 60.0, 40.0)
        cr = QRectF(r.center()-QPointF(2,2)  , QSizeF(4,4))

        testpath1 = QPainterPath()
        testpath1.arcMoveTo(r, 0.0)
        testpath1.arcTo(r, 0.0, 360.0)
        testpath2 = QPainterPath()
        testpath2.moveTo(40,80)
        testpath2.lineTo(40,10)

        points = self.intersectPathPoints(testpath1, testpath2)
        print("intersects:",len(points))
        print("intersects 0:",points[0])
        print("intersects 1:",points[1])
        #center = r.center()
        base   = QPointF(100, 50)
        offset = QLineF(r.center(),base) 
        angle1 = offset.angleTo(QLineF(r.center(),points[0])) 
        angle2 = offset.angleTo(QLineF(r.center(),points[1]))  
        #angle1 = QLineF(center,points[0]).angle() 
        #angle2 = QLineF(center,points[1]).angle() 

        print("angle:", angle1, angle2)

        testpath1 = QPainterPath()
        testpath1.arcMoveTo(r, angle1 )
        testpath1.arcTo(r, angle1, angle2 - angle1 )

        testpath3 = QPainterPath()   # center point
        testpath3.arcMoveTo(cr, 0.0)
        testpath3.arcTo(cr, 0.0, 360.0)

        self.renderAreas.append(RenderArea([testpath1,testpath2, testpath3] ,"intesect angle cut",result = "ipn:" + str(len(points)) )) 

        #-------------------------------------------------

        #-------------------------------------------------
        title = "正方形"
        print(title, "----------------------------")
        r = QRectF(20.0, 30.0, 50.0, 50.0)
        cr = QRectF(r.center()-QPointF(2,2)  , QSizeF(4,4))

        testpath1 = QPainterPath()
        testpath1.arcMoveTo(r, 0.0)
        testpath1.arcTo(r, 0.0, 360.0)
        testpath2 = QPainterPath()
        testpath2.moveTo(40,90)
        testpath2.lineTo(80,30)

        points = self.intersectPathPoints(testpath1, testpath2)
        print("intersects:",len(points))
        print("intersects 0:",points[0])
        print("intersects 1:",points[1])
        center = r.center()
        base   = QPointF(100, 50)
        offset = QLineF(center,base) 
        #angle1 = offset.angleTo(QLineF(center,points[0])) 
        #angle2 = offset.angleTo(QLineF(center,points[1]))  
        #points[0].setX(points[0].x() -6)
        #points[1].setX(points[1].x() )
        angle1 = QLineF(center,points[0]).angle()
        angle2 = QLineF(center,points[1]).angle()

        print("angle:", angle1, angle2)

        testpath1 = QPainterPath()
        testpath1.arcMoveTo(r, angle1 )
        testpath1.arcTo(r, angle1, angle2 - angle1)

        testpath3 = QPainterPath()   # center point
        testpath3.arcMoveTo(cr, 0.0)
        testpath3.arcTo(cr, 0.0, 360.0)

        self.renderAreas.append(RenderArea([testpath1,testpath2, testpath3] ,title,result = "ipn:" + str(len(points)) )) 

        #-------------------------------------------------
        title = "長方形"
        print(title, "----------------------------")
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

        line_angle = QLineF(L1,L2).angle() 
        print("**",QLineF(L1, L2).angleTo(QLineF(center,points[0])))
        print("**",QLineF(L1, L2).angleTo(QLineF(center,points[1])))
        angle1 = QLineF(center,points[0]).angle() + 12
        angle2 = QLineF(center,points[1]).angle() + 12

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

        #-------------------------------------------------
        title = "長方形2"
        print(title, "----------------------------")
        r = QRectF(20.0, 30.0, 60.0, 40.0)
        cr = QRectF(r.center()-QPointF(2,2)  , QSizeF(4,4))
        L1 = QPointF(30,80)
        L2 = QPointF(60,20)

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

        line_angle = QLineF(L1, L2).angle() 
        print("**",QLineF(L1, L2).angleTo(QLineF(center,points[0])))
        print("**",QLineF(L1, L2).angleTo(QLineF(center,points[1])))
        angle1 = QLineF(center,points[0]).angle() + 4
        angle2 = QLineF(center,points[1]).angle() + 8

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


        #-------------------------------------------------
        title = "長方形3"
        print(title, "----------------------------")
        r = QRectF(20.0, 30.0, 60.0, 40.0)
        cr = QRectF(r.center()-QPointF(2,2)  , QSizeF(4,4))
        L1 = QPointF(30,20)
        L2 = QPointF(60,80)

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

        line_angle = QLineF(L1, L2).angle() 
        print("**",QLineF(L1, L2).angleTo(QLineF(center,points[0])))
        print("**",QLineF(L1, L2).angleTo(QLineF(center,points[1])))
        angle1 = QLineF(center,points[0]).angle() + 4
        angle2 = QLineF(center,points[1]).angle() + 8

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


        #-------------------------------------------------
        title = "長方形4"
        print(title, "----------------------------")

        r = QRectF(20.0, 30.0, 60.0, 40.0 )
        cr = QRectF(r.center()-QPointF(2,2)  , QSizeF(4,4))

        testpath1 = QPainterPath()
        testpath1.arcMoveTo(r, 0.0)
        testpath1.arcTo(r, 0.0, 360.0)
        testpath2 = QPainterPath()
        testpath2.moveTo(20,80)
        #testpath2.lineTo(80,30)
        testpath2.lineTo(90,30)

        points = self.intersectPathPoints(testpath1, testpath2)
        print("intersects:",len(points))
        print("intersects 0:",points[0])
        print("intersects 1:",points[1])
        center = r.center()
        angle1 = QLineF(center,points[0]).angle() 
        angle1 = angle1 * r.width()/r.height()
        angle2 = QLineF(center,points[1]).angle()
        angle2 = angle2 * (1-r.width()/r.height())

        print("angle:", angle1, angle2)

        testpath1 = QPainterPath()
        #testpath1.arcMoveTo(20.0, 30.0, 60.0, 40.0, angle1 )
        #testpath1.arcTo(20.0, 30.0, 60.0, 40.0, angle1, angle2 - angle1 )
        testpath1.arcMoveTo(r, angle1 )
        testpath1.arcTo(r, angle1, angle2 - angle1 )

        testpath3 = QPainterPath()   # center point
        testpath3.arcMoveTo(cr, 0.0)
        testpath3.arcTo(cr, 0.0, 360.0)

        self.renderAreas.append(RenderArea([testpath1,testpath2, testpath3] ,title,result = "ipn:" + str(len(points)) )) 





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
        
        return QSize(50, 50)

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
    

    

