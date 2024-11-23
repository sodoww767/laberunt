import pygame

pygame.init()

window = pygame.display.set_mode((700,500))
pygame.display.set_caption("Лабіринт")

forest = pygame.transform.scale(pygame.image.load("forest.png"), (700,500))

#sp_1 = pygame.transform.scale(pygame.image.load("1.png"), (50,50))
#sp_2 = pygame.transform.scale(pygame.image.load("2.png"), (50,50))
#gold = pygame.transform.scale(pygame.image.load("gold.png"), (50,50))

game_over = False

clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play()

kick = pygame.mixer.Sound("kick.ogg")

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x = 0,player_y = 0,player_speed=5):
        self.image = pygame.transform.scale(pygame.image.load(player_image),(65,65))
        self.rect = self.image.get_rect()
        self.x = player_x
        self.y = player_y
        self.speed = player_speed

    def draw(self):
        window.blit(self.image,(self.x,self.y))

sp_1 = GameSprite("1.png",0, 0 ,10)
sp_2 = GameSprite("2.png",100, 100, 15)
gold = GameSprite("gold.png",200, 200, 5)

while not game_over:
    window.blit(forest,(0,0))
    
    sp_1.draw()
    sp_2.draw()
    gold.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
