# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\uiMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(517, 458)
        MainWindow.setMinimumSize(QtCore.QSize(517, 458))
        MainWindow.setMaximumSize(QtCore.QSize(517, 458))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(-1, 0, 521, 441))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_acceuil = QtWidgets.QWidget()
        self.tab_acceuil.setObjectName("tab_acceuil")
        self.label_19 = QtWidgets.QLabel(self.tab_acceuil)
        self.label_19.setGeometry(QtCore.QRect(10, 20, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.tabWidget.addTab(self.tab_acceuil, "")
        self.tab_envoyer = QtWidgets.QWidget()
        self.tab_envoyer.setObjectName("tab_envoyer")
        self.envoyer_btn_selectionner = QtWidgets.QPushButton(self.tab_envoyer)
        self.envoyer_btn_selectionner.setGeometry(QtCore.QRect(10, 10, 491, 31))
        self.envoyer_btn_selectionner.setObjectName("envoyer_btn_selectionner")
        self.envoyer_checkBox_cv = QtWidgets.QCheckBox(self.tab_envoyer)
        self.envoyer_checkBox_cv.setGeometry(QtCore.QRect(20, 60, 191, 31))
        self.envoyer_checkBox_cv.setObjectName("envoyer_checkBox_cv")
        self.envoyer_checkBox_lm = QtWidgets.QCheckBox(self.tab_envoyer)
        self.envoyer_checkBox_lm.setGeometry(QtCore.QRect(20, 100, 191, 31))
        self.envoyer_checkBox_lm.setObjectName("envoyer_checkBox_lm")
        self.envoyer_checkBox_formation = QtWidgets.QCheckBox(self.tab_envoyer)
        self.envoyer_checkBox_formation.setGeometry(QtCore.QRect(20, 140, 191, 31))
        self.envoyer_checkBox_formation.setObjectName("envoyer_checkBox_formation")
        self.envoyer_btn_visualiser = QtWidgets.QPushButton(self.tab_envoyer)
        self.envoyer_btn_visualiser.setGeometry(QtCore.QRect(10, 190, 191, 31))
        self.envoyer_btn_visualiser.setObjectName("envoyer_btn_visualiser")
        self.envoyer_btn_envoyer = QtWidgets.QPushButton(self.tab_envoyer)
        self.envoyer_btn_envoyer.setGeometry(QtCore.QRect(10, 370, 191, 31))
        self.envoyer_btn_envoyer.setObjectName("envoyer_btn_envoyer")
        self.envoyer_list = QtWidgets.QTreeWidget(self.tab_envoyer)
        self.envoyer_list.setGeometry(QtCore.QRect(220, 50, 281, 351))
        self.envoyer_list.setFrameShape(QtWidgets.QFrame.Box)
        self.envoyer_list.setFrameShadow(QtWidgets.QFrame.Plain)
        self.envoyer_list.setLineWidth(2)
        self.envoyer_list.setObjectName("envoyer_list")
        self.envoyer_label_pdf = QtWidgets.QLabel(self.tab_envoyer)
        self.envoyer_label_pdf.setGeometry(QtCore.QRect(20, 230, 171, 131))
        self.envoyer_label_pdf.setFrameShape(QtWidgets.QFrame.Box)
        self.envoyer_label_pdf.setLineWidth(2)
        self.envoyer_label_pdf.setAlignment(QtCore.Qt.AlignCenter)
        self.envoyer_label_pdf.setObjectName("envoyer_label_pdf")
        self.tabWidget.addTab(self.tab_envoyer, "")
        self.tab_contacts = QtWidgets.QWidget()
        self.tab_contacts.setObjectName("tab_contacts")
        self.contacts_input_entreprise = QtWidgets.QLineEdit(self.tab_contacts)
        self.contacts_input_entreprise.setGeometry(QtCore.QRect(10, 70, 231, 31))
        self.contacts_input_entreprise.setObjectName("contacts_input_entreprise")
        self.contacts_input_contact = QtWidgets.QLineEdit(self.tab_contacts)
        self.contacts_input_contact.setGeometry(QtCore.QRect(330, 70, 171, 31))
        self.contacts_input_contact.setObjectName("contacts_input_contact")
        self.contacts_input_telephone = QtWidgets.QLineEdit(self.tab_contacts)
        self.contacts_input_telephone.setGeometry(QtCore.QRect(10, 130, 231, 31))
        self.contacts_input_telephone.setObjectName("contacts_input_telephone")
        self.contacts_input_mail = QtWidgets.QLineEdit(self.tab_contacts)
        self.contacts_input_mail.setGeometry(QtCore.QRect(10, 190, 231, 31))
        self.contacts_input_mail.setObjectName("contacts_input_mail")
        self.contacts_label_entreprise = QtWidgets.QLabel(self.tab_contacts)
        self.contacts_label_entreprise.setGeometry(QtCore.QRect(10, 50, 231, 21))
        self.contacts_label_entreprise.setAlignment(QtCore.Qt.AlignCenter)
        self.contacts_label_entreprise.setObjectName("contacts_label_entreprise")
        self.contacts_label_contact = QtWidgets.QLabel(self.tab_contacts)
        self.contacts_label_contact.setGeometry(QtCore.QRect(270, 50, 231, 21))
        self.contacts_label_contact.setAlignment(QtCore.Qt.AlignCenter)
        self.contacts_label_contact.setObjectName("contacts_label_contact")
        self.contacts_label_telephone = QtWidgets.QLabel(self.tab_contacts)
        self.contacts_label_telephone.setGeometry(QtCore.QRect(10, 110, 231, 21))
        self.contacts_label_telephone.setAlignment(QtCore.Qt.AlignCenter)
        self.contacts_label_telephone.setObjectName("contacts_label_telephone")
        self.contacts_label_adresse = QtWidgets.QLabel(self.tab_contacts)
        self.contacts_label_adresse.setGeometry(QtCore.QRect(270, 110, 231, 21))
        self.contacts_label_adresse.setAlignment(QtCore.Qt.AlignCenter)
        self.contacts_label_adresse.setObjectName("contacts_label_adresse")
        self.contacts_label_mail = QtWidgets.QLabel(self.tab_contacts)
        self.contacts_label_mail.setGeometry(QtCore.QRect(10, 170, 231, 21))
        self.contacts_label_mail.setAlignment(QtCore.Qt.AlignCenter)
        self.contacts_label_mail.setObjectName("contacts_label_mail")
        self.contacts_textEdit_adresse = QtWidgets.QPlainTextEdit(self.tab_contacts)
        self.contacts_textEdit_adresse.setGeometry(QtCore.QRect(270, 130, 231, 91))
        self.contacts_textEdit_adresse.setObjectName("contacts_textEdit_adresse")
        self.contacts_btn_save = QtWidgets.QPushButton(self.tab_contacts)
        self.contacts_btn_save.setGeometry(QtCore.QRect(10, 372, 491, 31))
        self.contacts_btn_save.setObjectName("contacts_btn_save")
        self.contacts_label_commentaire = QtWidgets.QLabel(self.tab_contacts)
        self.contacts_label_commentaire.setGeometry(QtCore.QRect(10, 230, 121, 21))
        self.contacts_label_commentaire.setAlignment(QtCore.Qt.AlignCenter)
        self.contacts_label_commentaire.setObjectName("contacts_label_commentaire")
        self.contacts_textEdit_commentaire = QtWidgets.QPlainTextEdit(self.tab_contacts)
        self.contacts_textEdit_commentaire.setGeometry(QtCore.QRect(10, 250, 491, 111))
        self.contacts_textEdit_commentaire.setObjectName("contacts_textEdit_commentaire")
        self.contacts_combobox_sexe = QtWidgets.QComboBox(self.tab_contacts)
        self.contacts_combobox_sexe.setGeometry(QtCore.QRect(270, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.contacts_combobox_sexe.setFont(font)
        self.contacts_combobox_sexe.setObjectName("contacts_combobox_sexe")
        self.contacts_combobox_sexe.addItem("")
        self.contacts_combobox_sexe.addItem("")
        self.contacts_btn_rechercher = QtWidgets.QPushButton(self.tab_contacts)
        self.contacts_btn_rechercher.setGeometry(QtCore.QRect(10, 10, 491, 31))
        self.contacts_btn_rechercher.setObjectName("contacts_btn_rechercher")
        self.tabWidget.addTab(self.tab_contacts, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 517, 22))
        self.menuBar.setObjectName("menuBar")
        self.menu_option = QtWidgets.QMenu(self.menuBar)
        self.menu_option.setEnabled(True)
        self.menu_option.setObjectName("menu_option")
        MainWindow.setMenuBar(self.menuBar)
        self.actionLocalisation_Images = QtWidgets.QAction(MainWindow)
        self.actionLocalisation_Images.setObjectName("actionLocalisation_Images")
        self.actionConnexion_MYSQL = QtWidgets.QAction(MainWindow)
        self.actionConnexion_MYSQL.setObjectName("actionConnexion_MYSQL")
        self.actionConnexion_ACCESS = QtWidgets.QAction(MainWindow)
        self.actionConnexion_ACCESS.setObjectName("actionConnexion_ACCESS")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu_option.addAction(self.actionAbout)
        self.menuBar.addAction(self.menu_option.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python - pyMailing"))
        self.label_19.setText(_translate("MainWindow", "ACCUEIL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_acceuil), _translate("MainWindow", "ACCUEIL"))
        self.envoyer_btn_selectionner.setText(_translate("MainWindow", "SELECTIONNER"))
        self.envoyer_checkBox_cv.setText(_translate("MainWindow", "CURRICULUM VITAE"))
        self.envoyer_checkBox_lm.setText(_translate("MainWindow", "LETTRE MOTIVATION"))
        self.envoyer_checkBox_formation.setText(_translate("MainWindow", "FEUILLET FORMATION"))
        self.envoyer_btn_visualiser.setText(_translate("MainWindow", "VISUALISER"))
        self.envoyer_btn_envoyer.setText(_translate("MainWindow", "ENVOYER"))
        self.envoyer_list.headerItem().setText(0, _translate("MainWindow", "ENTREPRISE"))
        self.envoyer_list.headerItem().setText(1, _translate("MainWindow", "MAIL"))
        self.envoyer_label_pdf.setText(_translate("MainWindow", "PDF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_envoyer), _translate("MainWindow", "ENVOYER"))
        self.contacts_label_entreprise.setText(_translate("MainWindow", "ENTREPRISE"))
        self.contacts_label_contact.setText(_translate("MainWindow", "CONTACT"))
        self.contacts_label_telephone.setText(_translate("MainWindow", "TELEPHONE"))
        self.contacts_label_adresse.setText(_translate("MainWindow", "ADRESSE"))
        self.contacts_label_mail.setText(_translate("MainWindow", "MAIL"))
        self.contacts_btn_save.setText(_translate("MainWindow", "SAUVEGARDER"))
        self.contacts_label_commentaire.setText(_translate("MainWindow", "COMMENTAIRE"))
        self.contacts_combobox_sexe.setItemText(0, _translate("MainWindow", "Mme"))
        self.contacts_combobox_sexe.setItemText(1, _translate("MainWindow", "M"))
        self.contacts_btn_rechercher.setText(_translate("MainWindow", "RECHERCHER"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_contacts), _translate("MainWindow", "CONTACTS"))
        self.menu_option.setTitle(_translate("MainWindow", "Options"))
        self.actionLocalisation_Images.setText(_translate("MainWindow", "Localisation Images"))
        self.actionConnexion_MYSQL.setText(_translate("MainWindow", "Connexion MYSQL"))
        self.actionConnexion_ACCESS.setText(_translate("MainWindow", "Connexion ACCESS"))
        self.actionAbout.setText(_translate("MainWindow", "?"))
