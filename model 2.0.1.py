my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ak = 0

while ak < len(my_list):
    if my_list[ak] > 0:
        print (my_list[ak])
        ak += 1
    elif my_list[ak] == 0:
        ak += 1