#! /usr/bin/env python

"""
@author Xia Wenwen
@date 2018-08-01
This python script is used to read data file into memory and
store the data into proper data structure
"""

from __future__ import print_function
import os
from network_data_manager import NetworkDataManager
from network_record import NetworkRecord


def load_data(file_path, data_manager):
    print(file_path)
    with open(file_path) as f:
        for line in f:
            #print (line)
            store_data(line,data_manager)
        print ("load data completed!")



def store_data(line, data_manager):
    line_pair = list()
    for name in line.split(','):
        stripped_name = name.strip(" \r\n")
        line_pair.append(stripped_name)

    # add the two persons into map in order to generate ids
    data_manager.add_person(line_pair[0])
    data_manager.add_person(line_pair[1])


    index = [0,1]
    for i in index:
        record_name = line_pair[i]
        record_id = data_manager.person_dict[record_name]
        record_distance = 1

        record_friend_name = line_pair[1-i]
        record_friend_id = data_manager.person_dict[record_friend_name]

        # new record to be stored
        if record_id not in data_manager.record_dict:
            record_list = [record_friend_id]
            new_record = NetworkRecord(record_name, record_distance, record_list)
            data_manager.add_record(record_id, new_record)
            new_record.print_all()

        # existing record, update the record_list
        else:
            existing_record = data_manager.record_dict[record_id]
            existing_record.add_friend(record_friend_id)
            existing_record.remove_duplicates()
            existing_record.print_all()


if __name__ == '__main__':
    # initialize NetworkDataManager with two empty dictionaries: record_dict, person_dict
    data_manager = NetworkDataManager(dict(), dict())
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_data(dir_path + '/SocialNetwork_5.txt', data_manager)
