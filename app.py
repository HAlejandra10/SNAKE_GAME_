import pygame, sys, time , random


difficulty_level = 25

frame_size_h = 720
frame_size_v = 480


# looking for errors
check_errors = pygame.init()
#print(check_errors) output: (5,0) <---tuple

if check_errors[1] > 0:
    print(f"[!] Had {check_errors[1]} errors when initializing game, exiting...")
    sys.exit(-1)
else:
    print("[+] Game successfully initialized")
    
# to initialize game window
pygame.display.set_caption("Snake Snacker")
game_window = pygame.display.set_mode((frame_size_h, frame_size_v))

# putting colors on screen
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

#controller for frames (FPS)
fps_controller = pygame.time.Clock()

# Game variables
snake_initial_position = [100, 50]
snake_body_position = [[100, 50], [100-10, 50], [100-(2*10), 50]]
# food position w/ range
food_position = [random.randrange(1, (frame_size_h//10))* 10, random.randrange(1, (frame_size_v//10))* 10]
food_generate= True

#Snake Direction 
direction = 'RIGHT'
change_to = direction

#game score
score= 0 

# When Game Over
def game_over():
    my_font = pygame.font.SysFont('times new', 90)
    game_over_surface= my_font.render("YOU DIED!", True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop= (frame_size_h/2, frame_size_v/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()
    
    
#Score    
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score : " + str(score), True, color)
    score_rect = score_surface.get_rect()
    
    if choice == 1:
        score_rect.midtop = (frame_size_h/10, 15)
    else:
        score_rect.midtop = (frame_size_h/2, frame_size_v/1.25)
        
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()
    
#Main logic 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to= "UP"
            if event.key == pygame.K_UP or event.key == ord('s'):
                change_to= "DOWN"
            if event.key == pygame.K_UP or event.key == ord('a'):
                change_to= "LEFT"
            if event.key == pygame.K_UP or event.key == ord('d'):
                change_to= "RIGHT"   
                
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))    
    
    # Make sure snake no move in the opposite direction instantaneously
    if change_to == "UP" and direction != "DOWN":
        direction= "UP"
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT' 
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
        
    #Moving the snake
    if direction == 'UP':
        snake_body_position[1] -= 10
    if direction == 'DOWN':
        snake_body_position[1] += 10
    if direction == 'LEFT':
        snake_body_position[0] -= 10
    if direction == 'RIGHT':
        snake_body_position[0] += 10
        
    # Snake body growing
    snake_body_position.insert(0, list(snake_initial_position))
    if snake_initial_position[0] == food_position[0] and snake_body_position[1] == food_position[1]:
        score += 1
        food_generate = False
    else:
        snake_body_position.pop()
        
    # generate food on the screen
    if not food_generate:
        food_position =[random.randrange(1, (frame_size_h//10)) *10, random.randrange(1, (frame_size_v//10)) *10]
    food_generate = True

    #GFX
    game_window.fill(black)
    
    for pos in snake_body_position:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        #10, 10 = width, height
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        
    # Snake food
    pygame.draw.rect(game_window, white, pygame.Rect(food_position[0], food_position[1], 10, 10))
        
    





