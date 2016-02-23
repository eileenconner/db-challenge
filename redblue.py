# pattern: "abba"
# input: "redbluebluered"
# write fn that takes pattern, input and determines whether you have a match
# runtime of algorithm is exponential to length of input
# pattern can contain any chars in any order
# words must be at least 1 char long. input will be at least as long as the pattern.

def wordpattern(pattern, input_string):
    """given 2 strings, determine whether input matches pattern."""
    # if true, return 1. if false, return 0

    # convert argument strings to lists
    pattern_list = pattern.strip().split()

    # need to figure out how to separate input into words, not chars
    # I think the answer may be to build a list of words to act as our word bank
    # I am getting these words from downloading the input files for the challenge
    # iterate through the chars in input_string, using string concatenation to build a word
    # once we've built a word that is in the bank, append that word to the input_list
    # let's try it.

    input_list = []
    placeholder_word = None
    word_bank = ['red', 'blue', 'to', 'be', 'or', 'not', 'raise', 'rays', 'raze',
                 'one', 'two', 'three', 'four', 'cow', 'the', 'quick', 'brown', 'fox',
                 '1']

    for char in input_string:
        if placeholder_word is None:
            placeholder_word = char
        else:
            placeholder_word = placeholder_word + char

        print placeholder_word

        if placeholder_word in word_bank:
            input_list.append(placeholder_word)
            placeholder_word = None

        print "placeholder is ", placeholder_word
        print "input list is ", input_list

    # at this point we have 2 lists
    # if lengths are not ==, input_string is not in pattern
    if len(pattern_list) != len(input_list):
        return 0

    # analyze pattern in terms of ints
    int_pattern = []
    tracker = 0
    pattern_tracker_coords = {}

    # build list to keep track of pattern in terms of ints
    # keep track of which item gets each into coord in a dict
    for item in pattern_list:
        if item in pattern_tracker_coords:
            # append value of this item as stored in item_tracker_coords
            int_pattern.append(pattern_tracker_coords[item])
        else:
            # append tracker to list and add new pair to dict
            int_pattern.append(tracker)
            pattern_tracker_coords[item] = tracker
            tracker += 1

    # analyze input in ints as above, for comparison
    int_input = []
    tracker = 0
    input_tracker_coords = {}

    for item in input_list:
        if item in input_tracker_coords:
            # append val as stored in input_tracker_coords
            int_input.append(input_tracker_coords[item])
        else:
            # append tracker to list and add new pair to dict
            int_input.append(tracker)
            input_tracker_coords[item] = tracker
            tracker += 1

    # determine whether int_pattern and int_input match and return 1/0 accordingly
    if int_pattern == int_input:
        return 1
    return 0
