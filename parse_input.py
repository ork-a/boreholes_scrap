import re
import sys

class ParseInput(object):
    def __init__(self, m_input):
        self.input = m_input

    def return_limits(self):
        limits = self.input.split()
        #verify input
        for i in range(len(limits)):
            if not re.match("[0-9]+$", limits[i]) and limits[i] != 'NL':
                print('Error! Provide correct input!')
                sys.exit()
            try:
                limits[i] = int(limits[i])
            except ValueError:
                limits[i] = ''
        return[limits[0], limits[1]]
