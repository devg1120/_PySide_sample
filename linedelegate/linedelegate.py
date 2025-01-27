from __future__ import annotations

from PySide6.QtWidgets import QStyledItemDelegate, QStyle
from PySide6.QtCore import Qt, QEvent, QPoint, QPointF, QRectF, QModelIndex, QLine, QLineF
from PySide6.QtCore import  qFuzzyCompare, qFuzzyIsNull
from PySide6.QtGui import QPen, QStandardItemModel

## ORIGIN
## https://github.com/sendevent/linedelegate
##

class Line():
    DataRole = Qt.UserRole + 1

    def __init__(self, from_, to_):
        self._from = from_
        self._to = to_

    def isEmpty(self):
         return qFuzzyCompare(self._from, self._to)

    def isFull(self): 
        return (not self.isEmpty()) and qFuzzyIsNull(self._from) and qFuzzyCompare(1., self._to)

    def toQLine(self, viewport):
        center = viewport.center()
        p1 = QPointF(viewport.left(), center.y())
        p2 = QPointF(viewport.right(), center.y())
        if not self.isFull():
            p1.setX( viewport.left() + viewport.width() * self._from)
            p2.setX( viewport.left() + viewport.width() * self._to)
        return  QLineF(p1, p2) 

    def toQLineFull_(self, viewport):
        center = viewport.center()
        p1 = QPointF(viewport.left() + 4, center.y())
        p2 = QPointF(viewport.right() - 3 , center.y())
        return  QLineF(p1, p2) 

    def toQLineFull(self, viewport, y):
        p1 = QPointF(viewport.left() + 4, y)
        p2 = QPointF(viewport.right() - 3 , y)
        return  QLineF(p1, p2) 

    @classmethod
    def fromQLine(self, line, viewport):   # QLine  QRect
        w  = viewport.width()
        return Line( line.x1() / w, line.x2() / w )

class LineDelegate(QStyledItemDelegate):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.table = parent
        self.lineWidth = 8.0
        self.m_startIndex = QModelIndex();
        self.m_startPoint = { -1, -1 };
        #self.m_linePen =  QPen(Qt.darkGreen)
        self.m_linePen =  QPen(Qt.green)
        self.m_linePen.setWidth(self.lineWidth)

        self.m_gridPen =  QPen(Qt.gray)
        self.m_gridPen.setWidth(1.0)

        self.current_hover = [0, 0]
        #self.table.setMouseTracking(True)
        self.table.cellEntered.connect(self.on_table_cell_entered)
        self.table.currentCellChanged.connect(self.on_table_cell_changed)

    def on_table_cell_entered(self, row, column):
        print("cell enter:", row,column)
        self.current_hover = [row, column]

    def on_table_cell_changed(self, c_row, c_column, p_row, p_column):
        print("cell change:", c_row, c_column, p_row, p_column)

    def toGrid_v(self, viewport):
       # center = viewport.center()
        #p1 = QPointF(viewport.right() , center.y() -5)
        #p2 = QPointF(viewport.right() , center.y() +5)
        p1 = QPointF(viewport.right() , viewport.top())
        p2 = QPointF(viewport.right() , viewport.bottom())
        return  QLineF(p1, p2) 

    def toGrid_h(self, viewport):
       # center = viewport.center()
        #p1 = QPointF(viewport.right() , center.y() -5)
        #p2 = QPointF(viewport.right() , center.y() +5)
        p1 = QPointF(viewport.left() , viewport.bottom())
        p2 = QPointF(viewport.right() , viewport.bottom())
        return  QLineF(p1, p2) 

    def paint(self, painter, option, index):
        QStyledItemDelegate.paint(self, painter, option, index)
        painter.save()
        painter.setPen(self.m_gridPen)
        lineF = self.toGrid_v(option.rect)
        painter.drawLine(lineF)
        lineF = self.toGrid_h(option.rect)
        painter.drawLine(lineF)
        painter.restore()


        line = index.data(Line.DataRole)
        if line is None:
            #print("NonType")
            return
        elif not type(line) is Line:
            #print("no Line")
            return
        #print("Line")

        #lineF = line.toQLine(option.rect)

        #y = option.rect.center().y()
        y = option.rect.bottom() - (self.lineWidth)
        #y = option.rect.top()  +8
        lineF = line.toQLineFull(option.rect, y)



        painter.save()

        painter.setPen(self.m_linePen)
        painter.drawLine(lineF)

        painter.restore()


    ### https://doc.qt.io/qtforpython-6/PySide6/QtCore/QEvent.html#PySide6.QtCore.QEvent.Type
    """
    def event(self, event):
        if event.type() == QEvent.Enter:
            print("Enter")
        elif event.type() == QEvent.Leave:
            print("Leave")
        return super().event(event)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            print("Enter")
        elif event.type() == QEvent.Leave:
            print("Leave")
        return super().eventFilter(obj, event)
    """

    def editorEvent(self, event, model, option, index):
        #print("editorEvent", event.type())
        if event.type() == QEvent.MouseButtonPress:
            print("Press")
            self.handleMousePress(event, model, option, index)
        elif event.type() == QEvent.MouseMove:
            #print("Move")
            self.handleMouseMove(event, model, option, index)
        elif event.type() == QEvent.MouseButtonRelease:
            print("Release")
            self.handleMouseRelease(event, model, option, index)
        elif event.type() == QEvent.Enter:
            print("Enter2")
        elif event.type() == QEvent.Leave:
            print("Leave2")
        return super().editorEvent(event, model, option, index)


    def handleMousePress(self, event, model, option, index):
        if index.isValid():
           self.m_startIndex = index
           self.m_startPoint = QPoint( event.position().x() - option.rect.x(), option.rect.center().y() )
    
    def handleMouseMove(self, event, model, option, index):
        endPoint = QPoint(event.position().x() - option.rect.x(), option.rect.center().y())
        if (self.m_startIndex != index):
            self.m_startIndex = index
            self.m_startPoint = endPoint
        
        line = Line.fromQLine( QLine(self.m_startPoint, endPoint) , option.rect);
        model.setData(index, line, Line.DataRole);

    def handleMouseRelease(self, event, model, option, index):
        self.m_startIndex = QModelIndex();
        self.m_startPoint = { -1, -1 };



