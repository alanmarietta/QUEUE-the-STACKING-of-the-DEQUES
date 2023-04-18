from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  
  def push_front(self, val):
    # TODO replace pass with your implementation.
    # Use the head position for the front.

    # The big O notation of this method is O(n). We are using methods from Linked List
    # which will run in O(n) time.

    # If there are no items in the list we need to use append_element. We can use
    # insert_element_at if the list in non_empty. We also set the front as the new node
    if len(self.__list) == 0:
      front = self.__list.append_element(val)
    else:
      front = self.__list.insert_element_at(val, 0)
  
  def pop_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    
    # The big O notation of this method is O(1). We will be using remove_element_at
    # for this method and it will always be going to the 0th index.

    # Check to see if the list is empty before trying to do anything
    if len(self.__list) == 0:
      return
    else:
      val = self.__list.remove_element_at(0)
      # Make sure there is a node in the list we can change front to
      if len(self.__list) != 0:
        front = self.__list.get_element_at(0)
      return val

  def peek_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    
    # Big O notation of this method is O(1). We utilize the get_element_at method here which
    # only ever have to go to the 0th index

    # First check and see if there is anything in the list
    if len(self.__list) == 0:
      return
    else:
      x = self.__list.get_element_at(0)
      return x

  def push_back(self, val):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    
    # Big O notation of this method is O(n). The original append_element method is O(n)
    # so this method will differ in run time based on how many nodes are in the linked list.

    # We can use append_element here even if the list is empty becaues append_element
    # always inserts at the back. We set the back to the new node.
    back = self.__list.append_element(val)
  
  def pop_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.

    # The big O notation of this method is O(n). We will be using remove_element_at
    # for this method which has a run time that differs based on how many terms are in
    # the linked list

    # Check to see if the list is empty before trying to do anything
    if len(self.__list) == 0:
      return
    else:
      val = self.__list.remove_element_at(len(self.__list) - 1)
      # Make sure there is a node in the list we can change front to
      if len(self.__list) != 0:
        back = self.__list.get_element_at(len(self.__list) - 1)
      return val
  
  def peek_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.

    # Big O notation of this method is O(n). We utilize the get_element_at method and len here which
    # will have to iterate through the index to get to the last value.
    
    # First check and see if there is anything in the list
    if len(self.__list) == 0:
      return
    else:
      x = self.__list.get_element_at(len(self.__list) - 1)
      return x

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
