from math import ceil
class Pagination:

    def __init__(self, items = None, page_size = 10):
        self.items = items
        self.page_size = page_size
        self.total_pages = ceil(len(self.items)/self.page_size)
        self.current_page = 1

    def get_visible_items(self):
        print(self.items[self.current_page:self.page_size])
        return(self)        
    
    def next_page(self):
        self.current_page += 1
        self.get_visible_items()
        return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items().next_page())
# print(p.next_page())