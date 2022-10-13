
class Weather:
    def __init__(self,list1=0,Item=0):
        self.list2=list1
        self.item=Item 
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.list2==self.item:
        
            raise StopIteration 
        else:
            return self.item

    # def __ne__(self,other):
    #     for i in self.list2:
    #         if i.self==other.item:
    #             print(Weather(i.self)) 
                
    #     return print('Value is not present')
list1=['Abhi','Kumar','Sandhu','Ridhi','Jaiswal','Kumari']
word=('anmk')


for word in (list1):
    print('The Item is present in list.... ')
    break
