controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        mySprite.vy = -150
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`tile4`, function (sprite, location) {
    starkNextLevel()
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`MyCat`)
    animation.runImageAnimation(
    mySprite,
    assets.animation`CatWalkBack`,
    100,
    true
    )
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    mySprite.setImage(assets.image`MyCatBack`)
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    mySprite.setImage(assets.image`MyCat`)
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
})
function starkNextLevel () {
    for (let value of sprites.allOfKind(SpriteKind.Enemy)) {
        value.destroy(effects.hearts, 500)
    }
    currentLevel += 1
    if (currentLevel == 1) {
        tiles.setTilemap(tilemap`level0`)
        mySprite = sprites.create(assets.image`MyCatBack`, SpriteKind.Player)
        mySprite.sayText("Hi I'm here!")
        controller.moveSprite(mySprite, 100, 0)
        mySprite.ay = 500
        scene.cameraFollowSprite(mySprite)
        tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 0))
        for (let value of tiles.getTilesByType(assets.tile`tile5`)) {
            myEnemy = sprites.create(img`
                . . f f f . . . . . . . . . . . 
                f f f c c . . . . . . . . f f f 
                f f c c c . c c . . . f c b b c 
                f f c 3 c c 3 c c f f b b b c . 
                f f c 3 b c 3 b c f b b c c c . 
                f c b b b b b b c f b c b c c . 
                c c 1 b b b 1 b c b b c b b c . 
                c b b b b b b b b b c c c b c . 
                c b 1 f f 1 c b b c c c c c . . 
                c f 1 f f 1 f b b b b f c . . . 
                f f f f f f f b b b b f c . . . 
                f f 2 2 2 2 f b b b b f c c . . 
                . f 2 2 2 2 2 b b b c f . . . . 
                . . f 2 2 2 b b b c f . . . . . 
                . . . f f f f f f f . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, SpriteKind.Enemy)
            tiles.placeOnTile(myEnemy, value)
            myEnemy.follow(mySprite, 30)
        }
    } else if (currentLevel == 2) {
        tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 0))
        scene.setBackgroundColor(6)
        tiles.setTilemap(tilemap`level02`)
    } else {
        game.over(true)
    }
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`MyCatBack`)
    animation.runImageAnimation(
    mySprite,
    assets.animation`CatWalk`,
    100,
    true
    )
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`tile2`, function (sprite, location) {
    game.over(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    if (mySprite.bottom < otherSprite.y) {
        sprite.vy = -100
    } else {
        info.changeLifeBy(-1)
    }
})
let myEnemy: Sprite = null
let mySprite: Sprite = null
let currentLevel = 0
scene.setBackgroundColor(9)
currentLevel = 0
starkNextLevel()
game.onUpdate(function () {
    for (let value of sprites.allOfKind(SpriteKind.Enemy)) {
        if (value.isHittingTile(CollisionDirection.Bottom)) {
            if (value.tileKindAt(TileDirection.Left, assets.tile`tile1`) && value.vx < 100) {
                value.vy = -150
            } else if (value.tileKindAt(TileDirection.Right, assets.tile`tile1`) && value.vx < 100) {
                value.vy = -150
            }
        } else if (value.isHittingTile(CollisionDirection.Left)) {
            value.vx = 30
        } else if (value.isHittingTile(CollisionDirection.Right)) {
            value.vx = -30
        }
    }
})
