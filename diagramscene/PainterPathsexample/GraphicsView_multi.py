import sys
import os
import os.path

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader


def clamp(value, minValue, maxValue):
    return max(minValue, min(value, maxValue))


class UISample(QtWidgets.QDialog):

    def __init__(self, parent=None):

        super(UISample, self).__init__((parent))

        self.view = NodeView()
        layout  = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.view)

        self.scene = NodeScene()
        self.view.setScene(self.scene)

        item = self.scene.addEllipse(150, 150, 200, 100)
        item.setBrush(QtGui.QBrush(QtGui.QColor('pink')))

class UIMultiSample(QtWidgets.QDialog):

    def __init__(self, parent=None):

        super(UIMultiSample, self).__init__((parent))

        self.view1 = NodeView()
        self.view2 = NodeView()
        layout  = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.view1)
        layout.addWidget(self.view2)

        self.scene = NodeScene()
        self.view1.setScene(self.scene)
        self.view2.setScene(self.scene)

        item = self.scene.addEllipse(150, 150, 200, 100)
        item.setBrush(QtGui.QBrush(QtGui.QColor('pink')))

class NodeView(QtWidgets.QGraphicsView):

    def __init__(self, parent=None):
        super(NodeView, self).__init__(parent)

        self.zoom = 1
        self.setStyleSheet("NodeView { background-color: lightblue;}")

    def wheelEvent(self, e):
        #delta = e.delta()
        #adjust = (delta / 120) * 0.1
        #self.set_zoom(adjust)

        delta = e.angleDelta()
        adjust = (delta.y() / 120) * 0.1
        self.set_zoom(adjust)


    def set_zoom(self, value):

        ZOOM_MIN = 0.1
        ZOOM_MAX = 2
        # 今のズーム率 指定外にはならないようにする
        self.zoom = clamp(self.zoom + value, ZOOM_MIN, ZOOM_MAX)
        # リセットしてから
        self.resetTransform()
        # Transformを入れる
        self.scale(self.zoom, self.zoom)


class NodeScene(QtWidgets.QGraphicsScene):

    sel_item = None

    def __init__(self, parent=None):
        super(NodeScene, self).__init__(parent)

    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.sel_item = self.itemAt(e.scenePos(), QtGui.QTransform())
            self.mouse_pos = e.scenePos()

    def mouseMoveEvent(self, e):
        if self.sel_item is not None:
            cur = e.scenePos()
            val = cur - self.mouse_pos
            self.sel_item.moveBy(val.x(), val.y())
            self.mouse_pos = cur

    def viewer(self):
        return self.views()[0] if self.views() else None

    def mouseReleaseEvent(self, e):
        self.mouse_pos = None
        self.sel_item = None


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #window = UISample()
    window = UIMultiSample()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())

