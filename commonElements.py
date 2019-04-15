def common_elements(listA, listB):
    listCommon = []
    for item in listA:
        if item in listB:
            listCommon.append(item)
    return listCommon

    # return = [itemA for itemA in listA for itemB in listB if itemA == itemB]


a = [1, 3, 4, 6, 7, 9]
b = [1, 2, 4, 5, 9, 10]


print(common_elements(a, b))
