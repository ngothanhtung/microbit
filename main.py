def on_gesture_shake():
    global step
    step += 1
    led.stop_animation()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

step = 1

def on_forever():
    basic.show_number(step)
basic.forever(on_forever)
