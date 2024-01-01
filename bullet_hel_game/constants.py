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
E_VEL = 10  # Size divide by E_VEL (bigger is slower)
B_VEL = 10

# Entity Size

P_SIZE = 15
E_SIZE = 15
B_SIZE = 5
G_SIZE = 10

# Enemy Settings

SIZE_FACTOR = 0.1  # multiplicative
SPAWN_DISTANCE = 20  # how many pixels away from player are enemies allowed to spawn
SPAWN_CAP = 5  # how many enemy can exist on the map
E_HEALTH = 5  # initial enemy health
E_DMG = 10
E_INIT_COOLDOWN = 500  # 5 second

# Player Settings

PLAYER_INIT_HP = 1000
PLAYER_INIT_EXP = 25
B_INIT_COOLDOWN = 50  # 50 milli second
PLAYER_IFRAME = 10  # I frame for 0.1 seconds
COLLECT_DIST = 30  # the distance to collect the gems
LVL_SCALING = 1.05441  # the next lvl exp needed
