# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'binary_data_form2.ui'
#
# Created: Mon Mar 25 14:56:34 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BinaryDataForm(object):
    def setupUi(self, BinaryDataForm):
        BinaryDataForm.setObjectName(_fromUtf8("BinaryDataForm"))
        BinaryDataForm.setEnabled(True)
        BinaryDataForm.resize(394, 419)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        BinaryDataForm.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/meta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BinaryDataForm.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(BinaryDataForm)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 9)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.event_lbl = QtGui.QLabel(BinaryDataForm)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.event_lbl.setFont(font)
        self.event_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.event_lbl.setObjectName(_fromUtf8("event_lbl"))
        self.gridLayout.addWidget(self.event_lbl, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(BinaryDataForm)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(BinaryDataForm)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(BinaryDataForm)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.raw_data_table = QtGui.QTableWidget(BinaryDataForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.raw_data_table.sizePolicy().hasHeightForWidth())
        self.raw_data_table.setSizePolicy(sizePolicy)
        self.raw_data_table.setMinimumSize(QtCore.QSize(305, 93))
        self.raw_data_table.setMaximumSize(QtCore.QSize(305, 84))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.raw_data_table.setFont(font)
        self.raw_data_table.setFrameShadow(QtGui.QFrame.Plain)
        self.raw_data_table.setLineWidth(1)
        self.raw_data_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.raw_data_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.raw_data_table.setProperty("showDropIndicator", True)
        self.raw_data_table.setAlternatingRowColors(True)
        self.raw_data_table.setShowGrid(True)
        self.raw_data_table.setGridStyle(QtCore.Qt.DashDotLine)
        self.raw_data_table.setRowCount(3)
        self.raw_data_table.setColumnCount(3)
        self.raw_data_table.setObjectName(_fromUtf8("raw_data_table"))
        self.raw_data_table.horizontalHeader().setVisible(False)
        self.raw_data_table.horizontalHeader().setHighlightSections(False)
        self.raw_data_table.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.raw_data_table, 1, 1, 3, 3)
        self.label_4 = QtGui.QLabel(BinaryDataForm)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_9 = QtGui.QLabel(BinaryDataForm)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.clear_Btn = QtGui.QPushButton(BinaryDataForm)
        self.clear_Btn.setObjectName(_fromUtf8("clear_Btn"))
        self.horizontalLayout_2.addWidget(self.clear_Btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.back_calc_btn = QtGui.QPushButton(BinaryDataForm)
        self.back_calc_btn.setEnabled(False)
        self.back_calc_btn.setObjectName(_fromUtf8("back_calc_btn"))
        self.horizontalLayout_2.addWidget(self.back_calc_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_13 = QtGui.QLabel(BinaryDataForm)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_4.addWidget(self.label_13)
        self.effect_cbo_box = QtGui.QComboBox(BinaryDataForm)
        self.effect_cbo_box.setMinimumSize(QtCore.QSize(76, 20))
        self.effect_cbo_box.setMaximumSize(QtCore.QSize(76, 20))
        self.effect_cbo_box.setObjectName(_fromUtf8("effect_cbo_box"))
        self.horizontalLayout_4.addWidget(self.effect_cbo_box)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.groupBox = QtGui.QGroupBox(BinaryDataForm)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(32, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 2, 1)
        self.ci_label = QtGui.QLabel(self.groupBox)
        self.ci_label.setObjectName(_fromUtf8("ci_label"))
        self.gridLayout_2.addWidget(self.ci_label, 0, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(32, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 3, 2, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.est_lbl = QtGui.QLabel(self.groupBox)
        self.est_lbl.setMinimumSize(QtCore.QSize(0, 20))
        self.est_lbl.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.est_lbl.setFont(font)
        self.est_lbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.est_lbl.setObjectName(_fromUtf8("est_lbl"))
        self.horizontalLayout_3.addWidget(self.est_lbl)
        self.effect_txt_box = QtGui.QLineEdit(self.groupBox)
        self.effect_txt_box.setMinimumSize(QtCore.QSize(50, 20))
        self.effect_txt_box.setMaximumSize(QtCore.QSize(50, 20))
        self.effect_txt_box.setObjectName(_fromUtf8("effect_txt_box"))
        self.horizontalLayout_3.addWidget(self.effect_txt_box)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.low_lbl = QtGui.QLabel(self.groupBox)
        self.low_lbl.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.low_lbl.setFont(font)
        self.low_lbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.low_lbl.setObjectName(_fromUtf8("low_lbl"))
        self.horizontalLayout_5.addWidget(self.low_lbl)
        self.low_txt_box = QtGui.QLineEdit(self.groupBox)
        self.low_txt_box.setMinimumSize(QtCore.QSize(50, 20))
        self.low_txt_box.setMaximumSize(QtCore.QSize(50, 20))
        self.low_txt_box.setObjectName(_fromUtf8("low_txt_box"))
        self.horizontalLayout_5.addWidget(self.low_txt_box)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_5.addWidget(self.label)
        self.high_txt_box = QtGui.QLineEdit(self.groupBox)
        self.high_txt_box.setMinimumSize(QtCore.QSize(50, 20))
        self.high_txt_box.setMaximumSize(QtCore.QSize(50, 20))
        self.high_txt_box.setObjectName(_fromUtf8("high_txt_box"))
        self.horizontalLayout_5.addWidget(self.high_txt_box)
        self.high_lbl = QtGui.QLabel(self.groupBox)
        self.high_lbl.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.high_lbl.setFont(font)
        self.high_lbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.high_lbl.setObjectName(_fromUtf8("high_lbl"))
        self.horizontalLayout_5.addWidget(self.high_lbl)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.line = QtGui.QFrame(BinaryDataForm)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_2 = QtGui.QLabel(BinaryDataForm)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_6.addWidget(self.label_2)
        self.CI_spinbox = QtGui.QDoubleSpinBox(BinaryDataForm)
        self.CI_spinbox.setDecimals(1)
        self.CI_spinbox.setMinimum(40.0)
        self.CI_spinbox.setMaximum(100.0)
        self.CI_spinbox.setSingleStep(0.1)
        self.CI_spinbox.setProperty("value", 95.0)
        self.CI_spinbox.setObjectName(_fromUtf8("CI_spinbox"))
        self.horizontalLayout_6.addWidget(self.CI_spinbox)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.inconsistencyLabel = QtGui.QLabel(BinaryDataForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inconsistencyLabel.setFont(font)
        self.inconsistencyLabel.setObjectName(_fromUtf8("inconsistencyLabel"))
        self.horizontalLayout.addWidget(self.inconsistencyLabel)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.buttonBox = QtGui.QDialogButtonBox(BinaryDataForm)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(BinaryDataForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), BinaryDataForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), BinaryDataForm.reject)
        QtCore.QMetaObject.connectSlotsByName(BinaryDataForm)

    def retranslateUi(self, BinaryDataForm):
        BinaryDataForm.setWindowTitle(_translate("BinaryDataForm", "Binary Data", None))
        self.event_lbl.setText(_translate("BinaryDataForm", "event", None))
        self.label_6.setText(_translate("BinaryDataForm", "no event", None))
        self.label_10.setText(_translate("BinaryDataForm", "total", None))
        self.label_3.setText(_translate("BinaryDataForm", "group 1", None))
        self.label_4.setText(_translate("BinaryDataForm", "group 2", None))
        self.label_9.setText(_translate("BinaryDataForm", "total", None))
        self.clear_Btn.setText(_translate("BinaryDataForm", "Clear Form", None))
        self.back_calc_btn.setText(_translate("BinaryDataForm", "back-calculate table", None))
        self.label_13.setText(_translate("BinaryDataForm", "effect", None))
        self.ci_label.setToolTip(_translate("BinaryDataForm", "Use the box to the left to set the % confidence interval", None))
        self.ci_label.setText(_translate("BinaryDataForm", "X% Confidence Interval", None))
        self.est_lbl.setText(_translate("BinaryDataForm", "est.", None))
        self.low_lbl.setText(_translate("BinaryDataForm", "[", None))
        self.label.setText(_translate("BinaryDataForm", ",", None))
        self.high_lbl.setText(_translate("BinaryDataForm", "]", None))
        self.label_2.setText(_translate("BinaryDataForm", "Confidence Level:", None))
        self.CI_spinbox.setToolTip(_translate("BinaryDataForm", "Use this box to set the % confidence interval", None))
        self.CI_spinbox.setSuffix(_translate("BinaryDataForm", " %", None))
        self.inconsistencyLabel.setText(_translate("BinaryDataForm", "INCONSISTENT FORM", None))

import icons_rc
