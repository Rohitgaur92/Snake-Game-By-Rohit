import pygame

pygame.init()
import random

screen_width = 1000
height = 500

gameWindow= pygame.display.set_mode((screen_width,height))
Title = pygame.display.set_caption("Snake's by Rohit")
pygame.display.update()

font = pygame.font.SysFont(None,55,italic=False)
clock = pygame.time.Clock()

#color
white = (255,255,255)
red = (255,0,0)
orange = (255,165,0)
black = (0,0,0)


def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:

        pygame.draw.rect(gameWindow, color , (x, y, snake_size, snake_size))

def text_screen(text,color,x,y):
    screen_text = font.render(text , True, color)
    gameWindow.blit(screen_text,[x,y])

def wellcome():
    exit_game= False
    while not exit_game:

        gameWindow.fill(orange)
        text_screen("Welcome to Snakes",black,350,150)
        text_screen("Press Space to play",black,350,200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game= True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)



#Game loop

def gameloop():

    #Game Specific variable
    game_over = False
    game_exit = False
    snake_x = 250
    snake_y = 250
    snake_size = 20
    fps = 40
    velocity_x = 0
    velocity_y = 0
    score = 0
    food_x= random.randint(40,screen_width)
    food_y = random.randint(40, height/2)


    initial_velocity = 10

    snk_list= []
    snk_len=1

    with open("High Score.txt",'r') as f:
        hiscore = f.read()

    while not game_exit:
        if game_over:
            with open("High Score.txt",'w') as f:
                f.write(str(hiscore))
            gameWindow.fill(orange)
            if int(hiscore)<score:
                    hiscore=score
            text_screen("GameOver: Press Enter to continue",black,10,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        wellcome()



        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = initial_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -initial_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -initial_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = initial_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score+=10
            snake_x += velocity_x
            snake_y += velocity_y


            if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
                score+= 5
                if score % 25 == 0:
                    initial_velocity+=3 #It will increase the speed when snake eats 5 chunks

                food_x=random.randint(1,screen_width)
                food_y=random.randint(1,height)

                snk_len+=5
                if int(hiscore)<score:
                    hiscore=score


            gameWindow.fill(orange)
            text_screen(("Score:" + str(score) + "  HiScore:" + str(hiscore)),(200,130,76),6,6)


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_len:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over= True


            if snake_x<0 or snake_y<0 or snake_x>screen_width or snake_y>height:
                game_over= True

            plot_snake(gameWindow,black,snk_list,snake_size)



            pygame.draw.rect(gameWindow,white,(food_x,food_y,snake_size,snake_size))

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

wellcome()