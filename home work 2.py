# one way linkedlist Mahan Kiyani (data structure project Dr.Eskandari)

import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linklist:
    def __init__(self):
        self.head = None

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end= ' -> ')
            t = t.next  
        print('None')

    def instart(self, b):
        n = Node(b)    
        n.next = self.head
        self.head = n
        
    def inend(self, d):
        n = Node(d)
        if self.head is None:
            self.head = n
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = n
  
    def inafter(self, m, d):
        n = Node(d)
        n.next = m.next
        m.next = n
    
    def remove_node(self, d):
        t = self.head
        if t is not None:
            if t.data == d:
                self.head = t.next
                t = None
                return
        while t is not None:
            if t.data == d:
                break
            p = t
            t = t.next
        if t == None:
            return
        p.next = t.next
        t = None
        
def add_item():
    global l
    l = linklist()
    while True:
        x = int(input('N :'))
        l.instart(x)

        use = input('edame midi? y/n: ').lower()
        if use.startswith('n'):
            break
    return l

def chap():
    try:
        print(f'\nyour linkedlist is {l.display()}\n')
    except NameError:
        print('** please add item in linkedlist **\n')

def zarb():
    for i in range(n,n+1):
        for j in range(a,a+1):
            print(i*j)
def jam():
def main():

    while True:
        try:
            print(' 1)Add item\n','2)zarb\n','3)jam\n','4)chap\n','5)Exit program')

            value = int(input('*adad monaseb ra vared konid:'))
            print('\n')

        except TypeError:
            continue
        
        match value:
            case 1:
                l = add_item()
            case 2:
                zarb()
            case 3:
                jam()
            case 4:
                chap()
            case 5:
                sys.exit('Good bye')