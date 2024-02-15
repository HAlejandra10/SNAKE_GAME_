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
            
        


    





