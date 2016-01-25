import pygame
from Button import *

def rtext(txt,offset):
  smallText = pygame.font.Font('freesansbold.ttf',20)
  TextSurf, TextRect = text_objects(txt, smallText)
  TextRect.left = (20)
  TextRect.top = (display_height/4+50+(offset*23))
  gameDisplay.blit(TextSurf, TextRect)

def game_rules(self):

    next = "rules"

    while next == "rules":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(navy)
        pygame.draw.rect(gameDisplay, black,(10,(display_height/4+40),display_width-20,385))
        pygame.draw.rect(gameDisplay, gray,(15,(display_height/4+45),display_width-30,375))
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("RULES", largeText)
        TextRect.center = ((display_width/2),(display_height/6))
        gameDisplay.blit(TextSurf, TextRect)
        rtext("1. Diegene die het hoogst gooit begint met het spel", 0)
        rtext("2. Elke speler heeft zijn eigen hoek en start in die hoek met de klok mee", 1)
        rtext("3. Elke speler begint met 100 levenspunten en 15 conditiepunten", 2)
        rtext("4. Elke speler heeft een scorekaart van zijn karakter en een bijpassende pion", 3)
        rtext("5. Er wordt gedobbeld om voort te bewegen over het spelbord", 4)
        rtext("6. Wanneer een speler op een vakje 'Fight!' terecht komt, moet deze vechten tegen een superfighter", 5)
        rtext("7. Aan de hand van de scorekaart en de gedobbelde waarde kan een speler zijn aanval kiezen", 6)
        rtext("8. Wanneer men geen conditiepunten heeft, kan er geen aanval gekozen", 7)
        rtext("9. Wanneer er gevochten moet worden en beide spelers geen conditiepunten hebben, verliest de verdediger 15 levenspunten", 8)
        rtext("10. De hoogste aanval - de laagste aanval = het aantal levenspunten dat de speler met de laagste aanval kwijt raakt", 9)
        rtext("11. Wanneer er twee spelers op hetzelfde vak komen, wordt er tegen elkaar gevochten", 10)
        rtext("12. Wanneer er twee spelers op hetzelfde 'Fight!'-vak terecht komen wordt er alleen gevochten met de superfighter", 11)
        rtext("13. Als je langs je eigen hoek komt krijg je het maximale aantal conditiepunten (15)", 12)
        rtext("14. Je ontvangt 10 levenspunten als je op je eigen hoek komt", 13)
        rtext("15. Als de speler van een hoek af is of als een hoek geen speler heeft, geven de vakjes van die hoek -10 levenspunten schade", 14)
        rtext("16. Als je geen levenspunten meer hebt, heb je verloren", 15)

        button("BACK",(display_width/2-100),640,200,50,dark_gray,gray,game_menu)

        pygame.display.update()
        clock.tick(15)
