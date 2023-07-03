import pygame

class Plugboard:
    # convert string format for plugboard setting into a dictionary
    def __init__(self, plug_setting) -> None:
        self.start_point = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.end_point = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.plugboardConnections = plug_setting.upper().split(" ")
        
        self.plugboard_Dict = {}
        for pair in self.plugboardConnections:
            if len(pair)==2:
                pos_A = self.end_point.find(pair[0])
                pos_B = self.end_point.find(pair[1])
                self.end_point = self.end_point[:pos_A] + pair[1] + self.end_point[pos_A + 1:]
                self.end_point = self.end_point[:pos_B] + pair[0] + self.end_point[pos_B + 1:]
                '''
                self.plugboard_Dict[pair[0]] = pair[1]
                self.plugboard_Dict[pair[1]] = pair[0]
                
                # 13 is the maximum number of cables allowed
                if len(self.plugboard_Dict) == 13:
                    break
                '''
    def forward(self, signal):
        letter = self.start_point[signal]
        signal = self.end_point.find(letter)
        return signal
    
    def backward(self, signal):
        letter = self.end_point[signal]
        signal = self.start_point.find(letter)
        return signal
    
    '''
    # check if a letter is in the dictionary, returns its value if so otherwise pass letter as is.
    def checkBoard(self, letter) -> int:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        letter = alphabet[letter]
        if letter in self.plugboard_Dict.keys():
            if self.plugboard_Dict[letter]!="":
                return alphabet.index(self.plugboard_Dict[letter])
        else:
            return alphabet.index(letter)
    '''
    def draw(self, Screen, x, y , w, h, Font):
        rectangle = pygame.Rect(x, y, w, h)
        pygame.draw.rect(Screen, 'white', rectangle, width= 2, border_radius = 15)

        for i in range(26):
            # left
            letter = Font.render(self.end_point[i], True, 'white')
            textbox = letter.get_rect(center = (x+w/4, y+(i + 1)*h/27) )
            Screen.blit(letter, textbox)

            # right
            letter = Font.render(self.start_point[i], True, 'white')
            textbox = letter.get_rect(center = (x+w*3/4, y+(i + 1)*h/27) )
            Screen.blit(letter, textbox)