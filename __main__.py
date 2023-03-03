<<<<<<< HEAD
# libraries used
import pygame
from pygame.locals import *
import random

# Files
from genome import Genome
from geneh import GeneHistory
from population import Population

population = Population(100, 6, 1)

WIDTH = 400
HEIGHT = 400

pygame.display.init()
ds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Test')

sample_inputs = [(random.random()) for a in range(population.n_inputs)]

def setup():
    pass

def keydown_event(brain, event):
    # Set ctr to show best members of population
    show = True
    if event.key == K_n:
        population.next()
    if event.key == K_b:
        population.prev()
    
    if event.key == K_c:
        brain.add_gene()
    if event.key == K_a:
        brain.add_node()
    if event.key == K_m:
        brain.mutate()
    if event.key == K_o:
        print(brain.get_outputs(sample_inputs))

    if event.key == K_s:
        # Divide population in species
        population.speciate()
        # Evaluate each species
        for s in range(len(population.species)):
            population.species[s].evaluate()
        show = False

    if show:
        print(brain.get_outputs(sample_inputs))
        print(brain)

def mainloop():
    setup()
    run = True
    while run:
        ds.fill((255, 255, 255))
        population.best.show(ds)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                keydown_event(population.best, event)

        pygame.display.update()
    pygame.quit()
=======
import pygame

WIDTH = 600
HEIGHT = 600
FPS = 60

pygame.display.init()
main_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird AI")
clock = pygame.time.Clock()

def mainloop():
    run = True
    while run:
        main_screen.fill((11, 11, 11))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
        clock.tick(FPS)
    pass
>>>>>>> main

if __name__ == "__main__":
    mainloop()
