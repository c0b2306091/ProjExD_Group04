import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_ans(x,y):
     pos = pg.mouse.get_pos()
     if (x-10) <= pos[0] <= (x+10):
         if (y-10) <= pos[1] <= (y+10):
             return 1

def main():
    pg.display.set_caption("見つけろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    Fscreen = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_img = pg.transform.rotozoom(kk_img,10,1.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    x=300
    y=200

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
            
            elif event.type == pg.MOUSEBUTTONUP:
                ans = check_ans(x,y)
                if ans == 1:
                    print("a")

        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img,kk_rct)
        pg.display.update()        
        clock.tick(200)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()