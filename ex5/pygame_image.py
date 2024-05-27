import os
import sys
import pygame as pg
import random 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

"""追加機能
ランダムでコウカトンを表示する
"""

def efect(screen):
    happy = pg.image.load("fig/6.png")
    Ans_rct = [random.randint(0, 1600), random.randint(0, 900)]
    Ans_img = pg.transform.rotozoom(happy, 10, random.uniform(0.5, 1.5))
    Ans_ex_img = pg.transform.rotozoom(happy, 10, 2.0)
    miss_img_lst = ["fig/0.png", "fig/1.png", "fig/2.png", "fig/3.png", "fig/4.png", "fig/5.png", "fig/7.png", "fig/8.png", "fig/9.png"]
    
    
    rct_x=[]    
    rct_y=[]
    for i in range(len(miss_img_lst)):
        # screen.blit(pg.image.load(miss_img_lst[i]), [random.randint(0, 1600), random.randint(0, 900)])
        if i<len(miss_img_lst):
            rct_x.append(random.randint(0,1600))
            rct_y.append(random.randint(0,900))
                         
        else:
            pass
    screen.blit(happy, Ans_rct)
    return happy, Ans_rct, miss_img_lst, rct_x, rct_y  # 必要な情報をタプルで返す

#ここまでは来た

    # for i in range(len(rct_x)):
    #     screen.blit(pg.image.load(((miss_img_lst[i]),rct_x[i],rct_y[i])))







def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    Fscreen = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    # kk_img = pg.transform.rotozoom(kk_img, 10, random.uniform(0.2, 10))
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    # rct=[]
    # for i in range(9):
    #     rct.append(random.randint(1600,900))
    choice=efect(screen)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        screen.blit(bg_img,[0,0])
        for i in range(len(choice[3])):
            screen.blit(pg.image.load(choice[2][i]), [choice[3][i], choice[4][i]])

        
        screen.blit(choice[0],choice[1])
        screen.blit(kk_img, kk_rct)
        pg.display.update()        
        clock.tick(5)

    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()