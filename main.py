from pong import Game
import pygame as pg 

class PongGame():
    def __init__(self, win , width, height)
    self.game = Game(win, WIDTH, HEIGHT)
    self.left_paddle = self.game.left_paddle
    self.right_paddle = self.game.right_paddle
    self.ball = self.game.ball

def test_ai(self):
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
        game_info = game.loop()
        print(game_info.left_score, game_info.right_score)
        game.draw(False, True)
        pg.display.update()
    pg.quit()   
    
 


WIDTH, HEIGHT = 600, 700
win = pg.display.set_mode((WIDTH, HEIGHT))