import argparse
import sys
import logging
import os.path
import datetime

from os.path import isfile
logging.basicConfig(filename="logs.log", level = logging.INFO )
logging.info( "\n       WORD COUNTER")
logging.info( datetime.date.today() )


class CountWords:

    @staticmethod
    def get_parser():
        parser = argparse.ArgumentParser( description = "File path: " )
        parser.add_argument( "file_object", type = str )
        arg = parser.parse_args()
        InputFileValidator.validate( arg.file_object )
        return arg.file_object

    @staticmethod
    def count_words( file ):
        with open( file, "r" ) as file_to_count:
            buffer = file_to_count.read()
            file_to_count.close()
        words = buffer.split()
        counter = 0
        for string in words:
            if string.isalpha():
                counter += 1
        print( counter )

class InputFileValidator():
    @staticmethod
    def validate(file_object):
        logging.info( "Checking file: ")
        logging.info( file_object )
        if not isfile(file_object):
            logging.error( "Wrong file/path entered as an argument" )
            print("The following file doesn't exist")
            sys.exit("Enter the correct name/path to the file")

CountWords.count_words( CountWords.get_parser() )

