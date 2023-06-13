class GamePosition:
    def __init__(self,board,player,castling_rights,EnP_Target,HMC,history = {}):
        self.board = board
        self.player = player
        self.castling = castling_rights
        self.EnP = EnP_Target
        self.HMC = HMC
        self.history = history
        
    def getboard(self):
        return self.board
    def setboard(self,board):
        self.board = board
    def getplayer(self):
        return self.player
    def setplayer(self,player):
        self.player = player
    def getCastleRights(self):
        return self.castling
    def setCastleRights(self,castling_rights):
        self.castling = castling_rights
    def getEnP(self):
        return self.EnP
    def setEnP(self, EnP_Target):
        self.EnP = EnP_Target
    def getHMC(self):
        return self.HMC
    def setHMC(self,HMC):
        self.HMC = HMC

    def checkRepition(self):
        return any(value>=3 for value in self.history.itervalues())

    def addtoHistory(self,position):
        key = pos2key(position)
        self.history[key] = self.history.get(key,0) + 1

    def gethistory(self):
        return self.history
    
    def clone(self):
        clone = GamePosition(copy.deepcopy(self.board),
                             self.player,
                             copy.deepcopy(self.castling),
                             self.EnP,
                             self.HMC)
        return clone
    

class Shades:
    def __init__(self,image,coord):
        self.image = image
        self.pos = coord
    def getInfo(self):
        return [self.image,self.pos]


class Piece:
    def __init__(self,pieceinfo,chess_coord):
        piece = pieceinfo[0]
        color = pieceinfo[1]
        if piece=='K':
            index = 0
        elif piece=='Q':
            index = 1
        elif piece=='B':
            index = 2
        elif piece == 'N':
            index = 3
        elif piece == 'R':
            index = 4
        elif piece == 'P':
            index = 5
        left_x = square_width*index
        if color == 'w':
            left_y = 0
        else:
            left_y = square_height
        
        self.pieceinfo = pieceinfo
        self.subsection = (left_x,left_y,square_width,square_height)
        self.chess_coord = chess_coord
        self.pos = (-1,-1)

    def getInfo(self):
        return [self.chess_coord, self.subsection,self.pos]
    def setpos(self,pos):
        self.pos = pos
    def getpos(self):
        return self.pos
    def setcoord(self,coord):
        self.chess_coord = coord
    def __repr__(self):
        return self.pieceinfo+'('+str(chess_coord[0])+','+str(chess_coord[1])+')'
