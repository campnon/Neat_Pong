from pong import Game
import pygame as pg 



WIDTH, HEIGHT = 600, 700
win = pg.display.set_mode((WIDTH, HEIGHT))

game = Game(win, WIDTH, HEIGHT)

run = True
clock = pg.time.Clock()
while run:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        game.move_paddle(left=True, up=True)
    if keys[pg.K_s]:
        game.move_paddle(left=True, up=False)
    game.loop()
    game.draw()
    pg.display.update()
pg.quit()   
    