import pygame
from pygame.locals import *
import sys
import time
import random   
    
class TypingSpeed:
   
    def __init__(main):
        main.width=750
        main.height=500
        main.input_text=''
        main.word = ''
        main.reset=True
        main.active = False
        main.accuracy = '0%'
        main.time_start = 0
        main.time_total = 0
        main.results = 'Time:0 Accuracy:0 % Wpm:0 '
        main.wpm = 0
        main.end = False
        main.HEAD_Area = (255,213,102)
        main.TEXT_Area = (240,240,240)
        main.RESULT_Area = (255,70,70)
        
       
        pygame.init()
        main.open_img = pygame.image.load('bg0.jpg')
        main.open_img = pygame.transform.scale(main.open_img, (main.width,main.height))


        main.bg = pygame.image.load('bg1.jpg')
        main.bg = pygame.transform.scale(main.bg, (750,500))

        main.screen = pygame.display.set_mode((main.width,main.height))
        pygame.display.set_caption('Test Your Typing Speed')
       
    def get_sentence(main):
        f = open('sentences.txt').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence

    def draw_text(main, screen, msg, y ,fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1,color)
        text_rect = text.get_rect(center=(main.width/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()     
        

    def show_results(main, screen):
        if(not main.end):
            
            main.time_total = time.time() - main.time_start
               
            #Calculate accuracy
            count = 0
            for i,users_text in enumerate(main.word):
                try:
                    if main.input_text[i] == users_text:
                        count += 1
                except:
                    pass

            main.accuracy = count/len(main.word)*100
           
            
            main.wpm = len(main.input_text)*60/( 6*main.time_total)
            main.end = True

            print("You took ",main.time_total," to complete the test.")
                
            main.results = 'Time:'+str(round(main.time_total)) +" secs   Accuracy:"+ str(round(main.accuracy)) + "%" + '   Wpm: ' + str(round(main.wpm))

            
            main.time_img = pygame.image.load('icon.png')
            main.time_img = pygame.transform.scale(main.time_img, (50,50))

            screen.blit(main.time_img, (main.width/2 -25,main.height-90))
            main.draw_text(screen,"Try Again", main.height - 110, 26, (100,100,100))
            
            print(main.results)
            pygame.display.update()

    def run(main):
        main.reset_game()
        
    
       
        main.running=True
        while(main.running):
            clock = pygame.time.Clock()
            main.screen.fill((0,0,0), (50,250,650,50))
            pygame.draw.rect(main.screen,main.HEAD_Area, (50,250,650,50), 2)
            # update the text of user input
            main.draw_text(main.screen, main.input_text, 274, 26,(250,250,250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    main.running = False
                    pygame.display.quit()
                    pygame.quit()
                    quit()
                                
                elif event.type == pygame.KEYDOWN:
                    if main.active and not main.end:
                        if event.key == pygame.K_RETURN:
                            print("Text given : ")
                            print(main.word)
                            print("Your input : ")
                            print(main.input_text)
                            main.show_results(main.screen)
                            main.draw_text(main.screen, main.results,350, 28, main.RESULT_Area)  
                            main.end = True
                            
                        elif event.key == pygame.K_BACKSPACE:
                            main.input_text = main.input_text[:-1]
                        else:
                            try:
                                main.input_text += event.unicode
                            except:
                                pass

                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    # position of input box
                    if(x>=50 and x<=650 and y>=250 and y<=300):
                        main.active = True
                        main.input_text = ''
                        main.time_start = time.time() 

                     # position of reset box
                    if(x>=310 and x<=510 and y>=390 and main.end):
                        main.reset_game()
                        x,y = pygame.mouse.get_pos()
            
            pygame.display.update()
             
                
        clock.tick(60)

    def reset_game(main):

        main.screen.blit(main.open_img, (0,0))

        pygame.display.update()
        time.sleep(2)
        
        main.active=False
        main.reset=False
        main.end = False

        main.input_text=''
        main.word = ''
        main.time_start = 0
        main.time_total = 0
        main.wpm = 0

        main.word = main.get_sentence()
        if (not main.word): main.reset_game()

        #Heading
        main.screen.fill((0,0,0))
        main.screen.blit(main.bg,(0,0))
        msg = "Typing Speed Test"
        main.draw_text(main.screen, msg,80, 80,main.HEAD_Area)  
        # rectangle for input box
        pygame.draw.rect(main.screen,(255,192,25), (50,250,650,50), 2)

        # sentence string
        main.draw_text(main.screen, main.word,200, 28,main.TEXT_Area)
        
        pygame.display.update()



TypingSpeed().run()
