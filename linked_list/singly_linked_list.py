class SNode:
  def __init__(self, info):
    self.data = info
    self.next = None
    
class SLList:
  def __init__(self):
    self.head = None
    self.tail = None
    
   def insert(self, key):
    node = SNode(key)
    if not self.head:
      self.head = node
     else:
      self.tail.next = node
      self.tail = node
