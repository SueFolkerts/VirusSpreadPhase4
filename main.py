import pygame
from pygame.locals import *
import random
from virus import VirusNode
from doctor import Doctor
pygame.init()
size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (26, 255, 255)
font = pygame.font.SysFont(None, 70)
split_times = 10
bacteria = pygame.sprite.Group()
doctors = pygame.sprite.Group()
doc_num = 1
bac_num = 5
split_time = 500
done = False
# NEW FOLLOWS ***************************************
round_over = False
# NEW ABOVE *****************************************

def process_events():
    global done
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

def init():
# NEW FOLLOWS ****************************************
    global round_over
    bacteria.empty()
    doctors.empty()
    round_over = False
# NEW FOLLOWS ****************************************
    for i in range(bac_num):
        bacteria.add(VirusNode((random.randint(50, width - 50),
                                random.randint(50, height - 50)), split_time))
    for i in range(doc_num):
        doctors.add(Doctor((random.randint(50, width - 50), random.randint(50, height - 50))))

# NEW FOLLOWS ************************************************************************************
# Pause the game for about 5 seconds while still allowing events
def timeout():
    for i in range(300):
        clock.tick(60)
        process_events()

def end_of_round():
    timeout()
    init()
# NEW ABOVE **************************************************************************************

def main():
# NEW FOLLOWS **********************************************************
    global round_over
# NEW ABOVE ************************************************************
    init()
    while not done:
        clock.tick(60)
        process_events()
        if len(bacteria) > bac_num * split_times:
            text = font.render("You were overrun", True, (255, 0, 0))
            text_rect = text.get_rect()
# NEW FOLLOWS ***********************************************************
            round_over = True
# NEW ABOVE *************************************************************
        elif len(bacteria) == 0:
            text = font.render("Outbreak stopped", True, (255, 0, 0))
            text_rect = text.get_rect()
# NEW FOLLOWS ***********************************************************
            round_over = True
# NEW ABOVE *************************************************************
        else:
            doctors.update()
            bacteria.update()
            pygame.sprite.groupcollide(doctors, bacteria, False, True)
            text = font.render("Bacteria Count: {}".format(len(bacteria)), True, (255, 0, 0))
            text_rect = text.get_rect()
        doctors.update()
        bacteria.update()
        screen.fill(color)
        doctors.draw(screen)
        screen.blit(text, text_rect)
        bacteria.draw(screen)
        pygame.display.flip()
# NEW FOLLOWING *******************************************************************************
        if round_over:
            end_of_round()
# NEW ABOVE ***********************************************************************************

if __name__ == "__main__":
    main()
