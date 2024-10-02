# Lesson 2 - Loops & Lists

from game import run_game

speeds = [5, 10, 20]

for speed in speeds:
    run_game(log_speed=speed)
    
while len(speeds) > 0:
    run_game(log_speed=speeds.pop())