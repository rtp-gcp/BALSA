#!/usr/bin/env python3

#
# Common module to setup dirs
# It sets env variables to dirs
#

import datetime
import pathlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
import os.path
import numpy as np


# This dir will need to be sourced in current environment
# however the python variables can be exported
# 
# TODO: should implment a main

# The current directory will be where this src file is located.
# Which is in the src dir of the project
dirpath = os.getcwd()
print("current directory is : " + dirpath)

# Use pathlib to find the root dir of the git repo
root_path = pathlib.PurePath(dirpath).parents[0]
data_path = root_path / 'data'
logs_path = root_path / 'logs'
print("root directory is: ", root_path)
print("data directory is: ",  data_path)
print("logs directory is: ", logs_path)

# Create equivalent dir names in the environment
# root
ROOT_DIR_NAME = pathlib.PurePath(dirpath).as_posix()
print("ROOT_DIR_NAME: ", ROOT_DIR_NAME)
os.environ['ROOT_DIR_NAME'] = ROOT_DIR_NAME
# Logs
LOGS_DIR_NAME = logs_path.as_posix()
print("LOGS_DIR_NAME: ", LOGS_DIR_NAME)
os.environ['LOGS_DIR_NAME'] = LOGS_DIR_NAME
# Data
DATA_DIR_NAME = data_path.as_posix()
print("DATA_DIR_NAME: ", DATA_DIR_NAME)
os.environ['DATA_DIR_NAME'] = DATA_DIR_NAME

