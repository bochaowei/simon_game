from tkinter import Tk

from Wizard import Wizard
from choices import Demographic
from sequence import clicky
from NASA import NASA,comparequestions
import random    
            
class LikertWizard(Wizard):
    def __init__(self, parent, data):
        super().__init__(parent, data)
        flavors = ['mental', 'physical', 'temporal', 'performance',
           'effort', 'frustration']
        def choosetwo(lst):
            res = []
            for i in range(len(lst)):       
                for j in range(i+1, len(lst)):
                    tup = (lst[i], lst[j])
                    res.append(tup)

            return res
        flavor_pairs = choosetwo(flavors)
        
        def shuffle(lst):
            l = lst.copy()
            res = []
            while len(l) > 0:
                index = random.randint(0, len(l) - 1)
                res.append(l[index])
                del l[index]
            return res
        shuffled_flavor_pairs1 = shuffle(flavor_pairs)
        shuffled_flavor_pairs2 = shuffle(flavor_pairs)
        shuffled_flavor_pairs3 = shuffle(flavor_pairs)
        #for questions in shuffled_flavor_pairs:
        
        
        
            
                   
        steps = [Demographic(self,self.data,"demographics"),clicky(self,data,'Simon Game',3),NASA(self, self.data, "NASA survery 1")]
        for iii in shuffled_flavor_pairs1:
            steps.append(comparequestions(self, data,"NASA survery 1",iii))
        ###block 2
        steps.append(clicky(self,data,'Simon Game',6))
        steps.append(NASA(self, self.data, "NASA survery 2")) 
        for iii in shuffled_flavor_pairs2:
            steps.append(comparequestions(self, data,"NASA survery 2",iii))
         ###block 3   
        steps.append(clicky(self,data,'Simon Game',9))
        steps.append(NASA(self, self.data, "NASA survery 3")) 
        for iii in shuffled_flavor_pairs3:
            steps.append(comparequestions(self, data,"NASA survery 3",iii))

        self.set_steps(steps)
        self.start()
 ## in the results of the Game, 0 means soccer, 1 means football, 2 means compass, 3 means darth varder
if __name__ == "__main__":
    root = Tk()

    data = {}

    my_gui1 =LikertWizard(root, data)
    
    my_gui1.pack()

    root.mainloop()
