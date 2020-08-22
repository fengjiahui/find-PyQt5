import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
"""
控件和系统定制模式

"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = QDirModel()
    tree = QTreeView()

    tree.setWindowTitle('')
    tree.resize(600,400)
    tree.show()
    sys.exit(app.exec_())