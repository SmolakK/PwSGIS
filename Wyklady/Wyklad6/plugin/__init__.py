from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.utils import *
from qgis.core import *
from qgis.gui import *
from .form import Ui_Okno

def classFactory(iface):
    return NaszPlugin(iface)


class NaszPlugin:
    """To klasa naszego pluginu"""
    def __init__(self, iface):
        """
        Inicjalizacja
        :param iface: QgisInterface
        :return:
        """
        self.iface = iface

    def initGui(self):
        self.action = QAction(QIcon("""C:\\Users\\kamil\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\plugin\\icon.png"""),"NaszPlugin",self.iface.mainWindow())

        self.menu = QMenu(self.iface.mainWindow())
        self.menu.setTitle("Menu Wtyczki")
        self.menu.addAction(self.action)

        #self.iface.addToolBarIcon(self.action)
        self.action.triggered.connect(self.run)

        menuBar = self.iface.mainWindow().menuBar()
        menuBar.addAction(self.menu.menuAction())

    def unload(self):
        self.menu.deleteLater()
        del self.action

    def run(self):
        self.window = QDialog()
        self.form = Ui_Okno()
        self.form.setupUi(self.window)
        self.form.pushButton.setText("Otwieraj")
        self.form.pushButton.clicked.connect(self.otworz)
        self.form.pushButton_2.released.connect(self.zapisz)
        self.form.checkBox.clicked.connect(self.modyfikacje)
        self.window.show()

    def otworz(self):
        sciezka = QFileDialog.getOpenFileName(self.window, "Otworz", "C:\\", '*.shp')
        if QFileDialog.accepted:
            self.iface.addVectorLayer(sciezka[0], "plik", "ogr")
            self.form.lineEdit.setText(sciezka[0])

    def zapisz(self):
        sciezka = QFileDialog.getSaveFileName(self.window, "Zapisz", "C:\\")
        if QFileDialog.accepted:
            QgsVectorFileWriter.writeAsVectorFormat(self.iface.activeLayer(), sciezka[0], "UTF-8")

    def modyfikacje(self):
        self.form.spinBox.setValue(self.form.spinBox.value()+1)
        self.form.spinBox.setGeometry(self.form.spinBox.x(),self.form.spinBox.y(),self.form.spinBox.width()+1, self.form.spinBox.height()+1)