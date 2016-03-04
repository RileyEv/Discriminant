# -*- coding: utf-8 -*-

import random


class Discriminant:
    '''A class to calculate currencies'''
    # constructor
    def __init__(self):
        pass

    def generateQuestion(self, difficulty):
        maxCoefficient = 9
        minCoefficient = 1
        if difficulty == 'Medium':
            maxCoefficient = 15
            minCoefficient = 4
        elif difficulty == 'Hard':
            maxCoefficient = 20
            minCoefficient = 7
        elif difficulty == 'God':
            maxCoefficient = 30
            minCoefficient = 15

        coefficients = []
        for i in range(3):
            coefficients.append(random.randint(minCoefficient, maxCoefficient))

        if ((coefficients[1]) ^ 2 - 4 * coefficients[0] * coefficients[2]) > 0:
            answer = 'real'
        elif ((coefficients[1]) ^ 2 - 4 * coefficients[0] * coefficients[2]) < 0:
            answer = 'imaginary'
        else:
            answer = 'equal'

        return {
            'coefficients': coefficients,
            'answer': answer,
        }