if __name__ == "__main__":
    """ Run the application. """
    from PySide6.QtWidgets import (QApplication, QTableWidget, QTableView, QTableWidgetItem,
                                   QAbstractItemView)
    import sys

    app = QApplication(sys.argv)

    # Create and populate the tableWidget
    table_widget = QTableWidget(4, 4)
    table_widget.setShowGrid(False)
    #table_widget.setGridStyle(Qt.DotLine)
    #table_widget.setGridStyle(Qt.SolidLine)

    table_widget.setItemDelegate(LineDelegate(table_widget))
    table_widget.setEditTriggers(QAbstractItemView.DoubleClicked
                                 | QAbstractItemView.SelectedClicked)
    table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
   
    table_widget.setHorizontalHeaderLabels(["Title", "Genre", "Artist", "Rating"])
    data = [["Mass in B-Minor", "Baroque", "J.S. Bach", 5],
            ["Three More Foxes", "Jazz", "Maynard Ferguson", 4],
            ["Sex Bomb", "Pop", "Tom Jones", 3],
            ["Barbie Girl", "Pop", "Aqua", 5]]

    for r in range(len(data)):
        table_widget.setItem(r, 0, QTableWidgetItem(data[r][0]))
        table_widget.setItem(r, 1, QTableWidgetItem(data[r][1]))
        table_widget.setItem(r, 2, QTableWidgetItem(data[r][2]))
        #item = QTableWidgetItem()
        #item.setData(0, StarRating(data[r][3]).star_count)
        #table_widget.setItem(r, 3, item)

    
    """
    rowsCount = 100 
    columnsCount = 10 

    for (int row = 0; row < rowsCount; ++row) {
        m_model->insertRow(row);
        for (int column = 0; column < columnsCount; ++column) {
            if (m_model->columnCount() < columnsCount)
                m_model->insertColumn(column);

            const QModelIndex &id = m_model->index(row, column);
            m_model->setData(id, QString("[%1x%2]").arg(QString::number(row + 1), QString::number(column + 1)));
        }
    }
    """

    """
    rowsCount = 100 
    columnsCount = 10 
    model = QStandardItemModel()
    for row in range(rowsCount):
         model.insertRow(row)
         for column in range(columnsCount):
             if model.columnCount() < columnsCount:
                model.insertColumn(column)
             id = model.index(row, column)
             model.setData(id, f"[{str(row + 1)}x{str(column + 1)}]")

    table_widget.setModel(model)
    """

    table_widget.resizeColumnsToContents()
    table_widget.resize(500, 300)


    table_widget.show()

    sys.exit(app.exec())
