# simple tic_tac_toe game in python

print("\n\nWELCOME TO TIC TAC TOE GAME\n\n")

def player():
    symbol=[]
    a = input("select your player 'X' or 'O': ")
    symbol.append(a.upper())
    print(f"player 1 is '{symbol[0]}'")
    if symbol[0] == "X":
        print("player 2 is 'O'")
        symbol.append("O")
    else:
        print("player 2 is 'X'")
        symbol.append("X")
       
    return symbol    
    
   
def display(l):
     print(f"""
              {l[0]} | {l[1]} | {l[2]}
             ___________
                |   |   
              {l[3]} | {l[4]} | {l[5]}
             ___________
                |   |   
              {l[6]} | {l[7]} | {l[8]}
              """)
    

def game(l):  
    pos = [0,1,2,3,4,5,6,7,8]
    for i in range(len(pos)):
        if i%2==0:
            symbol_pos = 0
        else:
            symbol_pos = 1
       
        display(pos)
    
        if (pos[4]==pos[3]==pos[5])or(pos[4]==pos[1]==pos[7])or(pos[4]==pos[2]==pos[6])or(pos[4]==pos[0]==pos[8]):
            print(f'player {pos[4]} is winner')
            break
        elif (pos[0]==pos[1]==pos[2])or(pos[0]==pos[3]==pos[6]):
            print(f'player {pos[0]} is winner')
            break
        elif (pos[8]==pos[4]==pos[2])or(pos[8]==pos[7]==pos[6]):
            print(f'player {pos[8]} is winner')
            break
        
        player_input=int(input(f'player {l[symbol_pos]} enter position : '))
        pos[player_input] = l[symbol_pos]
    
    else:
        display(pos)
        print("game is tied")
        
game(player())
