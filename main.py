from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap, QMouseEvent

app = QtWidgets.QApplication([])
ui = uic.loadUi('design.ui')
ui.setWindowTitle('Image viewer')
ui.resize(768, 768)
image = QPixmap('noImage').scaledToWidth(620)
ui.image.setPixmap(image)
ui.statusbar.showMessage("No image")

def onClick():
  filename, _ = QtWidgets.QFileDialog.getOpenFileName(ui, "Open Image", "/", "Images (*.png *.jpg)")
  if (filename):
    global image
    image = QPixmap(filename)
    ui.scaleSlider.setValue(100)
    ui.image.setPixmap(image)
    ui.statusbar.showMessage("%s    %s x %s"%(filename, image.width(), image.height()))

def onScaleChanged():
  scale = ui.scaleSlider.value()
  ui.image.setPixmap(image.scaledToWidth(image.width()*scale//100))

def mousePressEvent(event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            ui.close() 

  # -- Connecting Signals -- #
ui.openButton.clicked.connect(onClick)
ui.scaleSlider.valueChanged.connect(onScaleChanged)

  # -- Executing App -- #
ui.show()
app.exec()
