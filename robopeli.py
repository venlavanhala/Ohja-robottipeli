import pygame
import random

class Robottipeli:
    def __init__(self):
        pygame.init()
        self.hirvio=pygame.image.load("monster.png")
        self.kolikko=pygame.image.load("coin.png")
        self.robo=pygame.image.load("robot.png")
        self.fontti = pygame.font.SysFont("Arial", 24)
        self.x=0
        self.y=480-self.robo.get_height()
        #self.naytto=pygame.display.set_mode((640, 480))
        self.naytto=pygame.display.set_mode((1000, 700))
        self.naytto.fill((102, 0, 102))
        pygame.display.set_caption("Robottipeli")
        self.kello = pygame.time.Clock()
        self.vihut = []
        self.rahat=[]
        self.pisteet=0
        self.silmukka()

    def silmukka(self):
        self.oikealle=False
        self.vasemmalle=False
        k= 0
        vaikeus=3000
        while True:
            k= (k+1)%(vaikeus//100)
            self.tutki_tapahtumat()
            self.piirra_naytto()
            if random.randint(0,vaikeus)==1:
                self.luo_vihu()
                self.luo_raha()
                vaikeus= max(1000,int(vaikeus-vaikeus/1000))
            if k==0:
                self.liikuta_vihuja()
                self.liikuta_rahoja()
            self.kello.tick(400)
            
    def luo_raha(self):
        self.rahat.append([random.randint(self.kolikko.get_width(),1000-self.kolikko.get_width()),-self.kolikko.get_height(),random.randint(1,2)*2])

    def luo_vihu(self):
        self.vihut.append([random.randint(self.hirvio.get_width(),1000-self.hirvio.get_width()),-self.hirvio.get_height(),random.randint(0,2)*2+1])
            
    def liikuta_rahoja(self):
        for raha in self.rahat:
            raha[1]+=raha[2]
            if raha[0]-10<self.x<raha[0]+self.kolikko.get_width() and raha[1]<self.y<raha[1]+self.kolikko.get_height():
                self.voitto()
                self.rahat.remove(raha)
            if raha[1]>480:
                self.rahat.remove(raha)

    def liikuta_vihuja(self):
        for vihu in self.vihut:
            vihu[1]+=vihu[2]
            if vihu[0]<self.x<vihu[0]+self.hirvio.get_width() and vihu[1]<self.y<vihu[1]+self.hirvio.get_height():
                self.havio()
            if vihu[1]>480:
                self.vihut.remove(vihu)

    def havio(self):
        teksti=self.fontti.render("Haluatko pelata uudelleen? Esc=En, Enter=Kyllä",True,(223,0,0))
        self.naytto.blit(teksti, (25, 40 * 200 + 10))
        quit()

    def voitto(self):
        self.pisteet+=1

    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle=True
                if tapahtuma.key==pygame.K_RIGHT:
                    self.oikealle=True
                if tapahtuma.key==pygame.K_RETURN:
                    self.silmukka()
            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key==pygame.K_LEFT:
                    self.vasemmalle=False
                if tapahtuma.key==pygame.K_RIGHT:
                    self.oikealle=False
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
                exit()
        

    def piirra_naytto(self):
        self.naytto.fill((102, 0, 102))
        self.naytto.blit(self.robo, (self.x, 200))
        teksti=self.fontti.render(f"Pisteesi: {self.pisteet}",True,(10,0,10))
        self.naytto.blit(teksti, (80,60))
        if self.oikealle:
            self.x+=0.4
        if self.vasemmalle:
            self.x-=0.4
        for vihu in self.vihut:
            self.naytto.blit(self.hirvio,(vihu[0],vihu[1]))
        for raha in self.rahat:
            self.naytto.blit(self.kolikko,(raha[0],raha[1]))
        pygame.display.flip()

if __name__ == "__main__":
    Robottipeli()