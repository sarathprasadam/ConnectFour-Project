from gameplan import Connectedfour
def home():
    print("Enter row colum and pieces in format -r6 -c7 -p4")
    userinput=input()
    input_lst=userinput.split()
    r=p=c=-1
    for i in range(len(input_lst)):
        if(len(input_lst[i])>2):
            if ord(input_lst[i][2]) not in range(48,58):
                    break
            elif(input_lst[i][1]=='r'):            
                r=int(input_lst[i][2])                        

            elif(input_lst[i][1]=='p'):
                p=int(input_lst[i][2])
            elif(input_lst[i][1]=='c'):
                c=int(input_lst[i][2])
            else:
                break
    while(p<=0):
        print("You cannot have {0} pieces to Connect".format(p))
        inp=input("Please enter a positive non-zero integer for the number of pieces to connect:")
        if ord(inp) not in range(48,58):
            break
        else:
            p=int(inp)
    while(c<=0):
        print("You cannot have {0} Columns".format(c))
        inp=input("Please enter a positive non-zero integer for the number of columns:")
        if ord(inp) not in range(48,58):
            break
        else:
            c=int(inp)
    while(r<=0):
        print("You cannot have {0} Rows".format(r))
        inp=input("Please enter a positive non-zero integer for the number of rows:")
        if ord(inp) not in range(48,58):
            break
        else:
            r=int(inp)
    
    playertest=True
    rerun_test=True
    while(rerun_test):
        game=Connectedfour(r,c,p)
        while(playertest):        
            player1=input("Player one, do you want red or yellow(r or y)? ")
            if(player1=='r'):
                playertest=False
                player2='y'
            elif(player1=='y'):
                player2='r'
                playertest=False
            else:
                print("Enter a valied color(r or y)")
        game.show_board()
        game_running=True
        current_player=['player1',player1]
        while(game_running):
            print("{},what column do you want to put your piece?".format(current_player[0]))
            print("Enter END to stop the game")
            colm_input_test=True
            while(colm_input_test):
                colminput=input()
                if(colminput=="END"):
                    game_running=False
                    rerun_test=False
                    colm_input_test=False
                elif ord(colminput) not in range(48,58):
                    print("Invalied column.Enter number")
                
                elif(int(colminput)>c or int(colminput)<1):
                    print("Invalied number.")
                else: 
                    colminput=int(colminput)
                    colm_input_test=False
            if(colminput!="END"):
                game.place_player(colminput,current_player[1])
                game.show_board()
                game_win=game.win_check(current_player[1])
                if(game_win==1):
                    game_running=False
                    replay_test=True
                    while(replay_test):
                        replay=input("Do you want to play again(0-no,1-yes?)")
                        if(replay not in ('0','1')):
                            print("Invalied Entry")
                        else:
                            if(replay=='0'):
                                rerun_test=False
                                replay_test=False
                            else:
                                replay_test=False
                                playertest=True
                if(current_player[0]=="player1"):
                    current_player=['player2',player2]
                else:
                    current_player=['player1',player1]
def main():
    foo = home()
    

if __name__ == "__main__":
    main()