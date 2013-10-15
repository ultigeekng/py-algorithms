#!/usr/bin/env python
class DListNode(object):
    """Doubly-linked list node"""
    def __init__(self, my_data=None):
        self.nex = None
        self.pre = None
        self.data = my_data

    def GetNextNode(self):
        return self.nex

    def getPrevNode(self):
        return self.pre

    def SetNextNode(self,next_node):
        self.next = next_node

    def SetPreviousNode(self,prev_node):
        self.pre = prev_node

    def GetData(self):
        return self.data

    def SetData(self,my_data):
        self.data = my_data


class DList(object):
  """Creating the double liked list"""
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def insert(self, data):
    """Inserting new node to the linked list"""
    new_node = DListNode(data)
    if self.head == None:
      self.head = new_node
      self.tail = self.head
    elif self.head == self.tail and self.head != None:
      self.head.nex = new_node
      self.tail = new_node
      self.tail.pre = self.head
    else:
      self.tail.nex = new_node
      new_node.pre = self.tail
      self.tail = new_node
    self.length += 1

  def appendLeft(self, data):
    """Appending a new element in left side (before head)"""
    new_node = DListNode(data)
    if self.head == None:
      self.head = new_node
      self.tail = self.head
    elif self.head == self.tail and self.head != None:
      self.head.pre = new_node
      new_node.nex = self.head
      self.tail = self.head
      self.head = new_node
    else:
      self.head.pre = new_node
      new_node.nex = self.head
      self.head = new_node
    self.length += 1

  def insertNextTo(self, data, element_data):
    """Inserts a new element next to the given element"""
    given_element = self.getElement(data)
    new_node = DListNode(element_data)
    new_node.nex = given_element.nex
    given_element.nex = new_node
    new_node.pre = given_element
    given_element.nex.pre = new_node
    

  def printDList(self):
    """Printing the hole double linked list"""
    current_node = self.head
    out_put = ''
    while current_node is not None:
      out_put += " " + str(current_node.data)
      current_node = current_node.nex
      #if current_node.nex is None:
      #  break
    print out_put

  def getElement(self, element_data):
    """Returns a first matching elemnt to the provided value"""
    current_node = self.head
    found_element = None
    while current_node.nex is not None:
      if element_data == current_node.data:
        found_element = current_node
        return current_node
      current_node = current_node.nex
    if found_element is None:
      raise "No element found"


if __name__ == "__main__":
    add_node = DList()
    for x in range(10):
      if x == 3:
        add_node.appendLeft(x + 1)
      elif x == 5:
        add_node.insertNextTo(2, x + 1)
      else:
        add_node.insert(x + 1)
    add_node.printDList()
