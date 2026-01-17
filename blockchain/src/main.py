"""
Docstring for blockchain.src.main
as i am making it for govemment we need few fields:
  sender
  reciever
  time_stamp
  amount
  prev_hash
  hash (current hash)
  agreement
"""
import datetime
from util.hash import generate_hash
class Block:
  def __init__(self, sender, receiver, time_stamp, amount, prev_hash, current_hash, agreement):
    self.sender = sender
    self.receiver = receiver
    self.time_stamp = time_stamp
    self.amount = amount
    self.__prev_hash = prev_hash
    self.__current_hash = current_hash
    self.agreement = agreement

  def get_prev_hash(self):
      return self.__prev_hash

  def get_current_hash(self):
      return self.__current_hash
    
class BlockChain:
  def __init__(self):
    self.chain = []

  def create_genisis_block(self):
    """
    this function creates the genisis block. The genisis block is the 1st block in a blockchain and has some predefault features like:
      1. initial message
      2. sender = system
      3. reciever = None
      4. transaction = None
    """
    date = datetime.datetime.now()
    agreement = f"This block was created on: {date}" 
    _hash = generate_hash(f"{date}{agreement}")
    block = Block(time_stamp=date, agreement=agreement, prev_hash=None, current_hash=_hash, sender="System", receiver=None, amount=None)
    self.chain.append(block)
  
  def add_block(self, sender, reciever, amount):
    date = datetime.datetime.now()
    prev_hash = self.chain[len(self.chain)-1].get_current_hash()
    agreement = f"{sender} sends {amount}-/ to {reciever} on {date}"
    current_hash = agreement + prev_hash
    new_block = Block(sender=sender, receiver=reciever, time_stamp=date,amount=amount,prev_hash=prev_hash, current_hash=current_hash,agreement=agreement)

    self.chain.append(new_block)
  
blockChain = BlockChain()
blockChain.create_genisis_block()
blockChain.add_block("Saumya","Roshan",1322)

for block in blockChain.chain:
  print(block.time_stamp)
  print(block.agreement)
  print(block.sender)
  print(block.receiver)
  print("-------")