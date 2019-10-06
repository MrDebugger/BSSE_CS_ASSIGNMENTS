#Task 2
class Bag:
    def __init__(self,items):
        self.items = items
    def numOf(self,item):
        return self.items.count(item)
    def __iter__(self):
        return iter(self.items)

bag = Bag(['Book','Book','Book','Pen','Pencil','Pen','Note Book','Note Book','Note Book'])
while True:
    print("[+] Following are the items in a bag:")
    print(', '.join(bag))
    print("[?] Enter item to find the number of occurence in bag or X to exit.")
    item = input("[>] Item (Case Sensitive): ")
    if item.lower() == 'x':
        break
    else:
        print("[+] Number of occurence of [",item,"] in bag is",bag.numOf(item),end="\n\n")
