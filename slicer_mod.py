from __main__ import vtk, qt, ctk, slicer

#root module layout - layout
#ctk collapsible button - for hiding menu
#qformlayout - new layout within menu
#qframe - holds elements
#qMRMLNodecombobox Qlabel Qpushbutton Qtextedit

class slicer_mod:
    def __init__(self,parent):
        parent.title = "slicer mod"
        parent.categories= [""]
        parent.dependencies=[]
        self.parent = parent


class slicer_modWidget:
    def __init__(self,parent=None):
        if not parent:
            self.parent= slicer.qMRMLWidget()
            self.parent.setLayout(qt.QVBoxLayout())
            self.parent.setMRMLScene(slicer.mrmlScene)
        else:
            self.parent=parent
        self.layout=self.parent.layout()
        if not parent:
            self.setup()
            self.parent.show()
    
    def setup(self):
        #create collapsible button
        collapsible_button = ctk.ctkcollapsible_button()
        collapsible_button.text= "collapsible menu"
        #bind to root layout
        self.layout.addWidget(collapsible_button)

        #new layout
        self.form.Layout= qt.QFormLayout(collapsible_button)

        #volume selector
        self.formFrame= qt.QFrame(collapsible_button)
        #set the layout to horizontal
        self.formFrame.setLayout(qt.QHBoxLayout())
        #bind new frame to existing layout in cm
        self.formLayout.addWidget(self.formFrame)

        #create new volume selector
        self.inputSelector= qt.QLabel("Input Volume: ", self.formFrame)
        self.fromFrame.layout().addWidget(self.inputSelector)



        #
        self.inputSelector= slicer.qMRMLNodeComboBox(self.formFrame)
        self.inputSelector.nodeTypes=(("vtkMRMLScalarVolumeNode"), "")
        self.inputSelector.addEnabled=False
        self.inputSelector.removeEnabled=False


        #bind current volume selector to current slicer scene
        self.inputSelector.setMRMLScene(slicer.mrmlScene)

        #bind input selector to frame
        self.formFrame.layout().addWidget(self.inputSelector)

        #button
        button = qt.QPushButton("Get Path")
        button.toolTip= "Displays the path of the selected volume"
        button.connect("clicked(bool)", self.informationButtonClicked)
        #bind button to frame
        self.formFrame.layout().addWidget(button)

        #a textfield
        self.textfield= qt.QTextEdit()
        self.textfield.setReadOnly(True)
        
        #bind textfield to frame
        self.formFrame.layout().addWidget(self.textfield)
    

    #return the string name of the current selected node from volume selector
    def informationButtonClicked(self):
        n = slicer.util.getNode(self.inputSelector.currentNode().GetName())
        nSN= n.GetStorageNode()
        path= nSN.GetFileName()
        self.textfield.insertPlainText(path)




