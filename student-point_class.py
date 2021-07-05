#! /usr/bin/env python

class Student: 
    def __init__(self, kp, ep, mp):
        self.korean = int(kp)
        self.english = int(ep)
        self.math = int(mp) 
    def showKorean(self):
        self.korean
        return
    def showEnglish(self):
        self.english
    def showMath(self):
        self.math 
    def showEverage(self):
        (self.korean + self.english + self.math)/3
park = Student(100, 30, 90)
print(park.korean, '점')
print(park.showKorean())
#print(park.showEnglish())
#print(park.showMath())
#print(park.showEverage())
