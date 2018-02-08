


def vaccuam(pre_location, location, status):
    if(location=='a'& satus == 'dirty'):
        return 'suck'
    elif(location== 'a' and status== 'clean'):
        return'b'
    elif (pre_location=='a'and location == 'b' and status == 'dirty'):
        return 'suck'
    elif (location== 'b' and status== 'clean'):
        return'c'
    elif (pre_location=='b'and location=='c' and status == 'dirty'):
        return 'suck'
    elif(pre_loacation=='b'and location == 'c' and status == 'clean'):
        return'b'
    elif(pre_location=='c' and location=='b' and status=='dirty' or status=='clean'):
        return 'a'
    
def main():
    power=1
    while(power==1):
        print("enter power condition")
        power=int(input())
        v_pre_location= input("Enter previous location")
        v_location= input("Enter current Location")
        v_status= input(" Enter current status")
        
        action= vaccuam(v_pre_location, v_location, v_status)
        
        if(action=='suck'):
            print (action)
        elif(action=='b'):
            print (action)
        elif(action=='c'):
            print (action)
        elif(action=='a'):
            print (action)
    None
        
    
