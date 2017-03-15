import os.path
import argparse
import sys
import os
import matplotlib.pyplot as plt
import numpy as np

from os.path import isfile

class LogParser:

    @staticmethod
    def parse_log( input_file, string_to_be_found ):
        result = []
        with open( input_file, "r" ) as file_object:
            data = file_object.read()
            file_object.close()
        splitted_data = data.split( "\n" )
        for string in splitted_data:
            if string_to_be_found in string:
                result.append( string )
        return result

    @staticmethod
    def get_parser():
        parser = argparse.ArgumentParser( description = "File path: " )
        parser.add_argument( "file_object", type = str )
        arg = parser.parse_args()
        InputFileValidator.validate( arg.file_object )
        return arg.file_object

    @staticmethod
    def save_result( file, result ):
        with open( file, "w" ) as result_file:
            for line in result:
                result_file.write( line )
                result_file.write( "\n")
            result_file.close()

class InputFileValidator():
    @staticmethod
    def validate(file_object):
        if not isfile(file_object):
            print("The following file doesn't exist")
            sys.exit("Enter the correct name/path to the file")

data = LogParser.parse_log( LogParser.get_parser(), "PrChecker.Downs" )[1:]
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

plt.plot( x_buffer[:], y_buffer[:], 'ro' )
plt.xlabel( "tracks" )
plt.xticks(x_buffer[:], y_buffer[:], rotation='vertical')
plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)
plt.savefig( 'result.png' )
os.system( "jupyter notebook ./result.png" )


# LogParser.save_result( "results", LogParser.parse_log( LogParser.get_parser(), "PrChecker.Downs" ) )
# os.system( "jupyter notebook ./results" )
