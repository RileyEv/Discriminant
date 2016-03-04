# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from discriminantClass import *


class mainWindow(QMainWindow):
    '''this class creates a main window to run the main program'''
    def __init__(self):
        super(mainWindow, self).__init__()
        self.discriminant_class = DiscriminantClass()
        self.setWindowTitle('Discriminant Game')
        self.title_font = QFont('Helvetica', 90, QFont.Helvetica)
        self.button_font = QFont('Helvetica', 30, QFont.Helvetica)
        self.create_main_window_layout()
        self.create_start_timer_layout()
        self.create_question_layout()
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.view_main_layout)
        self.stacked_layout.addWidget(self.view_start_timer_layout)
        self.stacked_layout.addWidget(self.view_question_layout)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        self.resize(600, 250)

    def create_main_window_layout(self):
        self.title_label = QLabel('Discriminant')
        self.title_label.setFont(self.title_font)
        self.title_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
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
        self.question_layout = QGridLayout()
        self.question_internal_layout = QGridLayout()
        self.question_label = QLabel(u'5x{0} + 6x + 10'.format(QChar(0x00B2)))
        self.question_label.setFont(self.title_font)
        self.question_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.countdown_label = QLabel('10')
        self.countdown_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.equal_roots_button = QPushButton('Equal Roots')
        self.equal_roots_button.setFont(self.button_font)
        self.imaginary_roots_button = QPushButton('Imaginary Roots')
        self.imaginary_roots_button.setFont(self.button_font)
        self.real_roots_button = QPushButton('Real Roots')
        self.real_roots_button.setFont(self.button_font)
        #############################
        #             #             #
        #     0,0     #     0,1     #
        #  From Label #     From    #
        #             #   ComboBox  #
        #############################
        self.question_internal_layout.addWidget(self.real_roots_button, 0, 0)
        self.question_internal_layout.addWidget(self.equal_roots_button, 0, 1)
        self.question_internal_layout.addWidget(self.imaginary_roots_button, 0, 2)
        self.question_internal_widget = QWidget()
        self.question_internal_widget.setLayout(self.question_internal_layout)
        #############################
        #           0,0             #
        #        Timer Label        #
        #############################
        #           1,0             #
        #         Question          #
        #          Label            #
        #############################
        #           2,0             #
        #     Internal Layout       #
        #############################
        self.question_layout.addWidget(self.countdown_label, 0, 0)
        self.question_layout.addWidget(self.question_label, 1, 0)
        self.question_layout.addWidget(self.question_internal_widget, 2, 0)
        self.view_question_layout = QWidget()
        self.view_question_layout.setLayout(self.question_layout)
        self.equal_roots_button.clicked.connect(lambda: self.answer_reaction('equal'))
        self.real_roots_button.clicked.connect(lambda: self.answer_reaction('real'))
        self.imaginary_roots_button.clicked.connect(lambda: self.answer_reaction('imaginary'))

    def start_action(self):
        self.timer_time = 3
        self.stacked_layout.setCurrentIndex(1)
        self.start_timer = QTimer()
        self.start_timer.timeout.connect(self.start_timer_countdown)
        self.start_timer.start(1000)

    def start_timer_countdown(self):
        self.timer_time = int(self.start_timer_label.text()) - 1
        if self.timer_time == 0:
            self.start_timer.stop()
            self.start_timer_label.setText('3')
            self.stacked_layout.setCurrentIndex(2)
            self.difficulty = self.difficulty_combobox.currentText()
            self.difficulty_combobox.setCurrentIndex(0)
            self.question_num = 0
            self.new_question()
        else:
            self.start_timer_label.setText(str(self.timer_time))

    def new_question(self):
        self.question_data = self.discriminant_class.generateQuestion(
            self.difficulty
        )
        print(self.question_data)
        self.question_label.setText(
            u'{1}x{0} + {2}x + {3}'.format(
                QChar(0x00B2),
                self.question_data['coefficients'][0],
                self.question_data['coefficients'][1],
                self.question_data['coefficients'][2],
            )
        )
        self.question_num += 1
        self.countdown_label.setText('10')
        self.timer_time = 10
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.question_timer_countdown)
        self.countdown_timer.start(1000)

    def question_timer_countdown(self):
        self.timer_time = int(self.countdown_label.text()) - 1
        if self.timer_time == 0:
            self.countdown_timer.stop()
            self.countdown_label.setText('10')
            if self.difficulty == 'God':
                self.message_box(
                    'HAHAHAHAHAHAH',
                    "You thought you were good enough, but you weren't!"
                )
            else:
                self.message_box('Too slow!', 'Better luck next time')
            self.stacked_layout.setCurrentIndex(0)
        else:
            self.countdown_label.setText(str(self.timer_time))

    def answer_reaction(self, button_clicked):
        self.countdown_timer.stop()
        if button_clicked == self.question_data['answer']:
            if self.question_num == 10:
                self.stacked_layout.setCurrentIndex(0)
                self.message_box(
                    'Congratulations',
                    'Now try the next difficulty!'
                )
            else:
                self.new_question()
        else:
            self.stacked_layout.setCurrentIndex(0)
            if self.question_num == 10:
                self.message_box('Hard Luck', 'You got so close! :(')
            else:
                self.message_box('Try again', 'Better luck next time')

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
