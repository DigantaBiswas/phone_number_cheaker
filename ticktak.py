def suggation(position1, position2):
    if(position1 == 'a' and position2 =='b'):
        return 'your move should be on c'
    elif(position1=='a' and position2=='d'):
        return 'your move should be on g'
    elif(position1=='a' and position2=='c'):
        return 'your move should be on b'
    elif(position1=='a' and position2=='g'):
        return 'your move should be on d'
    elif(position1=='b' and position2=='e'):
        return 'your move should be on h'
    elif(position1=='b' and position2=='h'):
        return 'your move should be on e'
    elif(position1=='a' and position2=='e'):
        return 'your move should be on f'
    elif(position1=='a' and position2=='f'):
        return 'your move should be on e'
    elif(position1=='g' and position2=='h'):
        return 'your move should be on i'
    elif(position1=='g' and position2=='i'):
        return 'your move should be on h'
    elif(position1=='c' and position2=='f'):
        return 'your move should be on i'
    elif(position1=='c' and position2=='i'):
        return 'your move should be on f'
    elif(position1=='b' and position2=='c'):
        return 'your move should be on a'
    elif(position1=='d' and position2=='g'):
        return 'your move should be on a'
    elif(position1=='c' and position2=='h'):
        return 'your move should be on b'
    elif(position1=='f' and position2=='i'):
        return 'your move should be on c'
    elif(position1=='g' and position2=='e'):
        return 'your move should be on c'
    elif(position1=='g' and position2=='c'):
        return 'your move should be on e'
    elif(position1=='e' and position2=='c'):
        return 'your move should be on g'
    elif(position1=='a' and position2=='e'):
        return 'your move should be on i'
    elif(position1=='a' and position2=='i'):
        return 'your move should be on e'
    elif(position1=='e' and position2=='i'):
        return 'your move should be on a'


def positions():
    for i=1; i<9; i++ :
        print "enter your position"+i+"value"
        position=input()
    action=
