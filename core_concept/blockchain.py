class Block:
    def __init__(self, data, hash):
        self.data = data
        self.__hash = hash
        
    def get_hash(self):
        return self.__hash   

class BlockChain:
    genisis_hash = 100000001
    def __init__(self):
        self.chain = []
        
    def create_block(self, data):
        if self.chain:
            print("Genisis block already decleared!")
            return
        genisis_block = Block(data, self.genisis_hash)
        self.chain.append(genisis_block)
        
    def add_block(self,data,prev_hash):
        if self.chain == None:
            print("Genisis block not decleared")
            return
        last_index = len(self.chain) - 1
        last_hash = self.chain[last_index].get_hash()
        if prev_hash == last_hash:
            new_hash = last_hash +1
            new_block = Block(data,new_hash)
            self.chain.append(new_block)
        else:
            print("hash did'nt match")
            return
    def get_data(self):
        for block in self.chain:
            print(block.data,  end = " -> ")
        print(None)

chain = BlockChain()
chain.create_block(12)
chain.add_block(121,100000001)
chain.add_block(121,100000002)
chain.add_block(154,100000005)

chain.get_data()




    