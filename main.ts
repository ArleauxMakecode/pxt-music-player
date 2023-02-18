input.onButtonPressed(Button.A, function () {
    music.startMelody(music.builtInMelody(Melodies.Funk), MelodyOptions.Once)
    Song = 1
})
input.onGesture(Gesture.ScreenDown, function () {
    music.startMelody(music.builtInMelody(Melodies.Ringtone), MelodyOptions.Once)
    Song = 4
})
input.onButtonPressed(Button.AB, function () {
    music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.Once)
    Song = 3
})
input.onButtonPressed(Button.B, function () {
    music.startMelody(music.builtInMelody(Melodies.Blues), MelodyOptions.Once)
    Song = 2
})
input.onGesture(Gesture.LogoDown, function () {
    music.startMelody(music.builtInMelody(Melodies.Chase), MelodyOptions.Once)
    Song = 5
})
let Song = 0
music.setBuiltInSpeakerEnabled(true)
basic.forever(function () {
    for (let index = 0; index < 4; index++) {
        basic.showNumber(Song)
    }
})
