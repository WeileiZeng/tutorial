import os
import pygame
from pygame.locals import *
import random
import array2d

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('sound', name)
    sound = pygame.mixer.Sound(fullname)
    return sound

def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def xor(a,b):
    if bool(a) != bool(b):
        return True
    else:
        return False

class Difficulty:
    def __init__(self, name, width, height, mines, cellsize):
        self.name = name
        self.width = width
        self.height = height
        self.mines = mines
        self.cell_size = cellsize

class Mines:
    def __init__(self):
        self.difficulty = 1
        self.difficulties = []
        self.difficulties.append(Difficulty("Easy"  ,  9,  9, 10, 35))
        self.difficulties.append(Difficulty("Medium", 16, 16, 40, 25))
        self.difficulties.append(Difficulty("Expert", 30, 16, 99, 20))
        self.difficulties.append(Difficulty("More Expert", 40, 25, 200, 18))
        self.difficulties.append(Difficulty("Narrow", 30, 5, 28, 20))
        self.difficulties.append(Difficulty("More Narrow", 40, 4, 35, 18))
        self.difficulties.append(Difficulty("Ridiculous", 50, 30, 320, 15))

        self.SW = 800
        self.SH = 600

        self.w = self.difficulties[self.difficulty].width
        self.h = self.difficulties[self.difficulty].height
        self.cell_size = self.difficulties[self.difficulty].cell_size
        self.mines = self.difficulties[self.difficulty].mines
        self.flagged = 0

        self.grid = list((array2d.Array2d(self.w,self.h,0),array2d.Array2d(self.w,self.h,0),array2d.Array2d(self.w,self.h,0)))

        self.xoff = (self.SW/2)-(self.cell_size*self.w/2)
        self.yoff = (self.SH/2)-(self.cell_size*self.h/2)+10

        self.gameover = False
        self.win = False

        self.small_font = pygame.font.Font(pygame.font.get_default_font(),12)
        self.medium_font = pygame.font.Font(pygame.font.get_default_font(),18)
        self.large_font = pygame.font.Font(pygame.font.get_default_font(),24)

        self.colors_bg = list(((50,55,65), (80,85,95), (70,75,85)))
        self.colors_text = (155,155,160)
        self.colors_text_win = (120,230,120)
        self.colors_text_lose = (230,120,120)
        self.colors_flag = list(((100,50,50),(200,100,100)))
        self.colors_flag2 = list(((50,50,100),(100,100,200)))
        self.colors_unrevealed = (165, 165, 165)
        self.colors_highlight = (180, 185, 190)
        self.colors_notouch = (148, 175, 190)
        self.colors_notouch_win = (175, 195, 178)
        self.colors_revealed = (185, 185, 185)
        self.colors_mine = (215, 185, 185)
        self.colors_back = (40,40,45)
        self.colors_back_win = (75,85,78)
        self.colors_back_lose = (85,78,75)
        self.colors_numbers = (0,0,0)
        
        self.background = pygame.Surface((self.SW,self.SH))
        self.background.fill((222,222,0))
        self.background.fill(self.colors_bg[0])

        self.sound_boom = load_sound('boomboomuhoh.wav')
        self.sound_boop = load_sound('boop.wav')
        self.sound_beeh = load_sound('beeh.wav')
        self.sound_wsh = load_sound('wsh.wav')
        self.sound_yes = load_sound('yes.wav')

        for x in range(int(self.SW/16)):
            for y in range(int(self.SH/12)):
                if xor(x%2,y%2):
                    pygame.draw.rect(self.background, self.colors_bg[1], (int(x*(self.SW/16))+1, int(y*(self.SH/12))+1, int(self.SW/16)-2, int(self.SH/12)-2) )
                else:
                    pygame.draw.rect(self.background, self.colors_bg[2], (int(x*(self.SW/16))+1, int(y*(self.SH/12))+1, int(self.SW/16)-2, int(self.SH/12)-2) )
        
        self.screen = pygame.display.set_mode((self.SW, self.SH))
        pygame.display.set_caption('Mines - ' + self.difficulties[self.difficulty].name)


    def surrounding(self, pos):
        count = 0

        if pos[0]:
            if pos[1]:
                if self.grid[0].v[pos[0]-1][pos[1]-1]:
                    count += 1
            if self.grid[0].v[pos[0]-1][pos[1]]:
                count += 1
            if pos[1] < self.h-1:
                if self.grid[0].v[pos[0]-1][pos[1]+1]:
                    count += 1

        if pos[0] < self.w-1:
            if pos[1] < self.h-1:
                if self.grid[0].v[pos[0]+1][pos[1]+1]:
                    count += 1
            if self.grid[0].v[pos[0]+1][pos[1]]:
                count += 1
            if pos[1]:
                if self.grid[0].v[pos[0]+1][pos[1]-1]:
                    count += 1

        if pos[1]:
            if self.grid[0].v[pos[0]][pos[1]-1]:
                count += 1
        if pos[1] < self.h-1:
            if self.grid[0].v[pos[0]][pos[1]+1]:
                count += 1
                
        return count
    

    def check_win(self):
        self.win = True
        for x in range(self.w):
            for y in range(self.h):
                if not self.grid[0].v[x][y] == self.grid[2].v[x][y]:
                    self.win = False

        if self.win:
            self.gameover = True
            for x in range(self.w):
                for y in range(self.h):
                    if not self.grid[0].v[x][y]:
                        self.grid[1].v[x][y] = 1

                    
    def reveal(self,x,y):
        if not self.gameover and not self.grid[2].v[x][y]:
            self.grid[1].v[x][y] = 1
        else:
            return 0
        
        if self.grid[0].v[x][y]:
            self.sound_boom.play()
            self.gameover = True

        if not self.surrounding((x,y)) and not self.gameover:
            if x and y and not self.grid[1].v[x-1][y-1]:
                self.reveal(x-1,y-1)
            if x and not self.grid[1].v[x-1][y]:
                self.reveal(x-1,y)
            if x and y < self.h-1 and not self.grid[1].v[x-1][y+1]:
                self.reveal(x-1,y+1)

            if x < self.w-1 and y and not self.grid[1].v[x+1][y-1]:
                self.reveal(x+1,y-1)
            if x < self.w-1 and not self.grid[1].v[x+1][y]:
                self.reveal(x+1,y)
            if x < self.w-1 and y < self.h-1 and not self.grid[1].v[x+1][y+1]:
                self.reveal(x+1,y+1)

            if y and not self.grid[1].v[x][y-1]:
                self.reveal(x,y-1)
            if y < self.h-1 and not self.grid[1].v[x][y+1]:
                self.reveal(x,y+1)
                

    def flag(self,x,y):
        if not self.gameover and not self.win and not self.grid[1].v[x][y]:
            if self.grid[2].v[x][y] == 1:
                self.grid[2].v[x][y] = 2
                self.flagged -= 1
            elif self.grid[2].v[x][y] == 2:
                self.grid[2].v[x][y] = 0
            else:
                self.sound_yes.play()
                self.grid[2].v[x][y] = 1
                self.flagged += 1
            self.check_win()
            

    def set_mines(self):
        for x in range(self.w):
            for y in range(self.h):
                self.grid[0].v[x][y] = 0
                self.grid[1].v[x][y] = 0
                self.grid[2].v[x][y] = 0

        done = False
        minesset = 0
        
        while not done:
            x = random.randint(0,(self.w-1))
            y = random.randint(0,(self.h-1))
            if self.grid[0].v[x][y] == 0:
                self.grid[0].v[x][y] = 1
                minesset += 1
            if minesset == self.mines:
                done = True

    def update_bg(self):
        self.background.fill((222,222,0))
        self.background.fill(self.colors_bg[0])
        for x in range(int(self.SW/16)):
            for y in range(int(self.SH/12)):
                if xor(x%2,y%2):
                    pygame.draw.rect(self.background, self.colors_bg[1], (int(x*(self.SW/16))+1, int(y*(self.SH/12))+1, int(self.SW/16)-2, int(self.SH/12)-2) )
                else:
                    pygame.draw.rect(self.background, self.colors_bg[2], (int(x*(self.SW/16))+1, int(y*(self.SH/12))+1, int(self.SW/16)-2, int(self.SH/12)-2) )

    def reset(self):
        self.win = False
        self.gameover = False
        self.flagged = 0

        self.w = self.difficulties[self.difficulty].width
        self.h = self.difficulties[self.difficulty].height
        self.cell_size = self.difficulties[self.difficulty].cell_size
        self.mines = self.difficulties[self.difficulty].mines

        self.xoff = (self.SW/2)-(self.cell_size*self.w/2)
        self.yoff = (self.SH/2)-(self.cell_size*self.h/2)+10

        self.grid = list((array2d.Array2d(self.w,self.h,0),array2d.Array2d(self.w,self.h,0),array2d.Array2d(self.w,self.h,0)))
        self.set_mines()
        pygame.display.set_caption('Mines - ' + self.difficulties[self.difficulty].name)


    def randomize_colors(self):
        self.colors_bg = list((random_color(), random_color(), random_color()))
        self.colors_text = random_color()
        self.colors_text_win = random_color()
        self.colors_text_lose = random_color()
        self.colors_flag = list((random_color(),random_color()))
        self.colors_flag2 = list((random_color(),random_color()))
        self.colors_unrevealed = random_color()
        self.colors_highlight = random_color()
        self.colors_notouch = random_color()
        self.colors_notouch_win = random_color()
        self.colors_revealed = random_color()
        self.colors_mine = random_color()
        self.colors_back = random_color()
        self.colors_back_win = random_color()
        self.colors_back_lose = random_color()
        self.colors_numbers = random_color()
        self.update_bg()
        

    def load_colors(self, fn = "default.color"):
        if os.path.exists(fn):
            fin = open(fn,"r")
            lines = fin.readlines()
            for line in lines:
                exec("self.colors_"+line)
            self.update_bg()
        else:
            print(fn + " does not exist.\n")

    def print_colors(self):
        print("bg = " + str(self.colors_bg))
        print("text = " + str(self.colors_text))
        print("text_win = " + str(self.colors_text_win))
        print("text_lose = " + str(self.colors_text_lose))
        print("flag = " + str(self.colors_flag))
        print("flag2 = " + str(self.colors_flag2))
        print("unrevealed = " + str(self.colors_unrevealed))
        print("highlight = " + str(self.colors_highlight))
        print("notouch = " + str(self.colors_notouch))
        print("notouch_win = " + str(self.colors_notouch_win))
        print("revealed = " + str(self.colors_revealed))
        print("mine = " + str(self.colors_mine))
        print("back = " + str(self.colors_back))
        print("back_win = " + str(self.colors_back_win))
        print("back_lose = " + str(self.colors_back_lose))
        print("numbers = " + str(self.colors_numbers))
        print("")
    
    def draw(self):
        self.screen.blit(self.background,(0,0))

        if self.win:
            pygame.draw.rect(self.screen, self.colors_back_win,(self.xoff-2, self.yoff-2, self.cell_size*self.w+4, self.cell_size*self.h+4))
        elif self.gameover:
            pygame.draw.rect(self.screen, self.colors_back_lose,(self.xoff-2, self.yoff-2, self.cell_size*self.w+4, self.cell_size*self.h+4))
        else:
            pygame.draw.rect(self.screen, self.colors_back,(self.xoff-2, self.yoff-2, self.cell_size*self.w+4, self.cell_size*self.h+4))

        for x in range(self.w):
            for y in range(self.h):
                if self.grid[1].v[x][y]:
                    if self.grid[0].v[x][y]:
                        pygame.draw.rect(self.screen, self.colors_mine, (self.xoff+x*self.cell_size, self.yoff+y*self.cell_size, self.cell_size-1, self.cell_size-1))
                    else:
                        if self.surrounding((x,y)):                            
                            pygame.draw.rect(self.screen, self.colors_revealed, (self.xoff+x*self.cell_size, self.yoff+y*self.cell_size, self.cell_size-1, self.cell_size-1))
                            self.screen.blit(self.small_font.render(str(self.surrounding((x,y))),True, self.colors_numbers),
                                             (self.xoff+x*self.cell_size+(self.cell_size/2)-(self.small_font.size(str(self.surrounding((x,y))))[0]/2)-1,
                                              self.yoff+y*self.cell_size+(self.cell_size/2)-(self.small_font.size(str(self.surrounding((x,y))))[1]/2)-1))
                        else:
                            if self.win:
                                pygame.draw.rect(self.screen, self.colors_notouch_win, (self.xoff+x*self.cell_size, self.yoff+y*self.cell_size, self.cell_size-1, self.cell_size-1))
                            else:
                                pygame.draw.rect(self.screen, self.colors_notouch, (self.xoff+x*self.cell_size, self.yoff+y*self.cell_size, self.cell_size-1, self.cell_size-1))
                else:
                    p = pygame.mouse.get_pos()
                    if (int((p[0] - self.xoff)/self.cell_size) == x) and (int((p[1] - self.yoff)/self.cell_size) == y):
                        pygame.draw.rect(self.screen, self.colors_highlight, (self.xoff+x*self.cell_size, self.yoff+y*self.cell_size, self.cell_size-1, self.cell_size-1))
                    else:
                        pygame.draw.rect(self.screen,self.colors_unrevealed, (self.xoff+x*self.cell_size, self.yoff+y*self.cell_size, self.cell_size-1, self.cell_size-1))
                    if self.grid[0].v[x][y] and self.gameover and not self.win:
                        pygame.draw.rect(self.screen, self.colors_mine, (self.xoff+x*self.cell_size, self.yoff+y*self.cell_size, self.cell_size-1, self.cell_size-1))
                    if self.grid[2].v[x][y] == 1:
                        pygame.draw.rect(self.screen, self.colors_flag[0], (self.xoff+x*self.cell_size+4, self.yoff+y*self.cell_size+4, self.cell_size-1-8, self.cell_size-1-8))
                        pygame.draw.rect(self.screen, self.colors_flag[1], (self.xoff+x*self.cell_size+5, self.yoff+y*self.cell_size+5, self.cell_size-1-10, self.cell_size-1-10))
                    if self.grid[2].v[x][y] == 2:
                        pygame.draw.rect(self.screen, self.colors_flag2[0], (self.xoff+x*self.cell_size+4, self.yoff+y*self.cell_size+4, self.cell_size-1-8, self.cell_size-1-8))
                        pygame.draw.rect(self.screen, self.colors_flag2[1], (self.xoff+x*self.cell_size+5, self.yoff+y*self.cell_size+5, self.cell_size-1-10, self.cell_size-1-10))

        if self.gameover:
            if not self.win:
                self.screen.blit(self.medium_font.render("GAME OVER", True, self.colors_text_lose), ((self.SW/2)-(self.medium_font.size("GAME OVER")[0]/2),10))
            else:
                self.screen.blit(self.medium_font.render("YOU WIN!", True, self.colors_text_win), ((self.SW/2)-(self.medium_font.size("YOU WIN!")[0]/2),10))
        self.screen.blit(self.medium_font.render("Change Difficulty With +/-",True, self.colors_text), (10,self.SH-25))
        
        pygame.draw.line(self.screen, self.colors_text, (10, 8+self.medium_font.size("Minesweeper")[1]), (10+self.medium_font.size("Minesweeper")[0], 8+self.medium_font.size("Minesweeper")[1]))
        self.screen.blit(self.medium_font.render("Minesweeper", True, self.colors_text), (10,10))
        self.screen.blit(self.medium_font.render("Difficulty: "+self.difficulties[self.difficulty].name, True, self.colors_text), (10,35))
        self.screen.blit(self.medium_font.render("Mines Left:"+str(self.mines-self.flagged), True, self.colors_text), (self.xoff, self.yoff - 25))

        if pygame.mouse.get_pos()[0] >= self.SW-25 and pygame.mouse.get_pos()[1] <= 25:
            pygame.draw.rect(self.screen, self.colors_highlight, (self.SW-25,0,25,25))
        else:
            pygame.draw.rect(self.screen, self.colors_unrevealed, (self.SW-25,0,25,25))
        self.screen.blit(self.medium_font.render("R", True, (50,50,50)), (self.SW-18, 4))
        
        pygame.display.flip()

        
    def play(self):
        self.set_mines()
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.pos[0] >= self.SW-20 and event.pos[1] <= 20:
                        self.reset()
                    if event.pos[0] >= self.xoff and event.pos[0] < self.xoff+(self.cell_size*self.w):
                        if event.pos[1] >= self.yoff and event.pos[1] < self.yoff+(self.cell_size*self.h):
                            if event.button == 1:
                                self.reveal(int((event.pos[0]-self.xoff)/self.cell_size), int((event.pos[1]-self.yoff)/self.cell_size))
                                if not self.gameover:
                                    self.sound_wsh.play()
                            elif event.button == 3:
                                self.flag(int((event.pos[0]-self.xoff)/self.cell_size), int((event.pos[1]-self.yoff)/self.cell_size))
                elif event.type == KEYDOWN:
                    if event.key == K_KP1:
                        self.load_colors("color/1.color")
                    if event.key == K_KP2:
                        self.load_colors("color/2.color")
                    if event.key == K_KP3:
                        self.load_colors("color/3.color")
                    if event.key == K_KP4:
                        self.load_colors("color/4.color")
                    if event.key == K_KP5:
                        self.load_colors("color/5.color")
                    if event.key == K_KP6:
                        self.load_colors("color/6.color")
                    if event.key == K_KP7:
                        self.load_colors("color/7.color")
                    if event.key == K_KP8:
                        self.load_colors("color/8.color")
                    if event.key == K_KP9:
                        self.load_colors("color/9.color")
                        
                    if event.key == K_r:
                        pygame.mixer.stop()
                        self.reset()
                    if event.key == K_z:
                        self.randomize_colors()
                    if event.key == K_x:
                        self.load_colors()
                    if event.key == K_c:
                        self.print_colors()
                    if event.key == K_KP_PLUS:
                        if self.difficulty < len(self.difficulties) - 1:
                            self.difficulty += 1
                            self.reset()
                        else:
                            self.difficulty = 0
                            self.reset()
                    if event.key == K_KP_MINUS:
                        if self.difficulty > 0:
                            self.difficulty -= 1
                            self.reset()
                        else:
                            self.difficulty = len(self.difficulties)-1
                            self.reset()
            self.draw()

def main():
    pygame.init()
    game = Mines()
    game.play()
    pygame.quit()

if __name__ == '__main__':
    main()
