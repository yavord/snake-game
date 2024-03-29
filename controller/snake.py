class SnakeController:
    def __init__(self, snake, ui):
        self.snake = snake
        self.ui = ui
    
    def animateSnake(self):
        self.snake.moveSnakeOneOver()

    def changeDirection(self, direction):
        self.snake.changeFirstIndexDirection(direction)

    def updateDirections(self):
        self.snake.getNewDirections()

    def eatApple(self):
        self.snake.growSnake()

    def checkSnakePosition(self, apple):
        firstIndex = self.snake.snakeList[0]
        if [firstIndex.x, firstIndex.y] == [apple.x, apple.y]:
            return True
        for i in range(1, len(self.snake.snakeList)-1):
            if [firstIndex.x, firstIndex.y] == [self.snake.snakeList[i].x, self.snake.snakeList[i].y]:
                return False 

    def gameOver(self):
        self.ui.print_('Game Over ')
        self.ui.stay_open()

    def placeSnake(self, height, width):
        for snakepiece in self.snake.snakeList:
            try:
                self.ui.place(snakepiece.x, snakepiece.y, snakepiece.color)
            except:
                if snakepiece.x > height:
                    snakepiece.x = 0
                    self.ui.place(snakepiece.x, snakepiece.y, snakepiece.color)
                elif snakepiece.x < 0:
                    snakepiece.x = height-1
                    self.ui.place(snakepiece.x, snakepiece.y, snakepiece.color)
                elif snakepiece.y > width:
                    snakepiece.y = 0
                    self.ui.place(snakepiece.x, snakepiece.y, snakepiece.color)
                elif snakepiece.y < 0:
                    snakepiece.y = width-1
                    self.ui.place(snakepiece.x, snakepiece.y, snakepiece.color)

