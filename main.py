list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]

def merge_lists(list_1, list_2):
    """
    Merge the information from list_1 and list_2 to create a new list, which has all the information about each student 
    from both lists in one single dict. 
    
    Args:
    - list_1: (list) a list of dictionaries representing student information
    - list_2: (list) a list of dictionaries representing student information
    
    Returns:
    - merged_list: (list) a list of dictionaries representing the merged information for each student
    
    """
    merged_list = []
    
    # Merge the two lists into a single list of dictionaries
    merged_dict = {}
    for d in list_1 + list_2:
        id = d.get('id')
        if id in merged_dict:
            # If the ID is already in the merged dict, update it with the new values
            merged_dict[id].update(d)
        else:
            # Otherwise, add a new entry to the merged dict
            merged_dict[id] = d
    
    # Convert the merged dict back into a list
    for id, d in merged_dict.items():
        merged_list.append(d)
    
    return merged_list

        
    
    # return list_3


list_3 = merge_lists(list_1, list_2)
