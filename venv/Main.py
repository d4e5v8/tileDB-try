import csv
import sys
import os
import configparser
import logging

# tiledb imports requirements
import tiledb

# Constants
CONFIG_FILE = './config.ini'
LOG_FILE = './log.txt'

# Global things
ArrayFileName: str

# Functions
def Init_Stuff():
    # remove the existing log file...
    if (os.path.isfile(LOG_FILE)):
        os.remove(LOG_FILE)
    # start logging
    logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)
    if (os.path.isfile(CONFIG_FILE)):
        logging.info("Config file found...")
    else:
        logging.critical("No config file, please create one!")
        sys.exit(1)
    logging.info("Loading Config...")
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    ArrayFileName: str = config['FILES']['LOCAL_ARRAY_FILE']
    logging.info("Local Array Filename is: %s", ArrayFileName)

# Main section (old school)
print("Running... \nSee Log.txt...")
Init_Stuff()
logging.info("Running tileDB thing... version: %s", tiledb.libtiledb.version())
logging.info("Current local directory: %s", os.getcwd())