from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np

class GameDriver:
    def __init__(self):
        self.url = "https://gabrielecirulli.github.io/2048/"
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.body = self.driver.find_element_by_tag_name('body')
        self.directions = {
            0: Keys.UP, 
            1: Keys.DOWN,
            2: Keys.LEFT,
            3: Keys.RIGHT
        }
        
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

game = GameDriver()
print(game.getGrid())
