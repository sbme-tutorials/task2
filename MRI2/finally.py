from random import randint
import time
import sys
import math
import numpy as np
import cv2
from PIL.ImageQt import ImageQt
import pyqtgraph as pg
from PIL import ImageEnhance,Image
from qimage2ndarray import gray2qimage  
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog,QVBoxLayout,QMainWindow,QMessageBox,QInputDialog,QGraphicsView
from PyQt5.QtGui import QPixmap,QPen,QPainter,QBrush,QColor
from Final import Ui_MainWindow

class PhotoViewer(QtWidgets.QGraphicsView):
    photoClicked = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, parent):
        super(PhotoViewer, self).__init__(parent)
        self._zoom = 0
        self._empty = True
        self._scene = QtWidgets.QGraphicsScene(self)
        self._photo = QtWidgets.QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.setScene(self._scene)
        self.setFixedSize(200,200)
        self.wheelEvent = self.zoom
        #self.setSceneRect(0, 0, 400, 400)
        self.wheelEvent = self.zoom
        #self.fitInView(0,0, 400, 400, QtCore.Qt.KeepAspectRatio)

        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        self.setFrameShape(QtWidgets.QFrame.NoFrame)

    def hasPhoto(self):
        return not self._empty

    def fitInVieww(self, scale=True):
        rect = QtCore.QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            if self.hasPhoto():
                viewrect = self.viewport().rect()
                print (viewrect)
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                print(factor)
                self.scale(factor, factor)
            self._zoom = 0

    def setPhoto(self, pixmap):
        self._zoom = 0
        if pixmap :
            self._empty = False
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            self._photo.setPixmap(pixmap)
            
        else:
            self._empty = True
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self._photo.setPixmap(QPixmap())
        self.fitInVieww()

    def zoom(self, event):
        if self.hasPhoto():
            print (event.angleDelta().y())
            if event.angleDelta().y() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInVieww()
                print('hi')
            else:
                self._zoom = 0

