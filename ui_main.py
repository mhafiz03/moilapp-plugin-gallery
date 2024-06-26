# Form implementation generated from reading ui file '.\plugins\moilapp-plugin-presentation\ui_main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1115, 844)
        self.verticalLayout = QtWidgets.QVBoxLayout(Main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(parent=Main)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.selectFolderButton = QtWidgets.QPushButton(parent=self.frame_5)
        self.selectFolderButton.setObjectName("selectFolderButton")
        self.horizontalLayout_4.addWidget(self.selectFolderButton)
        self.searchImagesButton = QtWidgets.QPushButton(parent=self.frame_5)
        self.searchImagesButton.setObjectName("searchImagesButton")
        self.horizontalLayout_4.addWidget(self.searchImagesButton)
        self.openCameraButton = QtWidgets.QPushButton(parent=self.frame_5)
        self.openCameraButton.setObjectName("openCameraButton")
        self.horizontalLayout_4.addWidget(self.openCameraButton)
        self.verticalLayout.addWidget(self.frame_5)
        self.searchFrame = QtWidgets.QFrame(parent=Main)
        self.searchFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.searchFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.searchFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.searchFrame.setObjectName("searchFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.searchFrame)
        self.horizontalLayout.setContentsMargins(0, 11, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=self.searchFrame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.imageLimit = QtWidgets.QSpinBox(parent=self.searchFrame)
        self.imageLimit.setMinimumSize(QtCore.QSize(60, 0))
        self.imageLimit.setObjectName("imageLimit")
        self.horizontalLayout.addWidget(self.imageLimit)
        spacerItem1 = QtWidgets.QSpacerItem(80, 0, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.searchLine = QtWidgets.QLineEdit(parent=self.searchFrame)
        self.searchLine.setMinimumSize(QtCore.QSize(500, 30))
        self.searchLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.searchLine.setObjectName("searchLine")
        self.horizontalLayout.addWidget(self.searchLine)
        self.searchButton = QtWidgets.QPushButton(parent=self.searchFrame)
        self.searchButton.setMinimumSize(QtCore.QSize(150, 30))
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.queryCommaCheck = QtWidgets.QCheckBox(parent=self.searchFrame)
        self.queryCommaCheck.setObjectName("queryCommaCheck")
        self.horizontalLayout.addWidget(self.queryCommaCheck)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.searchFrame)
        self.frame_3 = QtWidgets.QFrame(parent=Main)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.zoomFrame = QtWidgets.QFrame(parent=self.frame_3)
        self.zoomFrame.setMinimumSize(QtCore.QSize(0, 20))
        self.zoomFrame.setMaximumSize(QtCore.QSize(25000, 50))
        self.zoomFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.zoomFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.zoomFrame.setObjectName("zoomFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.zoomFrame)
        self.horizontalLayout_2.setContentsMargins(0, 7, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(200, 0, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(parent=self.zoomFrame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.galleryZoomSlider = QtWidgets.QSlider(parent=self.zoomFrame)
        self.galleryZoomSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.galleryZoomSlider.setObjectName("galleryZoomSlider")
        self.horizontalLayout_2.addWidget(self.galleryZoomSlider)
        spacerItem5 = QtWidgets.QSpacerItem(237, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3.addWidget(self.zoomFrame)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(parent=Main)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 500))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.galleryList = QtWidgets.QListWidget(parent=self.frame_2)
        self.galleryList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.galleryList.setObjectName("galleryList")
        self.verticalLayout_2.addWidget(self.galleryList)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Form"))
        self.selectFolderButton.setText(_translate("Main", "Select Folder"))
        self.searchImagesButton.setText(_translate("Main", "Search Images"))
        self.openCameraButton.setText(_translate("Main", "Open Camera"))
        self.label.setText(_translate("Main", "Num. of Images Limit:"))
        self.searchButton.setText(_translate("Main", "Search"))
        self.queryCommaCheck.setText(_translate("Main", "Seperate query with comma"))
        self.label_2.setText(_translate("Main", "Zoom:"))
