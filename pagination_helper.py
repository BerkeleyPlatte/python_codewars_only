# TODO: complete this class


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

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        page_dict = {each:[] for each in [each for each in range(int(page_count()))]}
        

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        pass


collection = range(1, 25)
helper = PaginationHelper(collection, 10)