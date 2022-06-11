import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Expectimax import Expectimax
from Game import Game
from time import sleep



class GameDriver:
    def __init__(self):
        self.url = "https://play2048.co/"
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.url)
        self.body = self.driver.find_element_by_tag_name('body')
        self.directions = {
            0: Keys.UP, 
            1: Keys.DOWN,
            2: Keys.LEFT,
            3: Keys.RIGHT
        }
        self.parser = argparse.ArgumentParser()
        self.tableTitle = ['R0C0', 'R0C1', 'R0C2', 'R0C3', 'R1C0', 'R1C1', 'R1C2', 'R1C3', 'R2C0', 'R2C1', 'R2C2', 'R2C3', 'R3C0', 'R3C1', 'R3C2', 'R3C3', 'ACTION'] 
        self.game = Game()
        self.agent = Expectimax()
        self.depth = 2
        self.reach = False
    def parse(self):
        self.parser.add_argument("--expectimax", help="execute expectimax agent", action="store_true")
        self.parser.add_argument("--mcts", help="execute lstm agent", action="store_true")
        self.parser.add_argument("--dqn", help="execute dqn agent", action="store_true")
        args = self.parser.parse_args()
        if args.expectimax: 
            self.agent = Expectimax()
        elif args.mcts:
            pass
        return args

    def getGrid(self):
        matrix = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        tiles = self.driver.find_elements(by=By.CLASS_NAME, value='tile')
        for tile in tiles:
            tile_cls = tile.get_attribute('class')
            col, row = tile_cls.split('tile-position-')[1].split(' ')[0].split('-')
            col, row = int(col)-1, int(row)-1
            num = int(tile_cls.split('tile tile-')[1].split(' ')[0])
            if num > matrix[row][col]:
                matrix[row][col] = num
        return matrix

    def play(self, args):
        dataset = []
        while(not self.reach):
            self.game.board = self.getGrid()
            for i in range(4):
                for j in range(4):
                    if self.game.board[i][j] == 2048:
                        self.reach = True 
            self.game.print_board()
            
            if args.expectimax:
                action = self.agent.get_next_action(self.game.board, self.depth)
           
            if action == -1:
                break
            
            grid = self.driver.find_element(by=By.TAG_NAME, value='body')
            # self.driver.find_element(by=By.CLASS_NAME, value='grid-container').click()
            grid.send_keys(self.directions[action])
            sleep(0.02)
            
        return df

try:        
    for _ in range(20):
        newGame = GameDriver()
        args = newGame.parse()
        df = newGame.play(args)

        newGame.driver.close()
except Exception as e:
    newGame.driver.close()
    print(str(e))