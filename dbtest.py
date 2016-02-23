# say what you see: transform string of digits based on its spoken description
# 1 -> "one 1" -> 11
# 21114 -> "one 2, three 1s, one 4" -> 123114
# 11111111111 -> "eleven ones" -> 111
# take an array of strings and return an array of strings
# input: ['12', '21']
# output: 1112
# 1211


def say_what_you_see(input_strings):
    """Translate list of strings containing numbers"""
    out = []

    for item in input_strings:
        counter = 1
        # initialize list for item to add to out
        add_to_out = []
        for i in range(len(item)):
            # check to see if item is the same as the next
            try:
                if item[i] == item[i+1]:
                    counter += 1
                else:
                    add_to_out.append(str(counter))
                    add_to_out.append(str(item[i]))
            except:
                add_to_out.append(str(counter))
                add_to_out.append(str(item[i]))
        out.append("".join(add_to_out))

    return out
