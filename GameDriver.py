from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import expectimax
import game
from time import sleep
class GameDriver:
    def __init__(self):
        self.url = "https://play2048.co/"
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.get(self.url)
        self.body = self.driver.find_element_by_tag_name('body')
        self.directions = {
            0: Keys.UP, 
            1: Keys.DOWN,
            2: Keys.LEFT,
            3: Keys.RIGHT
        }
        self.game = game.game()
        
    def getGrid(self):
        matrix = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        tiles = self.driver.find_elements_by_class_name('tile')
        for tile in tiles:
            tile_cls = tile.get_attribute('class')
            col, row = tile_cls.split('tile-position-')[1].split(' ')[0].split('-')
            col, row = int(col)-1, int(row)-1
            num = int(tile_cls.split('tile tile-')[1].split(' ')[0])
            if num > matrix[row][col]:
                matrix[row][col] = num
        return matrix
    def play(self):
        for _ in range(100):
            print(self.getGrid())
            action = expectimax.getAction(self.game, self.getGrid())
            grid = self.driver.find_element_by_tag_name('body')
            self.driver.find_element_by_class_name('grid-container').click()
            grid.send_keys(self.directions[action])
            sleep(0.1)
# try:            
newGame = GameDriver()
newGame.play()
# except:
    # newGame.driver.close()