Song = 0

def on_button_pressed_a():
    global Song
    music.start_melody(music.built_in_melody(Melodies.FUNK), MelodyOptions.ONCE)
    Song = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_screen_down():
    global Song
    music.start_melody(music.built_in_melody(Melodies.RINGTONE), MelodyOptions.ONCE)
    Song = 4
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_ab():
    global Song
    music.start_melody(music.built_in_melody(Melodies.NYAN), MelodyOptions.ONCE)
    Song = 3
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Song
    music.start_melody(music.built_in_melody(Melodies.BLUES), MelodyOptions.ONCE)
    Song = 2
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_logo_down():
    global Song
    music.start_melody(music.built_in_melody(Melodies.CHASE), MelodyOptions.ONCE)
    Song = 5
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_forever():
    for index in range(4):
        basic.show_number(Song)
basic.forever(on_forever)
