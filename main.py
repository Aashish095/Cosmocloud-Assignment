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

def merge_lists(list_1, list_2) -> list:
    # Initialize an empty list to hold the merged data
    merged = []
    
    # Iterate through each item in list_1
    for item1 in list_1:
        found = False
        
        # Iterate through each item in list_2
        for item2 in list_2:
            # If the "id" key in item1 matches the "id" key in item2
            if item1["id"] == item2["id"]:
                # Merge the information in item1 and item2
                item2.update(item1)
                # Append the merged item to the list
                merged.append(item2)
                # Set the found flag to True and break out of the loop
                found = True
                break
        
        # If the item1 id was not found in list_2, append it to the merged list
        if not found:
            merged.append(item1)
    
    # Iterate through each item in list_2
    for item2 in list_2:
        found = False
        
        # Iterate through each item in list_1
        for item1 in list_1:
            # If the "id" key in item2 matches the "id" key in item1
            if item2["id"] == item1["id"]:
                # Set the found flag to True and break out of the loop
                found = True
                break
        
        # If the item2 id was not found in list_1, append it to the merged list
        if not found:
            merged.append(item2)
    
    # Print the merged list (optional)
    print(merged)
    
    # Return the merged list
    return merged


list_3 = merge_lists(list_1, list_2)
