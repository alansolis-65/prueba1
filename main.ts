input.onButtonPressed(Button.A, function () {
    basic.showString("Hello!")
    basic.pause(1000)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Heart)
    basic.pause(1000)
})
basic.showIcon(IconNames.Happy)
basic.forever(function () {
	
})
