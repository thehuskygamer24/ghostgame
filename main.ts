controller.anyButton.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(idk)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    game.gameOver(false)
})
let err: Sprite = null
let ghost: Sprite = null
let idk: Sprite = null
if (("" as any) == ("dontchangethis" as any)) {
    idk = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . 2 2 2 2 2 2 2 2 . . . 
        . . . . 2 2 2 2 2 2 2 2 2 . . . 
        . . . . 2 2 2 2 2 2 2 2 2 . . . 
        . . . . 8 8 8 8 8 8 8 8 8 . . . 
        . . . 8 8 8 8 8 8 8 8 8 8 8 . . 
        . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
        . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
        . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
        . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
        . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
        . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
        . . 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
        . . . 8 8 8 8 8 8 8 8 8 8 8 . . 
        . . . . 8 8 8 8 8 8 8 8 8 . . . 
        . . . . . 8 8 8 8 8 8 8 . . . . 
        `, SpriteKind.Player)
    ghost = sprites.create(img`
        f f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f f 
        f f f 2 2 2 2 f f 2 2 2 2 f f f 
        f f f 2 2 2 2 f f 2 2 2 2 f f f 
        f f f 2 2 2 2 f f 2 2 2 2 f f f 
        f f f 2 2 2 2 f f 2 2 2 2 f f f 
        f f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f f 
        f f f f f f f f f f f f f f f f 
        `, SpriteKind.Enemy)
    ghost.setPosition(9, 14)
    ghost.follow(idk, 30)
    scene.setBackgroundColor(7)
} else {
    scene.setBackgroundColor(4)
    music.play(music.melodyPlayable(music.bigCrash), music.PlaybackMode.InBackground)
    pause(2000)
    err = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 . . . . . . . . . . . . . . 8 
        8 . . . . . . . . . . . . . . 8 
        8 . 1 1 1 . . 1 1 1 . 1 1 1 . 8 
        8 . 1 . . . . 1 . 1 . 1 . 1 . 8 
        8 . 1 1 1 . . 1 1 1 . 1 1 1 . 8 
        8 . 1 . . . . 1 1 . . 1 1 . . 8 
        8 . 1 1 1 . . 1 . 1 . 1 . 1 . 8 
        8 . . . . . . . . . . . . . . 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.Projectile)
    music.play(music.melodyPlayable(music.zapped), music.PlaybackMode.UntilDone)
}
game.onUpdateInterval(5000, function () {
	
})
