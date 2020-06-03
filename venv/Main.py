import csv
import sys
import os
import configparser
import logging
import shutil

# tiledb imports requirements
import tiledb
import numpy as np

# Constants
CONFIG_FILE = './config.ini'
LOG_FILE = './log.txt'

# Global things
ArrayFile = 'array'

# Functions

# Init function
def Init_Stuff():
    # remove the existing log file...
    global ArrayFile
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
    ArrayFile = config['FILES']['LOCAL_ARRAY_FILE']
    logging.info("Local Array Filename is: %s", ArrayFile)

# TileDB examples functions


def create_array():
    # The array will be 4x4 with dimensions "d1" and "d2", with domain [1,4].
    dom = tiledb.Domain(tiledb.Dim(name="d1", domain=(1, 4), tile=4, dtype=np.int32),
                        tiledb.Dim(name="d2", domain=(1, 4), tile=4, dtype=np.int32))

    # The array will be dense with a single attribute "a" so each (i,j) cell can store an integer.
    schema = tiledb.ArraySchema(domain=dom, sparse=False,
                                attrs=[tiledb.Attr(name="a", dtype=np.int32)])

    # Create the (empty) array on disk.
    tiledb.DenseArray.create(array_name, schema)

def write_array():
    # Open the array and write to it.
    with tiledb.DenseArray(array_name, mode='w') as A:
        data = np.array(([1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12],
                         [13, 14, 15, 16]))
        A[:] = data

def read_array():
    # Open the array and read from it.
    with tiledb.DenseArray(array_name, mode='r') as A:
        # Slice only rows 1, 2 and cols 2, 3, 4.
        data = A[1:3, 2:5]
        print(data["a"])

# Main section (old school)
print("Running... \nSee Log.txt...")
Init_Stuff()
logging.info("Running tileDB thing... version: %s", tiledb.libtiledb.version())
logging.info("Current local directory: %s", os.getcwd())

# Name of array.
array_name = ArrayFile

# Create an array, this will create a folder (name in the config file)

if os.path.exists(ArrayFile):
    logging.info("Array already exists, file: %s", ArrayFile)
else:
    create_array()

# Write stuff in the Array
write_array()

# Read and print the Array..
read_array()