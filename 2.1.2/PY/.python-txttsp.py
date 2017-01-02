# -*- coding: utf-8 -*-
import os
import sys
import time
import wave
from easygui import *
from pydub import AudioSegment
import pydub
glas='Vesna'
start_path=os.getcwd()
old_path=os.getcwd()
os.chdir(start_path+'\\vesna')

import shutil
import subprocess
imena_zlogov=0
izjeme=['k','d','p','t','d','g','j','k','c','b','s']
delcek=4 #kolikšen del krajšega zloga se prekriva (10 pomeni 1/10)

def cross_fade(file1, file2, prvi, drugi):
    if prvi==1:
        file1=file1.fade_out(10)
    else:
        file1=file1.fade_out(10)
    if drugi==1:
        file2=file2.fade_in(10)
    else:
        file2=file2.fade_in(10)
    file1=file1+silence
    result = file1.overlay(file2, position=mesto_za_overlay)                 #overlay konec od file1 in začetek od file2
    result.export(str(temp_st_rez)+"result.tmp", format="wav")     #shrani datoteko
    
def intonacija(list_zlogov):
    zanka=True
    stevec=0
    temp_list=[0,0]                 #lemp_list=[x,y...] x=število zlogov (dvočrkovnih) če y==0..ni končnega ločila na koncu besede, če y==1 je končno ločilo na koncu
    oznake_list=list()
    locila=['+','(','!']
    for n,i in enumerate(sound1):
        if (len(i))==2:
            stevec=stevec+1
            temp_list.append(n)
        elif i in locila:
            if stevec>0:
                temp_list[1]=1
                temp_list[0]=stevec
                oznake_list.append(temp_list)
                stevec=0
                temp_list=[0,0]                 #lemp_list=[x,y...] x=število zlogov (dvočrkovnih) če y==0..ni končnega ločila na koncu besede, če y==1 je končno ločilo na koncu
        elif i=='-':
            if stevec>0:
                temp_list[0]=stevec
                oznake_list.append(temp_list)
                stevec=0
                temp_list=[0,0]                 #lemp_list=[x,y...] x=število zlogov (dvočrkovnih) če y==0..ni končnega ločila na koncu besede, če y==1 je končno ločilo na koncu
    mesto_v_listu=0
    nrt=len(oznake_list)
    nr=0
    a=0
    for i in range (nrt):
        beseda=oznake_list[nr]
        nr=nr+1
        pika=beseda[1]
        st_zlogov=beseda[0]
        filename=beseda[2]
        if pika==1:
            filename=str(filename)
            shutil.move(filename+'.wav', filename+'a.wav')
            if st_zlogov==1:
                p=subprocess.Popen(['cmd', '/c', 'sox '+filename+'a.wav '+filename+'.wav pitch -77'])
                p.wait()
            else:
                p=subprocess.Popen(['cmd', '/c', 'sox '+filename+'a.wav '+filename+'.wav pitch 48'])
                p.wait()
                
            filename=len(beseda)-1
            filename=str(filename)
            shutil.move(filename+'.wav', filename+'a.wav')
            p=subprocess.Popen(['cmd', '/c', 'sox '+filename+'a.wav '+filename+'.wav pitch -95'])
            p.wait()

                


            
        else:
            if st_zlogov==1:
                filename=beseda[2]
                filename=str(filename)
                shutil.move(filename+'.wav', filename+'a.wav')
                if a==1:
                    p=subprocess.Popen(['cmd', '/c', 'sox '+filename+'a.wav '+filename+'.wav pitch 48'])
                    a=0
                else:
                    p=subprocess.Popen(['cmd', '/c', 'sox '+filename+'a.wav '+filename+'.wav pitch 13'])
                    a=1
                p.wait()

            if st_zlogov==2:
                filename=beseda[3]
                filename=str(filename)
                shutil.move(filename+'.wav', filename+'a.wav')
                p=subprocess.Popen(['cmd', '/c', 'sox '+filename+'a.wav '+filename+'.wav pitch 58'])
                p.wait()

                filename=beseda[2]
                filename=str(filename)
                shutil.move(filename+'.wav', filename+'a.wav')
                p=subprocess.Popen(['cmd', '/c', 'sox '+filename+'a.wav '+filename+'.wav pitch -56'])
                p.wait()
            elif st_zlogov==3:
                filename=beseda[3]
                filename=str(filename)
                shutil.move(filename+'.wav', filename+'a.wav')
                p=subprocess.Popen(['cmd', '/c', 'sox '+filename+'a.wav '+filename+'.wav pitch 39'])
                p.wait()

                filename=beseda[4]
                filename=str(filename)
                shutil.move(filename+'.wav', filename+'a.wav')
                p=subprocess.Popen(['cmd', '/c', 'sox '+filename+'a.wav '+filename+'.wav pitch -42'])
                p.wait()
            elif st_zlogov>3:
                b=beseda[0]
                c=1
                delc=90/b
                pitch=-10
                for i in range (b):
                    c=c+1
                    pitch=int(pitch)
                    pitch=pitch+delc
                    pitch=str(pitch)
                    filename=beseda[c]
                    filename=str(filename)
                    shutil.move(filename+'.wav', filename+'a.wav')
                    p=subprocess.Popen(['cmd', '/c', 'sox '+filename+'a.wav '+filename+'.wav pitch '+pitch])
                    p.wait()

            
                
                
    

