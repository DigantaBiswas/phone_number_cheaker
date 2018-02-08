def suggation(position0, position1, position2, position3,position4,position5,position6,position7,position8):
    if position0=='o' and position1=='o' and position2=='':
        return 'You should immadiately on position 2'
    elif position0=='o' and position2=='o' and position1=='':
        return 'You should immadiately on position 1'
    elif position2=='o' and position1=='o' and position0=='':
        return 'You should immadiately on position 0'
    elif position0=='o' and position3=='o' and position6=='':
        return 'You should immadiately on position 6'
    elif position0=='o' and position6=='o' and position3=='':
        return 'You should immadiately on position 3'
    elif position6=='o' and position3=='o' and position0=='':
        return 'You should immadiately on position 0'
    elif position2=='o' and position5=='o' and position8=='':
        return 'You should immadiately on position 8'
    elif position2=='o' and position8=='o' and position5=='':
        return 'You should immadiately on position 5'
    elif position5=='o' and position8=='o' and position2=='':
        return 'You should immadiately on position 2'
    elif position6=='o' and position7=='o' and position8=='':
        return 'You should immadiately on position 8'
    elif position6=='o' and position8=='o' and position7=='':
        return 'You should immadiately on position 7'
    elif position7=='o' and position8=='o' and position6=='':
        return 'You should immadiately on position 6'
    elif position0=='o' and position4=='o' and position8=='':
        return 'You should immadiately on position 8'
    elif position0=='o' and position8=='o' and position4=='':
        return 'You should immadiately on position 4'
    elif position4=='o' and position8=='o' and position0=='':
        return 'You should immadiately on position 0'
    elif position2=='o' and position4=='o' and position6=='':
        return 'You should immadiately on position 6'
    elif position2=='o' and position6=='o' and position4=='':
        return 'You should immadiately on position 4'
    elif position6=='o' and position4=='o' and position25=='':
        return 'You should immadiately on position 0'

def input_current_game():
    g_position1=input('Input value of position 0')
    g_position2=input('Input value of position 1')
    g_position3=input('Input value of position 2')
    g_position4=input('Input value of position 3')
    g_position5=input('Input value of position 4')
    g_position6=input('Input value of position 5')
    g_position7=input('Input value of position 6')
    g_position8=input('Input value of position 7')
    g_position9=input('Input value of position 8')

    action=suggation(g_position1,g_position2,g_position3,g_position4,g_position5,g_position6,g_position7,g_position8,g_position9)
    print (action)


input_current_game()

