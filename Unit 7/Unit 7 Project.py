def decimalDegree(ddmmss):
    degSign = ddmmss.find(chr(176))
    minSign = ddmmss.find("'")
    secSign = ddmmss.find('"')
    DD = float(ddmmss[:degSign])
    MM = float(ddmmss[degSign+1:minSign])
    SS = float(ddmmss[minSign+1:secSign])
    decimalDegree = DD + (MM/60) + (SS/3600)
    return decimalDegree


print(decimalDegree("5"+chr(176)+"0"+"'" +"0" + '"'))

    
