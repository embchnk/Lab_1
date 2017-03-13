import argparse
import sys
import logging
import os.path

from os.path import isfile

class CountWords:

    @staticmethod
    def check_if_exist( file_object ):
        if not isfile( file_object ):
            print( "The following file doesn't exist" )
            sys.exit( "Enter the correct name/path to the file" )

    @staticmethod
    def get_parser():
        parser = argparse.ArgumentParser( description = "File path: " )
        parser.add_argument( "file_object", type = str )
        arg = parser.parse_args()
        CountWords.check_if_exist( arg.file_object )
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

CountWords.count_words( CountWords.get_parser() )

