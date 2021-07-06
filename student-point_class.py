#! /usr/bin/env python

class Student: 
    def __init__(self, kp, ep, mp):
        self.__korean = int(kp)
        self.__english = int(ep)
        self.__math = int(mp) 
    def showKorean(self):
        k = self.__korean
        return k
    def showEnglish(self):
        e = self.__english
        return e
    def showMath(self):
        m = self.__math
        return m 
    def showEverage(self):
        result = (int(self.showKorean()) + int(self.showEnglish()) + int(self.showMath()))/3
        return result
park = Student(100, 30, 90)
#print(park.korean(), '점')
print(park.showKorean(),'점')
print(park.showEnglish(),'점')
print(park.showMath(),'점')
print(round(park.showEverage(),2),'점')
print(park.__korean)
