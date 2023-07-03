import pygame

class Reflector:
    def __init__(self, wiring):
        self.rotor_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.rotor_wiring = wiring

    def forward(self, signal):
        letter = self.rotor_wiring[signal]
        signal = self.rotor_alphabet.find(letter)
        return signal

    def draw(self, Screen, x, y , w, h, Font):
        rectangle = pygame.Rect(x, y, w, h)
        pygame.draw.rect(Screen, 'white', rectangle, width= 2, border_radius = 15)

        for i in range(26):
            # left
            letter = Font.render(self.rotor_alphabet[i], True, 'white')
            textbox = letter.get_rect(center = (x+w/4, y+(i + 1)*h/27) )
            Screen.blit(letter, textbox)

            # right
            letter = Font.render(self.rotor_wiring[i], True, 'white')
            textbox = letter.get_rect(center = (x+w*3/4, y+(i + 1)*h/27) )
            Screen.blit(letter, textbox)
