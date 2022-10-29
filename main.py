def on_button_pressed_a():
    microIoT.microIoT_ServoRun(microIoT.aServos.S1, 180)
    basic.pause(1000)
    microIoT.microIoT_ServoRun(microIoT.aServos.S1, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    microIoT.microIoT_MotorRun(microIoT.aMotors.M1, microIoT.Dir.CCW, 255)
    basic.pause(500)
    microIoT.microIoT_motorStop(microIoT.aMotors.M1)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.HAPPY)
microIoT.microIoT_initDisplay()
microIoT.microIoT_WIFI("cas-linksys", "4293894637")
microIoT.microIoT_showUserText(0, "Prueba de Motores")

def on_forever():
    pass
basic.forever(on_forever)
