###################################################################################
# program : Currency converter                                                    #
# Programmer : Riley Evans                                                        #
# Date : 05/03/2014                                                               #
# Description : a currency converter that allows the user to convert currencies   #
#               and to allow the user to update the currencies                    #
###################################################################################

#########---- Keyword Definitions ----#########
## self -- this is a variable that stores lots of items inside a class
## QLabel -- this is a text label that will display text on the screen
## QLineEdit -- this is an area that the user can input data into the program GUI
## QComboBox -- this is a drop down menu to allow the users to select a currency from the available ones
## QGridLayout -- this is a layout that can be used as a grid to display items on the window
## QWidget -- this is a widget that can be used to store grids so that they can be added to the stacked layout
## QStackedLayout -- this is an item that stores all the layouts needed for the program to work
## CentralWidget -- this is the main widget that is shown on the screen

#########---- imports ----#########
import sys
#imports the module sys to help control the windows that is created
from PyQt4.QtCore import *
#imports the PyQt core to create the windows and the core functions needed for the program
from PyQt4.QtGui import *
#imports the PyQt GUI to add class for the GUI objects
from currencyconverterclass import *
#imports the class that I have made to carry out the currency calculation that I need to do

#########---- Window Class ----#########
class mainWindow(QMainWindow):# creates a class for the windows
    '''this class creates a main window to run the main program'''
    # __init__ is a constructor method this means that it will be run automatically when the class is first instantiated
    def __init__(self):
        super().__init__() # call super class constructor
        print('    <--- create currency class --->')
        self.currency_class = Currency()#instantiates currency class that I have made so that I can do currency calculations
        print('        Success -- class made')
        print('    <--- end creation of currency class --->')
        self.setWindowTitle('Currency Convertor')#sets the window title that will be show to the user
        print('    <--- start creating layouts --->')
        self.create_main_window_layout()#creates main window layout - runs a method in the class to create all the objects for the main window
        print('        Success -- main window made')
        self.create_convert_currencies_layout()#creates convert currencies layout - runs a method in the class to make all the objects for the convert currencies window
        print('        Success -- convert currencies layout made')
        print('    <--- end creating layouts --->')
        print('    <--- start adding layouts to stacked layout --->')
        self.stacked_layout = QStackedLayout() #this holds the various layouts the window needs to function
        self.stacked_layout.addWidget(self.view_main_layout)#adding main menu layout to stacked layout
        self.stacked_layout.addWidget(self.view_convert_layout)#adding convert currencies layout to stacked layout
        print('    <--- end adding layouts to stacked layout --->')
        self.central_widget = QWidget()# creates the main widget that will be shown in the window that loads
        self.central_widget.setLayout(self.stacked_layout)#adds stacked layout to the central widget
        self.setCentralWidget(self.central_widget)# sets the central widget object to the item show in the windows
    # create main window method
    def create_main_window_layout(self):
        #this is the main layout of the window
        self.euro_label = QLabel('Euro')#creates Euro label that will display the word 'Euro'
        self.usd_label = QLabel('USD')#creates USD label that will display the word 'USD'
        self.yen_label = QLabel('YEN')#creates YEN label that will display the word 'YEN'
        self.euro_line_edit = QLineEdit()#creates Euro line edit so the user can enter values into the program
        self.usd_line_edit = QLineEdit()#creates usd line edit so the user can enter values into the program
        self.yen_line_edit = QLineEdit()#creates yen line edit so the user can enter values into the program
        # ''' - triple quotes means that you can create a string that goes over multiple lines.
        self.text = QLabel('''This is a currency converter.
Edit the currencies to the
left. Enter them when equal
to 1 GBP''')#create text on main menu so that the user knows how to use the program
        self.convert_currencies_button = QPushButton('Convert Currencies')#create convert button so that the user can change the window so that they can convert currencies
        self.change_currencies_button = QPushButton('Change Currencies')#create change currencies button so the user can run the update method so that they can edit the currencies stored
        self.main_window_grid = QGridLayout()#creates main grid layout for all the QWidgets to be stored in
        self.currencies_status_grid = QGridLayout()#creates internal grid layout for several QWidgets to be added to
        #add info to currencies status layout in lines 91-96
                    ####--- internal layout for main window ---####

                    #############################
                    #             #             #
                    #     0,0     #     0,1     #
                    #  Euro Label #     Euro    #
                    #             #   LineEdit  #
                    #############################
                    #             #             #
                    #     1,0     #     1,1     #
                    #  USD Label  #     USD     #
                    #             #   LineEdit  #
                    #############################
                    #             #             #
                    #     2,0     #     2,1     #
                    #  YEN Label  #     YEN     #
                    #             #   LineEdit  #
                    #############################
        self.currencies_status_grid.addWidget(self.euro_label,0,0)#add the Euro label widget to layout in pos 0,0
        self.currencies_status_grid.addWidget(self.usd_label,1,0)#add the usd label widget to layout in pos 1,0
        self.currencies_status_grid.addWidget(self.yen_label,2,0)#add the yen label widget to layout in pos 2,0
        self.currencies_status_grid.addWidget(self.euro_line_edit,0,1)#add the Euro line edit widget to layout in pos 0,1
        self.currencies_status_grid.addWidget(self.usd_line_edit,1,1)#add the usd line edit widget to layout in pos 1,1
        self.currencies_status_grid.addWidget(self.yen_line_edit,2,1)#add the yen line edit widget to layout in pos 2,1
        #add info to the main window grid in lines 112-115

                    ####layout for main window###

                    #############################
                    #             #             #
                    #     0,0     #     0,1     #
                    #     Text    #   Internal  #
                    #             #    Layout   #
                    #############################
                    #             #             #
                    #     1,0     #     1,1     #
                    #   Button    #   Button    #
                    #             #             #
                    #############################
        self.main_window_grid.addWidget(self.text,0,0)#add the text widget to layout in pos 0,0
        self.main_window_grid.addLayout(self.currencies_status_grid,0,1)#add the currency status grid to layout in pos 0,1
        self.main_window_grid.addWidget(self.convert_currencies_button,1,0)#add the convert currencies button to layout in pos 1,0
        self.main_window_grid.addWidget(self.change_currencies_button,1,1)#add the change currencies layout to layout in pos 1,1
        #create widget for layout
        self.view_main_layout = QWidget()#creates widget to hold the main window grid
        self.view_main_layout.setLayout(self.main_window_grid)#add the layout to the main layout
        current_currencies = self.currency_class.get()#gets current currencies stored in the currency class
        self.euro_line_edit.setText(str(current_currencies['Euro']))#--
        self.usd_line_edit.setText(str(current_currencies['USD']))#    }--sets line edit for each currency to the value stored in the currency class
        self.yen_line_edit.setText(str(current_currencies['YEN']))#----
        #connections
        self.change_currencies_button.clicked.connect(self.change_currencies_action)#sets action for the button so that the change_currencies_action is run
        self.convert_currencies_button.clicked.connect(self.convert_currencies_action)#sets action for the button so that the convert_currencies_action is run
    #create convert currencies window method
    def create_convert_currencies_layout(self):
        # this method creates the convert currencies layout
        self.convert_layout = QGridLayout()#creates layout for all widgets to be stored
        self.convert_internal_layout = QGridLayout()#creates internal layout for widgets to be stored in
        self.convert_from_label = QLabel('From: ')#creates convert from label to display the word 'From: '
        self.convert_to_label = QLabel('To: ')#creates convert to label to display the word 'To: '
        self.convert_amount_label = QLabel('Amount: ')#creates amount label to display the word 'Amount: '
        self.convert_from_combobox = QComboBox()#creates combo box so the user can use a drop down box to select the from currency
        self.convert_to_combobox = QComboBox()#creates combo box so the user can use a drop down box to select the to currencies
        currencyTypes = ['GBP','Euro','USD','YEN']#each currency type
        for eachType in currencyTypes:#loops through each currency type
            self.convert_from_combobox.addItem(eachType)#adds an item to the combo box for each type
            self.convert_to_combobox.addItem(eachType)#adds an item to the combo box for each type
        self.convert_amount_line_edit = QLineEdit()#creates amount line edit so the user can enter the amount to convert
        self.convert_submit_button = QPushButton('Convert')#creates convert button so the user can continue to convert the currencies
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
        self.convert_internal_layout.addWidget(self.convert_from_label,0,0)#add the convert_from_label widget to layout in pos 0,0
        self.convert_internal_layout.addWidget(self.convert_amount_label,1,0)#add the convert_amount_label widget to layout in pos 1,0
        self.convert_internal_layout.addWidget(self.convert_to_label,2,0)#add the convert_to_label widget to layout in pos 2,0
        self.convert_internal_layout.addWidget(self.convert_from_combobox,0,1)#add the convert_from_combobox widget to layout in pos 0,1
        self.convert_internal_layout.addWidget(self.convert_amount_line_edit,1,1)#add the convert_amount_line_edit widget to layout in pos 1,1
        self.convert_internal_layout.addWidget(self.convert_to_combobox,2,1)#add the convert_to_combobox widget to layout in pos 2,1
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
        self.convert_layout.addLayout(self.convert_internal_layout,0,0)#add the convert_internal_layout widget to layout in pos 0,0
        self.convert_layout.addWidget(self.convert_submit_button,1,0)#add the convert_submit_button widget to layout in pos 1,0
        self.view_convert_layout = QWidget()
        self.view_convert_layout.setLayout(self.convert_layout)
        self.convert_submit_button.clicked.connect(self.convert_the_currencies)
    # convert button action method run when convert button is pressed
    def convert_currencies_action(self):
        print('####-- convert button pressed changing screen --####')
        self.stacked_layout.setCurrentIndex(1)# changes the window to item 1 in the stacked layout which is the convert layout
    # create a message box method
    def message_box(self,title,message):
        QMessageBox.about(self,title,message)#creates message box window with the message passed into the function
    # change currencies button action method run when change button is pressed
    def change_currencies_action(self):
        print('####-- change button pressed --####')
        print('    <--- start update currencies --->')
        self.change_valid_euro = self.check_for_2dp(self.euro_line_edit.text())#checks the input for 2dp 
        self.change_valid_usd = self.check_for_2dp(self.usd_line_edit.text())#checks the input for 2dp
        self.change_valid_yen = self.check_for_2dp(self.yen_line_edit.text())#checks the input for 2dp
        if not self.change_valid_euro or not self.change_valid_usd or not self.change_valid_yen:# checks boolean values returned to see if any numbers are invalid
            self.message_box('Error!','''The input is not valid
please ensure that each
currency is in the format
0.00 or 2dp''')#creates message to inform user that the currencies are invalid
            print('        Error -- input not valid')
            print('        Restarting')
        else:#run if al values are valid
            self.currency_class.edit(self.euro_line_edit.text(),
                                     self.usd_line_edit.text(),
                                     self.yen_line_edit.text())#edits values stored and changes them to the ones inputed
            self.message_box('Success!','''The currencies have
been changed''')#creates a message box to inform the user that the currencies have been updated
            print('        Success -- currencies changed')
        print('    <--- end update currencies --->')
    # check for 2dp method
    def check_for_2dp(self,num):#checks that the value entered is 2dp
        print('        <--- start 2dp check --->')
        valid = True
        try:
            float(num)# tries to convert input to float 
        except ValueError:#if there is an error run code bellow
            valid = False#changes valid to false
        if not valid:
            print('            bad float -- cant convert to float')
            print('        <--- end 2dp check --->')
            return False
        else:#runs if input is a number
            print('            good float -- not 2dp')
            print('        <--- end 2dp check --->')
            return True
    # convert currencies method
    def convert_the_currencies(self):
        print('####-- convert button2 pressed --####')
        print('    <--- start convert currencies --->')
        valid = self.check_for_2dp(self.convert_amount_line_edit.text())#checks to see if the input is 2dp
        if valid:#checks if the value is valid
            self.convert_amount_in_pounds = self.currency_class.convertToPounds(self.convert_amount_line_edit.text(),
                                                                                self.convert_from_combobox.currentText())#converts the amount to pounds
            self.convert_amount_final = self.currency_class.convertFromPounds(self.convert_amount_in_pounds,
                                                                              self.convert_to_combobox.currentText())#converts the amount in pounds to the desired currency
            print('        Success -- currencies converted')
            print('        Printing conversion')
            self.message_box('Success!','{0} {1} = {2:.2f} {3}'.format(self.convert_amount_line_edit.text(),
			                                                           self.convert_from_combobox.currentText(),
                                                                       self.convert_amount_final,
                                                                       self.convert_to_combobox.currentText()))#outputs the values calculated to the user
            self.convert_from_combobox.setCurrentIndex(0)#sets selected item in the list back to the top of the list
            self.convert_to_combobox.setCurrentIndex(0)#sets selected item in the list back to the top of the list
            self.convert_amount_line_edit.setText('')#sets the line edit to empty
            self.stacked_layout.setCurrentIndex(0)#changes window back to main window
            print('        Returning to main window')
        else:#if the number is not valid run the code bellow
            self.message_box('Error!','''The input is not valid
please ensure that each
currency is in the format
0.00 or 2dp''')#creates message to inform the user that the input is invalid
            print('        Error -- input not valid')
            print('        Restarting')
        print('    <--- end convert currencies --->')
print('<--- start program --->')

#########---- Main Program ----#########
if __name__ == '__main__':#checks that the file has net been imported into another program
    currency_convertor = QApplication(sys.argv)#creates new application
    main_window = mainWindow()#creates new main select window instance
    main_window.show() #makes the instance visible
    main_window.raise_() # raise instance to top of window stack
    currency_convertor.exec_() #monitor application for events
print('<--- end program --->')
