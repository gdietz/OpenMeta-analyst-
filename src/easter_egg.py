from PyQt4.Qt import QDialog
import forms.ui_tom_form

class TomDialog(QDialog, forms.ui_tom_form.Ui_Dialog):
    def __init__(self, parent=None):
        super(TomDialog, self).__init__(parent)
        self.setupUi(self)
        
#class PersonDialog(QDialog, forms.ui_tom_form.Ui_Dialog):
#    def __init__(self, parent=None, person="tom"):
#        super(PersonDialog, self).__init__(parent)
#        self.setupUi(self)
#        
#        personPixmap = 
#        
#        self.label.setPixmap
    
    
    
    
    