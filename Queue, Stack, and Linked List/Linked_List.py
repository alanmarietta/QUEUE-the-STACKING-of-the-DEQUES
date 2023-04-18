class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Add in a value section, previous, and next. Initialized to None because this is defining the Node.
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        self.__size = 0
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.next = None
        self.__header.prev = None
        self.__trailer.prev = self.__header
        self.__iter_index = None

    def __len__(self):
        return self.__size

    def append_element(self, val):
        new = self.__Node(val)
        if self.__header.next == self.__trailer:
            self.__header.next = new
            new.next = self.__trailer
            new.prev = self.__header
            self.__trailer.prev = new
        else:
            cur = self.__header
            switch = True
            while switch == True:
                if cur.next == self.__trailer:
                    switch = False
                else:
                    cur = cur.next
            cur.next = new
            new.prev = cur
            self.__trailer.prev = new
            new.next = self.__trailer
        self.__size = self.__size + 1

    def insert_element_at(self, val, index):
        new = self.__Node(val)
        if index == self.__size or index < 0:
            raise IndexError
        else:
            cur = self.__header
            cur2 = self.__header
            for i in range(0,index):
                cur = cur.next
            for i in range (0, index + 1):
                cur2 = cur2.next
            new.next = cur2
            new.prev = cur
            cur.next = new
            cur2.prev = new
            self.__size = self.__size + 1


    def remove_element_at(self, index):
        if index >= self.__size or index < 0:
            raise IndexError
        else:
            cur = self.__header
            cur2 = self.__header
            cur3 = self.__header
            for i in range(0, index):
                cur3 = cur3.next
            for i in range(0, index + 1):
                cur = cur.next
            for i in range(0, index + 2):
                cur2 = cur2.next
            node_val = cur.val
            cur3.next = cur2
            cur2.prev = cur3
            cur.next = None
            cur.prev = None
            self.__size = self.__size - 1
            return node_val
        



    def get_element_at(self, index):
        if index >= self.__size  or index < 0:
            raise IndexError
        else:
            cur = self.__header
            for i in range(0, index + 1):
                cur = cur.next
            node_val = cur.val
            return node_val

    def rotate_left(self):
        if self.__size == 0 or self.__size == 1:
            return
        else:
            cur = self.__header
            cur2 = self.__header
            cur3 = self.__header
            for i in range (0,1):
                cur = cur.next
            for i in range (0,2):
                cur2 = cur2.next
            for i in range (0,self.__size):
                cur3 = cur3.next
            cur.prev = cur3
            cur.next = self.__trailer
            self.__trailer.prev = cur
            cur3.next = cur
            self.__header.next = cur2
            cur2.prev = self.__header
            
        
    def __str__(self):
        content =  '['
        if self.__size == 0:
            return '[ ]'
        else:
            cur = self.__header
            for i in range(0, self.__size + 1):
                cur = cur.next
                if cur != self.__trailer:
                    added = " " + str(cur.val) + ','
                    content += added
            content += ' ]'
            content = content[:-3] + content[-2:]
            return content

    def __iter__(self):
        self.__iter_index = self.__header.next
        return self

    def __next__(self):
        if self.__iter_index == self.__trailer:
            raise StopIteration
        else:
            to_return = self.__iter_index.val
            self.__iter_index = self.__iter_index.next
            return to_return



    def __reversed__(self):
        new_list = Linked_List()
        number = self.__size - 1
        if self.__size == 0:
            return new_list
        else:
            while number >= 0:
                for x in range(0, self.__size):
                    new_list.append_element(self.get_element_at(number))
                    number = number - 1
                return new_list

if __name__ == '__main__':
     A = Linked_List()
     print(A)
     # testing out append
     A.append_element(1)
     A.append_element(2)
     A.append_element(3)
     print(A)

     # testing out insert element
     A = Linked_List()
     print(A)
     try:
         # should succeed
         A.insert_element_at(1,0)
         A.insert_element_at(2,1)
         A.insert_element_at(3,2)
         A.insert_element_at(4,2)
         print(A)
     except IndexError:
         print('index error')
     try:
         # should fail
         A.insert_element_at(1,-1)
     except IndexError:
        print('index error')
     try:
         # should fail
         A.insert_element_at(1,4)
     except IndexError:
        print('index error')


     # testing out remove_element_at
     A = Linked_List()
     try:
         # should succeed
         A.append_element(1)
         A.append_element(2)
         A.append_element(3)
         A.remove_element_at(1)
         print(A)
     except IndexError:
         print('index error')
     try:
        #should fail
        A.remove_element_at(0)
     except IndexError:
        print('index error')
    # testing get_element_at
     try:
         # should succeed
         A = Linked_List()
         A.append_element(1)
         A.append_element(2)
         A.append_element(3)
         A.get_element_at(2)
     except IndexError:
         print('index error')
     try:
         # should fail
         A.get_element_at(-1)
     except IndexError:
         print('index error')
    # testing rotate_left
     A = Linked_List()
     A.append_element(1)
     A.append_element(2)
     A.append_element(3)
     A.rotate_left
     print(A)
    # testing reversed
     print(A)
     print(reversed(A))