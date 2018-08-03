#! /usr/bin/env python

"""
@author Xia Wenwen
@date 2018-08-01
This python script is used to define network relationship record to store
relationship data
"""

from __future__ import print_function

class NetworkRecord:
    def __init__(self, name, id, distance, friends_list):
        # self.name is the name of a person
        self.name = name
        # self.id is the integer id of the person
        self.id = id
        # self.distance is the relationship distance to the friends_list
        self.distance = distance
        # self.friends_list is a list of integer ids
        self.friends_list = friends_list

    def add_friend(self, friend_id):
        self.friends_list.append(friend_id)


    def remove_duplicates(self):
        self.friends_list = list(set(self.friends_list))

    def print_all(self):
        print("{}, {}, {}, {}".format(self.name, self.id, self.distance, self.friends_list))
