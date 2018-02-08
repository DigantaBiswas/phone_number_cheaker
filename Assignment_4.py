def decisions(last_green_side, a_traffic_condition,b_traffic_condition,c_traffic_condition,d_traffic_condition):
    if a_traffic_condition=='heavy' and b_traffic_condition=='heavy' and c_traffic_condition=='heavy' and d_traffic_condition=='heavy':
        if last_green_side=='a':
            return 'Turn green  B and others red'
        elif last_green_side=='b':
            return 'Turn green  C and others red'
        elif last_green_side=='c':
            return 'Turn green  D and others red'
        elif last_green_side=='d':
            return 'Turn green  A and others red'
    elif a_traffic_condition=='light' and b_traffic_condition=='light' and c_traffic_condition=='light' and d_traffic_condition=='light':
        if last_green_side=='a':
            return 'Turn green  B and others red'
        elif last_green_side=='b':
            return 'Turn green  C and others red'
        elif last_green_side=='c':
            return 'Turn green  D and others red'
        elif last_green_side=='d':
            return 'Turn green  A and others red'
    elif a_traffic_condition=='heavy' and b_traffic_condition=='heavy' and c_traffic_condition=='heavy' and d_traffic_condition=='light':
        if last_green_side=='a':
            return 'Turn green  B and others red'
        elif last_green_side=='b':
            return 'Turn green  C and others red'
        elif last_green_side=='c':
            return 'Turn green  A and others red'
    elif a_traffic_condition=='heavy' and b_traffic_condition=='heavy' and c_traffic_condition=='light' and d_traffic_condition=='heavy':
        if last_green_side=='a':
            return 'Turn green  B and others red'
        elif last_green_side=='b':
            return 'Turn green  D and others red'
        elif last_green_side=='d':
            return 'Turn green A and others red'
    elif a_traffic_condition=='heavy' and b_traffic_condition=='light' and c_traffic_condition=='heavy' and d_traffic_condition=='heavy':
        if last_green_side=='a':
            return 'Turn green  C and others red'
        elif last_green_side=='c':
            return 'Turn green  D and others red'
        elif last_green_side=='d':
            return 'Turn green  A and others red'
    elif a_traffic_condition=='light' and b_traffic_condition=='heavy' and c_traffic_condition=='heavy' and d_traffic_condition=='heavy':
        if last_green_side=='b':
            return 'Turn green  C and others red'
        elif last_green_side=='c':
            return 'Turn green  D and others red'
        elif last_green_side=='d':
            return 'Turn green  b and others red'
    elif a_traffic_condition=='light' and b_traffic_condition=='light' and c_traffic_condition=='heavy' and d_traffic_condition=='heavy':
        if last_green_side=='c':
            return 'Turn green  D and others red'
        elif last_green_side=='d':
            return'Turn green C and others red'
    elif a_traffic_condition=='heavy' and b_traffic_condition=='light' and c_traffic_condition=='heavy' and d_traffic_condition=='heavy':
        if last_green_side=='a':
            return 'Turn green  D and others red'
        elif last_green_side=='d':
            return'Turn green A and others red'
    elif a_traffic_condition=='heavy' and b_traffic_condition=='heavy' and c_traffic_condition=='light' and d_traffic_condition=='light':
        if last_green_side=='a':
            return 'Turn green  B and others red'
        elif last_green_side=='b':
            return'Turn green B and others red'
    elif a_traffic_condition=='light' and b_traffic_condition=='heavy' and c_traffic_condition=='heavy' and d_traffic_condition=='light':
        if last_green_side=='b':
            return 'Turn green  c and others red'
        elif last_green_side=='c':
            return'Turn green b and others red'
    elif a_traffic_condition=='light' and b_traffic_condition=='heavy' and c_traffic_condition=='light' and d_traffic_condition=='heavy':
        if last_green_side=='b':
            return 'Turn green  D and others red'
        elif last_green_side=='d':
            return'Turn green B and others red'
    elif a_traffic_condition=='heavy' and b_traffic_condition=='light' and c_traffic_condition=='heavy' and d_traffic_condition=='light':
        if last_green_side=='a':
            return 'Turn green  C and others red'
        elif last_green_side=='c':
            return'Turn green A and others red'
    elif a_traffic_condition=='heavy' and b_traffic_condition=='light' and c_traffic_condition=='light' and d_traffic_condition=='light':
         return 'Turn green A and other routes red'
        
    elif a_traffic_condition=='light' and b_traffic_condition=='heavy' and c_traffic_condition=='light' and d_traffic_condition=='light':
         return 'Turn green B and other routes red'
        
    elif a_traffic_condition=='light' and b_traffic_condition=='light' and c_traffic_condition=='heavy' and d_traffic_condition=='light':
         return 'Turn green C and other routes red'
        
    elif a_traffic_condition=='light' and b_traffic_condition=='light' and c_traffic_condition=='light' and d_traffic_condition=='heavy':
         return 'Turn green D and other routes red'

def input_output():
    a_side_condition=input('what is the condition of side A heavy or light?')
    b_side_condition=input('what is the condition of side B heavy or light?')
    c_side_condition=input('what is the condition of side C heavy or light?')
    d_side_condition=input('what is the condition of side D heavy or light?')
    previous_signal_on_side=input('which signal was displayed last?')

    decision=decisions(previous_signal_on_side,a_side_condition,b_side_condition,c_side_condition,d_side_condition)
    print(decision)

input_output()
    
    
    

