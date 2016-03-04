# -*- coding: utf-8 -*-

import random


class DiscriminantClass:
    '''A class to calculate currencies'''
    # constructor
    def __init__(self):
        pass

    def generateQuestion(self, difficulty):
        self._maxCoefficient = 9
        self._minCoefficient = -9
        if difficulty == 'Medium':
            self._maxCoefficient = 15
            self._minCoefficient = -15
        elif difficulty == 'Hard':
            self._maxCoefficient = 20
            self._minCoefficient = -20
        elif difficulty == 'God':
            self._maxCoefficient = 30
            self._minCoefficient = -30

        self._coefficients = [
            random.randint(
                self._minCoefficient,
                self._maxCoefficient
            ) for i in range(3)
        ]
        self._discriminant = (self._coefficients[1]) ^ 2 - 4 * self._coefficients[0] * self._coefficients[2]

        if self._discriminant > 0:
            self._answer = 'real'
        elif self._discriminant < 0:
            self._answer = 'imaginary'
        else:
            self._answer = 'equal'

        return {
            'coefficients': self._coefficients,
            'answer': self._answer,
        }
