from PyQt6.QtGui import QStandardItemModel
from PyQt6.QtCore import Qt

class NoEditableModel(QStandardItemModel):
    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled