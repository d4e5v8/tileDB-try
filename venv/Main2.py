import csv
import sys
import os
import configparser
import logging

# tiledb imports requirements
import tiledb
import pandas as pd

# Constants
CONFIG_FILE = './config.ini'
LOG_FILE = './log.txt'

# Global things
ArrayFileName: str

# Functions
def Init_Stuff():
    import pdb;
    pdb.set_trace();
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

# Main section (old school)
# print("Running... \nSee Log.txt...")
# Init_Stuff()
# logging.info("Running tileDB thing... version: %s", tiledb.libtiledb.version())
# logging.info("Current local directory: %s", os.getcwd())

# ctx = tiledb.Ctx()
# arr = tiledb.load(ctx, "data/Marine_CSV_sample.csv")
# arr.domain
# pd.DataFrame([(arr.attr(i).identification, arr.attr(i).latitude, arr.attr(i).longitude) for i in range(arr.natr)],
#              columns = ('Identification', 'Latitude', 'Longitude'))

config = configparser.ConfigParser()
config.read(CONFIG_FILE)
ArrayFileName: str = config['FILES']['LOCAL_ARRAY_FILE']
print(ArrayFileName)
tiledb.open(ArrayFileName)
# print(ArrayFileName.shape)
logging.info("Local Array Filename is: %s", ArrayFileName)