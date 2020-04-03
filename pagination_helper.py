# For this exercise you will be strengthening your page-fu mastery. You will complete the 
# PaginationHelper class, which is a utility class helpful for querying paging information 
# related to an array.

# The class is designed to take in an array of values and an integer indicating how many 
# items will be allowed per each page. The types of values contained within the collection/array 
# are not relevant.


class PaginationHelper:
    
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        remainder = len(self.collection) % self.items_per_page
        non_remainder = (len(self.collection) - remainder) / self.items_per_page
        if remainder > 0:
            return non_remainder +1
        else:
            return non_remainder
    
    
    # the below helper method creates a dictionary with pages as keys and their respective 
    # items clumped into lists as values    
    def dict_creator(self):
        # three cheers for nested comprehensions
        page_dict = {each:[] for each in [each for each in range(int(self.page_count()))]}
        coll_list = list(self.collection)
        i = 0
        # the following five lines attempt to mirror how one might deal with sorting things
        # in real life, like taking things out of one big box and sorting them into smaller
        # boxes.  the thing sorted into the smaller box is no longer in the big box (line 48).  once 
        # the current smaller box is full, you move on to the next smaller box (lines 49-50).  as long 
        # as I keep removing the first element in the collection list I don't have to actually iterate 
        # through the it.  once the collection list is empty, the sorting is done and the loop stops (line 46).
        # I now have a nice sorted dictionary I can use elsewhere.
        while len(coll_list) > 0:
            page_dict[i].append(coll_list[0])
            coll_list.remove(coll_list[0])
            if len(page_dict[i]) == self.items_per_page:
                i += 1
        return page_dict

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        try:
            return len(self.dict_creator()[page_index])
        except KeyError:
            return -1
            

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index >= 0:
            try:
                the_item = [each for each in self.collection][item_index]
                page_dict_reborn = self.dict_creator()
                for key, value in page_dict_reborn.items():
                    if the_item in value:
                        return key
            except IndexError:
                return -1
        else:
            return -1