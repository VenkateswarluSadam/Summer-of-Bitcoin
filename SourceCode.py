import csv                                                      #Import CSV to work with csv files
outputfile = open('block.txt','r+')                              #Creating a new file which stores the output->All transaction id's included in the block
weightTillNow = [0]                                             # Initialization of A list which tracks the current weight of the Block
blockIncludedTrans = []

class MempoolTransaction:                                       #Class which verifies the weight and parent of each transaction
    
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parents = parents
        
    def verify_weight(self):                                    #Method definition to check the weight constraint
        if weightTillNow[0]+self.weight<=4000000:
            weightTillNow[0]+=self.weight
            return True
        
    def verify_parent(self):                                    #Method definition to check the parent constraint
        if self.parents:
            if self.parents in blockIncludedTrans :
                return True
        else:
            return True
            
    def isValidTrans(self):                                     #Method definition for final evaluation of transaction to be included
        if self.verify_weight() and self.verify_parent():
            return self.txid
        else:
            return False
                
        
    
    
def parse_mempool_csv():                                        #Function definition to Read and Parse the mempool.csv file 
    with open("mempool.csv") as f:
        data = [line.strip().split(',') for line in f.readlines()]   
        
        
    for j,i in enumerate(data):                                 #sending each transaction details to validation
        
        if j!=0:
            objectTrans = MempoolTransaction(*data[j])          #Object Creation for each transaction 
            taxid = objectTrans.isValidTrans()                  
            
            if taxid:
                outputfile.writelines(taxid+'\n')               #Writing the Validated transaction id into the output file
                blockIncludedTrans.append(taxid)
    

parse_mempool_csv()
                                                 

#outputfile.seek(0)
#outputfile.truncate()
#outputfile.close()
#print(len(blockIncludedTrans))
