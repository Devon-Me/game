WIDTH = 400
HEIGHT = 400
score = 0
fox = Actor("fox")
game_over = False

coin = Actor("coin")
coin.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("score: " + str(score), color="black", topleft=(10, 10))

