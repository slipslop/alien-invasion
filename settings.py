class Settings:
    def __init__(self):
        self.screenWidth = 1200
        self.screenHeight = 800
        self.backgroundColor = (0,0,125)

        self.shipSpeed = 4

        self.bulletColor = (200,200,200)
        self.bulletHeight = 3
        self.bulletWidth = 15
        self.bulletSpeed = 6
        self.allowedBulletAmount = 3

        self.alienSpeedX = 0.4
        #1 = up, -1 = down
        self.alienMovementDirection = 1
        self.alienDropSpeed = -40

        self.shipLimit = 3