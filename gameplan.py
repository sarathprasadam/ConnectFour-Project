class Connectedfour:
    def __init__(self,r,c,p):
        self.row=r
        self.col=c
        self.pieces=p
        self.position=0
        self.matrix=[]
        for i in range(self.row):
            a=[]
            for j in range(self.col):                
                a.append(0)            
            self.matrix.append(a)
    def show_board(self):  
        for i in self.matrix:
            print("|",end="")
            for j in i:
                print(j,end="|")
            print("")
    def place_player(self,colm,player):
        if(colm>self.col):
            print("Column no exceed no of columns")
        else:
            for i in range(self.row-1,-1,-1):
                if(self.matrix[i][colm-1]==0):
                    self.matrix[i][colm-1]=player
                    self.position=[i,colm-1]                    
                    break
            else:
                print("THe column in comletely taken")
    def win_check(self,player):
        tester=0        
        rowaxis=self.position[0]
        colaxis=self.position[1]
        #HORIZONTAL CHECK
        for i in range(colaxis+1,self.col,1):
            if(self.matrix[rowaxis][i]==player):                
                tester+=1
            else:
                break
        for i in range(colaxis,-1,-1):
            if(self.matrix[rowaxis][i]==player):
                tester+=1                
            else:
                break       
        if(tester>=self.pieces):
            print(player," Wins")
            return 1
        #END HORIZONTAL CHECK
        #VERTICAL CHECK
        tester=0
        for i in range(rowaxis+1,self.row):
            if(self.matrix[i][colaxis]==player):
                tester+=1
            else:
                break
        for i in range(rowaxis,-1,-1):
            if(self.matrix[i][colaxis]==player):
                tester+=1
            else:
                break
        if(tester>=self.pieces):
            print(player," Wins")
            return 1
        #END VERTICAL CHECK
        #N-W TO S-E TEST
        tester=0
        j=colaxis-1
        for i in range(rowaxis+1,self.row,1):
            if(j<0):
                break            
            if(self.matrix[i][j]==player):
                tester+=1
                j-=1
            else:
                break
        i=rowaxis
        for j in range(colaxis,self.col,1):
            if(i<0):
                break
            if(self.matrix[i][j]==player):
                tester+=1
                i-=1
            else:
                break
        if(tester>=self.pieces):
            print(player," Wins")
            return 1
         #END N-W TO S-E TEST
        
        #SW TO NE TEST
        
        #NEPART
        tester=0
        j=colaxis+1
        for i in range(rowaxis+1,self.row,1):
            if(j>=self.col):
                break
            if(self.matrix[i][j]==player):
                tester+=1
                j+=1
            else:
                break
        #SW PART
        j=colaxis
        for i in range(rowaxis,-1,-1):
            if(j<=-1):
                break
            if(self.matrix[i][j]==player):
                tester+=1
                j-=1
            else:
                break
        if(tester==self.pieces):
            print(player," Wins")
            return 1
        #END SW TO NE TEST