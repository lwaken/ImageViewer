from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtCore import QDir

app = QtWidgets.QApplication([])
ui = uic.loadUi('design.ui')
ui.setWindowTitle('Image viewer')
ui.resize(768, 768)
image = QPixmap('noImage').scaledToWidth(620)
ui.image.setPixmap(image)
ui.statusbar.showMessage("No image")

folder_path = ""
files = []
idx = 0

def onRight():
  global idx
  idx += 1
  filename = folder_path + '/' + files[idx]
  global image
  image = QPixmap(filename)
  ui.scaleSlider.setValue(100)
  ui.image.setPixmap(image)
  ui.statusbar.showMessage("%s    %s x %s"%(filename, image.width(), image.height()))

def onLeft():
  global idx
  idx -=1
  filename = folder_path + '/' + files[idx]
  global image
  image = QPixmap(filename)
  ui.scaleSlider.setValue(100)
  ui.image.setPixmap(image)
  ui.statusbar.showMessage("%s    %s x %s"%(filename, image.width(), image.height()))

def onClick():
  filename, _ = QtWidgets.QFileDialog.getOpenFileName(ui, "Open Image", "/", "Images (*.png *.jpg)")
  if (filename):
    
    global folder_path
    folder_path = filename[0:filename.rfind('/')]
    
    global files
    filters = ["*.png", "*.jpg", "*.bmp", "*.gif", "*.jpeg"]
    folder = QDir(folder_path)
    folder.setNameFilters(filters)
    files = folder.entryList()
    print(files)
    global idx
    print(files[0])
    print(filename[filename.rfind('/')+1:])
    idx = files.index(filename[filename.rfind('/')+1:])
    print(idx)
    
    global image
    image = QPixmap(filename)
    ui.scaleSlider.setValue(100)
    ui.image.setPixmap(image)
    ui.statusbar.showMessage("%s    %s x %s"%(filename, image.width(), image.height()))

def onScaleChanged():
  scale = ui.scaleSlider.value()
  ui.image.setPixmap(image.scaledToWidth(image.width()*scale//100)) 

  # -- Connecting Signals -- #
ui.openButton.clicked.connect(onClick)
ui.scaleSlider.valueChanged.connect(onScaleChanged)
ui.leftButton.clicked.connect(onLeft)
ui.rightButton.clicked.connect(onRight)

  # -- Executing App -- #
ui.show()
app.exec()
