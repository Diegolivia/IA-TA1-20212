from config import *
from WorldGeneration import *
class Engine:
    def __init__(self, Ass_List):
        self.arr_imgBank = []
        self.arr_SpriteBank = []
        self.mtx_2WBoard=[]
        self.mtx_NodeBoard=[]
        self.mtx_Players=[]
        self.load_World(Ass_List)
        self.load_Players()

    def load_World(self,Ass_List):
        #Loading the images from the "Media" Folder
        f = open(Ass_List, "r")
        for x in f:
            x=x.strip()
            self.arr_imgBank.append(pyi.load(x))
        print("Imagenes Cargadas")

        #Setting up the variables for Assets Loading
        self.BACKGROUND_SCALE = SIZE/self.arr_imgBank[0].width
        self.SLOT_SCALE = self.BACKGROUND_SCALE*(9/BOARD_SIZE)
        self.JUMP = self.arr_imgBank[1].width*self.SLOT_SCALE
        Board = pyglet.sprite.Sprite(self.arr_imgBank[0],
                                     batch=Gfx_batch,
                                     group=GfxOrd_Background)
        Board.scale = self.BACKGROUND_SCALE
        self.arr_SpriteBank.append(Board)
        print("Sprite Tablero Cargado")
        #Calling WorldGeneration to create the mtx_2WBoard Object to draw the Size of the board
        worldgen=WorldGen(BOARD_SIZE)
        self.mtx_2WBoard=worldgen.Create2WMatrix()
        self.mtx_NodeBoard=worldgen.CreateNodeWeb(self.mtx_2WBoard)
        self.mtx_Players=worldgen.GeneratePlayers(NUMPLAYERS,self.mtx_2WBoard,self.mtx_NodeBoard)
        print(self.mtx_2WBoard)
        #Generating the objects in the board statically
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if (self.mtx_2WBoard[y][x]==0):
                    Slot = pyglet.sprite.Sprite(self.arr_imgBank[1],
                                                BOARD_BORDER + self.JUMP * x,
                                                BOARD_BORDER + self.JUMP * (BOARD_SIZE-y-1),
                                                batch=Gfx_batch,
                                                group=GfxOrd_BoardObjects)
                else:
                    Slot = pyglet.sprite.Sprite(self.arr_imgBank[2],
                                                BOARD_BORDER + self.JUMP * x,
                                                BOARD_BORDER + self.JUMP * (BOARD_SIZE-y-1),
                                                batch=Gfx_batch,
                                                group=GfxOrd_BoardObjects)
                Slot.scale = self.SLOT_SCALE
                self.arr_SpriteBank.append(Slot)
        print("Sprites Cargados")

    def load_Players(self):
        #Generates Players Actual Position Sprites
        for x in range(len(self.mtx_Players)):
            pSprite=pyglet.sprite.Sprite(self.arr_imgBank[4+x],
            BOARD_BORDER+self.JUMP*self.mtx_Players[x].ActualPos.posX,
            BOARD_BORDER+self.JUMP*(BOARD_SIZE-self.mtx_Players[x].ActualPos.posY-1),
            batch=Gfx_batch,
            group=GfxOrd_Players
            )
            pSprite.scale=self.SLOT_SCALE
            self.arr_SpriteBank.append(pSprite)
        #Generates Players Goal Position Sprites
        for x in range(len(self.mtx_Players)):
            pSprite=pyglet.sprite.Sprite(self.arr_imgBank[8+x],
            BOARD_BORDER+self.JUMP*self.mtx_Players[x].GoalPos.posX,
            BOARD_BORDER+self.JUMP*(BOARD_SIZE-self.mtx_Players[x].GoalPos.posY-1),
            batch=Gfx_batch,
            group=GfxOrd_Players
            )
            pSprite.scale=self.SLOT_SCALE
            self.arr_SpriteBank.append(pSprite)
        pass


    def key_command(self,key):
        if key == 4:
            #x = self.mtx_Players[0].ActualPos.posX
            #y = self.mtx_Players[0].ActualPos.posY
            print("te moviste hacia arriba")
            print("posiciones mtxplayer:")
            print(self.mtx_Players[0].ActualPos.posX,self.mtx_Players[0].ActualPos.posY)
            print("Board")
            print(self.mtx_2WBoard[self.mtx_Players[0].ActualPos.posX][self.mtx_Players[0].ActualPos.posY])
            
            if self.mtx_2WBoard[self.mtx_Players[0].ActualPos.posX][self.mtx_Players[0].ActualPos.posY-1] != 1 :
               self.mtx_Players[0].ActualPos.posY -= 1
               print(self.mtx_Players[0].ActualPos.posY)
               #print(self.mtx_2WBoard)
            else:
                print("Pared")
