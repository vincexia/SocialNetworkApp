#! /usr/bin/env python

"""
@author Xia Wenwen
@date 2018-08-01
This python script is used to define the data structure to store the loaded data
"""

from __future__ import print_function

class NetworkDataManager:
    def __init__(self, record_dict, person_dict):
        self.record_dict = record_dict;
        self.person_dict = person_dict;

    """
    @param id: person's id as key of the dict
    @param record: NetworkRecord instance as the value of the dict
    The record_dict structure is <id, record>
    """
    def add_record(self, id, record):
        if id not in self.record_dict:
            self.record_dict[id] = record

    """
    @param name: person's name as the key of the dict
    The value of the dict is the length of dict plus one
    The person_dict structure is <name, id>
    """
    def add_person(self, name):
        if name not in self.person_dict:
            length = len(self.person_dict)
            self.person_dict[name] = length + 1

