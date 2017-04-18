#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:35:27 2017

@author: benjbruno
"""
import pandas as pd

def is_repeating(n):
    'n is the number to check'
    if(len(set(n))) != (len(list(n))):
        return(True)
def intersect_count(i,h,c):
    'c common chars between i and h'
    if len(set(tuple(i)).intersection(set(tuple(h)))) == c:
        return(True)
    
def correct_charpos_count(i,h,l):
    'l chars in h have correct position(s) in i while the rest should not.'
    ctr=0
    for (hidx, hv) in pd.Series(list(h)).items():
        if i[hidx] == hv:   ctr+=1
    if ctr == l:
        return(True)
    
def incorrect_charpos_count(i,h,l):
    'l chars in h have incorrect position(s) in i.'
    cmn=set(tuple(i)).intersection(set(tuple(h)))
    
    ctr=0
    for (hidx, hv) in pd.Series(tuple(h)).items():
        if hv not in cmn:   continue
        if i[hidx] != hv:   ctr+=1
    if ctr == l:
        return(True)

def correct_char_n_pos(i,h,rc,rp):
    'rc# in h are in i; rp# of chars in h have correct position(s) in i.'
    cmn=set(tuple(i)).intersection(set(tuple(h)))
    retval = False
    if len(cmn) == rc:  
        ctr=0
        for (hidx, hv) in pd.Series(list(h)).items():
            if i[hidx] == hv:   ctr+=1
        if ctr == rp:
            retval = True
    else:
        retval = False
    return(retval)

def correct_char_bt_wrongpos(i,h,rc,wp):
    'rc# in h are in i; rp# of chars in h have incorrect position(s) in i.'
    cmn=set(tuple(i)).intersection(set(tuple(h)))
    retval = False
    if len(cmn) == rc:
        ctr=0
        for (hidx, hv) in pd.Series(tuple(h)).items():
            if hv not in cmn:   continue
            if i[hidx] != hv:   ctr+=1
        if ctr == wp:
            retval = True
    else:
        retval = False
    return(retval)

def crack_the_code():
    c=0
    for j in range(0,1000):
        i = str(j).rjust(3,'0')
        if is_repeating(i): continue
        if not correct_char_n_pos(i,'682',1,1): continue
        if not correct_char_bt_wrongpos(i,'614',1,1): continue
        if not correct_char_bt_wrongpos(i,'206',2,2): continue
        if not intersect_count(i,'738',0): continue
        if not correct_char_bt_wrongpos(i,'780',1,1): continue
    
        if not intersect_count(i,'682614206738780',3): continue
        print(i)
        c+=1
    print("%s possibilit(y/ies)" % c)
    
def crack_the_code_v1():
    c=0
    for j in range(0,1000):
        i = str(j).rjust(3,'0')
        if is_repeating(i): continue
        if not intersect_count(i,'682',1): continue
        if not intersect_count(i,'614',1): continue
        if not intersect_count(i,'206',2): continue
        if not intersect_count(i,'738',0): continue
        if not intersect_count(i,'780',1): continue
    
        if not correct_charpos_count(i,'682',1): continue
        if not incorrect_charpos_count(i,'614',1): continue
        if not incorrect_charpos_count(i,'206',2): continue
        if not incorrect_charpos_count(i,'780',1): continue
        if not intersect_count(i,'682614206738780',3): continue
        print(i)
        c+=1
    print("%s possibilit(y/ies)" % c)
    
crack_the_code()
    