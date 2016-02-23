# Given a pattern and a string, find if the string follows the same pattern
# pattern: [a b b a], string: cat dog dog cat

# solve for situation with string separated by spaces

# general plan of attack:
# break inputs into list on space
# determine whether length of two are the same; if not, return no

# create a new list
# create a tracker variable int starting at 0
# create a dictionary to store item-tracker coordinates
# iterate through pattern, checking each item to see if it's already in the list
# if not, add a new item with value of tracker to the list
# add the new pair to the dictionary
# and increment the tracker
# if yes, add a new item with same value as previous item to list (access via dictionary)

# reset tracker variable to 0
# repeat the above for the string (broken into list)
# can choose to go all the way through or to check value at each step against previous list (faster)

# compare two resulting lists and see if they are the same
# if yes, return true
# if not, return false


def find_matching_pattern(pattern, string):
    """Determine whether string conforms to general pattern."""
    # if lengths are not the same, string is not in pattern.
    if len(pattern) != len(string):
        return False

    # analyze pattern -> keep track in terms of ints
    int_pattern = []
    tracker = 0
    item_tracker_coords = {}

    # build list to keep track of pattern in terms of ints
    # keep track of which item gets each int coordinate in a dictionary
    for item in pattern:
        if item in item_tracker_coords:
            # append value of for this item as stored in item_tracker_coords
            int_pattern.append(item_tracker_coords[item])
        else:
            # append tracker to list and add new pair to dictionary
            int_pattern.append(tracker)
            item_tracker_coords[item] = tracker
        tracker += 1

    # analyze string as above, for comparison
    int_string = []
    tracker = 0
    string_tracker_coords = {}

    # build list to keep track of string in terms of ints
    # keep track of which item gets each int coordinate in a dictionary
    for item in string:
        if item in string_tracker_coords:
            # append value of for this item as stored in string_tracker_coords
            int_string.append(string_tracker_coords[item])
        else:
            # append tracker to list and add new pair to dictionary
            int_string.append(tracker)
            string_tracker_coords[item] = tracker
            tracker += 1

    # determine whether int_pattern and int_string match and return T/F accordingly
    if int_pattern == int_string:
        return True
    return False


def input_to_answer():
    pattern = raw_input()
    string = raw_input()
    # convert both of these to lists here
    pattern_list = pattern.strip().split(" ")
    string_list = string.strip().split(" ")
    print find_matching_pattern(pattern_list, string_list)


input_to_answer()
