STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

class igra:
    def __init__(self,geslo,crke=[]):
        self.geslo = geslo.upper()
        self.crke = crke

    def pravilne_crke(self):
            #pravilne = []
            #for crka in self.crke:
            #    if crka in self.geslo:       to jer isto kt uno spodi :)
            #        pravilne.append(crke):
            #return pravilne        
        return [crka for crka in self.crke if crka in self.geslo]

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False    
        return True

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        izpis = ''   
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                izpis += crka 
            else:
                izpis +='_'
        return izpis

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self,crka):
        velika_crka = crka.upper()
        self.crke.append(velika_crka)
        if self.zmaga():
            return ZMAGA
        elif self.poraz():
            return PORAZ
        else:
            if velika_crka in self.pravilne_crke():
                return PRAVILNA_CRKA
            elif velika_crka in self.napacne_crke():
                return NAPACNA_CRKA


bazen_besed = []
with open('besede.txt') as f:
    for vrstica in f:
        bazen_besed.append(vrstica.strip())

def nova_igra():
    import random
    izbrana_beseda = random.choice(bazen_besed)
    return igra(izbrana_beseda)


class Vislice:

    def __init__(self):
        self.igre = {}
 
    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre

    def ugibaj(self,id_igre,crka):
        igra,_ = self.igre[id_igre]
        poskus = igra.ugibaj(crka)
        self.igre[id_igre] = (igra,poskus)



