from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    return str(self.__dq)

  def __len__(self):
    return len(self.__dq)

  def push(self, val):
    self.__dq.push_front(val)

  def pop(self):
    x = self.__dq.pop_front()
    return x

  def peek(self):
    x = self.__dq.peek_front()
    return x