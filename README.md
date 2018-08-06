SocialNetworkApp

The SocialNetworkApp is used to achieve the two goals below:
1.	determines the total number of people in the social network
2.	determines the distance between A and B where the distance between two members of the network can be defined as the minimum number of ties required to connect two people in the social network. The values of A and B are as follows: A = STACEY_STRIMPLE, B = RICH_OMLI

The entry point of the application is social_network_app.py. The python framework is version 2.7. The recommended python is v2.7.13 or later. In Windows/Linux/MacOS, execute "python social_network_app.py" to start the application.

###############################################################

Sample Outputs are shown below:

file path is /Users/wenwenxia/PycharmProjects/SocialNetworkApp/SocialNetwork.txt

loading data ...

load data completed!

time consumed for data loading is 6.39485096931 seconds

total number of people is 82168

Expand to outer layer with distance 2 at RICH_OMLI side

Expand to outer layer with distance 2 at STACEY_STRIMPLE side

Expand to outer layer with distance 3 at RICH_OMLI side

minimum distance is 5

Minimum distance for STACEY_STRIMPLE and RICH_OMLI is 5

################################################################

The core algorithm is placed inside the search_distance() method of search_opertion.py file.

Imagine A is the origin of a group of relationship circles. The first circle represents the direct friends with distance 1. The second circle outwards represents the friends of the first circle elements, but without the origin point A. The third circle outwards represents the friends of the second circle elements, but without the first circle elements. The group of circles with the same origin A represents the relationship distances to origin A.

Similarly, at B side, there are also a group of relationship circles with the same origin B.

For distance equal to two or above, the search operation begins at the first circle of origin A. The program will check whether it has the common element with the first circle of origin B. If yes, the distance 2 is returned. Otherwise, the program will expand B to the second circle, and compare B's second circle with A's first circle. 

If no common element is found, the expansion will continue alternatively at A side or at B side. Until at some distance
the expanded outer layer circle does not exist, it means that A and B have no relationship intersection point and that no distance can be found between A and B.

