def count_substring(string, sub_string):
    cnt = 0
    index = string.find(sub_string)
    while index != -1 :
        index = string.find(sub_string, index+1)