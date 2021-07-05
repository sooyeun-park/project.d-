#! /usr/bin/env python

class Person:
    d_persons = {'Gu':'Canada','Niklas':'Germany','Mark':'USA','Alex':'Swiss','Alberto':'Italia'}       
    nation = 'A Nation'
    name = 'P_name'
    def showNation(self):
        self.name = delattr(self,
        if self.name in d_persons :
            print(d_persons[self.name])
        else : 
            print('fail TT')


#       #if str(self) in d_persons.keys():
#            return  d_persons[self]
#                       
#        else :
#            print(self, 'is not in database!')

    def setNation(self, in_nation):
        d_persons = {'Guillaume':'Canada ','Niklas ':'Germany',' Mark':'USA ','Alex':'Swiss ', 'Alberto':'Italia'}
       #if self in d_persons : 
        #    print(self,'is in database!')
        #else :
         #   d_persons[self] = in_nation

Mark = Person()
Sam = Person()
Mark.showNation()
#print(Mark.__dict__)
#(Sam.setNation('Korea'))
#print(Sam.showNation())

