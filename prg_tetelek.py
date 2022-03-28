#hozzatok létre egy sum füvvgényt ami paraméterül egész számok listájár kapja és összegzi ezeket és az összeggel tér vissza
szamok = [2,4,6,2,345,6,34]

def osszead(lista):
    osszeg = 0
    for szam in lista:
        osszeg +=szam

    return osszeg

print(osszead(szamok))

#számlálás tétele
#írjatok egy olyan függvényt ami paraméterül kap egy stringet és visszaadja hogy hány magyar ékezetes karakter van benne
def ekezet(szo):
    count = 0
    for betu in szo:
        if betu in "íöüóőúéáűÍÖÜÓŐÚŰÁÉ":
            count +=1

    return count

print(ekezet("töltőtoll"))