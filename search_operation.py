#! /usr/bin/env python

"""
@author Xia Wenwen
@date 2018-08-02
This python script is used to provide the search algorithm for the social network data
"""

from __future__ import print_function
from network_record import NetworkRecord
from sort_search_algorithms import sort, binary_search

'''
Check whether there is the same element for the two sorted lists with ascending order
@param active_list: the list, which actively searches and provides the targets
@param passive_list: the list, which passively accepts the comparison with the targets
@return True if at least one same element exists; False if no common element exists
Assumption: the two lists above have been sorted with ascending order
'''
def check_intersection_existence(active_list, passive_list):
    # check empty list
    if len(active_list) == 0 or len(passive_list) == 0:
        return False

    # take the max of the two smallest ids, which are at the first index location
    lower_limit = max(active_list[0], passive_list[0])

    # take the min of the two largest ids, which are at the last index location
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
@param lst: the input list with ascending order
@param low: the lower limit for the elements in the list
@param high: the higher limit for the elements in the list
@return truncated_lst: list with elements at range [low, high]
'''
def truncate_ascending_list(lst, low, high):
    if len(lst) == 0:
        return lst
    truncated_lst = [x for x in lst if x >= low and x <=high]
    return truncated_lst


'''
Based on the loaded records, expand the current list to the outer layer
@param current_list: the friends list of the current search layer
@param offset_list: the friends list of the previous search layer
@param loaded_data_manager: the data structures to hold the loaded data
@return outer_layer_list: the list of ids for the next layer outwards
outer_layer_list = (friends list of current layer list) - (friends list of the inner/previous layer) 
If the out_layer_list is empty, the search operation should be stopped and no minimum distance is found.
'''
def expand_to_outer_layer(current_list, offset_list, loaded_data_manager):
    full_outer_layer_list = []
    for id in current_list:
        direct_friends_record = loaded_data_manager.record_dict[id]
        full_outer_layer_list = full_outer_layer_list + direct_friends_record.friends_list
        # remove duplicates
        full_outer_layer_list = list(set(full_outer_layer_list))

    print("full outer layer list is {}".format(full_outer_layer_list))
    print ("offset list is {}".format(offset_list))
    # Remove the element shown in offset list, from full_outer_layer_list
    outer_layer_list = [x for x in full_outer_layer_list if x not in offset_list]

    #If the outer_layer_list is empty, there is no minimum distance for the two persons
    if len(outer_layer_list) == 0:
        print ("empty outer layer list!")
        return outer_layer_list

    # sort the outer layer list
    outer_layer_list = sort(outer_layer_list)
    print ("outer layer list is {}".format(outer_layer_list))
    return outer_layer_list


'''
Start the search process
@param id_A: the id of the first person
@param record_A: the instance of NetworkRecord for id_A
@param id_B: the id of the second person
@param record_B: the instance of the NetworkRecord for id_B
@param loaded_data_manager: the instance of the NetworkDataManager to hold the loaded data
@return the minimum distance for the two persons. If no minimum distance is found, return -1
'''
def search_distance(id_A, record_A, id_B, record_B, loaded_data_manager):
    # A and B are the same, distance is 0
    if record_A.name == record_B.name :
        print ("minimum distance is {}".format(0))
        return 0

    # A and B have distance one. They are direct friends
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

                    # get the cur and offset lists
                    B_cur_list = record_B_search_cur.friends_list
                    B_offset_list = record_B_search_temp.friends_list
                    # get the outer layer list
                    outer_layer_list_B = expand_to_outer_layer(B_cur_list, B_offset_list, loaded_data_manager)
                    if len(outer_layer_list_B) == 0:
                        print ("cannot find minimum distance. Search completed while expanding the second person!")
                        break;
                    else:
                        # update the cur with the outer layer
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

                    # get the cur and offset lists
                    A_cur_list = record_A_search_cur.friends_list
                    A_offset_list = record_A_search_temp.friends_list
                    # get the outer layer list
                    outer_layer_list_A = expand_to_outer_layer(A_cur_list, A_offset_list, loaded_data_manager)
                    if len(outer_layer_list_A) == 0:
                        print ("cannot find minimum distance. Search completed while expanding the first person!")
                        break;
                    else:
                        # update the cur with the outer layer
                        increment_distance_A = record_A_search_cur.distance + 1
                        record_A_search_cur = NetworkRecord(record_A.name, increment_distance_A, outer_layer_list_A)

                        # toggle active flag to "A"
                        active_flag = "A"

        # after the break, return status about no minimum distance found
        return -1

if __name__ == '__main__':
    active_list = [1, 3, 4, 8, 9, 23]
    passive_list = [21, 22, 24, 28, 29, 30]

    result = check_intersection_existence(active_list, passive_list)
    print (result)