class main(QMainWindow , Ui_MainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
    
        self.play=False
        self.check=False
        self.stop=True
        self.count=0
        self.x=0
        self.y=0
        self.layout()
         
    
    def linkedZoom(self,event):
        self.viewer.zoom(event)
        self.viewer2.zoom(event)
        self.viewer3.zoom(event)
        
        
    def layout(self):
        self.plotWindow1 = self.ui.graph_t1
        self.plotWindow2 = self.ui.graph_t2
        self.ui.browse.clicked.connect(self.button_browse)
        #strat up cycle
#        self.ui.Ernst_Angle.clicked.connect(self.Init_start_up)
        
        self.ui.image.mousePressEvent=self.getPos
        self.ui.Contrast_slider.valueChanged.connect(self.contrast_change)
        
        self.ui.comboBox.currentIndexChanged.connect(self.artifacts)
        
        
        self.ui.Brightness_slider.valueChanged.connect(self.brightness_change)
        self.ui.property_2.currentIndexChanged.connect(self.select_image)
        self.ui.Zooming_Box.currentIndexChanged.connect(self.select_Zooming)
        self.ui.Ernst_Angle.clicked.connect(self.earnest_angle)
        self.viewer = PhotoViewer(self.ui.graphicsView_phantom)
        self.viewer2 = PhotoViewer(self.ui.graphicsView_seq1)
        self.viewer3 = PhotoViewer(self.ui.graphicsView_seq2)
        self.ui.Start_seq1.clicked.connect(self.sequences)
        self.Gy=2*math.pi
        self.Start_up=True
        self.current_seq = ""
        
#        self.viewer.wheelEvent = self.linkedZoom
#        self.viewer2.wheelEvent = self.linkedZoom
        
    def button_browse(self):
       # try:
            self.size=int(self.ui.size_2.currentText())
            self.filename, _filter=QFileDialog.getOpenFileName(self,"open file"," ","Image File(*.png *.jpg *.jpeg *.bmp)")
            if self.filename:
                imagePath = self.filename
                imagePath = cv2.imread(self.filename,0)
                self.size_image=(len(imagePath))
                if (self.size==self.size_image):
                    self.plotWindow1.clear()
                    self.plotWindow2.clear()
                    self.ui.image.clear()
                    imagePath=gray2qimage(imagePath)  #b7wel el array le image
                    self.Image_in_graphic_veiw(imagePath)
                    self.show_image(imagePath)
                    self.ui.image.setToolTip("Click to select the pixel")
                    self.stop=True
                    self.count=0
                    self.check=False
                    self.Start_up=True
                    self.img_array = cv2.imread(self.filename,0)        ###????         
                    self.T1=np.zeros((self.size_image,self.size_image))
                    self.T2=np.zeros((self.size_image,self.size_image))
                    self.PD=np.copy(self.img_array)  ####???????
                    n = self.size_image
                    for i in range(n):
                        for j in range(n):
                            if(self.img_array[i,j] == 0):
                                self.T1[i,j]=900
                                self.T2[i,j]=80
                            elif (self.img_array[i,j] > 0 and self.img_array[i,j] <20):
                                 self.T1[i,j]=1000
                                 self.T2[i,j]=100    
                            elif ( self.img_array[i,j]>20 and  self.img_array[i,j]<180):
                                 self.T1[i,j]=1200
                                 self.T2[i,j]=120
                            elif ( self.img_array[i,j]>180 and  self.img_array[i,j]<255):
                                 self.T1[i,j]=1500
                                 self.T2[i,j]=150                   

                else:
                    print ("size doesn't match" )
                    QMessageBox.warning(self,"Message","size doesn't match")
#        except:
#            QMessageBox.warning(self,"Message","Chosse the size of pic")
#       # QApplication.processEvents()
                    
                    
                    
    def select_image(self):
           if (self.ui.property_2.currentText()=="T1"):
                array = (self.T1 - np.amin(self.T1)) * 255/ (np.amax(self.T1) - np.amin(self.T1))
                image_T1=gray2qimage(array) ### byh7wel el array to image
                self.show_image(image_T1)

           elif (self.ui.property_2.currentText()=="T2"): 
                array = (self.T2 - np.amin(self.T2)) * 255/ (np.amax(self.T2) - np.amin(self.T2))
                image_T2=gray2qimage(array)
                self.show_image(image_T2)
                
           elif (self.ui.property_2.currentText()=="Phantom"): 
                image_phantom=gray2qimage(self.img_array)
                self.show_image(image_phantom)
                
                
    def select_Zooming(self):
       if (self.ui.Zooming_Box.currentText()=="With Link"):
           self.viewer.wheelEvent = self.linkedZoom
           self.viewer2.wheelEvent = self.linkedZoom
           self.viewer3.wheelEvent = self.linkedZoom

       elif (self.ui.Zooming_Box.currentText()=="Without Link"):
           self.viewer.wheelEvent =self.viewer.zoom
           self.viewer2.wheelEvent =self.viewer2.zoom
           self.viewer3.wheelEvent =self.viewer3.zoom
           
           
    def sequences(self):
        self.select_Preparetion()
        self.select_Acquisition()
           
    def select_Preparetion(self):
        if (self.ui.Preparetion_Box.currentText()=="T1 Prep (IR)"):
            self.t_null()
            self.IR()
            self.T1_preparation(self.T1)
        elif (self.ui.Preparetion_Box.currentText()=="T2  Prep"): 
            self.T2_PREP()
            self.T2_preparation(self.time,self.T1)
        elif (self.ui.Preparetion_Box.currentText()=="Tagging Prep"): 
            self.Tagging()
            self.tagging()
            
    def select_Acquisition(self):
        if (self.ui.Acquisition_Box.currentText()=="GRE"):
            self.flipAngle()
            self.gre()
            self.GRE()
        elif (self.ui.Acquisition_Box.currentText()=="SSFP"): 
            self.flipAngle()
            self.ssfp()
            self.SSFP()
        elif (self.ui.Acquisition_Box.currentText()=="SE"): 
            self.SE()
            self.spin_Echo()
        
            
    
    def Image_in_graphic_veiw(self,image):
        self.viewer.setPhoto(QPixmap(image)) 
        
        
    def adjust_brightness(self,input_image, factor):
        image = Image.open(input_image).convert('L')
        enhancer_object = ImageEnhance.Brightness(image)
        out = enhancer_object.enhance(factor)
        out.save("hi2.png")
        self.show_image("hi2.png")
        
    def adjust_contrast(self,input_image, factor):
        image = Image.open(input_image).convert('L')
        enhancer_object = ImageEnhance.Contrast(image)
        out = enhancer_object.enhance(factor)
        out.save("hi.png")
        self.show_image("hi.png")

    def show_image(self,image):
        self.result = QPixmap(image)#piexel of image
        result=self.result.scaled(int(self.ui.image.height()), int(self.ui.image.width()),QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation) #scale 3la elabel
        self.ui.image.setPixmap(result) #label ya5od el sora w yezherha
        
    def contrast_change(self):
        self.contrast_value = self.ui.Contrast_slider.value()
        self.adjust_contrast(self.filename,self.contrast_value)
        
        
    def brightness_change(self):
        self.brightness_value = self.ui.Brightness_slider.value()
        self.adjust_brightness(self.filename,self.brightness_value)
    
    def getPos(self,event) :
        if (self.count==5):
            self.check=False
            print("done")
        else:
            print (int (self.ui.image.height()))
            self.x=math.floor((event.pos().x()*self.size)/self.ui.image.frameGeometry().width())
            print (self.x)
            self.y=math.floor((event.pos().y()*self.size)/self.ui.image.frameGeometry().height())
            print(self.y)
            try:
                
                self.flip_angle=self.flipangle
                self.time_spin=int(self.ui.spin_Edit.text())
                self.TR=int(self.ui.TR_Edit.text())
                self.TE=int(self.ui.TE_Edit.text())
                self.check=True
                self.draw(self.T1,self.T2,self.x,self.y)
            except:
                QMessageBox.warning(self,"Message","Enter the flip angle, spin time, TR and TE")
                
    def draw(self,t1,t2,x,y):
        arr1 = [] 
        arr2 = []
        
        
        while (self.check):
#            self.TR=int(self.ui.TR_Edit.text())
#            self.TE=int(self.ui.TE_Edit.text())
            for self.t in range(self.time_spin):
                theta=np.radians(self.flip_angle)          
                M0=([[0],[0],[1]])
                Flip=([[np.cos(theta),0,np.sin(theta)],[0,1,0],[-np.sin(theta),0,np.cos(theta)]])         
                Decay=([[np.exp(-self.t/self.T2[self.x,self.y]),0,0],[0,np.exp(-self.t/self.T2[self.x,self.y]),0],[0,0,np.exp(-self.t/self.T1[self.x,self.y])]])
                M_Recovery=([[0],[0],[1-np.exp(-self.t/self.T1[self.x,self.y])]])
                out1=(np.dot(Decay,Flip))
                out2=np.dot(out1,M0)
                self.MX,self.MY,self.MZ=out2+M_Recovery
                arr1.extend(self.MX)  #decay time         #extend >>merge between array
                arr2.extend(self.MZ)  #recovery time

            if (self.count==0):
                self.plotWindow1.plot(arr1, pen='r')
                self.plotWindow2.plot(arr2, pen='r')

            elif (self.count==1):
                self.plotWindow1.plot(arr1, pen='b')
                self.plotWindow2.plot(arr2, pen='b')

            elif (self.count==2):
                self.plotWindow1.plot(arr1, pen='g')
                self.plotWindow2.plot(arr2, pen='g')


            elif (self.count==3):
                self.plotWindow1.plot(arr1, pen='r')
                self.plotWindow2.plot(arr2, pen='r')

            else:
                  self.plotWindow1.plot(arr1, pen='b')
                  self.plotWindow2.plot(arr2, pen='b') 

            self.plotWindow1.plot([self.TE,self.TE],(1,0), pen='g')
            self.plotWindow1.plot([self.TR,self.TR],(1,0), pen='r')
            self.plotWindow2.plot([self.TR,self.TR],(1,0), pen='r')
            self.plotWindow2.plot([self.TE,self.TE],(1,0), pen='g')
            self.check=False     ## da ely hy5rgny mn el loop bta3t el loop
            self.count=self.count+1
            QApplication.processEvents()
            self.frame()
    

    def flipAngle(self):
        self.flipangle,ok=QInputDialog.getInt(self,"integer input dialog","enter a theta")
        
        
        
    def t_null(self):
        self.tnull,ok=QInputDialog.getInt(self,"integer input dialog","enter T NULL")
           
            
    def frame(self):
        QApplication.processEvents()
        self.painterInstance = QPainter(self.result)   #b3mel opject
        self.painterInstance.begin(self)  
        self.penRectangle =QPen(QtCore.Qt.red)  #yehdd el elon
        self.penRectangle.setWidth(1)
        self.penPoint =QPen(QtCore.Qt.blue)
        self.penPoint.setWidth(1)  #
        self.painterInstance.setPen(self.penPoint)  #apply el lon
        self.painterInstance.drawRect(self.x,self.y,1,1)
        self.painterInstance.setPen(self.penRectangle)
        self.painterInstance.drawRect(self.x-5,self.y-5,10,10)
        self.painterInstance.end()
        result=self.result.scaled(int(self.ui.image.height()), int(self.ui.image.width()),QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation) #scale 3la elabel
        self.ui.image.setPixmap(result)
        self.painterInstance.end()
        QApplication.processEvents()
        
#    def Init_start_up(self):
#        self.Start_up=True
#        QMessageBox.about(self,"Message","Applying start up cycle")
#        self.select_Acquisition()
#        
        
        
    
     


    def recovery_equation(self,phantom,TR,T1):
       
        phantom[2][0]=np.exp(-TR/T1)*phantom[2][0]+(1-np.exp(-TR/T1))
        return phantom 


    def earnest_angle(self):
     
       
        self.lb = QGraphicsView()
        self.lb=pg.PlotWidget()
        phantom=[[0],[0],[1]]
        step=1
        intenisty=np.zeros(int(180/step))
        j=0
        for theta in range(0,180,step):
            for i in range(10):
                phantom=self.rotate(np.radians(theta),phantom)
                phantom=self.decay(phantom,100,50)
                
                phantom=self.recovery_equation(phantom,100,2000)
                x=phantom[0][0]
                y=phantom[1][0]
            intenisty[j]=math.sqrt((x*x)+(y*y))
            j=j+1
        array=np.arange(0,180,step)
        
        self.lb.plot(array,intenisty)
        self.lb.show()    
    
    def T2_preparation(self,Tw,T1):
        row=self.size_image
        col=self.size_image
        self.phantom = self.createPhantom(row,col)
        self.phantom=self.RF_rotate(90,self.phantom,row,col)
        self.phantom=self.recovery(self.phantom,row,col,Tw,T1)
        self.phantom=self.RF_rotate(-90,self.phantom,row,col)
        
    
    def T1_preparation(self,T1):
        Tnull = self.tnull
        row=self.size_image
        col=self.size_image
        self.phantom = self.createPhantom(row,col)
        theta=np.radians(180)
        T=np.log(2)*Tnull
        self.phantom=self.RF_rotate(theta,self.phantom,row,col)
        self.phantom=self.recovery(self.phantom,row,col,T,T1)
        
    
    
    def RF_rotate(self,theta,phantom,row,col):
        for i in range(row):
            for j in range(col):
                phantom[i,j,:]=self.rotate(theta,phantom[i,j,:])
                
        return phantom    
    
    
    def rotate(self,theta,phantom):
        RF=([[np.cos(theta),0,np.sin(theta)],[0,1,0],[-np.sin(theta),0,np.cos(theta)]]) 
        phantom=np.dot(RF,phantom) 
        return phantom
    
        
    def decay(self,phantom,TE,T2):
        dec=np.exp(-TE/T2)
        phantom=np.dot(dec,phantom)
        return phantom
    
   
    def rotate_decay(self,phantom,theta,TE,T2,row,col):
        for i in range(row): 
            for j in range(col):
                phantom[i,j,:]=self.rotate(theta,phantom[i,j,:]) 
                phantom[i,j,:]=self.decay(phantom[i,j,:],TE,T2[i,j]) 
        return phantom    
        
    def tagging(self):
        
        row=self.size_image
        col=self.size_image
        self.phantom = self.createPhantom(row,col)
        for i in range(row):
            for c in range(col):
                theta=(i*math.pi)/row
                sinangle=np.sin(theta)
                self.phantom[i,c,:]=self.phantom[i,c,:]*sinangle
               
   
   
    def recovery(self,phantom,row,col,TR,T1):
        for ph_rowtr in range(row): 
            for ph_coltr in range(col):
                phantom[ph_rowtr,ph_coltr,0]=0
                phantom[ph_rowtr,ph_coltr,1]=0
                phantom[ph_rowtr,ph_coltr,2]=((phantom[ph_rowtr,ph_coltr,2])*np.exp(-TR/T1[ph_rowtr,ph_coltr]))+(1-np.exp(-TR/T1[ph_rowtr,ph_coltr]))
        return phantom 

    

    def createPhantom(self,row,col):
        phantom=np.zeros((row,col,3))
        for i in range(row):
            for j in range(col):
                phantom[i,j,2]=1
        return phantom
    

    def startup_cycle(self,phantom,theta,TE,TR,T2,T1,row,col,n):

        for r in range(n):  #rows
            
            phantom=self.rotate_decay(phantom,theta,TE,T2,row,col)
              
            phantom=self.recovery(phantom,row,col,TR,T1)  
        return phantom

    def SSFP(self):
    
        self.flip_angle=self.flipangle
        row=self.size_image
        col=self.size_image
        theta=np.radians(self.flip_angle) 
        TE=int(self.ui.TE_Edit.text())
        TR=int(self.ui.TR_Edit.text())
        Kspace_ssfp=np.zeros((self.img_array.shape[0],self.img_array.shape[1]),dtype=np.complex_) 
        
        if (self.Start_up==True):
            self.phantom=self.startup_cycle(self.phantom,theta/2,TE,TR,self.T2,self.T1,row,col,15)
        
        self.phantom=self.rotate_decay(self.phantom,theta/2,TE,self.T2,row,col)
        for ph_rowtr in range(row): 
            for ph_coltr in range(col):

                self.phantom[ph_rowtr,ph_coltr,2]=((self.phantom[ph_rowtr,ph_coltr,2])*np.exp(-TR/self.T1[ph_rowtr,ph_coltr]))+(1-np.exp(-TR/self.T1[ph_rowtr,ph_coltr]))
        #phantom=self.startup_cycle(phantom,theta,TE,TR,self.T2,self.T1,row,col,15)
        
        for r in range(Kspace_ssfp.shape[0]):  #rows
            self.phantom=self.rotate_decay(self.phantom,theta,TE,self.T2,row,col)
            for c in range(Kspace_ssfp.shape[1]):
                Gx_step=((2*math.pi)/row)*r
                Gy_step=(self.Gy/col)*c
                for ph_row in range(row): 
                    for ph_col in range(col):
                        Toltal_theta=(Gx_step*ph_row)+(Gy_step*ph_col)
                        Mag=math.sqrt(((self.phantom[ph_row,ph_col,0])*(self.phantom[ph_row,ph_col,0]))+((self.phantom[ph_row,ph_col,1])*(self.phantom[ph_row,ph_col,1])))

                        Kspace_ssfp[r,c]=Kspace_ssfp[r,c]+(Mag*np.exp(-1j*Toltal_theta))
                        QApplication.processEvents()

                QApplication.processEvents()
            theta=-theta  
            print(theta)
            for ph_rowtr in range(row): 
                for ph_coltr in range(col):
                    self.phantom[ph_rowtr,ph_coltr,2]=((self.phantom[ph_rowtr,ph_coltr,2])*np.exp(-TR/self.T1[ph_rowtr,ph_coltr]))+(1-np.exp(-TR/self.T1[ph_rowtr,ph_coltr]))  
            
            QApplication.processEvents()
        iff= np.fft.ifft2(Kspace_ssfp)

        #print(iff)
        inverse_array=np.abs(iff)
        inverse_array = (inverse_array - np.amin(inverse_array)) * 255/ (np.amax(inverse_array) - np.amin(inverse_array))
        inverse_img=gray2qimage(inverse_array)
        imgreconstruction = QPixmap(inverse_img)#piexel of image
        self.viewer2.setPhoto(QPixmap(imgreconstruction))    
    def Aliasing_artifact(self):
        self.Gy=np.radians(540)
        
    def spin_Echo(self):
        
        row=self.size_image
        col=self.size_image
        theta=np.radians(90) 
        TE=int(self.ui.TE_Edit.text())
        TR=int(self.ui.TR_Edit.text())
        Kspace_SE=np.zeros((self.img_array.shape[0],self.img_array.shape[1]),dtype=np.complex_)
        if (self.Start_up==True):
            self.phantom=self.startup_cycle(self.phantom,theta,TE,TR,self.T2,self.T1,row,col,15)

        for r in range(Kspace_SE.shape[0]):  #rows
            self.phantom=self.rotate_decay(self.phantom,np.radians(90),TE/2,self.T2,row,col)
            self.phantom=self.recovery(self.phantom,row,col,TE/2,self.T1)
            self.phantom=self.rotate_decay(self.phantom,np.radians(180),TE/2,self.T2,row,col)
            for c in range(Kspace_SE.shape[1]):
  
                Gx_step=((2*math.pi)/row)*r
                Gy_step=(self.Gy/col)*c
                for ph_row in range(row): 
                    for ph_col in range(col):
                        Toltal_theta=(Gx_step*ph_row)+(Gy_step*ph_col)
                        Mag=math.sqrt(((self.phantom[ph_row,ph_col,0])*(self.phantom[ph_row,ph_col,0]))+((self.phantom[ph_row,ph_col,1])*(self.phantom[ph_row,ph_col,1])))
                        
                        
                        Kspace_SE[r,c]=Kspace_SE[r,c]+(Mag*np.exp(-1j*Toltal_theta))
                        QApplication.processEvents()
                       
                QApplication.processEvents()
                
            self.phantom=self.recovery(self.phantom,row,col,TR,self.T1)  
            
            QApplication.processEvents()
           
        
        iff= np.fft.ifft2(Kspace_SE)

        inverse_array=np.abs(iff)
        inverse_array = (inverse_array - np.amin(inverse_array)) * 255/ (np.amax(inverse_array) - np.amin(inverse_array))
        inverse_img=gray2qimage(inverse_array)
        imgreconstruction = QPixmap(inverse_img)#piexel of image
        
        self.viewer2.setPhoto(QPixmap(imgreconstruction))
    


    def artifacts(self):
        if(self.ui.comboBox.currentText()=="Bluring"):
            self.Start_up=False
            self.sequences()
        if(self.ui.comboBox.currentText()=="Alaising"):
            self.Gy=np.radians(540)
            self.sequences()
            
            
    
    
    
    def GRE(self):
        self.flip_angle=self.flipangle
        row=self.size_image
        col=self.size_image
        theta=np.radians(self.flip_angle) 
        TE=int(self.ui.TE_Edit.text())
        TR=int(self.ui.TR_Edit.text())
        Kspace=np.zeros((self.img_array.shape[0],self.img_array.shape[1]),dtype=np.complex_) 
        
        if (self.Start_up==True):
            self.phantom=self.startup_cycle(self.phantom,theta,TE,TR,self.T2,self.T1,row,col,15)

        
        for r in range(Kspace.shape[0]):  #rows
            self.phantom=self.rotate_decay(self.phantom,theta,TE,self.T2,row,col)
            
            for c in range(Kspace.shape[1]): #columns
                Gx_step=((2*math.pi)/row)*r
                Gy_step=((self.Gy)/col)*c
                for ph_row in range(row): 
                    for ph_col in range(col):
                        Toltal_theta=(Gx_step*ph_row)+(Gy_step*ph_col)
                        Mag=math.sqrt(((self.phantom[ph_row,ph_col,0])*(self.phantom[ph_row,ph_col,0]))+((self.phantom[ph_row,ph_col,1])*(self.phantom[ph_row,ph_col,1])))

                        Kspace[r,c]=Kspace[r,c]+(Mag*np.exp(-1j*Toltal_theta))
                        QApplication.processEvents()
                QApplication.processEvents()
            self.phantom=self.recovery(self.phantom,row,col,TR,self.T1)        
            QApplication.processEvents()
        
        iff= np.fft.ifft2(Kspace)
        
        inverse_array=np.abs(iff)
        inverse_array = (inverse_array - np.amin(inverse_array)) * 255/ (np.amax(inverse_array) - np.amin(inverse_array))
        inverse_img=gray2qimage(inverse_array)
        imgreconstruction = QPixmap(inverse_img)#piexel of image
        self.viewer2.setPhoto(QPixmap(imgreconstruction)) 

        
        
        
    def IR (self):
        self.ui.GV_prep.clear() 
        tx=np.arange(0,200,.001)
        T3=(np.sin(1.5*(tx-10))/(tx-10))
        self.ui.GV_prep.plot(tx,T3,pen = 'r')
        #self.ui.lbl_prep.setText("Prepration:IR")
        

    def gre (self):
        #self.AQUA=self.GRE
        self.te=int(self.ui.TE_Edit.text())
        self.tr=int(self.ui.TR_Edit.text())
        self.f=self.flipangle
        
        te = round(self.te/3)
        self.ui.GV_aqua.clear()
        tx=np.arange(0,self.tr)
        Rf=(np.sin(((self.f*2)/180)*(tx-te))/(tx-te)+10)
        Gx = self.RectangularGraph(self.tr,8,(te*2),1,te)
        Gy = self.RectangularGraph(self.tr,6,(te*3),1,te)
        Readout = self.RectangularGraph(self.tr,4,(te*4),1,te)
        
        self.ui.GV_aqua.plot(tx,Rf,pen = [255,0,0])
        self.ui.GV_aqua.plot(tx,Gx,pen = [255,0,0])
        self.ui.GV_aqua.plot(tx,Gy,pen = [255,0,0])
        self.ui.GV_aqua.plot(tx,Readout,pen = [255,0,0])

        
    def Tagging(self):
        self.ui.GV_aqua.clear() 
        tx=np.arange(0,15,.001)
        T3=(0.5*np.sin(2*tx))  #RF 180 shifted 2
        self.ui.GV_prep.plot(tx,T3,pen = [255,0,0])

    def T2_PREP (self):
        self.ui.GV_prep.clear() 
        self.time , ok = QInputDialog.getInt(self,"T_Dialog", "Enter the Required time")
        tx=np.arange(0,70,.001)
        T1=(np.sin((tx-10))/(tx-10))
        T2=(np.sin(-(tx-self.time))/(tx-self.time))
        self.ui.GV_prep.plot(tx,T1,pen = 'r')
        self.ui.GV_prep.plot(tx,T2,pen = 'r')

        #self.ui.lbl_prep.setText("Prepration:T2_PREP")





    def SE (self):

        self.te=int(self.ui.TE_Edit.text())
        self.tr=int(self.ui.TR_Edit.text())
        self.f=self.flipangle
        self.ui.GV_aqua.clear()
        tx=np.arange(0,self.tr)
        te = round(self.te/3)
        

        Rf1=(np.sin(((self.f*2)/180)*(tx-te))/(tx-te)+10)
        Rf2=(2*np.sin(((self.f*2)/180)*(tx-(te*2)))/(tx-(te*2))+10)

        Gx = self.RectangularGraph(self.tr,8,(te*3),1,te)
        Gy = self.RectangularGraph(self.tr,6,(te*4),1,te)
        Readout = self.RectangularGraph(self.tr,4,(te*5),1,te)
        
        self.ui.GV_aqua.plot(tx,Rf1,pen = [255,0,0])
        self.ui.GV_aqua.plot(tx,Rf2,pen = [255,0,0])

        self.ui.GV_aqua.plot(tx,Gx,pen = [255,0,0])
        self.ui.GV_aqua.plot(tx,Gy,pen = [255,0,0])
        self.ui.GV_aqua.plot(tx,Readout,pen = [255,0,0])



    def ssfp (self):
        self.te=int(self.ui.TE_Edit.text())
        self.tr=int(self.ui.TR_Edit.text())
        self.f=self.flipangle
        te = round(self.te/3)
        self.ui.GV_aqua.clear()
        tx=np.arange(0,self.tr)
        Rf=(np.sin(((self.f*2)/180)*(tx-te))/(tx-te)+10)
        Gx = self.RectangularGraph(self.tr,8,(te*2),1,te)
        Gy = self.RectangularGraph(self.tr,6,(te*3),1,te)
        Readout = self.RectangularGraph(self.tr,4,(te*4),1,te)
        GxReversed = self.RectangularGraph(self.tr,8,(te*5+30),-1,te)
        GyReversed = self.RectangularGraph(self.tr,6,(te*5+30),-1,te)

        self.ui.GV_aqua.plot(tx,Rf,pen = [255,0,0])
        self.ui.GV_aqua.plot(tx,Gx,pen = [255,0,0])
        self.ui.GV_aqua.plot(tx,Gy,pen = [255,0,0])
        self.ui.GV_aqua.plot(tx,Readout,pen = [255,0,0])
        self.ui.GV_aqua.plot(tx,GxReversed,pen = [255,0,0])
        self.ui.GV_aqua.plot(tx,GyReversed,pen = [255,0,0])


 
        
        
    def RectangularGraph(self,tR,shiftDown,shiftRight,step,width):
        z = []
        
        for i in range (0,tR):
            if i < int(shiftRight):
                z.append(shiftDown) 
            elif i >= int(shiftRight) and i < int(width+shiftRight):
                z.append(shiftDown+(step*1)) 
            else:
                z.append(shiftDown) 
        return z

        
app= QApplication(sys.argv)
window = main()
window.show()

sys.exit(app.exec_()) 