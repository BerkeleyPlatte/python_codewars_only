collection = range(1, 25)
items_per_page = 10

def page_count():
        remainder = len(collection) % items_per_page
        non_remainder = (len(collection) - remainder) / items_per_page
        if remainder > 0:
            return non_remainder +1
        else:
            return non_remainder
        
def dict_creator():
    page_dict = {each:[] for each in [each for each in range(int(page_count()))]}
    coll_list = list(collection)
    i = 0
    while len(coll_list) > 0:
        page_dict[i].append(coll_list[0])
        coll_list.remove(coll_list[0])
        if len(page_dict[i]) == items_per_page:
            i += 1
    return page_dict

def page_index(item_index):
        try:
            the_item = [each for each in collection][item_index]
            page_dict_reborn = dict_creator()
            for key, value in page_dict_reborn.items():
                if the_item in value:
                    return key
        except IndexError:
            return -1

print(page_index(3)) 