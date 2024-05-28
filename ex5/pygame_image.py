import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def check_ans(x,y):
     """
     正解のこうかとんにカーソルが合っているかどうかの判定についての関数
     引数：正解のこうかとんの座標x,y
     """
     pos = pg.mouse.get_pos() #カーソル座標の取得
     if (x-10) <= pos[0] <= (x+10): #こうかとんの座標から猶予範囲内なら
         if (y-10) <= pos[1] <= (y+10):
             return 1 #1を返す

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
    kk_rct.center = 300,200 #こうかとんの初期位置、表示　->こうかとんをランダムで生成する関数の実装後、削除
    x=300 #判定の初期位置
    y=200 

    score = 0 #スコア値の初期値

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
            
            elif event.type == pg.MOUSEBUTTONUP: #左クリックされたら 
                ans = check_ans(x,y) #正解のこうかとんかどうか判定
                if ans == 1: #合っていたら
                    score += 1 #スコア+1 -> のちにスコア関数組み合わせる
                
                ###ここにこうかとんをランダムで表示させる関数が入り、判定のx,yの値を取得する###
                    
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img,kk_rct)
        pg.display.update()        
        clock.tick(200)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()