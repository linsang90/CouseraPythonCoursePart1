# Mini-project # 4 - "Pong"

import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

def spawn_ball(direction):
    """Generate a new ball at a random velocity."""
    global ball_pos, ball_vel 
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    vel_h = random.randrange(2, 4)
    vel_v = random.randrange(1, 3)
    if direction == RIGHT :
        ball_vel = [float(vel_h), float(-vel_v)]
    else :
        ball_vel = [float(-vel_h), float(-vel_v)]

def new_game():
    """Start a new game by initializing positions, velocity and scores."""
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)

def draw(canvas):
    """Updating the game situations on table."""
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    
    #1. Draw table.
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
     
    #2. Draw ball and deal with touch of top & bottom wall.
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Yellow", "Yellow")
    
    if ball_pos[1] - BALL_RADIUS <= 0 \
    or ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] = -ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    #3. Draw paddles and set boundary.
    if paddle1_pos + paddle1_vel > HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel < HEIGHT -HALF_PAD_HEIGHT  : 
        paddle1_pos = paddle1_pos + paddle1_vel
    if paddle2_pos + paddle2_vel > HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel < HEIGHT - HALF_PAD_HEIGHT :
        paddle2_pos = paddle2_pos + paddle2_vel

    canvas.draw_polygon([[0, paddle1_pos - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],\
                         [PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [0, paddle1_pos + HALF_PAD_HEIGHT]],\
                        1, "Blue", "Blue")
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos - HALF_PAD_HEIGHT],\
                         [WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]],\
                        1, "Red", "Red")

    #4. Check ball touches paddle or gutters.
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH :
        if ball_pos[1] > paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] < paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else :
            score2 += 1
            spawn_ball(RIGHT)
        
    elif ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH :
        if ball_pos[1] > paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] < paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:
            score1 += 1
            spawn_ball(LEFT)

    #5. Draw scores.
    canvas.draw_text(str(score1), (WIDTH / 4,HEIGHT / 4), 30, "Blue")
    canvas.draw_text(str(score2), (WIDTH * 3 / 4,HEIGHT / 4), 30, "Red")
        
def keydown(key):
    """Handle key down issues."""
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"] :
        paddle1_vel = -3
    elif key == simplegui.KEY_MAP["s"] :
        paddle1_vel = 3
    elif key == simplegui.KEY_MAP["up"] :
        paddle2_vel = -3
    elif key == simplegui.KEY_MAP["down"] :
        paddle2_vel = 3
   
def keyup(key):
    """Handle key up issues."""
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"] :
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"] :
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"] :
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"] :
        paddle2_vel = 0

frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

new_game()
frame.start()