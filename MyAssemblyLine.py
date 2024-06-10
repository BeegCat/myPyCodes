import pygame
import time

pygame.init()

screenx=1200
screeny=600

windw= pygame.display.set_mode((screenx, screeny))

pygame.display.set_caption("simulation testing")
clk= pygame.time.Clock()

class Production:
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.color=(255,0,0)
        self.count=0

    def draw(self, windw):
        pygame.draw.rect(windw,self.color,(self.x,self.y,self.width,self.height), 0)

    def move(self):
        self.x+=self.vel

    def wait(self):
        self.vel=0

    def count_and_finish(self):
        global count
        count+=1

class Workstation():
    def __init__(self, name, x, y, width, height, cycltime):
        self.name=name
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.cycltime=cycltime
        self.color=(0,255,0)
        self.complete= False
        self.seconds=0
        self.secondstotal=0

    def draw(self, windw):
        pygame.draw.rect(windw, self.color, (self.x, self.y, self.width, self.height), 0)
    
    def doWork(self):
        self.seconds= clk.get_time()/1000
        self.secondstotal+=self.seconds
        if self.secondstotal>=self.cycltime:
            self.complete=True
            self.seconds=0
            self.secondstotal=0

def redrawScreen():
    windw.fill((0,0,0))
    pygame.draw.line(windw, (255, 0, 0), (0, screeny//2+155), (screenx, screeny//2+155), 5)
    pygame.draw.line(windw, (255, 0, 0), (0, screeny//2-155), (screenx, screeny//2-155), 5)    
    ws1.draw(windw)
    ws2.draw(windw)
    ws3.draw(windw)
    
    for product in products:
        product.draw(windw)

    windw.blit(pygame.font.SysFont('None',50).render('ws1'+str(round(ws1.cycltime-ws1.secondstotal,2)),0,(255,255,255)), (ws1.x,ws1.y-55))
    windw.blit(pygame.font.SysFont('None',50).render('ws2'+str(round(ws2.cycltime-ws1.secondstotal,2)),0,(255,255,255)), (ws2.x,ws2.y-55))
    windw.blit(pygame.font.SysFont('None',50).render('ws3'+str(round(ws3.cycltime-ws1.secondstotal,2)),0,(255,255,255)), (ws3.x,ws3.y-55))
    windw.blit(pygame.font.SysFont('None',50).render('count'+str(count), 0, (255,255,255)), (5,5))

    pygame.display.update()

count=0
products=[]
ws1=Workstation("ws1", 200, 165, 160, 165, 5)
ws2=Workstation("ws1", 500, 165, 160, 165, 8)
ws3=Workstation("ws1", 800, 165, 160, 165, 3)
    
run=True
while run:
    clk.tick(30)
    for evt in pygame.event.get():
        if evt.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        time.sleep(.25)
        products.append(Production(0,round(screeny//2-75), 150, 150))

    for product in products:
        if product.x>=0 and product.x + product.width + 15<=screenx:
            if products.index(product)!=0:
                if product.x>=products[products.index(product)-1].x-product.width-10:
                    product.wait()
                elif product.x==ws1.x+5:
                    product.wait()
                    ws1.doWork()
                    if ws1.complete:
                        product.vel=5
                        ws1.complete=False
                        product.move()
                elif product.x==ws2.x+5:
                    product.wait()
                    ws2.doWork()
                    if ws1.complete:
                        product.vel=5
                        ws2.complete=False
                        product.move()
                elif product.x==ws3.x+5:
                    product.wait()
                    ws3.doWork()
                    if ws3.complete:
                        product.vel=5
                        ws3.complete=False
                        product.move()
                else:
                    product.vel=5
                    product.move()
            else:
                if product.x==ws1.x+5:
                    product.wait()
                    ws1.doWork()
                    if ws1.complete:
                        product.vel=5
                        ws1.complete=False
                        product.move()
                elif product.x==ws2.x+5:
                    product.wait()
                    ws2.doWork()
                    if ws1.complete:
                        product.vel=5
                        ws2.complete=False
                        product.move()
                elif product.x==ws3.x+5:
                    product.wait()
                    ws3.doWork()
                    if ws3.complete:
                        product.vel=5
                        ws3.complete=False
                        product.move()
                else:
                    product.vel=5
                    product.move()
        else:
            product.pop(products.index(product))
            product.count_and_finish()
    print(str(count))
    redrawScreen()
pygame.quit()