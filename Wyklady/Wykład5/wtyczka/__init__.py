from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
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
        self.iface.addToolBarIcon(self.action)
        self.action.triggered.connect(self.run)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def run(self):
        self.window = QDialog()
        self.form = Ui_Okno()
        self.form.setupUi(self.window)
        self.window.show()
