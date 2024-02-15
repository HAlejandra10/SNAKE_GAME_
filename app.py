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
