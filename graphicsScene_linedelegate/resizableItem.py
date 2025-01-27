import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor, QBrush
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsItem


class ResizableRectItem(QGraphicsRectItem):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setPen(QPen(Qt.black))
        self.setBrush(QBrush(Qt.gray))
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

        self.handleSize = 8
        self.handles = {}
        self.directions = ['topLeft', 'topRight', 'bottomLeft', 'bottomRight']
        self.createHandles()

    def createHandles(self):
        rect = self.rect()
        pen = QPen(QColor(0, 0, 0))
        for direction in self.directions:
            handle = QGraphicsRectItem(-self.handleSize/2, -self.handleSize/2, self.handleSize, self.handleSize, self)
            handle.setPen(pen)
            handle.setFlags(QGraphicsItem.ItemIsMovable)
            handle.setVisible(False)
            # Use getattr to replace this calls like this: rect.upperLeft()
            handle.setPos(getattr(rect, direction)())
            self.handles[direction] = handle

    def itemChange(self, change, value):
        # Intercept selection event to change visibility of handles
        if change == QGraphicsItem.GraphicsItemChange.ItemSelectedChange:
            for handle in self.handles.values():
                handle.setVisible(bool(value))
        # Pass to original method to handle all other changes
        return super().itemChange(change, value)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(500, 500, 500, 500)
        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        rectItem = ResizableRectItem(100, 100, 200, 200)
        self.scene.addItem(rectItem)

        self.setCentralWidget(self.view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
