import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # Deque tests

  # push_front tests
  def test_push_front_oneinteger(self):
    self.__deque.push_front(5)
    self.assertEqual('[ 5 ]', str(self.__deque))

  def test_push_front_twointeger(self):
    self.__deque.push_front(5)
    self.__deque.push_front(2)
    self.assertEqual('[ 2, 5 ]', str(self.__deque))

  def test_push_front_threeinteger(self):
    self.__deque.push_front(5)
    self.__deque.push_front(2)
    self.__deque.push_front(6)
    self.assertEqual('[ 6, 2, 5 ]', str(self.__deque))

  def test_push_front_onestring(self):
    self.__deque.push_front('Data')
    self.assertEqual('[ Data ]', str(self.__deque))

  def test_push_front_twostring(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    self.assertEqual('[ Structures, Data ]', str(self.__deque))

  def test_push_front_twostringandnone(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    self.__deque.push_front(None)
    self.assertEqual('[ None, Structures, Data ]', str(self.__deque))

  # push_back tests
  def test_push_back_oneinteger(self):
    self.__deque.push_back(5)
    self.assertEqual('[ 5 ]', str(self.__deque))

  def test_push_back_twointeger(self):
    self.__deque.push_back(5)
    self.__deque.push_back(2)
    self.assertEqual('[ 5, 2 ]', str(self.__deque))

  def test_push_back_threeinteger(self):
    self.__deque.push_back(5)
    self.__deque.push_back(2)
    self.__deque.push_back(6)
    self.assertEqual('[ 5, 2, 6 ]', str(self.__deque))

  def test_push_back_onestring(self):
    self.__deque.push_back('Data')
    self.assertEqual('[ Data ]', str(self.__deque))

  def test_push_back_twostring(self):
    self.__deque.push_back('Data')
    self.__deque.push_back('Structures')
    self.assertEqual('[ Data, Structures ]', str(self.__deque))

  def test_push_back_twostringandnone(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    self.__deque.push_front(None)
    self.assertEqual('[ Data, Structures, None ]', str(self.__deque))

  # pop_front tests
  def test_pop_front_oneinteger(self):
    self.__deque.push_front(2)
    returned = self.__deque.pop_front()
    self.assertEqual(2, returned)
  
  def test_pop_front_twointeger(self):
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    returned = self.__deque.pop_front()
    self.assertEqual(3, returned)
    
  def test_pop_front_twice_twointeger(self):
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.__deque.pop_front()
    returned = self.__deque.pop_front()
    self.assertEqual(2, returned)
  
  def test_pop_front_twostring(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    returned =  self.__deque.pop_front()
    self.assertEqual('Structures', returned)
      
  def test_pop_front_twice_twostring(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    self.__deque.pop_front()
    returned =  self.__deque.pop_front()
    self.assertEqual('Data', returned)
    
  def test_pop_front_twostringnone(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    self.__deque.push_front(None)
    returned =  self.__deque.pop_front()
    self.assertEqual(None, returned)

    # pop_back tests
  def test_pop_back_oneinteger(self):
    self.__deque.push_front(2)
    returned = self.__deque.pop_back()
    self.assertEqual(2, returned)
  
  def test_pop_back_twointeger(self):
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    returned = self.__deque.pop_back()
    self.assertEqual(2, returned)
    
  def test_pop_back_twice_twointeger(self):
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.__deque.pop_back()
    returned = self.__deque.pop_back()
    self.assertEqual(3, returned)
  
  def test_pop_back_twostring(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    returned =  self.__deque.pop_back()
    self.assertEqual('Data', returned)
      
  def test_pop_back_twice_twostring(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    self.__deque.pop_back()
    returned =  self.__deque.pop_back()
    self.assertEqual('Structures', returned)
    
  def test_pop_back_twostringnone(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    self.__deque.push_front(None)
    returned =  self.__deque.pop_back()
    self.assertEqual('Data', returned)
  
  # peek_front tests
  def test_peek_front_oneinteger(self):
    self.__deque.push_front(2)
    returned = self.__deque.peek_front()
    self.assertEqual(2, returned)
  
  def test_peek_front_twointeger(self):
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    returned = self.__deque.peek_front()
    self.assertEqual(3, returned)
    
  def test_peek_front_twostring(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    returned =  self.__deque.peek_front()
    self.assertEqual('Structures', returned)
    
  def test_peek_front_twostringnone(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    self.__deque.push_front(None)
    returned =  self.__deque.peek_front()
    self.assertEqual(None, returned)

  # peek_back tests
  def test_peek_back_oneinteger(self):
    self.__deque.push_front(2)
    returned = self.__deque.peek_back()
    self.assertEqual(2, returned)
  
  def test_peek_back_twointeger(self):
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    returned = self.__deque.peek_back()
    self.assertEqual(2, returned)
    
  def test_peek_back_twostring(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    returned =  self.__deque.peek_back()
    self.assertEqual('Data', returned)
    
  def test_peek_back_twostringnone(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    self.__deque.push_front(None)
    returned =  self.__deque.peek_back()
    self.assertEqual('Data', returned)
  
  # push_front and push_back tests
  def test_push_frontandback_twointegers(self):
    self.__deque.push_front(1)
    self.__deque.push_back(2)
    self.assertEqual('[ 1, 2 ]', str(self.__deque))

  def test_push_frontandback_threeintegers(self):
    self.__deque.push_front(1)
    self.__deque.push_back(2)
    self.__deque.push_back(3)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__deque))

  def test_push_frontandback_twostrings(self):
    self.__deque.push_front('Data')
    self.__deque.push_back('Structures')
    self.assertEqual('[ Data, Structures ]', str(self.__deque))

  def test_push_frontandback_twostringsnone(self):
    self.__deque.push_front('Data')
    self.__deque.push_back('Structures')
    self.__deque.push_front(None)
    self.assertEqual('[ None, Data, Structures ]', str(self.__deque))

  # len tests
  def test_len_frontandback_twointegers(self):
    self.__deque.push_front(1)
    self.__deque.push_back(2)
    self.assertEqual(2, len(self.__deque))

  def test_len_frontandback_threeintegers(self):
    self.__deque.push_front(1)
    self.__deque.push_back(2)
    self.__deque.push_back(3)
    self.assertEqual(3, len(self.__deque))

  def test_len_frontandback_twostrings(self):
    self.__deque.push_front('Data')
    self.__deque.push_back('Structures')
    self.assertEqual(2, str(self.__deque))

  def test_len_frontandback_twostringsnone(self):
    self.__deque.push_front('Data')
    self.__deque.push_back('Structures')
    self.__deque.push_front(None)
    self.assertEqual(3, str(self.__deque))

  def test_len_front_oneinteger(self):
    self.__deque.push_front(2)
    returned = self.__deque.pop_front()
    self.assertEqual(2, returned)
  
  def test_len_front_twointeger(self):
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    returned = self.__deque.pop_front()
    self.assertEqual(3, returned)
    
  def test_len_front_twice_twointeger(self):
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.__deque.pop_front()
    self.assertEqual(1, len(self.__deque))
      
  def test_len_front_twice_twostring(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque))
    
  def test_len_front_twostringnone(self):
    self.__deque.push_front('Data')
    self.__deque.push_front('Structures')
    self.__deque.push_front(None)
    self.__deque.pop_front()
    self.assertEqual(2, len(self.__deque))

  # Stack tests, len and str are in this, but not labeled individually

  # Push test
  def test_push_oneinteger(self):
    self.__stack.push(1)
    self.assertEqual(1,len(self.__stack))
  
  def test_push_twointeger(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.assertEqual(2,len(self.__stack))

  def test_push_threeinteger(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.push(3)
    self.assertEqual(3,len(self.__stack))
  
  def test_push_onestring(self):
    self.__stack.push('Data')
    self.assertEqual(1, len(self.__stack))

  def test_push_twostring(self):
    self.__stack.push('Data')
    self.__stack.push('Structures')
    self.assertEqual('[ Structures, Data ]', str(self.__stack))

  def test_push_twostringandnone(self):
    self.__stack.push('Data')
    self.__stack.push('Structures')
    self.__stack.push(None)
    self.assertEqual('[ None, Structures, Data ]', str(self.__stack))

    # Pop tests
  def test_pop_oneinteger(self):
    self.__stack.push(1)
    returned = self.__stack.pop()
    self.assertEqual(1, returned)
  
  def test_pop_twointeger(self):
    self.__stack.push(1)
    self.__stack.push(2)
    returned = self.__stack.pop()
    self.assertEqual(2, returned)
    
  def test_pop_twice_twointeger(self):
    self.__stack.push(2)
    self.__stack.push(3)
    self.__stack.pop()
    returned = self.__stack.pop()
    self.assertEqual(2, returned)
  
  def test_pop_twostring(self):
    self.__stack.push('Data')
    self.__stack.push('Structures')
    self.__stack.pop()
    returned = self.__stack.pop()
    self.assertEqual('Data', returned)
      
  def test_pop__string(self):
    self.__stack.push('Data')
    self.__stack.push('Structures')
    returned =  self.__stack.pop_back()
    self.assertEqual('Structures', returned)
    
  def test_pop_twostringnone(self):
    self.__stack.push('Data')
    self.__stack.push('Structures')
    self.__stack.push(None)
    returned =  self.__stack.pop_back()
    self.assertEqual(None, returned)
  
  # Peek tests
  def test_peek_oneinteger(self):
    self.__stack.push(1)
    returned = self.__stack.peek()
    self.assertEqual(1, returned)
  
  def test_peek_twointeger(self):
    self.__stack.push(1)
    self.__stack.push(2)
    returned = self.__stack.peek()
    self.assertEqual(2, returned)
    
  def test_peek_twice_twointeger(self):
    self.__stack.push(2)
    self.__stack.push(3)
    self.__stack.peek()
    returned = self.__stack.peek()
    self.assertEqual(3, returned)
  
  def test_peek_twostring(self):
    self.__stack.push('Data')
    self.__stack.push('Structures')
    returned = self.__stack.peek()
    self.assertEqual('Structures', returned)
      
  def test_peek__string(self):
    self.__stack.push('Data')
    returned =  self.__stack.peek()
    self.assertEqual('Data', returned)
    
  def test_peek_twostringnone(self):
    self.__stack.push('Data')
    self.__stack.push('Structures')
    self.__stack.push(None)
    returned =  self.__stack.peek()
    self.assertEqual(None, returned)

  # Push and pop tests
  def test_pushpop_oneinteger(self):
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual('[ ]',str(self.__stack))

  def test_pushpop_twointeger(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.pop()
    self.assertEqual('[ 1 ]',str(self.__stack))

  def test_pushpop_threeinteger(self):
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.push(3)
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('[ 1 ]',str(self.__stack))

  def test_pushpop_twostring(self):
    self.__stack.push('Data')
    self.__stack.push('Structures')
    self.__stack.pop()
    self.assertEqual('[ Data ]', str(self.__stack))

  def test_pushpop_twostringandnone(self):
    self.__stack.push('Data')
    self.__stack.push('Structures')
    self.__stack.push(None)
    self.__stack.pop()
    self.assertEqual('[ Structures, Data ]', str(self.__stack))

  # Queue tests, len and str tested in here too, but not individually

  # Enqueue tests
  def test_enqueue_oneinteger(self):
    self.__queue.enqueue(1)
    self.assertEqual(1,len(self.__queue))
  
  def test_enqueue_twointeger(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.assertEqual(2,len(self.__queue))

  def test_enqueue_threeinteger(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    self.assertEqual(3,len(self.__queue))
  
  def test_enqueue_onestring(self):
    self.__queue.enqueue('Data')
    self.assertEqual(1,len(self.__queue))

  def test_enqueue_twostring(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.assertEqual([' Data, Structures '],str(self.__queue))

  def test_enqueue_twostringandnone(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.enqueue(None)
    self.assertEqual([' Data, Structures, None '],str(self.__queue))

   # Dequeue Tests

  def test_dequeue_oneinteger(self):
    self.__queue.enqueue(1)
    returned = self.__queue.dequeue()
    self.assertEqual(1, returned)
  
  def test_dequeue_twointeger(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    returned = self.__queue.dequeue()
    self.assertEqual(2, returned)
    
  def test_dequeuetwice_twointeger(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.dequeue()
    returned = self.__queue.dequeue()
    self.assertEqual(1, returned)

  def test_dequeue_twostring(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.dequeue()
    returned = self.__queue.dequeue()
    self.assertEqual('Data', returned)
      
  def test_dequeue_string(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    returned = self.__queue.dequeue()
    self.assertEqual('Structures', returned)
    
  def test_dequeue_twostringnone(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.enqueue(None)
    returned = self.__queue.dequeue()
    self.assertEqual(None, returned)

  # Peek Tests

  def test_peek_oneinteger(self):
    self.__queue.enqueue(1)
    returned = self.__queue.peek()
    self.assertEqual(1,returned)
  
  def test_peek_twointeger(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    returned = self.__queue.peek()
    self.assertEqual(1,len(self.__queue))

  def test_peek_threeinteger(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    returned = self.__queue.peek()
    self.assertEqual(1,returned)
  
  def test_peek_onestring(self):
    self.__queue.enqueue('Data')
    returned = self.__queue.peek()
    self.assertEqual('Data',returned)

  def test_peek_twostring(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    returned = self.__queue.peek()
    self.assertEqual('Data',returned)

  def test_enqueue_twostringandnone(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.enqueue(None)
    returned = self.__queue.peek()
    self.assertEqual('Data',returned)

  # Enqueue and Dequeue Tests
  def test_EQDQ_oneinteger(self):
    self.__queue.enqueue(1)
    self.__queue.dequeue()
    self.assertEqual('[ ]',str(self.__queue))

  def test_EQDQ_twointeger(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.dequeue()
    self.assertEqual('[ 1 ]',str(self.__queue))

  def test_EQDQ_threeinteger(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.dequeue()
    self.__queue.enqueue(3)
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual('[ ]',str(self.__queue))

  def test_EQDQ_twostring(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.dequeue()
    self.assertEqual('[ Data ]', str(self.__queue))

  def test_pushpop_twostringandnone(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.enqueue(None)
    self.__queue.dequeue()
    self.assertEqual('[ Data, Structures ]', str(self.__queue))
    
if __name__ == '__main__':
  unittest.main()

