# tee ratkaisu tänne
import string

def jaa_merkkeihin(merkkijono: str):

    eka = ""
    toka = ""
    kolmas = ""
    for i in merkkijono:
        if i in string.ascii_letters:
            eka = eka + i
        elif i in string.punctuation:
            toka += i
        else:
            kolmas += i
    
    return eka,toka,kolmas


osat = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
print(osat[0])
print(osat[1])
print(osat[2])