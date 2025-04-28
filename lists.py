# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) > 5:
        del list_to_remove_elements[5]
    if len(list_to_remove_elements) > 4:
        del list_to_remove_elements[4]
    if len(list_to_remove_elements) > 1:
        del list_to_remove_elements[0]

    return list_to_remove_elements

def add_elements(list_to_add_elements):
    new_list = list_to_add_elements[:]
    new_list.insert(0, 'Pink')
    new_list.append('Yellow')

    return new_list


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return len(list_to_check) == 0
    else:
        return len(list_to_check) == 0



def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) > 2 and len(list_to_compare2) > 2:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
    else:
        return False

def list_of_lists(list_of_lists_to_modify):
    new_list = []
    new_list.append(list_of_lists_to_modify[0][:2])
    new_list.append(list_of_lists_to_modify[1][1:4])
    new_list.append(list_of_lists_to_modify[2][-2:])
    return new_list
