#! /usr/bin/env python

"""
@author Xia Wenwen
@date 2018-08-02
This python script is used to start the social network application
"""

from __future__ import print_function
from network_record import NetworkRecord
from sort_search_algorithms import sort, binary_search

'''
Check whether there is the same element for the two sorted lists with ascending order
'''
def check_intersection_existence(active_list, passive_list):
    # check empty list
    if len(active_list) == 0 or len(passive_list) == 0:
        return False

    # take the max of the two smallest ids, at the first index location
    lower_limit = max(active_list[0], passive_list[0])

    # take the min of the two largest ids, at the last index location
    higher_limit = min(active_list[-1], passive_list[-1])

    if lower_limit > higher_limit:
        return False
    else:
        active_truncated_list = truncate_ascending_list(active_list, lower_limit, higher_limit)
        passive_truncated_list = truncate_ascending_list(passive_list, lower_limit, higher_limit)
        for x in active_truncated_list:
            result_index = binary_search(passive_truncated_list, 0, len(passive_truncated_list) - 1, x)

            # if returned index is not negative,it means there is a common element found
            if result_index >=0:
                return True
        # no common element in the two truncated lists
        return False


'''
Truncate ascending list to the range [low, high]
The purpose of truncation is to reduce the search range
'''
def truncate_ascending_list(lst, low, high):
    if len(lst) == 0:
        return lst
    truncated_lst = [x for x in lst if x >= low and x <=high]
    print ("truncated list: {}".format(truncated_lst))
    return truncated_lst


'''
Based on the loaded records, expands the current list to the outer layer
The offset list is the common friends list of the inner layer.
outer_layer_list = (friends list of current layer) - (friends list of the inner layer) 
'''
def expand_to_outer_layer(current_list, offset_list, loaded_data_manager):
    full_outer_layer_list = []
    for id in current_list:
        direct_friends_record = loaded_data_manager.record_dict[id]
        full_outer_layer_list = full_outer_layer_list + direct_friends_record.friends_list
        # remove duplicates
        full_outer_layer_list = list(set(full_outer_layer_list))

    # Remove the element shown in offset list, from full_outer_layer_list
    outer_layer_list = [x for x in full_outer_layer_list if x not in offset_list]

    ##?? consider the end scenario, outer_layer_list is empty? there is no minimun distance for two ids

    # sort the outer layer list
    outer_layer_list = sort(outer_layer_list)
    print (outer_layer_list)
    return outer_layer_list


'''
Start the search process
'''
def search_distance(id_A, record_A, id_B, record_B, loaded_data_manager):
    # A and B are the same, distance is 0
    if record_A.name == record_B.name :
        print ("minimum distance is {}".format(0))
        return 0

    # A and B have distance one
    elif (id_A in record_B.friends_list or id_B in record_A.friends_list) :
        print("minimum distance is {}".format(1))
        return 1

    # mininum distance >= 2
    else:
        # initial status for the search operation is false
        found = False

        # active_flag "A" or "B" indicate who is actively searching
        active_flag = "A"

        # temporary records to be updated during the search process, friends_list should be sorted in ascending order
        record_A_search_pre = NetworkRecord(record_A.name, 0, [id_A])
        record_A_search_cur = NetworkRecord(record_A.name, 1, sort(record_A.friends_list))

        record_B_search_pre = NetworkRecord(record_B.name, 0, [id_B])
        record_B_search_cur = NetworkRecord(record_B.name, 1, sort(record_B.friends_list))

        # start the search alternatively at A side or at B side
        while(not found):
            if active_flag == "A":
                # check whether the current two lists intersects with each other
                found = check_intersection_existence(record_A_search_cur.friends_list, record_B_search_cur.friends_list)

                if(found):
                    distance_AB = record_A_search_cur.distance + record_B_search_cur.distance
                    print("minimum distance is {}".format(distance_AB))
                    return distance_AB
                else:
                    '''prepare record_B lists with update to a outer layer'''
                    # store the record_B_search_pre into the temp variable for later use
                    record_B_search_temp = record_B_search_pre

                    # update the pre with the cur
                    record_B_search_pre = record_B_search_cur

                    # update the cur with the outer layer
                    B_cur_list = record_B_search_cur.friends_list
                    outer_layer_list_B = expand_to_outer_layer(B_cur_list, record_B_search_temp, loaded_data_manager)
                    increment_distance_B = record_B_search_cur.distance + 1
                    record_B_search_cur = NetworkRecord(record_B.name, increment_distance_B, outer_layer_list_B)

                    # toggle active flag to "B"
                    active_flag = "B"

            # active_flag equal to "B"
            else:
                # check whether the current two lists intersects with each other
                found = check_intersection_existence(record_B_search_cur.friends_list, record_A_search_cur.friends_list)

                if(found):
                    distance_AB = record_A_search_cur.distance + record_B_search_cur.distance
                    print("minimum distance is {}".format(distance_AB))
                    return distance_AB

                else:
                    '''prepare record_A lists with update to a outer layer'''
                    # store the record_A_search_pre into the temp variable for later use
                    record_A_search_temp = record_A_search_pre

                    # update the pre with the cur
                    record_A_search_pre = record_A_search_cur

                    # update the cur with the outer layer
                    A_cur_list = record_A_search_cur.friends_list
                    outer_layer_list_A = expand_to_outer_layer(A_cur_list, record_A_search_temp, loaded_data_manager)
                    increment_distance_A = record_A_search_cur.distance + 1
                    record_A_search_cur = NetworkRecord(record_A.name, increment_distance_A, outer_layer_list_A)

                    # toggle active flag to "A"
                    active_flag = "A"

if __name__ == '__main__':
    active_list = [1, 3, 4, 8, 9, 23]
    passive_list = [21, 22, 24, 28, 29, 30]

    result = check_intersection_existence(active_list, passive_list)
    print (result)