zanka=1
ime_rezultata='1'
while zanka==1:
    temp_st_rez=1
    vnos_zanka=1
    imena_zlogov=0
    os.chdir(old_path+'\\'+glas)
    shutil.copy('sox.exe','temp//sox.exe')
    shutil.copy('zlib.dll','temp//zlib.dll')
    shutil.copy('silence.wav','temp//silence.wav')
    if ime_rezultata=='2':
        ime_rezultata='1'
    else:
        ime_rezultata='2'
    print '''                    SLO text to speech
                       <Vid Klopcic>
    _____________________________________________________
    glas: '''+glas+'''
    '''
    print'''    
    ------------------pomoc in informacije-----------------
    -siroki E .... E
    -ozki E   .... E z ostrivcem *
    
    -siroki O .... O
    -ozki O   .... O z ostrivcem *
    
    *ALT Gr + 9 (ostrivec), nato pa pritisnete na crko.
    
    Sumniki so podprti, stevila pa trenutno se ne delujejo.
    -------------------------------------------------------
    
    '''
    while vnos_zanka==1:        #beseda, je besedilo, ki se pretvori v govor

        ch1=buttonbox(msg='Izberite dejanje', title='SLO text to speech', choices=('Vnos besedila','Sprememba glasu','DONACIJA', 'Izhod'),image=None, root=None)

        if ch1=='Vnos besedila':
            vnos_zanka=0
            beseda=textbox(msg='''    ------------------pomoc in informacije-----------------
    -siroki E .... E
    -ozki E   .... E z ostrivcem *
    
    -siroki O .... O
    -ozki O   .... O z ostrivcem *
    
    *ALT Gr + 9 (ostrivec), nato pa pritisnete na crko.
    
    Sumniki so podprti, stevila pa trenutno se ne delujejo.
    -------------------------------------------------------------------
    
    Tukaj vnesite besedilo''', text='', codebox=0)

        if ch1=='Izhod':
            sys.exit()
            
        if ch1=='Sprememba glasu':
            ch_glasu=buttonbox(msg='Izberite glas:', title='Izbira glasu', choices=('Vesna','Vid'),image=None, root=None)
            if ch_glasu=='Vesna':
                os.chdir(start_path+'\\vesna')
                delcek=4
                glas='Vesna'
                
            if ch_glasu=='Vid':
                os.chdir(start_path+'\\vid')
                delcek=5
                glas='Vid'
                
        if ch1=='DONACIJA':
            p=subprocess.Popen(['cmd', '/c', 'start http://vidklopcic.3owl.com'])
            p.wait()
            ch_fail=buttonbox(msg='''Hvala za podporo ;)''', title='DONACIJA', choices=('Nazaj','Izhod'),image=None, root=None)
            if ch_fail=='Izhod':
                sys.exit()
            
            
    p=subprocess.Popen(['cmd', '/c', 'cls'])
    p.wait()
    nr=-1
    lp=len(beseda)
    beseda=list(beseda)                  #vnos spremeni v list
    print 'kopiranje glasov:  ',
    for i in range (2,lp):
        nr=nr+1
        s_v=beseda[nr]+beseda[nr+1]+beseda[nr+2]
        if s_v==' v ':
            beseda[nr+1]='v'
        elif s_v==' s ':
            beseda[nr+1]='s3'
        elif s_v==' z ':
            beseda[nr+1]='z3'


    beseda+=['-','-','-']                #doda "presledke" oz. 0,5sec pavze na konec (za lepši iztek zvoka)

    for n,i in enumerate(beseda):   #pretvori posebne znake v druge vrednosti

        if i==u' ':
            beseda[n]='-' #presledek

        if i==u'\n':
            beseda[n]='-'  #enter
        if i==u'\xf3':
            beseda[n]='Q' #mali ozki o
        if i==u'\xd3':
            beseda[n]='Q' #veliki ozki Ó
        if i==u'\xa2':
            beseda[n]='Q' #CMDmali ozki o
        if i==u'\xe0':
            beseda[n]='Q' #CMDveliki ozki Ó

        if i==u'\xf4':
            beseda[n]='O' #mali široki ô                
        if i==u'\xd4':
            beseda[n]='O' #veliki široki Ô
        if i==u'\x93':
            beseda[n]='O' #CMDmali široki ô                
        if i==u'\xe2':
            beseda[n]='O' #CMDveliki široki Ô

        if i==u'.':
            beseda[n]='+'
        if i==u',':
            beseda[n]='!'
        if i==u'(':
            beseda[n]=''
        if i==u')':
            beseda[n]=''
        if i==u'?':
            beseda[n]='('
        if i==u'!':
            beseda[n]='+'
        if i==u':':
            beseda[n]='-'
        if i==u';':
            beseda[n]='-'

        if i==u'\xc9':
            beseda[n]='X' #veliki ozki É
        if i==u'\xe9':
            beseda[n]='X' #mali ozki é
        if i==u'\x90':
            beseda[n]='X' #veliki ozki É
        if i==u'\x82':
            beseda[n]='X' #mali ozki é
            

        if i==u'č':
            beseda[n]='2' #mali č
        if i==u'Č':
            beseda[n]='2' #veliki Č
        if i==u'\x9f':
            beseda[n]='2' #mali č
        if i==u'\xac':
            beseda[n]='2' #veliki Č

        if i==u'ž':
            beseda[n]='W' #mali ž
        if i==u'Ž':
            beseda[n]='W' #veliki Ž
        if i==u'\xa7':
            beseda[n]='W' #mali ž
        if i==u'\xa6':
            beseda[n]='W' #veliki Ž
            
        if i==u'Š':
            beseda[n]='1' #veliki Š
        if i==u'š':
            beseda[n]='1' #mali š
        if i==u'\xe6':
            beseda[n]='1' #veliki Š
        if i==u'\xe7':
            beseda[n]='1' #mali š




            
    stevilo = len(beseda)                #vrednost "stevilo" postane enako številu črk v vnešeni besedi
    stevilo = stevilo - 1
    a=1                                  #spremenljivka za zanko while
    vrst=0                               #če prvi dve črki nista zlog (sog, sam) se spremeni v 1 (pri part2 se ponovi isti postopek)
    vrst1=1                              #-----II----- le da je za 2. mesto
    sound=list()
    sound1=list()

    cnt=1
    while a==1:
        cnt=cnt+1
        if cnt==20:
            print '.',
            cnt=0
        b=1
        ne_append=0
        if vrst1>stevilo:
            tst=beseda[vrst]         #tst dobi vrednost prvih dveh znakov v listu
            part=''.join(tst)        #vejice, ki ločujejo znake se izbrišejo
            sound+=part
            a=0
        else:
            part=beseda[vrst],beseda[vrst1]         #part dobi vrednost prvih dveh znakov v listu
            part=''.join(part)               #vejice, ki ločujejo znake se izbrišejo
            try:                             #preizkusi ali obstaja datoteka s takim imenom
               with open(part+'.wav') as f: pass
            except IOError as e:             #če ne, preskoči error in postane part le prvi znak vnosa
                try:
                    part=part[0]
                    with open(part+'.wav') as f: pass
                    part=beseda[vrst]
                    b=0
                except IndexError as e:
                    part='-'
                except IOError as e:
                    do_nothing=None
                    ne_append=1
            if ne_append==1:
                if part=='+':
                    sound1.append(part)
                    ne_append=0
                if part=='(':
                    sound1.append(part)
                    part='+'
                    ne_append=0
                if part=='!':
                    sound1.append(part)
                    part='+'
                    ne_append=0
            else:
                sound1.append(part)
                
            if ne_append==0:
                temp=str(imena_zlogov)
                shutil.copy(part+'.wav','temp//'+temp+'.tmp')
                imena_zlogov=imena_zlogov+1
                sound.append(part)
            if vrst1==stevilo:
                a=0
            if b==0:
                vrst=vrst+1                        #mesti za znake v part2 se premakneta za eno nazaj
                vrst1=vrst1+1
            else:
                vrst=vrst+2
                vrst1=vrst1+2

    temp=int(temp)+1
    shutil.copy('-.wav','temp//'+str(temp)+'.tmp')
    temp=temp+1
    shutil.copy('-.wav','temp//'+str(temp)+'.tmp')
    temp=temp+1
    shutil.copy('-.wav','temp//'+str(temp)+'.tmp')
    temp=int(temp)+1
    shutil.copy('-.wav','temp//'+str(temp)+'.tmp')
    temp=temp+1
    shutil.copy('-.wav','temp//'+str(temp)+'.tmp')
    temp=temp+1
    shutil.copy('-.wav','temp//'+str(temp)+'.tmp')
    temp=int(temp)+1
    shutil.copy('-.wav','temp//'+str(temp)+'.tmp')
    temp=temp+1
    shutil.copy('-.wav','temp//'+str(temp)+'.tmp')
    temp=temp+1
    shutil.copy('-.wav','temp//'+str(temp)+'.tmp')
    os.chdir(os.getcwd()+'\\temp')
    #intonacija(sound1)
