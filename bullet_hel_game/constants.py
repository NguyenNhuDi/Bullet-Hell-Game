# Screen Setting
S_WIDTH = 800
S_HEIGHT = 600
TITLE = 'Bullet Hell'
BACKGROUND_COLOR = (180, 196, 222)
FONT_COLOR = (52, 58, 235)

# Bullet Type

BASIC = 1
SPLIT = 2
HONING = 3

# Entity Velocity

P_VEL = 5
E_VEL = 3
B_VEL = 10

# Entity Size

P_SIZE = 15
E_SIZE = 15
B_SIZE = 5
G_SIZE = 10

# Enemy Settings

SPEED_FACTOR = 0.1  # multiplicative
SIZE_FACTOR = 0.1  # multiplicative
COLOR_FACTOR = 10  # additive (makes enemy more red)
SPAWN_DISTANCE = 20  # how many pixels away from player are enemies allowed to spawn
SPAWN_CAP = 1  # how many enemy can exist on the map
E_HEALTH = 5  # initial enemy health

# Time Setting
B_INIT_COOLDOWN = 500  # 1 second
E_INIT_COOLDOWN = 500  # 5 second
