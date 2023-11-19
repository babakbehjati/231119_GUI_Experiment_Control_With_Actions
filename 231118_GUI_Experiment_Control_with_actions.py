#PythonQT GUI for Thorlabs Kinesis Translation Stage, Nano Positioner Piezosystem Jena, Teledyne Photometric Camera Camera
#GUI Only
# IAP - Nano Physics and Quantum Photonics
# Last time edited 20.11.2023 by Babak Behjati #_________________________________________________________________________________________________________________________________


# First Part of Program ---->  UI



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont

#_________import pyLabLib libraries

import pylablib as pll
from pylablib.devices import Thorlabs
import numpy as np
#________________________



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Microscope Experiment Control GUI')
        self.setGeometry(800, 800, 1400, 1200)                           # Windows Dimensions
        #self.setStyleSheet("background-color:  #DDDDDD;")              # Background Color  

#------------------------------
#Input Fields

        self.move_x_to_pos_int = int(0)
        self.move_x_to_pos = QLineEdit()
        self.move_y_to_pos_int = int(0)
        self.move_y_to_pos = QLineEdit()
        self.exposure_time = QLineEdit()
        self.camera_att_2 = QLineEdit()
        self.camera_att_3 = QLineEdit()
        self.aux_field = QLineEdit()
        self.stage_x = Thorlabs.KinesisMotor("27256282")
        self.stage_y = Thorlabs.KinesisMotor("27256259")


        
        
#------------------------------        
#Console Initiation        

        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.console.append("_______________________________________________________")
        self.console.append("Institute for Applied Physics - Nano Physics and Quantum Photonics")
        self.console.append("https://www.nano.uni-bonn.de/")    
        self.console.append("-------------------------------------------------------")    
        self.console.append("Welcome to  Experiment UI Control ...")
        self.console.append("                     ")
        self.console.append("----------------")
        
#------------------------------
#Buttons

        self.btn1 = QPushButton('Connect µ Stages')
        self.btn1.setStyleSheet("background-color: #C5E3E7")
        self.btn1.clicked.connect(self.connect_micro_stages)      #Connects button to action in function section

        self.btn2 = QPushButton('Connect Piezos')
        self.btn2.setStyleSheet("background-color: #C5E3E7")
        self.btn2.clicked.connect(self.connect_piezos)

        self.btn3 = QPushButton('Connect Camera')
        self.btn3.setStyleSheet("background-color: #C5E3E7")
        self.btn3.clicked.connect(self.connect_camera)
        
        self.btn4 = QPushButton('Home All Stages')
        self.btn4.setStyleSheet("background-color: #C5E3E7")
        self.btn4.clicked.connect(self.home_all_stages)
        
        
        self.btn5 = QPushButton('Set Position Reference')
        self.btn5.setStyleSheet("background-color: #C5E3E7")
        self.btn5.clicked.connect(self.set_position_ref)
        
        
        self.btn6 = QPushButton('Get Current Position')
        self.btn6.setStyleSheet("background-color: #C5E3E7")
        self.btn6.clicked.connect(self.get_current_pos)

        self.btn7 = QPushButton('Capture')
        self.btn7.setStyleSheet("background-color: #ff8279")
        self.btn7.clicked.connect(self.camera_capture)

        self.btn8 = QPushButton('Start Grid Scan')
        self.btn8.setStyleSheet("background-color: #FFC100")
        self.btn8.clicked.connect(self.start_grid_scan)

        self.btn9 = QPushButton('aux_button')
        self.btn9.setStyleSheet("background-color:  #C5E3E7")
        self.btn9.clicked.connect(self.aux_button)

        self.btn10 = QPushButton('Clear Console')
        self.btn10.setStyleSheet("background-color: #C5E3E7")
        self.btn10.clicked.connect(self.clearConsole)

        self.btn11 = QPushButton('Exit')
        self.btn11.setStyleSheet("background-color: #f5ccd2")
        self.btn11.clicked.connect(self.close)
        
        self.btn12 = QPushButton("Move Stage X")
        self.btn12.setStyleSheet("background-color: #C5E3E7")
        self.btn12.clicked.connect(self.move_stage_x_to)
        
        self.Casting()
        
        
        
        self.btn13 =  QPushButton("Move Stage Y")
        self.btn13.setStyleSheet("background-color: #C5E3E7")
        self.btn13.clicked.connect(self.move_stage_y_to) 
        
        self.btn14 =  QPushButton("Clear Fields")     
        self.btn14.setStyleSheet("background-color: #C5E3E7")
        self.btn14.clicked.connect(self.clearInputs) 

