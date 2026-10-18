import random

import pygame
from pygame import mixer


class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)
        
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
pygame.init()
mixer.init()

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("My Game With Music")
clock = pygame.time.Clock()

stars = []
for _ in range(100):
    pos = Vector2D(random.randint(0, 700), random.randint(0, 500))
    vel = Vector2D(0, random.uniform(0.5, 2.03))
    stars.append({"pos": pos, "vel": vel})

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for star in stars:
        star["pos"] = star["pos"] + star["vel"]
        
        if star["pos"].x > 500:
           star["pos"].x = 0
           star["vel"].y = random.randint(0, 700)
    
    screen.fill((12, 5, 18))
    
    pygame.draw.circle(screen, color=(0, 0, 0    ))
    
    pygame.display.flip()
    
    clock.tick(165)
            
pygame.quit()
    
    