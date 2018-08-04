#! /usr/bin/env python

'''
@author Xia Wenwen
@date 2018-08-01
This python script is used to read data file into memory and
store the data into proper data structure
'''

from __future__ import print_function
import os
import time
from network_data_manager import NetworkDataManager
from network_record import NetworkRecord

'''
This method is the entry point to load data from file system into memory
@param file_path: the SocialNetwork.txt file path in file system
@param data_manager: the instance of NetworkDataManager class to hold data storage structures
@return the total number of people in the txt file
'''
def load_data(file_path, data_manager):
    print("file path is {}".format(file_path))
    t0 = time.time()
    with open(file_path) as f:
        print ("loading data ...")
        for line in f:
            #print (line)
            store_data(line,data_manager)
        print ("load data completed!")
    t1 = time.time()
    duration = t1-t0
    print("time consumed for data loading is {} seconds".format(duration))

    # total number of people equal to the length of the person_dic
    total_num = len(data_manager.person_dict)
    print("total number of people is {}".format(total_num))
    return total_num


'''
This method is to store each line of the txt file into data_manager
@param line: the each line of txt file, containing two names separated by comma,
@param data_manager: the instance of NetworkDataManager

'''
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

        # existing record, update the record_list
        else:
            existing_record = data_manager.record_dict[record_id]
            existing_record.add_friend(record_friend_id)
            existing_record.remove_duplicates()


if __name__ == '__main__':
    # initialize NetworkDataManager with two empty dictionaries: record_dict, person_dict
    data_manager = NetworkDataManager(dict(), dict())
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_data(dir_path + '/SocialNetwork.txt', data_manager)
