import json
import os

import paramiko
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTreeWidgetItem
from elasticsearch import Elasticsearch


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1171, 323)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 200))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 1000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 861, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 31))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.txtSourceIP = QtWidgets.QLineEdit(self.groupBox)
        self.txtSourceIP.setGeometry(QtCore.QRect(120, 30, 121, 31))
        self.txtSourceIP.setObjectName("txtSourceIP")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(290, 30, 51, 31))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.txtSourcePort = QtWidgets.QLineEdit(self.groupBox)
        self.txtSourcePort.setGeometry(QtCore.QRect(360, 30, 61, 31))
        self.txtSourcePort.setObjectName("txtSourcePort")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 101, 31))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.txtSourceUsername = QtWidgets.QLineEdit(self.groupBox)
        self.txtSourceUsername.setGeometry(QtCore.QRect(120, 80, 121, 31))
        self.txtSourceUsername.setObjectName("txtSourceUsername")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(270, 80, 71, 31))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.txtSourcePassword = QtWidgets.QLineEdit(self.groupBox)
        self.txtSourcePassword.setGeometry(QtCore.QRect(360, 80, 141, 31))
        self.txtSourcePassword.setObjectName("txtSourcePassword")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 101, 31))
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.txtPathRepo = QtWidgets.QLineEdit(self.groupBox)
        self.txtPathRepo.setGeometry(QtCore.QRect(120, 180, 381, 31))
        self.txtPathRepo.setObjectName("txtPathRepo")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 130, 101, 31))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.txtRepository = QtWidgets.QLineEdit(self.groupBox)
        self.txtRepository.setGeometry(QtCore.QRect(120, 130, 121, 31))
        self.txtRepository.setObjectName("txtRepository")
        self.txtSnapshot = QtWidgets.QLineEdit(self.groupBox)
        self.txtSnapshot.setGeometry(QtCore.QRect(360, 130, 141, 31))
        self.txtSnapshot.setObjectName("txtSnapshot")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(270, 130, 71, 31))
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 230, 101, 31))
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.txtPathVolume = QtWidgets.QLineEdit(self.groupBox)
        self.txtPathVolume.setGeometry(QtCore.QRect(120, 230, 381, 31))
        self.txtPathVolume.setObjectName("txtPathVolume")
        self.txtSSHAddress = QtWidgets.QLineEdit(self.groupBox)
        self.txtSSHAddress.setGeometry(QtCore.QRect(640, 30, 201, 31))
        self.txtSSHAddress.setObjectName("txtSSHAddress")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(540, 30, 91, 31))
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(530, 80, 101, 31))
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.txtSSHUsername = QtWidgets.QLineEdit(self.groupBox)
        self.txtSSHUsername.setGeometry(QtCore.QRect(640, 80, 201, 31))
        self.txtSSHUsername.setObjectName("txtSSHUsername")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(530, 130, 101, 31))
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.txtSSHPassword = QtWidgets.QLineEdit(self.groupBox)
        self.txtSSHPassword.setGeometry(QtCore.QRect(640, 130, 201, 31))
        self.txtSSHPassword.setObjectName("txtSSHPassword")
        self.btnBackUp = QtWidgets.QPushButton(self.groupBox)
        self.btnBackUp.setGeometry(QtCore.QRect(710, 210, 131, 51))
        self.btnBackUp.setObjectName("btnBackUp")
        self.btnClose = QtWidgets.QPushButton(self.groupBox)
        self.btnClose.setGeometry(QtCore.QRect(540, 210, 131, 51))
        self.btnClose.setObjectName("btnClose")
        self.btnTestConnection = QtWidgets.QPushButton(self.groupBox)
        self.btnTestConnection.setGeometry(QtCore.QRect(430, 30, 71, 31))
        self.btnTestConnection.setObjectName("btnTestConnection")
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(880, 10, 271, 291))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.treHistory = QtWidgets.QTreeWidget(self.groupBox_2)
        self.treHistory.setGeometry(QtCore.QRect(10, 30, 251, 241))
        self.treHistory.setObjectName("treeWidget")
        self.horizontalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtSourceIP, self.txtSourcePort)
        MainWindow.setTabOrder(self.txtSourcePort, self.txtSourceUsername)
        MainWindow.setTabOrder(self.txtSourceUsername, self.txtSourcePassword)
        MainWindow.setTabOrder(self.txtSourcePassword, self.txtRepository)
        MainWindow.setTabOrder(self.txtRepository, self.txtSnapshot)
        MainWindow.setTabOrder(self.txtSnapshot, self.txtPathRepo)
        MainWindow.setTabOrder(self.txtPathRepo, self.btnBackUp)
        MainWindow.setTabOrder(self.btnBackUp, self.btnClose)

        self.btnBackUp.clicked.connect(self.backup)
        self.btnClose.clicked.connect(self.close)
        self.btnTestConnection.clicked.connect(self.testConnection)

        self.txtPathRepo.setText('/usr/share/elasticsearch/backup')
        self.txtPathVolume.setText('/var/lib/docker/volumes/elastic/_data/backup/')
        self.txtSnapshot.setText('sna-m')
        self.txtRepository.setText('rep-m')

        self.txtSourceIP.setText('192.168.83.224')
        self.txtSourcePort.setText('9200')
        self.txtSourceUsername.setText('elastic')
        self.txtSourcePassword.setText('Douran@123')

        self.txtSSHAddress.setText('192.168.83.224')
        self.txtSSHUsername.setText('root')
        self.txtSSHPassword.setText('123')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Backup And Restore Elastic Search"))
        self.groupBox.setTitle(_translate("MainWindow", "Source "))
        self.label.setText(_translate("MainWindow", "Address :"))
        self.label_2.setText(_translate("MainWindow", "Port :"))
        self.label_3.setText(_translate("MainWindow", "Username :"))
        self.label_4.setText(_translate("MainWindow", "Password :"))
        self.label_9.setText(_translate("MainWindow", "Path Repo :"))
        self.label_10.setText(_translate("MainWindow", "Repository :"))
        self.label_11.setText(_translate("MainWindow", "Snapshot :"))
        self.label_12.setText(_translate("MainWindow", "Path Volume :"))
        self.label_13.setText(_translate("MainWindow", "SSH Address :"))
        self.label_14.setText(_translate("MainWindow", "SSH Username :"))
        self.label_15.setText(_translate("MainWindow", "SSH Password :"))
        self.btnBackUp.setText(_translate("MainWindow", "Backup"))
        self.btnClose.setText(_translate("MainWindow", "Close"))
        self.btnTestConnection.setText(_translate("MainWindow", "Test Conn"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Repository And Snapshot"))
        self.treHistory.headerItem().setText(0, _translate("MainWindow", "Title"))
        self.treHistory.headerItem().setText(1, _translate("MainWindow", "Description"))

    def testConnection(self):
        data = {}
        data.update({'IP': self.txtSourceIP.text()})
        data.update({'Port': self.txtSourcePort.text()})
        data.update({'Username': self.txtSourceUsername.text()})
        data.update({'Password': self.txtSourcePassword.text()})

        es = Elasticsearch(
            [data.get('IP')],
            http_auth=(data.get('Username'), data.get('Password')),
            scheme="http",
            port=data.get('Port')
        )

        repo = es.snapshot.get_repository(repository='_all')

        for key, value in repo.items():
            root = QTreeWidgetItem(self.treHistory)
            root.setText(0, key)
            root.setText(1, value.get('settings', {}).get('location'))
            snap = es.snapshot.get(repository=key, snapshot='_all')
            snap = snap.get('snapshots')
            for value2 in snap:
                child = QTreeWidgetItem(root)
                child.setText(0, value2.get('snapshot'))
                child.setText(1, str(value2.get('indices')))

    def close(self):
        sys.exit()

    def backup(self):
        data = {}
        data.update({'IP': self.txtSourceIP.text()})
        data.update({'Port': self.txtSourcePort.text()})
        data.update({'Username': self.txtSourceUsername.text()})
        data.update({'Password': self.txtSourcePassword.text()})
        data.update({'Repository': self.txtRepository.text()})
        data.update({'Snapshot': self.txtSnapshot.text()})
        data.update({'Path': self.txtPathRepo.text()})
        data.update({'PathVolume': self.txtPathVolume.text()})
        data.update({'SSHAddress': self.txtSSHAddress.text()})
        data.update({'SSHUsername': self.txtSSHUsername.text()})
        data.update({'SSHPassword': self.txtSSHPassword.text()})

        es = Elasticsearch(
            [data.get('IP')],
            http_auth=(data.get('Username'), data.get('Password')),
            scheme="http",
            port=data.get('Port')
        )

        print('Ping Elastic Source : ', es.ping())

        repo_body = {
            "type": "fs",
            "settings": {
                "location": data.get('Path')
            }
        }
        es.snapshot.create_repository(repository=data.get('Repository'), body=repo_body)

        snapshot_body = {
            "indices": "*,-.*",
            "ignore_unavailable": True,
            "include_global_state": False
        }
        es.snapshot.create(repository=data.get('Repository'), snapshot=data.get('Snapshot'), body=snapshot_body)

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(None, "Save", "", ".tar.gz", options=options)
        file_name_with_extension = os.path.basename(file_name)

        output_filename = file_name_with_extension

        hostname = data.get('SSHAddress')
        username = data.get('SSHUsername')
        password = data.get('SSHPassword')

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)

        volumeMountPoint = data.get('PathVolume')
        zip_command = f"cd {volumeMountPoint} ; tar -czvf {output_filename} *"
        stdin, stdout, stderr = ssh.exec_command(zip_command)

        print("Output:", stdout.read().decode())
        print("Errors:", stderr.read().decode())

        sftp = ssh.open_sftp()
        sftp.get(volumeMountPoint + output_filename, file_name)

        ssh.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyle('Fusion')
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
