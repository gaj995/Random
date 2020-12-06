"""
average_colour is the main function to envoke with two 6-digit hexadecimal strings
"""

def average_colour(hex_one, hex_two):
    """
    Takes in two 6-digit hexadecimal strings and returns the average color in a 6-digit hexadecimal string
    """
    hex_one_split = split_hex(hex_one)
    hex_two_split = split_hex(hex_two)
    rgb_list_one = hex_to_rgb(hex_one_split)
    rgb_list_two = hex_to_rgb(hex_two_split)
    average_rgb_list = average_rgb (rgb_list_one, rgb_list_two)
    averaged_hex = rgb_to_hex(average_rgb_list)
    return '#{}{}{}'.format(averaged_hex[0], averaged_hex[1], averaged_hex[2]) 

def hex_to_rgb(hex_list):
    """
    Takes in a list of hex colour and converts them to a list of rgb colour
    """
    rgb_list = [int(i, 16) for i in hex_list]
    return rgb_list

def split_hex(string):
    """
    Takes in a string of hex and coverts it to paired list of hex.
    Pairing is determined by split_num
    """
    split_num = 2
    split_list = [string[i:i + split_num] for i in range(0, len(string), split_num)]
    return split_list

def average_rgb(rgb_list_one, rgb_list_two):
    """
    Takes in two lists of rgb colours and generates the average between the two at the same index
    """
    rgb_list = [(i + y) / 2 for i, y in zip(rgb_list_one, rgb_list_two)]
    return rgb_list

def rgb_to_hex(rgb_list):
    """
    Takes in a list of rgb colour and converts them to a list of hex colour
    """
    hex_value = [format(i, '02x') for i in rgb_list]
    return hex_value
    
