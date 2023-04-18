from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # Capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # Initialize a front and a back
    self.__front = None
    self.__back = None
    # Add in something to keep track of number of items in deque
    self.__size = 0

  def __str__(self):
    # This method will run in O(n) time. It has to correctly output values
    # in order from front to back. The time used varies on how many variables
    # are in the array.
    content = '['
    if self.__size == 0:
      return '[ ]'
    else:
      content += " " + str(self.__contents[self.__front]) + ','
      front2 = self.__front
      # This part sorts by front and back to make sure front is outputted first
      for i in range(1, self.__size):
        content += " " + str(self.__contents[(front2 + 1) % self.__capacity]) + ','
        front2 = (front2 + 1) % self.__capacity
      # Finish off the final string  with a bracket and get rid of the last comma
      content += ' ]'
      content = content[:-3] + content[-2:]
      return content
    
  def __len__(self):
    # This method runs in O(1). It doesn't have to loop through anything and
    # instead just fetches one of the attributes.
    return self.__size

  def __grow(self):
    # This method will run in O(n) time. Although doubling the size is in O(1),
    # depending on how many values are in the deque, it will take O(n) to sort
    # them and then put them into the new array. It is necessary for the items to
    # start in cell 0 because we need to have more space to pop and push items.

    # Make a new array and double the capacity.
    new = self.__contents + [None] * self.__capacity
    self.__capacity = self.__capacity * 2
    # Copy over the values in the deque and sort them correctly from front to back
    new[0] = self.__contents[self.__front]
    for i in range(1, self.__size):
      new[i] = self.__contents[(self.__front + 1) % self.__size]
      self.__front = (self.__front + 1) % self.__size
    # Initialize front on the left and back to the right, make the new
    # array self.__contents
    self.__front = 0
    self.__back = self.__size - 1
    self.__contents = new

  def push_front(self, val):
    # This method will run in O(1) time. The amount of items in the array does
    # not affect the runtime of this method.

    # Checks to see if there is any room left in the array and
    # grows the array if there is not.
    if self.__size == self.__capacity:  
      self.__grow()
    # If there is only one space in the array we need to make sure the new
    # cell is both front and back
    if self.__capacity == 1:
      self.__contents[0] = val
      self.__front = 0
      self.__back = 0
    # If all is well then we put in a new value and change the front to its new index
    else:
      self.__front = (self.__front - 1 + self.__capacity) % self.__capacity
      self.__contents[self.__front] = val
    # Increase size by one because we added in one item.
    self.__size += 1
    
  def pop_front(self):
    # This method will run in O(1) time. No matter how many items are in the array
    # the method will run in constant time.

    # Checks to see if the array is empty
    if self.__size == 0:
      return
    # If the array only has one space, we remove the value and set front and back
    # to None
    if self.__capacity == 1:
      val = self.__contents[self.__front]
      self.__contents[self.__front] = None
      self.__back = None
      self.__front = None
      self.__size -= 1
      return val
    # If there are no special cases we just go ahead as normal and set the back
    # value to None and change where back is pointing to.
    else:
      val = self.__contents[self.__front]
      self.__contents[self.__front] = None
      self.__front = (self.__front + 1) % self.__capacity
      self.__size -= 1
      return val
    
  def peek_front(self):
    # This method will run in O(1) time. The amount of items in the array does
    # not affect the runtime of this method.

    # First check to see if there is anything in the array. If there's
    # not, we can go ahead use this method.
    if self.__size == 0:
      return
    else:
      return self.__contents[self.__front]
    
  def push_back(self, val):
    # This method will run in O(1) time. The amount of items in the array does
    # not affect the runtime of this method.
    
    # Checks to see if there is any room left in the array and
    # grows the array if there is not.
    if self.__size == self.__capacity:  
      self.__grow()
    # If there is only one space in the array we need to make sure the new
    # cell is both front and back
    if self.__capacity == 1:
      self.__contents[0] = val
      self.__front = 0
      self.__back = 0
    # If all is well then we put in a new value and change the back to its new index
    else:
      self.__back = (self.__back + 1) % self.__capacity
      self.__contents[self.__back] = val
    # Increase size by one because we added in one item.
    self.__size += 1
  
  def pop_back(self):
    # This method will run in O(1) time. No matter how many items are in the array
    # the method will run in constant time.

    # Checks to see if the array is empty
    if self.__size == 0:
      return
    # If the array only has one space, we remove the value and set front and back
    # to None
    if self.__capacity == 1:
      val = self.__contents[self.__back]
      self.__contents[self.__back] = None
      self.__back = None
      self.__front = None
      self.__size -= 1
      return val
    # If there are no special cases we just go ahead as normal and set the back
    # value to None and change where back is pointing to.
    else:
      val = self.__contents[self.__back]
      self.__contents[self.__back] = None
      self.__back = (self.__back - 1 + self.__capacity) % self.__capacity
      self.__size -= 1
      return val
      
  def peek_back(self):
    # This method will run in O(1) time. The amount of items in the array does
    # not affect the runtime of this method.

    # First check to see if there is anything in the array. If there's
    # not, we can go ahead use this method.
    if self.__size == 0:
      return
    else:
      return self.__contents[self.__back]

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
