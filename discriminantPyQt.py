# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from discriminantClass import *


class mainWindow(QMainWindow):
    '''this class creates a main window to run the main program'''
    def __init__(self):
        super(mainWindow, self).__init__()
        self.currency_class = Currency()
        self.setWindowTitle('Discriminant Game')
        self.title_font = QFont('Helvetica', 90, QFont.Helvetica)
        self.button_font = QFont('Helvetica', 30, QFont.Helvetica)
        self.create_main_window_layout()
        self.create_start_timer_layout()
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.view_main_layout)
        self.stacked_layout.addWidget(self.view_start_timer_layout)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        self.resize(600, 250)

    def create_main_window_layout(self):
        self.title_label = QLabel('Discriminant')
        self.title_label.setFont(self.title_font)
        self.difficulty_label = QLabel('Difficulty: ')
        self.difficulty_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.start_button = QPushButton('Start')
        self.start_button.setFont(self.button_font)
        self.close_button = QPushButton('Close')
        self.close_button.setFont(self.button_font)
        self.difficulty_combobox = QComboBox()
        Dificulties = ['Easy', 'Medium', 'Hard', 'God']
        for eachDiff in Dificulties:
            self.difficulty_combobox.addItem(eachDiff)
        self.main_window_grid = QGridLayout()
        self.start_inline_grid = QGridLayout()
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
        self.start_inline_grid.addWidget(self.difficulty_label, 0, 0)
        self.start_inline_grid.addWidget(self.start_button, 1, 0)
        self.start_inline_grid.addWidget(self.difficulty_combobox, 0, 1)
        self.start_inline_grid.addWidget(self.close_button, 1, 1)
        self.widget_start_inline_grid = QWidget()
        self.widget_start_inline_grid.setLayout(self.start_inline_grid)
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
        self.main_window_grid.addWidget(self.title_label, 0, 0)
        self.main_window_grid.addWidget(self.widget_start_inline_grid, 1, 0)
        self.view_main_layout = QWidget()
        self.view_main_layout.setLayout(self.main_window_grid)
        # connections
        self.start_button.clicked.connect(self.start_action)
        self.close_button.clicked.connect(self.close_action)

    def create_start_timer_layout(self):
        self.start_timer_layout = QGridLayout()
        self.start_timer_label = QLabel('3')
        self.start_timer_label.setFont(self.title_font)
        self.start_timer_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.start_timer_layout.addWidget(self.start_timer_label, 0, 0)
        self.view_start_timer_layout = QWidget()
        self.view_start_timer_layout.setLayout(self.start_timer_layout)

    def create_question_layout(self):
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
        #############################
        #             #             #
        #     0,0     #     0,1     #
        #  From Label #     From    #
        #             #   ComboBox  #
        #############################
        self.convert_internal_layout.addWidget(self.convert_from_label,0,0)
        self.convert_internal_layout.addWidget(self.convert_amount_label,1,0)
        self.convert_internal_layout.addWidget(self.convert_to_label,2,0)
        self.convert_internal_layout.addWidget(self.convert_from_combobox,0,1)
        self.convert_internal_layout.addWidget(self.convert_amount_line_edit,1,1)
        self.convert_internal_layout.addWidget(self.convert_to_combobox,2,1)
        #############################
        #           0,0             #
        #        Timer Label        #
        #############################
        #           0,0             #
        #         Question          #
        #          Label            #
        #############################
        #           1,0             #
        #       Submit button       #
        #############################
        self.convert_layout.addLayout(self.convert_internal_layout,0,0)
        self.convert_layout.addWidget(self.convert_submit_button,1,0)
        self.view_start_timer_layout = QWidget()
        self.view_start_timer_layout.setLayout(self.start_timer_layout)
        self.convert_submit_button.clicked.connect(self.convert_the_currencies)

    def start_action(self):
        self.timer_time = 3
        self.stacked_layout.setCurrentIndex(1)
        self.start_timer = QTimer()
        self.start_timer.timeout.connect(self.start_timer_countdown)
        self.start_timer.start(1000)

    def start_timer_countdown(self):
        self.timer_time = int(self.start_timer_label.text())
        self.timer_time -= 1
        if self.timer_time == 0:
            self.start_timer.stop()
            self.start_timer_label.setText('3')
            self.stacked_layout.setCurrentIndex(0)
        else:
            self.start_timer_label.setText(str(self.timer_time))

    def message_box(self, title, message):
        QMessageBox.about(self, title, message)

    def close_action(self):
        self.close()


if __name__ == '__main__':
    Discriminant = QApplication(sys.argv)
    main_window = mainWindow()
    main_window.show()
    main_window.raise_()
    Discriminant.exec_()
