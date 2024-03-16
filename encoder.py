import numpy as np
from random import choice as c, randint as r
key = """'ab    cdefghijklmnopqrstuvwxyz []-_=+{}()1234567890ABCDEFGH☺IJKLMNOPQRSTUVWXYZ!@#$"%^&*<:;>,.?/\|\n"""
def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find and (idx+1)%2==0:
                return idx
def alphatize(n):
        g,h,l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],['k', 'l', 'm', 'n', 'o', 'p', 'A', 'B', 'C', 'D']
        if(isinstance(n, int)):
                n = str(n)
                result = ''.join([c([g,h,l])[int(n[x])] for x in range(len(n))])
                return result
        else:
                result = int(''.join([str(np.where(np.array([g,h,l]) == n[z])[1][0]) for z in range(len(n))]))
                return result
def decryption(d):
        decrypt = d.split(',')
        answer1 = [alphatize(i) for i in decrypt]
        answer1 = [key[int((answer1[find_indices(answer1,t)-1]-1)/(t+1))] for t in range(int(len(answer1)/2))]
        return ''.join(answer1)
def encryption(u):
        answer = [(key.index(u[a])+1)*(a+1) for a in range(len(u))]
        answer1,f= [],[]
        for c in range(len(answer)):
                a = r(0,len(answer)-1)
                while a in f:
                        a = r(0,len(answer)-1)
                f.append(a)
                answer1.append(alphatize(answer[a]))
                answer1.append(alphatize(a))
        return ','.join(answer1)
