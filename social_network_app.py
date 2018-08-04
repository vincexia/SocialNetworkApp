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
from search_operation import search_distance


def main():
    # initialize NetworkDataManager with two empty dictionaries: record_dict, person_dict
    data_manager = NetworkDataManager(dict(), dict())

    # load data into data_manager
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_data(dir_path + '/SocialNetwork_5.txt', data_manager)

    name_A = "MARTIN_OMERSA"
    name_B = "CHRIS_POLAND"

    try:
        id_A = data_manager.person_dict[name_A]
        id_B = data_manager.person_dict[name_B]

        record_A = data_manager.record_dict[id_A]
        record_B = data_manager.record_dict[id_B]

        final_result = search_distance(id_A, record_A, id_B, record_B, data_manager)

        if final_result < 0:
            print ("No minimum distance found for {} and {}".format(name_A, name_B))
        else:
            print ("Minimum distance for {} and {} is {}".format(name_A, name_B, final_result))

    except KeyError as e:
        print ("KeyError {}. Please check the correctness of input name".format(e))
    except:
        print ("Unexpected error:", sys.exc_info()[0])
        raise

if __name__ == '__main__':
    main()