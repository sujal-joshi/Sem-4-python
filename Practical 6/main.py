# Here set is used to remove all duplicate numbers from list and
# convert to set and again convert into list

def common_elements(a, b):
    return list(set(a) & set(b))


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(common_elements(a, b))