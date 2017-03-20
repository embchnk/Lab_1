import os
import matplotlib.pyplot as plt

from LogParser import LogParser
from InputFileValidator import InputFileValidator

InputFileValidator.validate(LogParser.get_parser())

data = LogParser.parse_log(LogParser.get_parser(), "PrChecker.Downs")[1:]
data_to_strings = []
iterator = 0
x_buffer = []
y_buffer = []
for buffer in data:
        part = buffer.split()
        for atom in part:
            if atom.isdigit():
                data_to_strings.append( atom )
for string in data_to_strings:
    if iterator == 0:
        x_buffer.append( string )
        iterator += 1
    elif iterator == 1:
        y_buffer.append( string )
        iterator += 1
    else:
        iterator = 0

LogParser.save_result( "./results/results", LogParser.parse_log( LogParser.get_parser(), "PrChecker.Downs" ) )

plt.plot( x_buffer[:], y_buffer[:], 'ro' )
plt.xlabel( "tracks" )
plt.savefig( './results/result.png' )
os.system( "jupyter notebook ./results/result.png" )


