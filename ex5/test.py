import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class BGMPlayer:
    def __init__(self, filename):
        self.filename = filename
        pg.mixer.init(frequency=44100)  # 初期設定
        pg.mixer.music.load(self.filename)  # 音楽ファイルの読み込み

    def play(self, loops=-1):
        pg.mixer.music.play(loops)  # 音楽の再生回数（デフォルトはループ再生）

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    Fscreen = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200

    # BGMプレイヤーを初期化して再生
    bgm_player = BGMPlayer("Numbers Don't Lie.mp3")
    bgm_player.play()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        clock.tick(60)  # フレームレートを60に設定

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
