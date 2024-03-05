import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem

class TreeExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tree Example")
        self.setGeometry(100, 100, 400, 400)

        self.init_ui()

    def init_ui(self):
        # Create a tree widget
        tree_widget = QTreeWidget(self)
        tree_widget.setHeaderLabels(["Title", "Description"]) # Set headers

        # Add root items
        root1 = QTreeWidgetItem(tree_widget)
        root1.setText(0, "Root 1")
        root1.setText(1, "Description of Root 1")

        root2 = QTreeWidgetItem(tree_widget)
        root2.setText(0, "Root 2")
        root2.setText(1, "Description of Root 2")

        # Add child items to root1
        child1 = QTreeWidgetItem(root1)
        child1.setText(0, "Child 1 of Root 1")
        child1.setText(1, "Description of Child 1")

        child2 = QTreeWidgetItem(root1)
        child2.setText(0, "Child 2 of Root 1")
        child2.setText(1, "Description of Child 2")

        # Add child items to root2
        child3 = QTreeWidgetItem(root2)
        child3.setText(0, "Child 1 of Root 2")
        child3.setText(1, "Description of Child 1")

        child4 = QTreeWidgetItem(root2)
        child4.setText(0, "Child 2 of Root 2")
        child4.setText(1, "Description of Child 2")

        # Expand all items
        tree_widget.expandAll()

        self.setCentralWidget(tree_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tree_example = TreeExample()
    tree_example.show()
    sys.exit(app.exec_())
