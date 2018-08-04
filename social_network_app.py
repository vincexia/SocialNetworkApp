#! /usr/bin/env python

"""
@author Xia Wenwen
@date 2018-08-01
This python script is used to start the social network application
"""

from __future__ import print_function
import os
import sys
from data_file_reader import load_data
from network_data_manager import NetworkDataManager
from search_operation import search_distance

'''
The main method takes the two people's names, and performs search operation on the loaded data structures
The name_A and name_B can be changed based on user's preferences
'''
def main():
    # initialize NetworkDataManager with two empty dictionaries: record_dict, person_dict
    data_manager = NetworkDataManager(dict(), dict())

    # load data into data_manager
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_data(dir_path + '/SocialNetwork.txt', data_manager)

    # name of the first person STACEY_STRIMPLE
    name_A = "STACEY_STRIMPLE"
    # name of the second person RICH_OMLI
    name_B = "RICH_OMLI"

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