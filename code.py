#! /usr/bin/env python

#Remove comma
CMA = "1,234,567"
print(CMA.replace(",",""))
print('-' * 30)

#Counting DNA Nucleotide
Nuc='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
print(Nuc.count('A'), end = ' ')
print(Nuc.count('T'), end = ' ')
print(Nuc.count('G'), end = ' ')
print(Nuc.count('C'))
print('-' * 30)

#Transcribing iDNA into RNA
DNA = 'GATGGAACTTGACTACGTAAATT'
RNA = DNA.replace('T','U')
print(RNA)
print('-' * 30)

#Complementing a Strand of DNA
DNA1 = 'AAAACCCGGT'
RNA1 = DNA1[::-1]
RNA1 = RNA1.replace('A', 't')
RNA1 = RNA1.replace('T', 'a')
RNA1 = RNA1.replace('C', 'g')
RNA1 = RNA1.replace('G', 'c')
print(RNA1.upper())
print('-' * 30)

#Make list
lang0 = ['Python', 'JAVA']
lang1 = ['C', 'C++','VB'] 
totalLang = lang0 + lang1
print(totalLang)
print('-' * 30)

#Dictionary application
regNum0 = "951213-0000000"
regNum1 = "960125-0000000"
regNum2 = "970705-0000000"
month={'01':"Jan", '02':"Feb", '03':"Mar", '04':"Apr", '05':"May", '06':"Jun", '07':"Jul", '08':"Aug", '09':"Sep", '10':"Oct", '11':"Nov", '12':"Dec"}
print("regNum0:" + month.get(regNum0[2:4]) +'-'+ regNum0[4:6])
print("regNum1:" + month.get(regNum1[2:4]) +'-'+ regNum1[4:6])
print("regNum2:" + month.get(regNum2[2:4]) +'-'+ regNum2[4:6])

#DNA nucleotide: Complement
#sent="We tried list and we tried dicts also we tried Zen"
#spl=sent.split()
#dic = {}
#for k,v in spl


#큰수 출력하기
#num0 = input('num0: ')
#num1 = input('num1: ') 
#if num0 > num1:
   #print( num0)
#elif num0 < num1 :
    #print(num1)
#else :
   #print('same!')
#한줄로 축약
#print(num1) if num0 < num1 else print(num0)
print('-' * 30)


#등급 지정하기
#score = input("점수 입력: ")
#if score.isdigit()== False : 
#    import sys
#    sys.exit('incorrect score')
#else : 
#    score = int(score)
#if 90<=score <= 100 :
#    grade = 'A'
#elif 80<= score <= 89 :
#    grade = 'B'
#elif 70 <= score <= 79 :  
#    grade= 'C'
#elif 60 <= score <= 69 : 
#    grade = 'D'
#else :
#    grade = 'F'
#print(grade)

#환율계산기
#nation = input("통화명: ").upper()
#cash = int(input("금액: "))
#if nation == 'USD':
#    print(cash * float('1203.82'), 'KRW')
#elif nation == 'EUR':
#    print(cash * float('1365.73'), 'KRW')
#elif nation == 'JRY':
#    print(cash * float('11.22'), 'KRW')
#elif nation == 'CNY':
#    print(cash * float('172.04'), 'KRW')

#d_nation = {'USD':1203.82, 'EUR':1365.73, 'JRY':11.22, 'CNY':172.04}
#if nation == 'USD':
#    result = (cash * d_nation['USD'])
#elif nation == 'EUR':
#    result = (cash * d_nation['EUR'])
#elif nation == 'JRY' : 
#    result = (cash * d_nation['JRY'])
#else :
#    result = (cash * d_nation['CNY'])
#print(round(result, 2),'KRW')


#nation = input("금액: ").upper()
#l_nation = nation.split(',')
#d_nation = {'USD':1203.82, 'EUR':1365.73, 'JPY':11.22, 'CNY':172.04}
#print(l_nation[0][-3:])
#l_result = []
#for a in l_nation : 
#    if a[-3:] == 'USD':
#        result = int(a[0:-4]) * float(d_nation['USD'])
#        l_result.append(str(round(result,2)))
#    elif a[-3:] == 'EUR':
#        result = int(a[0:-4]) * float(d_nation['EUR'])
#        l_result.append(str(round(result,2)))
#    elif a[-3:] == 'JPY':
#        result = int(a[0:-4]) * float(d_nation['JPY'])
#        l_result.append(str(round(result,2)))
#    elif a[-3:] == 'CNY':
#        result = int(a[0:-4]) * float(d_nation['CNY'])
#        l_result.append(str(round(result,2)))
#test1 = " KRW, ".join(l_result)
#test2 = test1+" KRW"
#print(test2)

