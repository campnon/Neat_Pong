from pong import Game
import pygame as pg 
import neat
import os 
WIDTH, HEIGHT = 600, 700
win = pg.display.set_mode((WIDTH, HEIGHT))

class PongGame():
    def __init__(self, win , width, height):    
        self.game = Game(win, WIDTH, HEIGHT)
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball

    def test_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)
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
            output = net.activate((self.right_paddle.y, self.ball.y, abs(self.right_paddle.x - self.ball.x)))
            decision = output2.index(max(output))
            if decision == 0:
                pass
            elif decision == 1:
                self.game.move_paddle(left=False, up=True)  
            else:
                self.game.move_paddle(left=False, up=False)
            game_info = game.loop()
            print(game_info.left_score, game_info.right_score)
            game.draw(False, True)
            pg.display.update()
        pg.quit()  

    def train_ai(self, genome1, genome2, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)
        run = True
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
            output1 = net1.activate((self.left_paddle.y, self.ball.y, abs(self.left_paddle.x - self.ball.x)))
            decision1 = output1.index(max(output1))
            if decision1 == 0:
                pass
            elif decision1 == 1:
                self.game.move_paddle(left=True, up=True)
            else:
                self.game.move_paddle(left=True, up=False)
            output2 = net2.activate((self.right_paddle.y, self.ball.y, abs(self.right_paddle.x - self.ball.x)))
            decision2 = output2.index(max(output2))
            if decision2 == 0:
                pass
            elif decision2 == 1:
                self.game.move_paddle(left=False, up=True)
            else:
                self.game.move_paddle(left=False, up=False)
            game_info = self.game.loop()
            self.game.draw(draw_score=False, draw_hits=True)
            pg.display.update() 
            if game_info.left_score >= 1 or game_info.right_score >=1 or game_info.left_hits > 50:
                self.calculate_fitness(genome1,genome2, game_info)
                break
    def calculate_fitness(self, genome1, genome2, game_info):
        genome1.fitness += game_info.left_hits
        genome2.fitness += game_info.right_hits


def eval_genomes(genomes, config):
    WIDTH, HEIGHT = 700, 500
    win = pg.display.set_mode((WIDTH, HEIGHT))

    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[i + 1:]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            game = PongGame(win, WIDTH, HEIGHT)
            game.train_ai(genome1, genome2, config)
            

    



def run_neat(config):
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))
    winner = p.run(eval_genomes, 100)




if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    run_neat(config)