#--------------------!prva dva zloga!---------------------
    r=1
    z=1
    file=sound[0]
    files=sound[1]
    time.sleep(2)
    silence=AudioSegment.from_wav('silence.wav')
    try:
        file1 = AudioSegment.from_wav("0.tmp")                 #Če je intonacija vključena mora biti pred.wav črka a; datoteki za crossfade
        file2 = AudioSegment.from_wav("1.tmp")                 #Če je intonacija vključena mora biti pred.wav črka a; datoteki za crossfade
        
        if len(file1)<len(file2):
            procenti=len(file1)/delcek
            mesto_za_overlay=len(file1)-procenti
        else:
            procenti=len(file2)/delcek
            mesto_za_overlay=len(file1)-procenti
        procenti=procenti*1.5
        procenti=int (procenti)
        dolzina=5000-len(file2)+procenti
        silence=silence[dolzina:]
        test=files
        if (test[0]) in izjeme:
                    r=0
        if len(test)==1:
            dolzina=dolzina-(round(procenti/1,3))
        cross_fade(file1, file2, z, r)
    except IOError as e:                                            #če zvok ne obstaja se izogne IOErrorju kot:
            print '''---------------------------------------
crka (''',file,'''oz.''',files,''') ne obstaja
---------------------------------------'''

