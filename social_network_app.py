#! /usr/bin/env python

"""
@author Xia Wenwen
@date 2018-08-01
This python script is used to start the social network application
"""

from __future__ import print_function
import os
import sys
import argparse
from data_file_reader import load_data
from network_data_manager import NetworkDataManager


def main():
    # initialize NetworkDataManager with two empty dictionaries: record_dict, person_dict
    data_manager = NetworkDataManager(dict(), dict())

    # load data into data_manager
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_data(dir_path + '/SocialNetwork.txt', data_manager)





if __name__ == '__main__':
    main()