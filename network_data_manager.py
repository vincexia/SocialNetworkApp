#! /usr/bin/env python

"""
@author Xia Wenwen
@date 2018-08-01
This python script is used to manage the data structure used in this app
"""

from __future__ import print_function

class NetworkDataManager:
    def __init__(self, record_dict, person_dict):
        self.record_dict = record_dict;
        self.person_dict = person_dict;

    """
    @name person'name as key of the dict
    @record NetworkRecord instance as the value of the dict
    """
    def add_record(self, name, record):
        if name not in self.record_dict:
            self.record_dict[name] = record

    """
    @name person's name as the key of the dict
    The value of the dict is the length of dict plus one
    """
    def add_person(self, name):
        if name not in self.person_dict:
            length = len(self.person_dict)
            self.person_dict[name] = length + 1
            print ("{}:{}".format(name, self.person_dict[name]))

