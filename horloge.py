import time

class Horloge:
    def __init__(self, mode_12_heures=False):
        self.mode_12_heures = mode_12_heures
        self.en_marche = True
        self.alarme = None
        self.pause = False
        self.heure = (0, 0, 0)

    def afficher_heure(self):
        if self.mode_12_heures:
            heures = self.heure[0] % 12
            if heures == 0:
                heures = 12
            suffixe = 'AM' if self.heure[0] < 12 else 'PM'
            heure_formattee = "{:02d}:{:02d}:{:02d} {}".format(heures, self.heure[1], self.heure[2], suffixe)
        else:
            heure_formattee = "{:02d}:{:02d}:{:02d}".format(self.heure[0], self.heure[1], self.heure[2])
        print(heure_formattee)

    def regler_heure(self, heures, minutes, secondes):
        self.heure = (heures, minutes, secondes)
        self.afficher_heure()

    def regler_alarme(self, heures, minutes, secondes):
        self.alarme = (heures, minutes, secondes)

    def verifier_alarme(self):
        if self.alarme and self.heure == self.alarme:
            print("Alarme! L'heure correspond à l'heure de l'alarme.")

    def choisir_mode_affichage(self, mode_12_heures):
        self.mode_12_heures = mode_12_heures
        self.afficher_heure()

    def mettre_en_pause(self):
        self.pause = True

    def relancer(self):
        self.pause = False

    def demarrer(self):
        while self.en_marche:
            if not self.pause:
                self.heure = tuple(time.localtime(time.time())[3:6])
                self.afficher_heure()
                self.verifier_alarme()
            time.sleep(1)

if __name__ == "__main__":
    horloge = Horloge(mode_12_heures=False) 
    horloge.regler_heure(16, 30, 0) 
    horloge.regler_alarme(17, 0, 0) 
    horloge.demarrer()
