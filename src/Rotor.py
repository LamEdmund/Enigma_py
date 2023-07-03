import pygame

class Rotor:
    def __init__(self, wiring, notch):
        self.rotor_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.rotor_wiring = wiring
        self.notch = notch # represents the turnover notch on the rotor

    # use a different rotor, ring settings need to be applied seperately
    def changeRotor(self, new_wiring, new_notch):
        self.rotor_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.rotor_wiring = new_wiring
        self.notch = new_notch

    def showRotor(self):
        print(self.rotor_alphabet)
        print(self.rotor_wiring)
        print("")
        
    # shift the string to the left to "rotate" the rotor
    def step(self, steps) -> None:
        self.rotor_alphabet = self.rotor_alphabet[steps:] + self.rotor_alphabet[:steps]
        self.rotor_wiring = self.rotor_wiring[steps:] + self.rotor_wiring[:steps]

    def forward(self, signal):
        letter = self.rotor_wiring[signal]
        signal = self.rotor_alphabet.find(letter)
        return signal

    def backward(self, signal):
        letter = self.rotor_alphabet[signal]
        signal = self.rotor_wiring.find(letter)
        return signal
    
    # apply the ring setting which will offset the rotor internally
    def setRing(self, ring_setting):
        # rotate backwards
        self.step(-ring_setting)
        # adjust notch
        new_Notch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(self.notch)
        self.notch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[(new_Notch - ring_setting) % 26]
    
    def draw(self, Screen, x, y , w, h, Font):
        rectangle = pygame.Rect(x, y, w, h)
        pygame.draw.rect(Screen, 'white', rectangle, width= 2, border_radius = 15)

        for i in range(26):
            # left
            letter = Font.render(self.rotor_alphabet[i], True, 'white')
            textbox = letter.get_rect(center = (x+w/4, y+(i + 1)*h/27) )
            # highlight rotor pos
            if i == 0:
                pygame.draw.rect(Screen, 'teal', textbox, border_radius = 5)
            if self.rotor_alphabet[i] == self.notch:
                pygame.draw.rect(Screen, 'blue', textbox, border_radius = 5)
            Screen.blit(letter, textbox)

            # right
            letter = Font.render(self.rotor_wiring[i], True, 'white')
            textbox = letter.get_rect(center = (x+w*3/4, y+(i + 1)*h/27) )
            Screen.blit(letter, textbox)

