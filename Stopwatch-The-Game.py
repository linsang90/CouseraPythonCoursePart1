# mini-project # 3 - "Stopwatch: The Game"

import simplegui

current_time = 0
number_stop = 0
number_hit = 0
is_stoped = False

def format(t) :
    """ Transform current time into correct format."""
    tenth = (t % 10)
    second = (t / 10) % 60
    minute = (t - tenth) / 600
    if(second > 9) :
        time = (str(minute) + ":" + str(second) + "." + str(tenth))
    else :
        time = (str(minute) + ":0" + str(second) + "." + str(tenth))
    return time
    
def start() :
    """ Start the watch."""
    timer.start()
    global is_stopped 
    is_stopped = False

def stop() :
    """ Stop the watch and update counters."""
    timer.stop()
    global number_stop, number_hit, is_stopped
    if(not is_stopped) :
        number_stop += 1
        if(current_time % 10 == 0) :
            number_hit += 1
    is_stopped = True

def reset() :
    """ Reset the watch and counters to zero."""
    timer.stop()
    global current_time, number_stop, number_hit 
    current_time = number_stop = number_hit = 0

def tick() :
    """ Timer handler to count time."""
    global current_time 
    current_time += 1
    
def draw(canvas) :
    """ Draw formatted time and counters on canvas."""
    time = format(current_time)
    counter = str(number_hit) + "/" + str(number_stop)
    canvas.draw_text(time, [120, 150], 25, "White")
    canvas.draw_text(counter, [250, 30], 20, "Green")
    
    
frame = simplegui.create_frame("Stopwatch", 300, 300)
timer = simplegui.create_timer(100, tick)

frame.set_draw_handler(draw)
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)

frame.start()