#------------------------------------------------------------





    
    stevilo=len(sound)                                              #stevilo vseh zlogov
    mesto=2                                                         #mesto je spremenljivka, ki naraste za 1 po vsakem dodanem zlogu
    file=2
    konec=stevilo-1                                                 #spremenljivka za prikaz napredka
    print ''
    print 'obdelovanje 1 od',konec                                  #prvi korak od vsega dela
    file_n1=0
    file_n2=1
    temp_st_rez=1
    cntr_set_tsr=0
    while mesto<stevilo:                                            #ponavlja zanko dokler ni dodal vseh zlogov
        cntr_set_tsr=cntr_set_tsr+1
        if cntr_set_tsr>50:             #v en vmesni rezultat zlepi toliko črk
            temp_st_rez=temp_st_rez+1
            cntr_set_tsr=0
            #--------------------ustvari n-result.tmp-------------------
            silence=AudioSegment.from_wav('silence.wav')
            file_n1=int(file_n1)+1
            file_n2=int(file_n2)+1
            file_n1=file_n1+1
            file_n2=file_n2+1
            file_n1=str(file_n1)
            file_n2=str(file_n2)
            try:
                z=1
                r=1
                print 'obdelovanje',mesto,'od',konec                    #prikaz napredka
                #file1 = sound[mesto]                                     #file postane n-ti zlog
                #mesto = mesto+1
                #file2 = sound[mesto]
                mesto=mesto+1
                file1 = AudioSegment.from_wav(file_n1+'.tmp')                 #Če je intonacija vključena mora biti pred.wav črka a; datoteki za crossfade
                file2 = AudioSegment.from_wav(file_n2+'.tmp')                 #Če je intonacija vključena mora biti pred.wav črka a; datoteki za crossfade
                if len(file1)<len(file2):
                    procenti=len(file1)/delcek
                    mesto_za_overlay=len(file1)-procenti
                else:
                    procenti=len(file2)/delcek
                    mesto_za_overlay=len(file1)-procenti
                procenti=procenti*1.5
                procenti=int (procenti)
                dolzina=5000-len(file2)+procenti
                silence=silence[dolzina:]
                test=files
                if (test[0]) in izjeme:
                            r=0
                if len(test)==1:
                    dolzina=dolzina-(round(procenti/1,3))
                cross_fade(file1, file2, z, r)
            except IOError as e:                                            #če zvok ne obstaja se izogne IOErrorju kot:
                    print '''---------------------------------------
        crka (''',file,'''oz.''',files,''') ne obstaja
        ---------------------------------------'''


            #os.chdir(start_path+'\\'+glas)
            #shutil.copy('blank.wav','temp//'+str(temp_st_rez)+'result.tmp')
            #os.chdir(temp_1)
            #-----------------------------------------------------------
        file_n1=int(file_n1)
        file_n2=int(file_n2)
        file_n1=file_n1+1
        file_n2=file_n2+1
        file_n1=str(file_n1)
        file_n2=str(file_n2)
        try:
            r=1
            z=1
            silence=AudioSegment.from_wav('silence.wav')
            print 'obdelovanje',mesto,'od',konec                    #prikaz napredka
            file = sound[mesto]                                     #file postane n-ti zlog
            mesto = mesto-1
            adijo = sound[mesto]
            mesto=mesto+2
            
            test = AudioSegment.from_wav(file_n1+".tmp")                  #za test če je prejšnji zlog krajši
            ime_zloga = AudioSegment.from_wav(file_n2+".tmp")             #v ime_zloga se naloži wav posnetek trenutnega zloga
            temp_res = AudioSegment.from_wav(str(temp_st_rez)+"result.tmp")               #datoteki za crossfade
            if len(test)<len(ime_zloga):
                procenti=len(test)/delcek
                mesto_za_overlay=len(temp_res)-procenti
            else:
                procenti=len(ime_zloga)/delcek
                mesto_za_overlay=len(temp_res)-procenti
            procenti=procenti*1.5
            procenti=int (procenti)
            dolzina=5000-len(ime_zloga)+procenti
            spr_2=file
            spr_1=adijo
                       
            if (spr_2[0]) in izjeme:
                r=0

            if (spr_1[0]) in izjeme:
                z=0
            if len(test)==1:
                dolzina=dolzina-(round(procenti/1,3))
            
            silence=silence[dolzina:]
            cross_fade(temp_res, ime_zloga, z, r)
                                 
        except IOError as e:            #če zvok ne obstaja se izogne IOErrorju kot:
            try:
                z=1
                r=1
                time.sleep(0.5)
                silence=AudioSegment.from_wav('silence.wav')
                test = AudioSegment.from_wav(file_n1+".tmp")                  #Če je intonacija vključena mora biti pred.wav črka a; za test če je prejšnji zlog krajši
                ime_zloga = AudioSegment.from_wav(file_n2+".tmp")             #Če je intonacija vključena mora biti pred.wav črka a; v ime_zloga se naloži wav posnetek trenutnega zloga
                temp_res = AudioSegment.from_wav(str(temp_st_rez)+"result.tmp")               #datoteki za crossfade
        
                if len(test)<len(ime_zloga):
                    procenti=len(test)/delcek
                    mesto_za_overlay=len(temp_res)-procenti
                else:
                    procenti=len(ime_zloga)/delcek
                    mesto_za_overlay=len(temp_res)-procenti
                procenti=procenti*1.5
                procenti=int (procenti)
                dolzina=5000-len(ime_zloga)+procenti
                spr_2=file
                spr_1=adijo
                           
                if (spr_2[0]) in izjeme:
                    r=0

                if (spr_1[0]) in izjeme:
                    z=0

                if len(test)==1:
                    dolzina=dolzina-(round(procenti/1,3))
                    #če je (ptkfhsšcč) dodaj polglasnik
                silence=silence[dolzina:]
                cross_fade(temp_res, ime_zloga, z, r)
                
            except IOError as e:
                print '''---------------------------------------
crka (''',file,''') ne obstaja
---------------------------------------'''
        

    time.sleep(1)

