class game_menu:
   
   def game_menu(self):

        next = "menu"
        while next == "menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
            gameDisplay.fill(navy)
            largeText = pygame.font.Font('freesansbold.ttf',115)
            TextSurf, TextRect = text_objects("MENU", largeText)
            TextRect.center = ((display_width/2),(display_height/6))
            gameDisplay.blit(TextSurf, TextRect)
      
            button("PLAY",(display_width/2-100),240,200,50,dark_gray,gray,game_loop)
            button("RULES",(display_width/2-100),340,200,50,dark_gray,gray,game_rules)
            button("EXIT",(display_width/2-100),440,200,50,dark_gray,gray,quitgame)

            pygame.display.update()
            clock.tick(15)
