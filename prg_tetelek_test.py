import prg_tetelek
from prg_tetelek import osszead
from prg_tetelek import ekezet
def test_osszead():
    #given
    numbers = [1,2,3,4,5,6,7,8,9,10]

    #when
    result = osszead(numbers)

    #then
    #összehasonlítjuk az elvárt értékeket a kapott értékekkel
    assert result==55 #output

def test_osszead_short():
    assert osszead([1,2,3,4,5,6,7,8,9,10]) == 55

def test_countekezet():
    assert ekezet("töltőtőll") == 3