#------------------------------
#Layout
        
        input_layout = QVBoxLayout()
        input_layout.addWidget(QLabel('Move Stage X to :'))
        input_layout.addWidget(self.move_x_to_pos)
        input_layout.addWidget(QLabel('Move Stage Y to'))
        input_layout.addWidget(self.move_y_to_pos)
        input_layout.addWidget(QLabel('Camera attr. 2'))
        input_layout.addWidget(self.camera_att_2)
        input_layout.addWidget(QLabel('Camera attr. 3'))
        input_layout.addWidget(self.camera_att_3)
        input_layout.addWidget(QLabel('aux_field:'))
        input_layout.addWidget(self.aux_field)
        input_layout.addWidget(QLabel('Exposure Time:'))
        input_layout.addWidget(self.exposure_time)
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.btn1)               # Order of Buttons in Windows
        button_layout.addWidget(self.btn2)
        button_layout.addWidget(self.btn3)
        button_layout.addWidget(self.btn4)
        button_layout.addWidget(self.btn5)
        button_layout.addWidget(self.btn6)
        button_layout.addWidget(self.btn12)
        button_layout.addWidget(self.btn13)
        button_layout.addWidget(self.btn7)
        button_layout.addWidget(self.btn8)
        button_layout.addWidget(self.btn9)
        button_layout.addWidget(self.btn14)
        button_layout.addWidget(self.btn10)
        button_layout.addWidget(self.btn11)

        layout = QHBoxLayout()                          # Type of Layout
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addWidget(self.console)
        self.console.setStyleSheet("background-color: #cbe3f4")

        self.setLayout(main_layout)

    #------------------------------
    
    #     End of UI
    
    
    
    # Actions 
    def Casting(self):
        #self.move_x_to_pos_int = int(str(self.move_x_to_pos))
        self.move_y_to_pos_int = +self.move_y_to_pos
            
    
    def Connect_Stages(self):
        Thorlabs.list_kinesis_devices()
        self.console.append("Serial Ports :  ")  
        self.console.append(pll.list_backend_resources("serial"))
        pll.list_backend_resources("Serial number of stages:")  
        Thorlabs.list_kinesis_devices()           
        self.console.append(Thorlabs.list_kinesis_devices())
        
    def connect_micro_stages(self):
        Thorlabs.list_kinesis_devices()
        self.console.append("Detected Serial Ports on PC :  ") 
        self.console.append("       ") 
        self.console.append(str(pll.list_backend_resources("serial")))
        self.console.append("       ") 
        self.console.append("   Stage x ------------>  Serial# : '27256282'    " )
        self.console.append("   Number  of channels :")
        self.console.append(str(self.stage_x.get_number_of_channels() )) 
        self.console.append(" Stage y ------------>  Serial# : '27256259'  ")
        self.console.append("   Number of channels :") 
        self.console.append(str(self.stage_y.get_number_of_channels() ) )
        self.console.append("       ")
        self.console.append("  Stages are Connected!     ")
         
        return
        
     
    def connect_piezos(self):
        self.console.append("Piezo stage is on the way :)  Please wait 20 more weeks...")
        #self.console.append("serial and port address")
        return
    
    def connect_camera(self):
        self.console.append("Feature is not available at the moment. Try again next week... :)) :")
        #self.console.append("serial and port address")
        return 
    
    def home_all_stages(self):
        self.console.append("   Homing in Progress... ")
        self.console.append("       ") 
        self.stage_x.home(sync=True, force=True, channel=1, timeout=None)
        self.stage_x.wait_for_home(channel=1, timeout=5)
        self.console.append("   Stage x is homing...")
        self.console.append("       ") 
        self.stage_x.close()
        self.console.append("   Stage y is homing...")
        self.console.append("       ") 
        self.stage_y.home(sync=True, force=True, channel=1, timeout=None)
        self.stage_y.wait_for_home(channel=1, timeout=5)
        self.stage_y.close()
        self.console.append("   Homing finished successfully ! ")
        return
    
    def move_stage_x_to(self):
        self.console.append("Stage x current position :")
        self.console.append(str(self.stage_x.get_position(channel = None, scale = True)))
        self.console.append("Stage x moving is in progress...")
        self.stage_x.move_to(position =  self.move_x_to_pos_int , channel = 1, scale = True)
        self.stage_x.wait_move(channel=None, timeout=None)
        self.console.append("Stage x final position :")
        self.console.append(str(self.stage_x.get_position(channel = 1, scale = True)))
        self.stage_x.close()
        
        
    
    
    def move_stage_y_to(self):
        #move_y_input =  self.move_y_to_pos.text()
        #self.console.append(move_y_input)
        self.console.append("       ") 
        self.console.append("Stage y current position :")
        self.console.append("       ") 
        self.console.append(str(self.stage_y.get_position(channel = None, scale = True)))
        self.console.append("Stage y moving is in progress...")
        self.stage_y.move_to(position = self.move_y_to_pos_int  , channel = 1, scale = True)
        self.stage_y.wait_move(channel=None, timeout=None)
        self.console.append("       ") 
        self.console.append("Stage y final position :")
        self.console.append(str(self.stage_y.get_position(channel = 1, scale = True)))
        self.stage_y.close()
        #move_x_input =  self.move_x_to_pos.text()
        aux_field = self.aux_field.text()
        self.console.append(aux_field)
        #stage_x.move_to(position = move_x_input , scale = True)
    
         
    def set_position_ref(self):
        self.console.append("position stage x before reset to 0 :")
        self.console.append(str(self.stage_x.get_position(channel = 1, scale = True)))
        self.console.append("Setting stage x position to 0...")
        self.stage_x.set_position_reference(position=0, channel = 1, scale=True)
        self.console.append(" Done!  ")
        self.stage_x.close()   
        self.console.append("   ")
        self.console.append("position stage y before setting position reference :")
        self.console.append(str(self.stage_y.get_position(channel = 1, scale = True)))
        self.console.append("Setting stage y position to 0...")
        self.stage_y.set_position_reference(position=0, channel = 1, scale=True)
        self.console.append(" Done!  ")
        self.stage_y.close()
        self.console.append("Stage y position after setting reference :")
        self.console.append(self.stage_y.get_position(channel = 1, scale = True)) 
        
    def get_current_pos(self):
        self.console.append("Aquiring Positions...")
        self.console.append("Stage x current position :")
        self.console.append(str(self.stage_x.get_position(channel = 1, scale = True)))
        self.console.append("Stage y current position :")
        self.console.append(str(self.stage_y.get_position(channel = 1, scale = True)))
        self.console.append("   ")
        return
    
    def camera_capture(self):
        exposure_time =  self.exposure_time.text()
        camera_att_2 = self.camera_att_2.text()
        camera_att_3 = self.camera_att_3.text()
        self.console.append(exposure_time)
        self.console.append(camera_att_2)
        self.console.append(camera_att_3)     
        self.console.append("Captured!")
        self.console.append("Saved to : "   "")
        
    
    def start_grid_scan(self):
        self.console.append("Captured!")
        self.console.append("Saved to : "   "")
        
    def aux_button(self):
        self.console.append("I'm the extra button, define some actions in me :)")
        self.console.append("...")
          
    def clearInputs(self):
        self.move_x_to_pos.clear()
        self.move_y_to_pos.clear()
        self.exposure_time.clear()
        self.camera_att_2.clear()
        self.camera_att_3.clear()
        self.aux_field.clear()
        

    def clearConsole(self):
        self.console.clear()
        self.console.append("_______________________________________________________")
        self.console.append("Institute for Applied Physics - Nano Physics and Quantum Photonics")
        self.console.append("https://www.nano.uni-bonn.de/")    
        self.console.append("-------------------------------------------------------")    
        self.console.append("Welcome to  Experiment UI Control ...")
        self.console.append("                     ")
        self.console.append("----------------")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())