# -*- coding: cp1250 -*-
loop=1
while loop==1:
    list=[]
    import mechanize
    import re
    vnos=raw_input('vnesite željeno besedo: ')
    response = mechanize.urlopen('http://bos.zrc-sazu.si/c/SP/neva.exe?name=sp&expression='+vnos+'&hs=1')
    html_cel=response.read()
    html_part1=html_cel.find('<font face="Arial Unicode MS" color=firebrick><b></font><font color=red face="Arial Unicode MS">')
    html_cel=html_cel[html_part1:]
    html_cel=re.split(r'''<font face="Arial Unicode MS" color=firebrick><b></font><font color=red face="Arial Unicode MS">''', html_cel)
    html_cel=''.join(html_cel)
    html_cel=re.split(r'''</font>''', html_cel)
    html_done=html_cel[0]
    html_done=html_done.replace("ĂŞ", "(siroki E)")
    html_done=html_done.replace("e&#x0301;", "(ozki E)")
    html_done=html_done.replace("e&#x0301;", "(ozki E)")
    html_done=html_done.replace("e&#x0301;", "(ozki E)")
    html_done=html_done.replace("e&#x0301;", "(ozki E)")
    html_done=html_done.replace("e&#x0301;", "(ozki E)")
    html_done=html_done.replace("e&#x0301;", "(ozki E)")
    html_done=html_done.replace("&#x0301;", "")
    
        
    print html_done
