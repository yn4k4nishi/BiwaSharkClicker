import math
import random
import pyxel
# import pyxel.pyxel as pyxel

#####################################################################
SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256

PNG_WIDTH = 300
PNG_HEIGHT = 300

SHARK_NUM = 50

#####################################################################
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#####################################################################
class Shark:
    def __init__(self):
        self.pos = Vec2(random.uniform(0,3), random.uniform(0,3))
        self.vec = Vec2(random.uniform(0,3), random.uniform(0,3))
        self.is_dead = False

    def update(self):
        if self.is_dead:
            return

        self.pos.x += self.vec.x
        self.pos.y += self.vec.y

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            dx = pyxel.mouse_x - (self.pos.x + 25)
            dy = pyxel.mouse_y - (self.pos.y + 25)
            if math.sqrt(dx*dx+dy*dy) < 20:
                self.is_dead = True

        if self.pos.x < 0 or self.pos.x > (SCREEN_WIDTH-50):
            self.vec.x *= -1
        if self.pos.y < 0 or self.pos.y > (SCREEN_HEIGHT-50):
            self.vec.y *= -1

#####################################################################

class Setomaru:
    def __init__(self):
        self.pos = Vec2(random.uniform(0,3), random.uniform(0,3))
        self.vec = Vec2(random.uniform(0,3), random.uniform(0,3))
        self.is_dead = False

    def update(self):
        self.pos.x += self.vec.x
        self.pos.y += self.vec.y

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            dx = pyxel.mouse_x - (self.pos.x + 25)
            dy = pyxel.mouse_y - (self.pos.y + 25)
            if math.sqrt(dx*dx+dy*dy) < 20:
                self.is_dead = True

        if self.pos.x < 0 or self.pos.x > (SCREEN_WIDTH-50):
            self.vec.x *= -1
        if self.pos.y < 0 or self.pos.y > (SCREEN_HEIGHT-50):
            self.vec.y *= -1

#####################################################################
class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        # pyxel.load("biwa_shark.pyxres")
        self.sharks = [Shark() for _ in range(SHARK_NUM) ]
        self.setomaru = Setomaru()
        self.score = 0
        
        pyxel.load("setomaru.pyxres")
        pyxel.image(1).load(0,0,"biwa_shark2.png")
        
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnr(pyxel.KEY_R):
            self.sharks = [Shark() for _ in range(SHARK_NUM) ]
            self.setomaru = Setomaru()
            self.score = 0
            
        self.score = 0

        id = 0
        for s in self.sharks:
            s.update()

            if s.is_dead:
                self.score += 1
                # self.sharks.pop(id)
            # else:
            #     id += 1
            
        self.setomaru.update()

    def draw(self):
        pyxel.cls(0)
        
        if self.setomaru.is_dead:
            pyxel.text(100, 128, "GAME OVER", 7)
            pyxel.text(120, 158, "puress R key", 3)
            return

        for shark in self.sharks:
            if shark.is_dead:
                pyxel.text(shark.pos.x +20, shark.pos.y+25, "+1", 11)
            else:
                pyxel.blt(shark.pos.x, shark.pos.y, 1, 0,0,50,50,0)

        pyxel.blt(self.setomaru.pos.x, self.setomaru.pos.y, 0, 0,0,50,50,0)

        pyxel.circb(pyxel.mouse_x,pyxel.mouse_y ,10,8)

        if pyxel.frame_count % 50 < 10:
            pyxel.text(100, 128, "BIWA SHARK", pyxel.frame_count % 15 + 1)
        pyxel.text(100, 140, "score :" + str(self.score), 12)

if __name__ == "__main__":
    App()
