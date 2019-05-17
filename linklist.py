#link list
class node:
  def __init__(self,x):
    self.data=x
    self.next=None
class sll:
  def __init__(self):
    self.head=None
  def insertAtBeg(self):
    val=int(input())
    newnode=node(val)
    newnode.nextt=self.head
    self.head=newnode
  def insertAtEnd(self):
    v=int(input())
    new=node(v)
    temp=self.head
    while temp.nextt=None:
      temp=temp.nextt
    if temp.nextt=None:
      temp.nextt=new  

  def delete(self):
    temp=self.head
    self.head=temp.next
    temp.next=None
  def deletegiven(self):
    v=input()
    temp=self.head
    d=temp.data
    prev=temp
    if self.head.data==v:
      self.head=self.head.nextt
      temp.nextt=None
    while temp.data!=v and temp.nextt!=None:
      prev=temp
      temp=temp.nextt
    if temp.data==v:
      prev.nextt=temp.nextt
      temp.nextt=None   
  
  def deletionAtEnd(self):
    temp=self.head
    prev=temp
    while temp.nextt!=None:
      prev=temp
      print(prev.data)
      temp=temp.nextt
    if temp.nextt=None:
      prev.nextt=None
  def deletenodeAtBeg(self):
    temp=self.head
    self.head=temp.nextt
    temp.nextt=None
  def Search(self):
    v=int(input())
    temp=self.head
    p=1
    while temp.data!=v and temp.nextt!=None:
      temp=temp.nextt
      p+=1
    if temp.data==v:
      print("found",p)
    else:
      print("not found") 
  def insertAtM(self):
    v=int(input())
    temp=self.headpos=1
    while pos<v:
      temp=temp.nextt
      pos+=1
    if v==pos:
      val=int(input())
      new=node(val)
      new.nextt=temp.nextt
      temp.nextt=new  



      
  def display(self):
    temp=self.head
    while temp!=None:
      print(temp.data,end=" ")
      temp=temp.next   
sl1=sll()
ch=0
while ch!=9:
  print("1.inserAtBeg 2.insertAtM 3.insertAtEnd 4.search 5.display 6.delAtBeg 7.delAtEnd 8.delGiven 9.exit")
  ch=int(input())
  if ch==1:
    sl1.insertAtBeg()
    sl1.display()
  elif ch==2:
    sl1.insertAtM()
    sl1.display()
  elif ch==3:
      sl1.insertAtEnd()
    sl1.display()
  elif ch==4:
      sl1.deletionAtEnd()
    sl1.display()
  elif ch==5:
      sl1.delgiven()
    sl1.display()
  elif ch==6:
      sl1.deletenodeAtBeg()
    sl1.display()
  elif ch==7:
      sl1.search()
    sl1.display()
  elif ch==8:
      
    sl1.display()
  else:
      print("invalid choice")
    
      
