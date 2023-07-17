import matplotlib.pyplot as plt
from PySide2.QtWidgets import QMessageBox
import re
from PySide2 import QtCore, QtGui, QtWidgets

import GUI


def validInputs(function, minX, maxX):
    answer = "true"
    try:  # check if the minimum and maximum value valid (integer)
        forCheckingMinX = int(minX)
        forCheckingMaxX = int(maxX)
    except Exception:
        answer = "Please enter a valid values for minimum and maximum"
        return answer
    function = replace_implicit_multiplication(function)
    if forCheckingMinX > forCheckingMaxX:
        answer = "The minimum must be smaller than the maximum"
    elif function == "":  #
        answer = "please enter the function "
    elif minX == "" or maxX == "":
        answer = "The maximum and maximum must be given "
    elif validFunctionUpper(function) != "true":
        answer = validFunctionUpper(function)
    elif valid_function_valid_terms(function) != "true":
        answer = valid_function_valid_terms(function)
    else:
        try:
            tmp = function.replace("x", '(' + str(2) + ')')  # if we have x^2 and x is negative
            tmp = tmp.replace("^", "**")
            tmp = tmp.replace(' ', '')
            x = eval(tmp)
            answer = "true"
        except:

            answer = "enter a valid function"

    return answer


def validFunctionUpper(function):
    for char in function:
        if char.isupper():
            return "please enter the function in lower case"
        return "true"


def valid_function_valid_terms(function):
    if function[-1].isalnum():
        return "true"
    return "enter a valid function"

def replace_implicit_multiplication(s):
    pattern = r'(\d+)([a-zA-Z])'
    repl = r'\1*\2'
    return re.sub(pattern, repl, s)