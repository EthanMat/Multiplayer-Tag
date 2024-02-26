import os
import pygame

width = 1200
height = 700
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 1

class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.vel_y = 0
        self.width = width
        self.height = height
        self.rect = (x, y, width, height)
        self.PLAYER_IMAGE = pygame.image.load("Assets/Player" + str (clientNumber) + "/main.png")
        self.image = pygame.transform.scale(self.PLAYER_IMAGE, (self.width, self.height))
        self.vel = 3

    def draw(self, WIN):
        WIN.blit(self.image, self.rect)
        print(self.x)
        print(self.y)

    def move(self):
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_LEFT] and self.x > 0:
            dx -= self.vel

        if keys[pygame.K_RIGHT] and self.x < width - self.width:
            dx += self.vel

        if keys[pygame.K_UP] and self.y > 0:
            dy -= self.vel

        if keys[pygame.K_DOWN] and self.y < height - self.height:
            dy += self.vel

        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        if self.y > height - self.height:
            dy = 0

        self.x += dx
        self.y += dy

        self.rect = (self.x, self.y, self.width, self.height)

def redrawWINdow(WIN, player):
    WIN.fill((255, 255, 255))
    player.draw(WIN)
    pygame.display.update()

def main():
    run = True
    p = Player(50, 50, 50, 50)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWINdow(WIN, p)

main()