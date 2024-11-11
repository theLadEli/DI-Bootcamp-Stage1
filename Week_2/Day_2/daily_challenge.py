class Pagination:

    def __init__(self, items = None, page_size = 10):
        self.items = items
        self.page_size = page_size
        self.items_to_list = []
        self.page_min = 0

    def get_visible_items(self):
        for l in self.items[self.page_min:self.page_size]:
            self.items_to_list.append(l)
        self.items = self.items_to_list
    
    def next_page(self):
        self.page_size += 4
        self.page_min = 0
        print(self.items)


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.items)
# print(p.next_page())