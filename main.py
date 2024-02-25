import os
import pygame

width = 1200
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 1

class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = (x, y, width, height)
        self.PLAYER_IMAGE = pygame.image.load("Assets/Player" + str (clientNumber) + "/main.png")
        self.image = pygame.transform.scale(self.PLAYER_IMAGE, (self.width, self.height))
        self.vel = 3

    def draw(self, win):
        win.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)

def redrawWindow(win, player):
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()

def main():
    run = True
    p = Player(50, 50, 100, 100)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p)

main()