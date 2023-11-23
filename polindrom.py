con = str(input("Enter a sentence: "))

while len(con) <= 0:
    con = str(input("Enter a sentence: "))


def palindrom(sentence):
    structure = sentence.lower().split()
    rezalt, newlist, dublicate = [], [], []
    for elem in structure:
        elem_list = list(elem)
        copy_el_ls_rev = elem_list[::-1]
        if elem_list == copy_el_ls_rev:
            str_elem = elem_list
            convert_el_ls = ''.join(map(str, str_elem))
            rezalt.append(convert_el_ls)
    if not rezalt:
        return "We dont't found polidrom"
    for i in rezalt:
        if i not in newlist:
            newlist.append(i)
        else:
            dublicate.append(i)
    return f"We found polindrom: {newlist}"


print(palindrom(con))
