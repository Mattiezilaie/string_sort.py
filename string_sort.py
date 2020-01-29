# Author: Mahtab Zilaie
# Date: January 28 2020
# Description: insertion sort that sorts a list of strings and sorting ignores the case.


def string_sort(string_list):
    """Sorts a list string_list and ignores case"""

    for i in range(1, len(string_list)):     #Traverse through 1 to len(string_list)
        j = i-1
        while j >= 0 and string_list[j].casefold() > string_list[j+1].casefold():  #comparing the strings in string_list
            key = string_list[j]                                                   #and ignoring case
            string_list[j] = string_list[j + 1]
            string_list[j+1] = key
            j -= 1
        return string_list