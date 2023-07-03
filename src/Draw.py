import pygame

margins = {'top': 200, 'bottom': 200, 'left': 100, 'right': 100}

# draw our input and output strings
def drawIOStrings(Screen, input_string, output_string, width, height, Font):
    spacing = 20
    width = width/2
    height = height/11

    # cypher text usually gets split into groups of 4
    # https://www.geeksforgeeks.org/python-insert-character-after-every-character-pair/
    input_string = '   '.join(input_string[i:i+4] for i in range(0, len(input_string),4))
    output_string = '   '.join(output_string[i:i+4] for i in range(0, len(output_string),4))

    # draw text input
    input_text = Font.render(input_string, True, 'white')
    textbox = input_text.get_rect(center = (width, height) )
    Screen.blit(input_text, textbox)
    # draw text output
    output_text = Font.render(output_string, True, 'white')
    textbox = output_text.get_rect(center = (width, height + spacing) )
    Screen.blit(output_text, textbox)

# draw our enigma machine with encryption path if available      
def drawComponents(EnigmaMachine, Screen, width, height, Font):
    # draw var for machine
    # margins = {'top': 200, 'bottom': 200, 'left': 100, 'right': 100}
    x_coord = margins['left']
    y_coord = margins['top']
    x_spacing = 100
    component_width = (width - margins['left'] - margins['right'] - 5 * x_spacing) / 6
    component_height = height - margins['top'] - margins['bottom']
    
    # generate path coordinates and draw it
    if len(EnigmaMachine.encryption_path) > 0:
        y = [margins['top']+(signal + 1) * component_height/27 for signal in EnigmaMachine.encryption_path]
        x = [width - margins['right'] - component_width/2]
        for i in [4,3,2,1,0]: # forward
            x.append(margins['left'] + i * (component_width + x_spacing) + component_width*3/4)
            x.append(margins['left'] + i * (component_width + x_spacing) + component_width*1/4)
        x.append(margins['left'] + component_width*3/4) #reflector
        for i in [1,2,3,4]: # Backward
            x.append(margins['left'] + i * (component_width + x_spacing) + component_width*1/4)
            x.append(margins['left'] + i * (component_width + x_spacing) + component_width*3/4)
        x.append(width - margins['right'] - component_width/2)

        # draw path
        # pygame does not like transparent lines so none of that for now
        for i in range(1, 21):
                if i < 10: # forward
                    color = '#228B22' # forest green #228B22
                elif i < 12: # reflector
                        color = '#CCCC00' # dark yellow #CCCC00
                else: # backward
                        color = '#8B0000' # dark red #8B0000
                start = [x[i-1], y[i-1]]
                end =  [x[i], y[i]]
                pygame.draw.line(Screen, color, start, end, width=2)
        pygame.draw.circle(Screen, '#5A5A5A', [x[0],y[0]], 10) # circle for keyboard
        pygame.draw.circle(Screen, '#CCCC00', end, 10) # draw lamplight

    # draw machine components
    # box outline for text
    pygame.draw.rect(Screen, 
                     'white',
                      pygame.Rect(width/2 - margins['left']*3, height/2 - margins['top']*2, margins['left']*6, margins['top']/2.5), 
                      width= 2, 
                      border_radius = 15)
    for component in [EnigmaMachine.ReflectorRotor, 
                        EnigmaMachine.RotorA, 
                        EnigmaMachine.RotorB, 
                        EnigmaMachine.RotorC, 
                        EnigmaMachine.Board, 
                        EnigmaMachine.Kb]:
            component.draw(Screen, x_coord, y_coord, component_width, component_height, Font)
            x_coord += component_width + x_spacing

    # draw labels
    x_coord = margins['left'] + component_width/2
    y_coord = margins['top']*4/5
    for name in ['Reflector', 'Rotor A', 'Rotor B', 'Rotor C', 'Plugboard', 'Keyboard/Lamp']:
        label = Font.render(name, True, 'white')
        textbox = label.get_rect(center = (x_coord, y_coord) )
        Screen.blit(label, textbox)
        x_coord += component_width + x_spacing