#final = ""
#for t in l_result:
#     final = final + str(t) + " KRW, "
#print(final)
print('-' * 30)

#Condition and Loop
#inStr = input()
#ia, b = inStr.split()
#myList = []
#for i in range(int(a), int(b)):
#    if i % 2 == 1 : 
#        myList.append(i)
#print(sum(myList)) 
#print('-' * 30)

#Palindromic sequence
#seq1 = input('Input sequence: ')
#seq2 = seq1
#for i in seq1 : 
#    if i == 'A':
#        seq1 = seq1.replace('A', 'T')
#    elif i == 'T':
#        seq1 = seq1.replace('T', 'A') 
#    elif i == 'G':
#        seq1 = seq1.replace('G', 'C') 
#    else :
#        seq1 = seq1.replace('C', 'G') 
#    print(seq1)
#if seq1 == seq2[::-1] : 
#    print('seq1 is palindromic.')
#else :
#    print('seq1 is not palindromic.')
#print('-' * 15,'fail','-'*15)

#seq1 = input('Input sequence: ')
#comp_seq = ""
#dic = { 'A':'T', 'T':'A', 'G':'C', 'C':'G'}
#for i in seq1 : 
#    if i == 'A':
#        comp_seq += dic[i]
#    if i == 'T':
#        comp_seq += 'A'
#        comp_seq += dic[i]
#    if i == 'G':
#        comp_seq += 'C'
#        comp_seq += dic[i]
#    if i == 'C':
#        comp_seq += 'G'
#        comp_seq += dic[i]
#rev_seq = comp_seq[::-1]
#if seq1 == rev_seq: 
#    print(seq1,'is palindromic.')
#else :
#    print(seq1,'is not palindromic.')




#Dictionaries

#letters = input('letters: ')
#l_letters = letters.split(' ')
#print(l_letters)
#d_letters = {}
#for i in l_letters : 
#    if i in d_letters : 
#        d_letters[i] += 1
#    else :
#        d_letters[i] = 1
#for k,v in d_letters.items(): 
#    print(k,v)


#from collections import counter
#toCount = 'We tried list and we tried dicts also we tried Zen'
#tocount = toCount.split()
#cnt = counter(tocount)
#print(cnt)

# 사칙연산
#num0 = int(input('number0:'))
#op = input('option:')
#num1 = int(input('number1:'))
#def calc(num0, num1, op):
#    print('{} {} {} = '.format(num0, op, num1), end = " ")
#    if op == '+' :
#        result = num0 + num1
#    elif op == '-' :
#        result = num0 - num1
#    elif op == '/' :
#        result = num0 / num1
#    elif op == '*' :
#        result = num0 * num1
#    return result
#print(calc(num0, num1, op))
#print(calc(2,7,'*'))
#print(calc(1,1,'+'))
#print(calc(8,4,'/'))
#print(calc(3,1,'-'))

#피보나치 수열
def pivo(ip):
    l_pivo = []
    for i in range(0,ip):
        if i == 0 :
            l_pivo.append(i)
        elif i == 1 :
            l_pivo.append(i)
        elif i > 1 :
            l_pivo.append((int(l_pivo[-2])+(l_pivo[-1])))
            #l_pivo.append(int(sum(l_f[-2:-1])))
    return l_pivo

ip = int(input('input step: '))
result = pivo(ip)
print(result[-1])
print(result)

def d_pivo(ip):
    pivo_dict = {}
    for i in range(0,ip):
        if i == 0 : 
            pivo_dict['F0'] = 0
        elif i == 1 : 
            pivo_dict['F1'] = 1
        elif i > 1 :
            pivo_dict['F'+str(i)] = (pivo_dict['F'+str(i-2)]+pivo_dict['F'+str(i-1)])
    return pivo_dict

ip = int(input('input step: '))
result = d_pivo(ip)
print(sum(result.values()))
print(result.keys())