#-------------merging result--------------------
    print '''
-----------------------
Ustvarjanje rezultata: ''',
    counter=1
    tmp1=AudioSegment.from_wav(str(counter)+'result.tmp')
    a=1
    lst_rez='1result.tmp '
    temp_st_rez=temp_st_rez-1
    for i in range (temp_st_rez):
        counter=counter+1
        lst_rez=lst_rez+str(counter)
        lst_rez=lst_rez+'result.tmp '
    p=subprocess.Popen(['cmd', '/c', 'sox '+lst_rez, str(ime_rezultata)+'result.wav'])
    p.wait()  
#-----------------------------------------------
    print 'koncano!'
    ch1=buttonbox(msg='Izberite dejanje', title='Koncano', choices=('Predvajaj besedilo','Shrani kot WAV datoteko'),image=None, root=None)
    if ch1=='Predvajaj besedilo':
        print '''odpiranje rezultata...'''
        p=subprocess.Popen(['cmd', '/c', '@ECHO OFF&'+ime_rezultata+'result.wav'])
        p.wait()
    elif ch1=='Shrani kot WAV datoteko':
        save=filesavebox(msg=None, title='Sharni kot', default='%userprofile%\govor.wav')
        if save!=None:
            shutil.copy(ime_rezultata+'result.wav',save)
            print ''        
            print 'Shranjeno!'
            time.sleep(2)
    time.sleep(.3)
    print 'ciscenje temp direktorija'
    p=subprocess.Popen(['cmd', '/c', '@ECHO OFF&cd '+glas+'&cd temp&del /f /q *.tmp*'])
    p.wait()
    p=subprocess.Popen(['cmd', '/c', '@ECHO OFF&cls'])
    p.wait()
    del temp
