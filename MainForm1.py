import sys
from PyQt5.QtWidgets import QApplication, QMessageBox

def show_message_box():
    app = QApplication(sys.argv)

    # Create a message box
    msg_box = QMessageBox()
    msg_box.setWindowTitle("پیغام")
    msg_box.setText("این یک پیغام است.")
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setStandardButtons(QMessageBox.Ok)

    # Show the message box
    msg_box.exec_()

if __name__ == "__main__":
    show_message_box()
    greeting = "     Hello!  "

    print(greeting.strip(), "How are you?")