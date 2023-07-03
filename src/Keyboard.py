import pygame

class Keyboard:
    # converts letter to signal
    def forward(self, letter) -> int:
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(letter)
    # and signal to letter
    def backward(self, signal):
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[signal]
    
    def draw(self, Screen, x, y , w, h, Font):
        rectangle = pygame.Rect(x, y, w, h)
        pygame.draw.rect(Screen, 'white', rectangle, width= 2, border_radius = 15)

        for i in range(26):
            letter = Font.render('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i], True, 'white')
            textbox = letter.get_rect(center = (x+w/2, y+(i + 1)*h/27) )
            Screen.blit(letter, textbox)