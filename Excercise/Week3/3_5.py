collection = {}

def update_record(dict, id, property, value):
    # Check if id is not in target dictionary
    if id not in dict:
        return dict
        # dict.update({id: {}})

    # Check if user's input is empty string then remove the following property
    if value == '':
        dict[id].pop(property, None)
        return dict

    if property != 'tracks':
        dict[id].update({property: value})

    if property == 'tracks':
        if 'tracks' not in dict[id]:
            dict[id].update({'tracks': [value]})
        else:
            dict[id]['tracks'].append(value) 
        
    return dict

update_record(collection, 1234, 'artistName', 'Oak')
update_record(collection, 12345, 'artistName2', 'Pooh')
update_record(collection, 1234, 'tracks', 'Song1')
update_record(collection, 1234, 'tracks', 'Song2')
update_record(collection, 1234, 'year', '2004')
update_record(collection, 1234, 'tracks', '')
update_record(collection, 1234, 'year', '2009')
update_record(collection, 1234, 'tracks', 'Song3')
print(collection)

