


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph.opengl as gl
import pyqtgraph as pg
from PyQt5.QtGui import QPalette, QColor
import time
import numpy as np
from pathlib import Path
from scipy.stats import kde
import random
import pyqtgraph.Vector
import math
from scipy.spatial import distance
import ctypes




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1641, 889)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.parameter = QtWidgets.QGroupBox(self.centralwidget)
        self.parameter.setGeometry(QtCore.QRect(210, 0, 201, 141))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)

        self.parameter.setFont(font)
        self.parameter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parameter.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.parameter.setObjectName("parameter")
        self.collision = QtWidgets.QCheckBox(self.parameter)
        self.collision.setGeometry(QtCore.QRect(120, 20, 61, 17))
        self.collision.setObjectName("collision")
        self.trace = QtWidgets.QCheckBox(self.parameter)
        self.trace.setGeometry(QtCore.QRect(120, 50, 70, 17))
        self.trace.setObjectName("trace")
        self.grid = QtWidgets.QCheckBox(self.parameter)
        self.grid.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.grid.setChecked(True)
        self.grid.setObjectName("grid")
        self.pxmode = QtWidgets.QCheckBox(self.parameter)
        self.pxmode.setGeometry(QtCore.QRect(20, 50, 70, 17))
        self.pxmode.setChecked(True)
        self.pxmode.setObjectName("pxmode")
        self.g1 = QtWidgets.QLineEdit(self.parameter)
        self.g1.setGeometry(QtCore.QRect(120, 80, 61, 20))
        self.g1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.g1.setObjectName("g1")
        self.t1 = QtWidgets.QLineEdit(self.parameter)
        self.t1.setGeometry(QtCore.QRect(120, 110, 61, 21))
        self.t1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.t1.setObjectName("t1")
        self.g = QtWidgets.QLabel(self.parameter)
        self.g.setGeometry(QtCore.QRect(30, 80, 47, 13))
        self.g.setObjectName("g")
        self.t = QtWidgets.QLabel(self.parameter)
        self.t.setGeometry(QtCore.QRect(30, 110, 61, 20))
        self.t.setObjectName("t")
        self.color = QtWidgets.QGroupBox(self.centralwidget)
        self.color.setGeometry(QtCore.QRect(210, 140, 201, 71))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.color.setFont(font)
        self.color.setAlignment(QtCore.Qt.AlignCenter)
        self.color.setObjectName("color")
        self.colorsetting = QtWidgets.QComboBox(self.color)
        self.colorsetting.setGeometry(QtCore.QRect(10, 20, 181, 31))
        self.colorsetting.setEditable(False)
        self.colorsetting.setMaxVisibleItems(5)
        self.colorsetting.setMinimumContentsLength(3)
        self.colorsetting.setObjectName("colorsetting")
        self.colorsetting.addItem("")
        self.colorsetting.addItem("")
        self.colorsetting.addItem("")
        self.astresetting = QtWidgets.QGroupBox(self.centralwidget)
        self.astresetting.setGeometry(QtCore.QRect(0, 0, 201, 211))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.astresetting.setFont(font)
        self.astresetting.setAlignment(QtCore.Qt.AlignCenter)
        self.astresetting.setObjectName("astresetting")
        self.lineEdit = QtWidgets.QLineEdit(self.astresetting)
        self.lineEdit.setGeometry(QtCore.QRect(92, 30, 101, 20))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.astresetting)
        self.lineEdit_2.setGeometry(QtCore.QRect(92, 60, 101, 20))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.astresetting)
        self.lineEdit_3.setGeometry(QtCore.QRect(92, 90, 101, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.astresetting)
        self.lineEdit_4.setGeometry(QtCore.QRect(92, 120, 101, 20))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.astresetting)
        self.lineEdit_5.setGeometry(QtCore.QRect(92, 150, 101, 20))
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.x = QtWidgets.QLabel(self.astresetting)
        self.x.setGeometry(QtCore.QRect(10, 30, 71, 20))
        self.x.setObjectName("x")
        self.y = QtWidgets.QLabel(self.astresetting)
        self.y.setGeometry(QtCore.QRect(10, 60, 81, 21))
        self.y.setObjectName("y")
        self.z = QtWidgets.QLabel(self.astresetting)
        self.z.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.z.setObjectName("z")
        self.mass = QtWidgets.QLabel(self.astresetting)
        self.mass.setGeometry(QtCore.QRect(10, 120, 71, 21))
        self.mass.setObjectName("mass")
        self.size = QtWidgets.QLabel(self.astresetting)
        self.size.setGeometry(QtCore.QRect(10, 150, 71, 21))
        self.size.setObjectName("size")
        self.ringsetting = QtWidgets.QGroupBox(self.centralwidget)
        self.ringsetting.setGeometry(QtCore.QRect(0, 210, 411, 341))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ringsetting.setFont(font)
        self.ringsetting.setAlignment(QtCore.Qt.AlignCenter)
        self.ringsetting.setObjectName("ringsetting")
        self.xcoordcenter = QtWidgets.QLineEdit(self.ringsetting)
        self.xcoordcenter.setGeometry(QtCore.QRect(310, 20, 81, 20))
        self.xcoordcenter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.xcoordcenter.setObjectName("xcoordcenter")
        self.ycoordcenter = QtWidgets.QLineEdit(self.ringsetting)
        self.ycoordcenter.setGeometry(QtCore.QRect(310, 50, 81, 20))
        self.ycoordcenter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ycoordcenter.setObjectName("ycoordcenter")
        self.zcoordcenter = QtWidgets.QLineEdit(self.ringsetting)
        self.zcoordcenter.setGeometry(QtCore.QRect(310, 80, 81, 20))
        self.zcoordcenter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.zcoordcenter.setObjectName("zcoordcenter")
        self.nring = QtWidgets.QLineEdit(self.ringsetting)
        self.nring.setGeometry(QtCore.QRect(310, 110, 81, 20))
        self.nring.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nring.setObjectName("nring")
        self.distcenter = QtWidgets.QLineEdit(self.ringsetting)
        self.distcenter.setGeometry(QtCore.QRect(310, 140, 81, 20))
        self.distcenter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.distcenter.setObjectName("distcenter")
        self.widthcenter = QtWidgets.QLineEdit(self.ringsetting)
        self.widthcenter.setGeometry(QtCore.QRect(310, 170, 81, 20))
        self.widthcenter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.widthcenter.setObjectName("widthcenter")
        self.speedring = QtWidgets.QLineEdit(self.ringsetting)
        self.speedring.setGeometry(QtCore.QRect(310, 200, 81, 20))
        self.speedring.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.speedring.setObjectName("speedring")
        self.anglering = QtWidgets.QLineEdit(self.ringsetting)
        self.anglering.setGeometry(QtCore.QRect(310, 230, 81, 20))
        self.anglering.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.anglering.setObjectName("anglering")
        self.ticknesscenter = QtWidgets.QLineEdit(self.ringsetting)
        self.ticknesscenter.setGeometry(QtCore.QRect(310, 260, 81, 20))
        self.ticknesscenter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ticknesscenter.setObjectName("ticknesscenter")
        self.xcenter = QtWidgets.QLabel(self.ringsetting)
        self.xcenter.setGeometry(QtCore.QRect(20, 20, 131, 20))
        self.xcenter.setObjectName("xcenter")
        self.ycenter = QtWidgets.QLabel(self.ringsetting)
        self.ycenter.setGeometry(QtCore.QRect(20, 50, 131, 21))
        self.ycenter.setObjectName("ycenter")
        self.zcenter = QtWidgets.QLabel(self.ringsetting)
        self.zcenter.setGeometry(QtCore.QRect(20, 80, 161, 20))
        self.zcenter.setObjectName("zcenter")
        self.n = QtWidgets.QLabel(self.ringsetting)
        self.n.setGeometry(QtCore.QRect(20, 110, 101, 20))
        self.n.setObjectName("n")
        self.dist = QtWidgets.QLabel(self.ringsetting)
        self.dist.setGeometry(QtCore.QRect(20, 140, 141, 20))
        self.dist.setObjectName("dist")
        self.width = QtWidgets.QLabel(self.ringsetting)
        self.width.setGeometry(QtCore.QRect(20, 170, 101, 20))
        self.width.setObjectName("width")
        self.speed = QtWidgets.QLabel(self.ringsetting)
        self.speed.setGeometry(QtCore.QRect(20, 200, 71, 20))
        self.speed.setObjectName("speed")
        self.angle = QtWidgets.QLabel(self.ringsetting)
        self.angle.setGeometry(QtCore.QRect(20, 230, 81, 16))
        self.angle.setObjectName("angle")
        self.tickness = QtWidgets.QLabel(self.ringsetting)
        self.tickness.setGeometry(QtCore.QRect(20, 260, 111, 20))
        self.tickness.setObjectName("tickness")
        self.ring = QtWidgets.QPushButton(self.ringsetting)
        self.ring.setGeometry(QtCore.QRect(0, 290, 411, 41))
        self.ring.setObjectName("ring")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(0, 770, 141, 61))
        self.start.setObjectName("start")
        self.openGLWidget = gl.GLViewWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(420, 0, 1500, 891))
        self.openGLWidget.setObjectName("openGLWidget")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(140, 770, 141, 61))
        self.stop.setObjectName("stop")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(280, 770, 141, 121))
        self.clear.setObjectName("clear")
        self.freeze = QtWidgets.QPushButton(self.centralwidget)
        self.freeze.setGeometry(QtCore.QRect(140, 830, 141, 61))
        self.freeze.setObjectName("freeze")
        self.unfreeze = QtWidgets.QPushButton(self.centralwidget)
        self.unfreeze.setGeometry(QtCore.QRect(0, 830, 141, 61))
        self.unfreeze.setObjectName("unfreeze")
        self.cameraoption = QtWidgets.QGroupBox(self.centralwidget)
        self.cameraoption.setGeometry(QtCore.QRect(0, 550, 411, 211))
        self.cameraoption.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.cameraoption.setObjectName("cameraoption")
        self.camerapos = QtWidgets.QGroupBox(self.cameraoption)
        self.camerapos.setGeometry(QtCore.QRect(10, 9, 141, 191))
        self.camerapos.setObjectName("camerapos")
        self.camx = QtWidgets.QLabel(self.camerapos)
        self.camx.setGeometry(QtCore.QRect(10, 30, 47, 13))
        self.camx.setObjectName("camx")
        self.camy = QtWidgets.QLabel(self.camerapos)
        self.camy.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.camy.setObjectName("camy")
        self.camz = QtWidgets.QLabel(self.camerapos)
        self.camz.setGeometry(QtCore.QRect(10, 110, 47, 13))
        self.camz.setObjectName("camz")
        self.elevation = QtWidgets.QLabel(self.camerapos)
        self.elevation.setGeometry(QtCore.QRect(10, 150, 81, 16))
        self.elevation.setObjectName("elevation")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.camerapos)
        self.lineEdit_6.setGeometry(QtCore.QRect(70, 30, 61, 20))
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.camerapos)
        self.lineEdit_7.setGeometry(QtCore.QRect(70, 70, 61, 20))
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.camerapos)
        self.lineEdit_8.setGeometry(QtCore.QRect(70, 110, 61, 20))
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.camerapos)
        self.lineEdit_9.setGeometry(QtCore.QRect(70, 150, 61, 20))
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.cameraoption)
        self.lineEdit_10.setGeometry(QtCore.QRect(280, 60, 113, 20))
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.camdst = QtWidgets.QLabel(self.cameraoption)
        self.camdst.setGeometry(QtCore.QRect(160, 60, 101, 20))
        self.camdst.setObjectName("camdst")
        self.horizontalSlider = QtWidgets.QSlider(self.cameraoption)
        self.horizontalSlider.setGeometry(QtCore.QRect(230, 120, 161, 22))
        self.horizontalSlider.setMaximum(360)
        self.horizontalSlider.setProperty("value", 60)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.camfov = QtWidgets.QLabel(self.cameraoption)
        self.camfov.setGeometry(QtCore.QRect(160, 120, 61, 20))
        self.camfov.setObjectName("camfov")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.cameraoption)
        self.lineEdit_11.setGeometry(QtCore.QRect(160, 160, 231, 20))
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.colorsetting.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "simulation"))
        
        
        
        self.parameter.setTitle(_translate("MainWindow", "general parameter"))
        self.collision.setText(_translate("MainWindow", "collision"))
        self.trace.setText(_translate("MainWindow", "trace"))
        self.grid.setText(_translate("MainWindow", "grid"))
        self.pxmode.setText(_translate("MainWindow", "pxmode"))
        self.g1.setText(_translate("MainWindow", "1"))
        self.t1.setText(_translate("MainWindow", "1"))
        self.g.setText(_translate("MainWindow", "g value"))
        self.t.setText(_translate("MainWindow", "time value"))
        self.color.setTitle(_translate("MainWindow", "color setting"))
        self.colorsetting.setItemText(0, _translate("MainWindow", "random"))
        self.colorsetting.setItemText(2, _translate("MainWindow", "depend on scalar speed"))
        self.colorsetting.setItemText(1, _translate("MainWindow", "depend on coord speed"))
        self.astresetting.setTitle(_translate("MainWindow", "star setting"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
        self.lineEdit_4.setText(_translate("MainWindow", "100"))
        self.lineEdit_5.setText(_translate("MainWindow", "10"))
        self.x.setText(_translate("MainWindow", "x coordonate"))
        self.y.setText(_translate("MainWindow", "y coordonate"))
        self.z.setText(_translate("MainWindow", "z coordonate"))
        self.mass.setText(_translate("MainWindow", "mass"))
        self.size.setText(_translate("MainWindow", "size"))
        self.ringsetting.setTitle(_translate("MainWindow", "ring setting"))
        self.xcoordcenter.setText(_translate("MainWindow", "0"))
        self.ycoordcenter.setText(_translate("MainWindow", "0"))
        self.zcoordcenter.setText(_translate("MainWindow", "0"))
        self.nring.setText(_translate("MainWindow", "500"))
        self.distcenter.setText(_translate("MainWindow", "100"))
        self.widthcenter.setText(_translate("MainWindow", "10"))
        self.speedring.setText(_translate("MainWindow", "1"))
        self.anglering.setText(_translate("MainWindow", "0"))
        self.ticknesscenter.setText(_translate("MainWindow", "1"))
        self.xcenter.setText(_translate("MainWindow", "x coordonate of the center"))
        self.ycenter.setText(_translate("MainWindow", "y coordonate of the center"))
        self.zcenter.setText(_translate("MainWindow", "z coordonate of the center"))
        self.n.setText(_translate("MainWindow", "number of astre"))
        self.dist.setText(_translate("MainWindow", "distance of the center"))
        self.width.setText(_translate("MainWindow", "width of the ring"))
        self.speed.setText(_translate("MainWindow", "speed"))
        self.angle.setText(_translate("MainWindow", "angle of the ring"))
        self.tickness.setText(_translate("MainWindow", "tickness of the ring"))
        self.ring.setText(_translate("MainWindow", "add ring"))
        self.ring.clicked.connect(ring)
        self.start.setText(_translate("MainWindow", "start simulation"))
        self.start.clicked.connect(start)
        self.stop.setText(_translate("MainWindow", "stop simulation"))
        self.stop.clicked.connect(stop)
        self.clear.setText(_translate("MainWindow", "clear ring"))
        self.clear.clicked.connect(clear)
        self.freeze.setText(_translate("MainWindow", "freeze movement"))
        self.freeze.clicked.connect(freez)
        self.unfreeze.setText(_translate("MainWindow", "unfreeze movement"))
        self.unfreeze.clicked.connect(unfreez)
        self.cameraoption.setTitle(_translate("MainWindow", "camera option"))
        self.camerapos.setTitle(_translate("MainWindow", "camera position"))
        self.camx.setText(_translate("MainWindow", "x"))
        self.camy.setText(_translate("MainWindow", "y"))
        self.camz.setText(_translate("MainWindow", "z"))
        self.elevation.setText(_translate("MainWindow", "elevation"))
        self.lineEdit_6.setText(_translate("MainWindow", "0"))
        self.lineEdit_7.setText(_translate("MainWindow", "0"))
        self.lineEdit_8.setText(_translate("MainWindow", "0"))
        self.lineEdit_9.setText(_translate("MainWindow", "30"))
        self.lineEdit_10.setText(_translate("MainWindow", "300"))
        self.camdst.setText(_translate("MainWindow", "distance from center"))
        self.camfov.setText(_translate("MainWindow", "field of view"))



w=0
t=0
g=0
colorspeed=0
stay=True
collision1=False
trace=False
blackhole=[0,0,0,0,0,0,0,0,0]
sp1=0
bh=0
pxmode=True


points=[]
final = np.array([[0,0,0,0,0,0,0]])


def ring():
    n=int(ui.nring.text())
    dst=int(ui.distcenter.text())
    x=float(ui.xcoordcenter.text())
    y=float(ui.ycoordcenter.text())
    z=float(ui.zcoordcenter.text())
    l=float(ui.widthcenter.text())
    speed=float(ui.speedring.text())
    angle=float(ui.anglering.text())
    t=float(ui.ticknesscenter.text())
    create_aneau(n,dst,[x,y,z],l,speed,angle,t)
    
def create_aneau(nombre_dastre_aneau,distance_centre,point_centrale,largeur_aneau,vt,z_angle,epaiseur):

    global points,pxmode
    angle=(2*math.pi/nombre_dastre_aneau)
    for i in range(nombre_dastre_aneau):
        cos=math.cos(angle*i)
        sin=math.sin(angle*i)
        x1=cos*distance_centre
        x2=cos*(distance_centre+largeur_aneau)
        y1=sin*distance_centre
        y2=sin*(distance_centre+largeur_aneau)
        x=random.uniform(x1,x2)+point_centrale[0]
        y=random.uniform(y1,y2)+point_centrale[1]
        z=random.randint(0,epaiseur)+point_centrale[2]

        if pxmode==True :
            masse=random.randint(10,50)
            size=masse/20            

        if pxmode==False:
            masse=random.randint(10,50)
            size=masse/20
        red=random.uniform(0,1)
        green=random.uniform(0,1)
        blue=random.uniform(0,1)
        white=1#random.uniform(0,1)
        vx=sin*-vt
        vy=cos*vt
        vz=0
        if z_angle!=0:
            x=x*math.cos(z_angle)+z*math.sin(z_angle)
            z=x*math.sin(z_angle)+z*math.cos(z_angle)
            vx=math.cos(z_angle)*-vt*sin
            vy=cos*vt
            vz=math.sin(z_angle)*-vt*cos
        points.append([x,y,z,masse,size,red,green,blue,white,vx,vy,vz])

def move(points):   
    global t
    global colorspeed
    global trace
    
    for i in range(len(points)):
        points[i][0]+=points[i][9]*t
        points[i][1]+=points[i][10]*t
        points[i][2]+=points[i][11]*t
        if colorspeed==1:
            points[i][5]=(abs(points[i][9])/10)+0.1
            points[i][7]=(abs(points[i][10])/10)+0.1
            points[i][6]=(abs(points[i][11])/10)
        if colorspeed==2:
            speed=math.sqrt((points[i][9])**2+(points[i][10])**2+(points[i][11])**2)
            speed1=(speed/10)+0.1
            points[i][5]=speed1
            points[i][6]=0.3
            points[i][7]=0.5
        if trace == True:
           global final
           final=np.concatenate((final,[[points[i][0],points[i][1],points[i][2],points[i][4],points[i][5],points[i][6],points[i][7]]]))
    return points

def gravity(astre,points):
    global t
    global g
    m=astre[4]
    temp=np.array(points)
    for i in range(len(points)):        
        dst = distance.euclidean(astre[0:3],temp[i,0:3])
        a=((g*m)/dst**2)*temp[i,0:3]*points[i][3]*0.01
        points[i][9]+=a[0]*t
        points[i][10]+=a[1]*t
        points[i][11]+=a[2]*t
    
    return points

def check_collision(astre_static,i):
        global points
        temp=np.array(points)
        dst  = distance.euclidean(astre_static[0:3],temp[i,0:3])
        temp=0
        if dst <=points[i][4]+astre_static[4]:
            return True
        else:
            return False

def collision(astre_static,points):
    print(astre_static[4])    
    if len(points)<1:
        return False
    for i in range(len(points)):
        if check_collision(astre_static,i)==True:
           astre_static[3]+=points[i][3]
           astre_static[4]=((astre_static[4]**3)+(points[i][4])**3)**(1/3)
           del points[i]
           break
    return astre_static , points

def update():
    global trace,collision1,blackhole,sp1,bh,stay,w,t
    print(t)
    #camera
    
    w.opts['fov']=float(ui.horizontalSlider.value())
    ui.lineEdit_11.setText(str(ui.horizontalSlider.value()))

    print(len(points))



    if stay==False:
        return False

    if len(points)<2:
        points.clear()
        #create_aneau(50,60,blackhole[0:3],10,1,0,0)
        return points

    if collision1 == True:
        collision(blackhole,points)
        

    gravity(blackhole,points)
    move(points)

    temp=np.array(points)

    if trace == True :
        global final
        sp1.setData(pos=final[:,0:3] , size=final[:,3],color=final[:,4:8])
    else :
        sp1.setData(pos=temp[:,0:3] , size=temp[:,4],color=temp[:,5:9])

    bh.setData(pos=np.array(blackhole[0:3]) , size=blackhole[4],color=blackhole[5:9])

def start():
    global t ,g,trace,colorspeed,collision1,sp1,bh,blackhole,w,stay,time,pxmode
    if len(points)<1:
        return False
    stay=True


    w = ui.openGLWidget
    xc=float(ui.lineEdit_6.text())
    yc=float(ui.lineEdit_7.text())
    zc=float(ui.lineEdit_8.text())
    w.setCameraPosition(pos=pyqtgraph.Vector(xc,yc,zc))
    w.opts['elevation']=float(ui.lineEdit_9.text())
    w.opts['distance']=float(ui.lineEdit_10.text())
    t=float(ui.t1.text())
    g=float(ui.g1.text())*-1

    colorspeed=ui.colorsetting.currentIndex()
    grid=ui.grid.isChecked()
    collision1=ui.collision.isChecked()
    pxmode=ui.pxmode.isChecked()
    trace=ui.trace.isChecked()


    if grid==True:
        x = gl.GLGridItem()
        x.setSize(x=1000,y=1000,z=0)
        x.setSpacing(x=100,y=100,z=100)
        w.addItem(x)


    #blackhole
    x=float(ui.lineEdit.text())
    y=float(ui.lineEdit_2.text())
    z=float(ui.lineEdit_3.text())
    masse=float(ui.lineEdit_4.text())
    size=float(ui.lineEdit_5.text())


    blackhole=[x,y,z,masse,size,1,1,1,1]

    temp=np.array(points)


    bh=gl.GLScatterPlotItem(pos=np.array(blackhole[0:3]) , size=blackhole[4],color=blackhole[5:9],pxMode=False)
    sp1=gl.GLScatterPlotItem(pos=temp[:,0:3] , size=temp[:,4],color=temp[:,5:9],pxMode=pxmode)

    temp=0
    w.addItem(bh)
    w.addItem(sp1)
    w.show()
    
    time = QtCore.QTimer(w)
    
    time.timeout.connect(update)
    time.start(40)

def clear():
    global sp1,final
    points.clear()
    points.append([0,0,0,0,0,0,0,0,0,0,0,0])
    final = np.array([[0,0,0,0,0,0,0]])
    sp1.setData(pos=np.array([[0,0,0]]) , size=0,color=[0,0,0,0])

def stop():
    global w,final,stay,time
    stay=False
    points.clear()
    #points.append([0,0,0,0,0,0,0,0,0,0,0,0])
    final = np.array([[0,0,0,0,0,0,0]])
    sp1.setData(pos=np.array([[0,0,0]]) , size=0,color=[0,0,0,0])
    for item in w.items:
        item._setView(None)
    w.items= []
    w.update
    time.stop()
       
def freez():
    global stay
    stay=False

def unfreez():
    global stay
    stay=True



if __name__ == "__main__":
    import sys  
    app = QtWidgets.QApplication(sys.argv)
    file = open('C:/Users/JF/Desktop/stylesheet/Geoo.qss','r')#change this for the repetory you put the 'geoo.qss' file in
    with file:
        qss = file.read()
        app.setStyleSheet(qss)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
