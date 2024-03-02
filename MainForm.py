# -*- coding: utf-8 -*-
import datetime
import json
import os
import tarfile
import zipfile

import paramiko
# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from elasticsearch import Elasticsearch


class Ui_MainWindow(object):
    def __init__(self):
        self.repository_name = ''
        self.snapshot_name = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(542, 503)
        MainWindow.setMinimumSize(QtCore.QSize(542, 464))
        MainWindow.setMaximumSize(QtCore.QSize(542, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 231))
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
        self.label.setGeometry(QtCore.QRect(30, 30, 51, 31))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.txtSourceIP = QtWidgets.QLineEdit(self.groupBox)
        self.txtSourceIP.setGeometry(QtCore.QRect(100, 30, 251, 31))
        self.txtSourceIP.setObjectName("txtSourceIP")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(360, 30, 51, 31))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.txtSourcePort = QtWidgets.QLineEdit(self.groupBox)
        self.txtSourcePort.setGeometry(QtCore.QRect(430, 30, 71, 31))
        self.txtSourcePort.setObjectName("txtSourcePort")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 71, 31))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.txtSourceUsername = QtWidgets.QLineEdit(self.groupBox)
        self.txtSourceUsername.setGeometry(QtCore.QRect(100, 80, 141, 31))
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
        self.label_9.setGeometry(QtCore.QRect(10, 180, 71, 31))
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.txtPath = QtWidgets.QLineEdit(self.groupBox)
        self.txtPath.setGeometry(QtCore.QRect(100, 180, 401, 31))
        self.txtPath.setObjectName("txtPath")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 130, 71, 31))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.txtRepository = QtWidgets.QLineEdit(self.groupBox)
        self.txtRepository.setGeometry(QtCore.QRect(100, 130, 141, 31))
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
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 260, 521, 171))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 51, 31))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.txtDestinationIP = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtDestinationIP.setGeometry(QtCore.QRect(100, 30, 251, 31))
        self.txtDestinationIP.setObjectName("txtDestinationIP")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(360, 30, 51, 31))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.txtDestinationPort = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtDestinationPort.setGeometry(QtCore.QRect(430, 30, 71, 31))
        self.txtDestinationPort.setObjectName("txtDestinationPort")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 71, 31))
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.txtDestinationUsername = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtDestinationUsername.setGeometry(QtCore.QRect(100, 80, 141, 31))
        self.txtDestinationUsername.setObjectName("txtDestinationUsername")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(270, 80, 71, 31))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.txtDestinationPassword = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtDestinationPassword.setGeometry(QtCore.QRect(360, 80, 141, 31))
        self.txtDestinationPassword.setObjectName("txtDestinationPassword")
        self.chk = QtWidgets.QCheckBox(self.groupBox_2)
        self.chk.setGeometry(QtCore.QRect(100, 130, 401, 17))
        self.chk.setObjectName("chk")
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.btnBackUp = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackUp.setGeometry(QtCore.QRect(394, 440, 131, 51))
        self.btnBackUp.setObjectName("btnBackUp")
        self.btnRestore = QtWidgets.QPushButton(self.centralwidget)
        self.btnRestore.setGeometry(QtCore.QRect(240, 440, 131, 51))
        self.btnRestore.setObjectName("btnRestore")
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(10, 440, 131, 51))
        self.btnClose.setObjectName("btnClose")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtSourceIP, self.txtSourcePort)
        MainWindow.setTabOrder(self.txtSourcePort, self.txtSourceUsername)
        MainWindow.setTabOrder(self.txtSourceUsername, self.txtSourcePassword)
        MainWindow.setTabOrder(self.txtSourcePassword, self.txtRepository)
        MainWindow.setTabOrder(self.txtRepository, self.txtSnapshot)
        MainWindow.setTabOrder(self.txtSnapshot, self.txtPath)
        MainWindow.setTabOrder(self.txtPath, self.txtDestinationIP)
        MainWindow.setTabOrder(self.txtDestinationIP, self.txtDestinationPort)
        MainWindow.setTabOrder(self.txtDestinationPort, self.txtDestinationUsername)
        MainWindow.setTabOrder(self.txtDestinationUsername, self.txtDestinationPassword)
        MainWindow.setTabOrder(self.txtDestinationPassword, self.chk)
        MainWindow.setTabOrder(self.chk, self.btnBackUp)
        MainWindow.setTabOrder(self.btnBackUp, self.btnRestore)
        MainWindow.setTabOrder(self.btnRestore, self.btnClose)

        self.btnBackUp.clicked.connect(self.backup)
        self.btnRestore.clicked.connect(self.restore)
        self.btnClose.clicked.connect(self.close)

        # self.txtPath.setText('/usr/share/elasticsearch/backup/')
        self.txtPath.setText('backup/')
        self.txtSnapshot.setText('sna-m')
        self.txtRepository.setText('rep-m')

        self.txtSourceIP.setText('192.168.83.224')
        self.txtSourcePort.setText('9200')
        self.txtSourceUsername.setText('elastic')
        self.txtSourcePassword.setText('Douran@123')

        self.txtDestinationIP.setText('192.168.83.224')
        self.txtDestinationPort.setText('9300')
        self.txtDestinationUsername.setText('elastic')
        self.txtDestinationPassword.setText('Douran@123')




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Backup And Restore Elastic Search"))
        self.groupBox.setTitle(_translate("MainWindow", "Source "))
        self.label.setText(_translate("MainWindow", "IP :"))
        self.label_2.setText(_translate("MainWindow", "Port :"))
        self.label_3.setText(_translate("MainWindow", "Username :"))
        self.label_4.setText(_translate("MainWindow", "Password :"))
        self.label_9.setText(_translate("MainWindow", "Path :"))
        self.label_10.setText(_translate("MainWindow", "Repository :"))
        self.label_11.setText(_translate("MainWindow", "Snapshot :"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Destination"))
        self.label_5.setText(_translate("MainWindow", "IP :"))
        self.label_6.setText(_translate("MainWindow", "Port :"))
        self.label_7.setText(_translate("MainWindow", "Username :"))
        self.label_8.setText(_translate("MainWindow", "Password :"))
        self.chk.setText(_translate("MainWindow", "Delete all previous data"))
        self.btnBackUp.setText(_translate("MainWindow", "Backup"))
        self.btnRestore.setText(_translate("MainWindow", "Restore"))
        self.btnClose.setText(_translate("MainWindow", "Close"))
    def close(self):
        es = Elasticsearch(
            [self.txtSourceIP.text()],
            http_auth=(self.txtSourceUsername.text(), self.txtSourcePassword.text()),
            scheme="http",
            port=self.txtSourcePort.text()
        )
        es2 = Elasticsearch(
            [self.txtDestinationIP.text()],
            http_auth=(self.txtDestinationUsername.text(), self.txtDestinationPassword.text()),
            scheme="http",
            port=self.txtDestinationPort.text()
        )

        print(es.indices.get_alias().keys())
        print(es2.indices.get_alias().keys())


    def restore(self):
        data = {}
        data.update({'IP': self.txtDestinationIP.text()})
        data.update({'Port': self.txtDestinationPort.text()})
        data.update({'Username': self.txtDestinationUsername.text()})
        data.update({'Password': self.txtDestinationPassword.text()})
        data.update({'Path': self.txtPath.text()})
        self.repository_name = self.txtRepository.text()
        self.snapshot_name = self.txtSnapshot.text()

        es_restore = Elasticsearch(
            [f'{data.get("IP")}'],
            http_auth=(data.get('Username'), data.get('Password')),
            scheme="http",
            port=data.get('Port')
        )

        print('Ping Elastic Destination : ', es_restore.ping())

        repo_body = {
            "type": "fs",
            "settings": {
                "location": data.get('Path')
            }
        }
        es_restore.snapshot.create_repository(repository=self.repository_name, body=repo_body)
        es_restore.snapshot.create(repository=self.repository_name, snapshot=self.snapshot_name)

        restore_body = {
            "indices": "_all",  # تمامی ایندکس‌ها را بازیابی کن
            "ignore_unavailable": True,
            "include_global_state": False,
            "rename_pattern": "index_(.+)",  # الگوی تغییر نام ایندکس‌ها
            "rename_replacement": "restored_index_$1"  # الگوی جایگزینی برای نام‌های جدید ایندکس‌ها
        }
        es_restore.snapshot.restore(repository=self.repository_name, snapshot=self.snapshot_name, body=restore_body)

    def backup(self):
        # data = {}
        # data.update({'IP': self.txtSourceIP.text()})
        # data.update({'Port': self.txtSourcePort.text()})
        # data.update({'Username': self.txtSourceUsername.text()})
        # data.update({'Password': self.txtSourcePassword.text()})
        # data.update({'Repository': self.txtRepository.text()})
        # data.update({'Snapshot': self.txtSnapshot.text()})
        # data.update({'Path': self.txtPath.text()})
        #
        # es = Elasticsearch(
        #     [data.get('IP')],
        #     http_auth=(data.get('Username'), data.get('Password')),
        #     scheme="http",
        #     port=data.get('Port')
        # )
        #
        # print('Ping Elastic Source : ', es.ping())
        #
        # self.repository_name = data.get('Repository')
        # self.snapshot_name = data.get('Snapshot')
        #
        # repo_body = {
        #     "type": "fs",
        #     "settings": {
        #         "location": data.get('Path')
        #     }
        # }
        # es.snapshot.create_repository(repository=self.repository_name, body=repo_body)
        #
        # snapshot_body = {
        #     "indices": "*,-.*",
        #     "ignore_unavailable": True,
        #     "include_global_state": False
        # }
        # es.snapshot.create(repository=self.repository_name, snapshot=self.snapshot_name, body=snapshot_body)
        output_filename = f"elastc-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.tar.gz"

        hostname = "192.168.83.224"
        username = "root"
        password = "123"

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        volume = 'elastic'

        zip_command = f"docker volume inspect {volume}"
        stdin, stdout, stderr = ssh.exec_command(zip_command)

        volume_mountpoint  = json.loads(stdout.read().decode())
        volume_mountpoint = volume_mountpoint[0].get('Mountpoint') + '/' + self.txtPath.text()

        # print("Output:", stdout.read().decode())
        # print("Errors:", stderr.read().decode())

        zip_command = f"cd {volume_mountpoint} ; tar -czvf {output_filename} *"
        stdin, stdout, stderr = ssh.exec_command(zip_command)

        # print("Output:", stdout.read().decode())
        # print("Errors:", stderr.read().decode())

        sftp = ssh.open_sftp()
        sftp.get(volume_mountpoint + output_filename, output_filename)

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
