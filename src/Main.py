import pygame
import Draw
from Enigma import Enigma

if __name__ =='__main__':
    # init pygame
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Enigma Simulator')

    MonoFont = pygame.font.SysFont('Arial', 20)
    BoldFont = pygame.font.SysFont('Arial', 20, bold = True)
    width = 1600
    height = 900

    # RotorA, RotorB, RotorC, reflector, plug connections, rotor starting positions, ring settings
    EnigmaMachine = Enigma('I', 'II', 'III', 'UKW-B', 'AB CD EF', 'AAC', 'AAA')
    Screen = pygame.display.set_mode((width, height))

    input_string = ''
    output_string = ''

    main_loop = True
    while main_loop:
        # drawing code
        # put stuff after screen.fill or else it will paint over
        Screen.fill('black') # dim grey: #696969

        Draw.drawIOStrings(Screen, input_string, output_string, width, height, MonoFont)
        Draw.drawComponents(EnigmaMachine, Screen, width, height, BoldFont)
        pygame.display.flip()
        

        # track user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_loop = False
            elif event.type == pygame.KEYDOWN:
                # manual adjustment of rotor positions via left, down and right key
                # not done during machine operation
                if event.key == pygame.K_DOWN:
                    EnigmaMachine.RotorB.step(1)
                elif event.key == pygame.K_LEFT:
                    EnigmaMachine.RotorA.step(1)
                elif event.key == pygame.K_RIGHT:
                    EnigmaMachine.RotorC.step(1)
                elif event.key == pygame.K_UP: # save for debug
                    pass
                elif event.key == pygame.K_BACKSPACE: # clear text
                    input_string, output_string = '',''
                else:
                    key = event.unicode
                    if key in 'abcdefghijklmnopqrstuvwxyz':
                        letter = key.upper()
                        input_string = input_string + letter
                        cipher_letter = EnigmaMachine.encode(letter)
                        # print(EnigmaMachine.encryption_path)
                        output_string = output_string + cipher_letter
                        # use string slicing to ditch the oldest letter
                        if len(input_string) > 24:
                            input_string = input_string[1:]
                            output_string = output_string[1:]