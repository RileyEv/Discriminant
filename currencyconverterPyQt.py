import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from currencyconverterclass import *


class mainWindow(QMainWindow):
    '''this class creates a main window to run the main program'''
    def __init__(self):
        super().__init__()
        self.currency_class = Currency()
        self.setWindowTitle('Currency Convertor')
        self.create_main_window_layout()
        self.create_convert_currencies_layout()
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.view_main_layout)
        self.stacked_layout.addWidget(self.view_convert_layout)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
    # create main window method
    def create_main_window_layout(self):
        #this is the main layout of the window
        self.title_text = QLabel('Discriminant')
        self.difficulty_label = QLabel('Difficulty')
		self.start_button = QPushButton('Start')
        self.close_button = QPushButton('Close')
        self.difficulty_combobox = QComboBox()
        Dificulties = ['Easy','Medium','Hard','God']
        for eachDiff in Dificulties:
            self.difficulty_combobox.addItem(eachDiff)
        self.main_window_grid = QGridLayout()
        self.start_inline_grid = QGridLayout()
                    ####--- internal layout for main window ---####

                    #############################
                    #             #             #
                    #     0,0     #     0,1     #
                    #  Difficulty #  Dificulty  #
                    #     Label   #  ComboBox   #
                    #             #             #
                    #############################
                    #             #             #
                    #     1,0     #     1,1     #
                    #    Start    #    Close    #
                    #   Button    #    Button   #
                    #############################
                    
        self.start_inline_grid.addWidget(self.difficulty_label,0,0)
        self.start_inline_grid.addWidget(self.start_button,1,0)
        self.start_inline_grid.addWidget(self.difficulty_combobox,0,1)
        self.start_inline_grid.addWidget(self.close_button,1,1)

                    ####layout for main window###

                    ###############
                    #             #
                    #     0,0     #
                    #    Title    #
                    #             #
                    ###############
                    #             #
                    #     1,0     #
                    #   Internal  #
                    #   Layout    #
                    ###############
		
        self.main_window_grid.addWidget(self.title, 0, 0)
        self.main_window_grid.addWidget(self.start_inline_grid, 1, 0)
        self.view_main_layout = QWidget()
        self.view_main_layout.setLayout(self.main_window_grid)
        #connections
        self.start_button.clicked.connect(self.start_action)
        self.close_button.clicked.connect(self.close_action)
        
    def create_convert_currencies_layout(self):
        # this method creates the convert currencies layout
        self.convert_layout = QGridLayout()
        self.convert_from_label = QLabel('From: ')
        self.convert_to_label = QLabel('To: ')
        self.convert_amount_label = QLabel('Amount: ')
        self.convert_from_combobox = QComboBox()
        self.convert_to_combobox = QComboBox()
        currencyTypes = ['GBP','Euro','USD','YEN']
        for eachType in currencyTypes:
            self.convert_from_combobox.addItem(eachType)
            self.convert_to_combobox.addItem(eachType)
        self.convert_amount_line_edit = QLineEdit()
        self.convert_submit_button = QPushButton('Convert')
        #add info to currencies status layout in lines 161-166
        ####--- internal layout for main window ---####
        
        #############################
        #             #             #
        #     0,0     #     0,1     #
        #  From Label #     From    #
        #             #   ComboBox  #
        #############################
        #             #             #
        #     1,0     #     1,1     #
        #    Amount   #   Amount    #
        #     Label   #   LineEdit  #
        #############################
        #             #             #
        #     2,0     #     2,1     #
        #   To Label  #     To      #
        #             #   ComboBox  #
        #############################
        self.convert_internal_layout.addWidget(self.convert_from_label,0,0)
        self.convert_internal_layout.addWidget(self.convert_amount_label,1,0)
        self.convert_internal_layout.addWidget(self.convert_to_label,2,0)
        self.convert_internal_layout.addWidget(self.convert_from_combobox,0,1)
        self.convert_internal_layout.addWidget(self.convert_amount_line_edit,1,1)
        self.convert_internal_layout.addWidget(self.convert_to_combobox,2,1)
        #add info to the main window grid in lines 179-180
                    ####layout for main window###

                    #############################
                    #                           #
                    #           0,0             #
                    #         Internal          #
                    #          Layout           #
                    #############################
                    #           1,0             #
                    #       Submit button       #
                    #############################
        self.convert_layout.addLayout(self.convert_internal_layout,0,0)
        self.convert_layout.addWidget(self.convert_submit_button,1,0)
        self.view_convert_layout = QWidget()
        self.view_convert_layout.setLayout(self.convert_layout)
        self.convert_submit_button.clicked.connect(self.convert_the_currencies)
        
    def start_action(self):
        self.stacked_layout.setCurrentIndex(1)
    def message_box(self,title,message):
        QMessageBox.about(self,title,message)
    def close_action(self):
        if not self.change_valid_euro or not self.change_valid_usd or not self.change_valid_yen:
            self.message_box('Error!','''The input is not valid
please ensure that each
currency is in the format
0.00 or 2dp''')
        else:
            self.currency_class.edit(self.euro_line_edit.text(),
                                     self.usd_line_edit.text(),
                                     self.yen_line_edit.text())
            self.message_box('Success!','''The currencies have
been changed''')
    
    # convert currencies method
    def convert_the_currencies(self):
        valid = self.check_for_2dp(self.convert_amount_line_edit.text())
        if valid:
            self.convert_amount_in_pounds = self.currency_class.convertToPounds(self.convert_amount_line_edit.text(),
                                                                                self.convert_from_combobox.currentText())
            self.convert_amount_final = self.currency_class.convertFromPounds(self.convert_amount_in_pounds,
                                                                              self.convert_to_combobox.currentText())
            self.message_box('Success!',
            				 '{0} {1} = {2:.2f} {3}'.format(
        						 self.convert_amount_line_edit.text(),
								 self.convert_from_combobox.currentText(),
                                 self.convert_amount_final,
                                 self.convert_to_combobox.currentText()))
            self.convert_from_combobox.setCurrentIndex(0)
            self.convert_to_combobox.setCurrentIndex(0)
            self.convert_amount_line_edit.setText('')
            self.stacked_layout.setCurrentIndex(0)
        else:
            self.message_box('Error!','''The input is not valid
please ensure that each
currency is in the format
0.00 or 2dp''')


if __name__ == '__main__':
    currency_convertor = QApplication(sys.argv)
    main_window = mainWindow()
    main_window.show()
    main_window.raise_()
    currency_convertor.exec_()
