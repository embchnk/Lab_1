import argparse
import sys
import logging
import datetime

from os.path import isfile

logging.basicConfig(filename="logs.log", level = logging.INFO )
logging.info( "\n       WORD COUNTER")
logging.info( datetime.datetime.now() )

class CountWords:

    @staticmethod
    def get_parser():
        parser = argparse.ArgumentParser( description = "File path: " )
        parser.add_argument( "file_object", type = str )
        if len( sys.argv ) == 1:
            logging.error( "No file given as an argument" )
            sys.exit( "You need to give a file as an argument" )
        arg = parser.parse_args()
        InputFileValidator.validate( arg.file_object )
        return arg.file_object

    @staticmethod
    def count_words( file, string_to_count ):
        with open( file, "r" ) as file_to_count:
            buffer = file_to_count.read()
            file_to_count.close()
        words = buffer.split()
        counter = 0
        logging.info( "Looking for word: '" + string_to_count + "'" )
        table = []
        for string in words:
            if string not in table:
                table.append( string )
        table_with_counts = [ ( string, words.count( string ) ) for string in table if words.count( string ) > 1 ]
        table_with_counts.sort( key = lambda table_with_counts: table_with_counts[1] )
        for string in table_with_counts:
            print( string )
        # for string in words:
        #     if not string.find( string_to_count ) == -1:
        #         counter += 1
        # print( counter )

class InputFileValidator():
    @staticmethod
    def validate( file_object ):
        logging.info( "Checking file: " + file_object )
        if not isfile( file_object ):
            logging.error( "Wrong file/path entered as an argument" )
            print( "The following file doesn't exist" )
            sys.exit( "Enter the correct name/path to the file" )
        logging.info( "File is valid, counting selected word" )

CountWords.count_words( CountWords.get_parser(), "PrChecker.Downs" )

