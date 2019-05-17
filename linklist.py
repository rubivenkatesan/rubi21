#rubiclass node:
  def __init__(self,x):
    self.data=x
    self.next=None
class sll:
  def __init__(self):
    self.head=None
  def delete(self):
    temp=self.head
    self.head=temp.next
    temp.next=None
  def deletemid(self):
    val=input()
    temp=self.head
    d=temp.data
    prev=temp
  
    while d!=val and temp.next!=None:
      prev=temp
      temp=temp.next
    if d==val:
      prev.next=temp.next
      temp=None 
      
  def display(self):
    temp=self.head
    while temp!=None:
      print(temp.data,end=" ")
      temp=temp.next   
sl1=sll()
sl1.head=node("mon")
n2=node("tue")
n3=node("wed")
sl1.head.next=n2
n2.next=n3
sl1.deletemid()
sl1.display()

