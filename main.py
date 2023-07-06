from pygame import *
from pygame.locals import *
from random import *
from math import *
import os
import time as ttime

flags = FULLSCREEN | DOUBLEBUF
# mixer.pre_init(44100, 16, 2, 4096)
init()

WIDTH, HEIGHT = 1200, 800
# screen = display.set_mode((WIDTH, HEIGHT), flags, 16)
screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Solo Leveling: The Game")

# VECTOR VARIABLES
vec = math.Vector2

# COLOUR VARIABLES
RED = (255, 0, 0)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
paletteList = [(32, 32, 24), (125, 189, 154), (46, 81, 79)]

# BASIC GAME VARIABLES
FPS = 30
# initializing mouse pos
mx, my = 0, 0

# TIMER VARIABLES
clock = time.Clock()
cooldown = USEREVENT + 1
time.set_timer(cooldown, 1000)


# LOAD IMAGES FUNCTION
def image_load(inverted, animList, animNames, animListInverted=None):
    for element in animNames:
        animList.append(image.load(element).convert_alpha())
        if inverted:
            animListInverted.append(transform.flip(image.load(element).convert_alpha(), True, False))


# LOADING ALL IMAGES

# player images - death, run, atk, idle --------------------------------
deathAnim = []
deathNames = [("assets/anims/death" + str(i) + ".png") for i in range(7)]
image_load(False, deathAnim, deathNames)

runRight, runLeft = [], []
runNames = [("assets/anims/runn" + str(i) + ".png") for i in range(8)]
image_load(True, runRight, runNames, runLeft)

atkRight, atkLeft = [], []
atkNames = ["assets/anims/attack/atk" + str(i) + ".png" for i in range(1, 5)]
image_load(True, atkRight, atkNames, atkLeft)

atkUp, atkDown = [transform.flip((transform.rotate(atkRight[i], 300)), False, True) for i in range(len(atkRight))], \
                 [transform.rotate(atkRight[i], 300) for i in range(len(atkRight))]

idleRight, idleLeft = [], []
idleNames = [("assets/anims/idle" + str(i) + ".png") for i in range(4)]
image_load(True, idleRight, idleNames, idleLeft)

# boss images - left and right ------------------------------------------
tuskRight, tuskLeft = [], []
demonNames = [("assets/anims/boss/demonwalk" + str(i) + ".png") for i in range(12)]
image_load(True, tuskRight, demonNames, tuskLeft)

rasakaRight, rasakaLeft = [], []
rasakaNames = [("assets/anims/boss/rasaka" + str(i) + ".png") for i in range(5)]
image_load(True, rasakaRight, rasakaNames, rasakaLeft)

necromancerRight, necromancerLeft = [], []
necromancerNames = [("assets/anims/boss/necromancer" + str(i) + ".png") for i in range(8)]
image_load(True, necromancerRight, necromancerNames, necromancerLeft)

spiderRight, spiderLeft = [], []
spiderNames = [("assets/anims/boss/spider" + str(i) + ".png") for i in range(3)]
image_load(True, spiderRight, spiderNames, spiderLeft)

architectRight, architectLeft = [], []
architectNames = [("assets/anims/boss/architect" + str(i) + ".png") for i in range(10)]
image_load(True, architectRight, architectNames, architectLeft)

deathbringerRight, deathbringerLeft = [], []
deathbringerNames = [("assets/anims/boss/deathbringer" + str(i) + ".png") for i in range(8)]
image_load(True, deathbringerRight, deathbringerNames, deathbringerLeft)

ogreRight, ogreLeft = [], []
ogreNames = [("assets/anims/boss/ogre" + str(i) + ".png") for i in range(3)]
image_load(True, ogreRight, ogreNames, ogreLeft)

cerberusRight, cerberusLeft = [], []
cerberusNames = [("assets/anims/boss/cerberus" + str(i) + ".png") for i in range(2)]
image_load(True, cerberusRight, cerberusNames, cerberusLeft)

doomRight, doomLeft = [], []
doomNames = [("assets/anims/boss/doom" + str(i) + ".png") for i in range(3)]
image_load(True, doomRight, doomNames, doomLeft)

serpentRight, serpentLeft = [], []
serpentNames = [("assets/anims/boss/serpent" + str(i) + ".png") for i in range(4)]
image_load(True, serpentRight, serpentNames, serpentLeft)

# enemy images - left and right --------------------------------------------
wolfRight, wolfLeft = [], []
wolfNames = [("assets/enemies/wolf" + str(i) + ".png") for i in range(5)]
image_load(True, wolfRight, wolfNames, wolfLeft)

goblinRight, goblinLeft = [], []
goblinNames = [("assets/enemies/goblin" + str(i) + ".png") for i in range(7)]
image_load(True, goblinRight, goblinNames, goblinLeft)

wizardRight, wizardLeft = [], []
wizardNames = [("assets/enemies/wizard" + str(i) + ".png") for i in range(2)]
image_load(True, wizardRight, wizardNames, wizardLeft)

antRight, antLeft = [], []
antNames = [("assets/enemies/ant" + str(i) + ".png") for i in range(6)]
image_load(True, antRight, antNames, antLeft)

minoRight, minoLeft = [], []
minoNames = [("assets/enemies/minotaur" + str(i) + ".png") for i in range(8)]
image_load(True, minoRight, minoNames, minoLeft)

magicianRight, magicianLeft = [], []
magicianNames = [("assets/enemies/magician" + str(i) + ".png") for i in range(6)]
image_load(True, magicianRight, magicianNames, magicianLeft)

hippogriffRight, hippogriffLeft = [], []
hippogriffNames = [("assets/enemies/hippogriff" + str(i) + ".png") for i in range(6)]
image_load(True, hippogriffRight, hippogriffNames, hippogriffLeft)

knightRight, knightLeft = [], []
knightNames = [("assets/enemies/knight" + str(i) + ".png") for i in range(3)]
image_load(True, knightRight, knightNames, knightLeft)

lizardRight, lizardLeft = [], []
lizardNames = [("assets/enemies/lizard" + str(i) + ".png") for i in range(9)]
image_load(True, lizardRight, lizardNames, lizardLeft)

steelRight, steelLeft = [], []
steelNames = [("assets/enemies/steel" + str(i) + ".png") for i in range(7)]
image_load(True, steelRight, steelNames, steelLeft)

# LOADING BOSSES WITH IMAGES AND DETAILS
bossAnims = [[rasakaLeft, rasakaRight], [spiderRight, spiderLeft], [tuskRight, tuskLeft],
             [necromancerLeft, necromancerRight], [architectLeft, architectRight],
             [deathbringerRight, deathbringerLeft], [cerberusLeft, cerberusRight],
             [doomRight, doomLeft], [serpentLeft, serpentRight], [ogreRight, ogreLeft]]
# imgList, name, dmg, reward, special, health
allBosses = [[bossAnims[0], "Rasaka", 10, 5, "Snake", 200, image.load("assets/anims/fireball0.png").convert_alpha()],
             [bossAnims[1], "Spider", 15, 5, "Web", 300, image.load("assets/anims/fireball1.png").convert_alpha()],
             [bossAnims[2], "Tusk", 10, 5, "Hymm of Fire", 400, image.load("assets/anims/fireball2.png").convert_alpha()],
             [bossAnims[3], "Wizard", 5, 7, "Undead", 600, image.load("assets/anims/fireball0.png").convert_alpha()],
             [bossAnims[6], "Cerberus", 20, 10, "Woof", 800, image.load("assets/anims/fireball0.png").convert_alpha()],
             [bossAnims[5], "Death Bringer", 15, 15, "Death", 1000, image.load("assets/anims/fireball2.png").convert_alpha()],
             [bossAnims[7], "Doom", 25, 20, "Boom", 1400, image.load("assets/anims/fireball1.png").convert_alpha()],
             [bossAnims[8], "Serpent King", 30, 30, "Slither", 1500, image.load("assets/anims/fireball2.png").convert_alpha()],
             [bossAnims[9], "Ogre Demon", 35, 35, "OGREEEE", 1700, image.load("assets/anims/fireball0.png").convert_alpha()],
             [bossAnims[4], "Architect", 40, 40, "Creation", 2000, image.load("assets/anims/fireball1.png").convert_alpha()]]

# LOADING ENEMIES WITH IMAGES AND DETAILS
enemyPics = [[wolfRight, wolfLeft], [goblinLeft, goblinRight], [wizardLeft, wizardRight],
             [antRight, antLeft], [minoLeft, minoRight], [magicianLeft, magicianRight],
             [hippogriffLeft, hippogriffRight], [knightLeft, knightRight], [lizardRight, lizardLeft],
             [steelLeft, steelRight]]
# img, name, dmg, speed, reward, health
allEnemies = [[enemyPics[0], "Steel Fanged Raikan", 5, 3, 10, 50],
              [enemyPics[2], "Necromancer", 6, 2, 20, 60],
              [enemyPics[1], "Goblins", 3, 4, 20, 50],
              [enemyPics[3], "Ants", 7, 7, 30, 90],
              [enemyPics[4], "Minotaur", 12, 2, 30, 130],
              [enemyPics[5], "Magician", 10, 4, 40, 150],
              [enemyPics[6], "Hippogriff", 20, 5, 40, 170],
              [enemyPics[8], "Lizard", 35, 3, 25, 220],
              [enemyPics[7], "Knight", 40, 4, 30, 270],
              [enemyPics[9], "Steel", 50, 3, 20, 300]]

# ENEMY VARIABLES
spawned = 0  # track amount of enemies spawned
dungeonEnemies = [3, 5, 7, 7, 7, 8, 8, 8, 9, 9]  # enemycount for each dungeon


# DEATH ANIMATINO VARIABLES
dead = (0, 0)  # coordinates for sprite death (enemy, player, boss) - used for death animation


# SOUND EFFECTS

# sword sounds - swing and equip
swingsfx = []
for i in range(3):
    swingsfx.append(mixer.Sound("assets/sfx/swing" + str(i) + ".wav"))
    mixer.Sound.set_volume(swingsfx[i], 0.1)
    
equipsfx = []
for i in range(5):
    equipsfx.append(mixer.Sound("assets/sfx/equip" + str(i) + ".wav"))
    mixer.Sound.set_volume(equipsfx[i], 0.1)

# boss magic sound
magicsfx = mixer.Sound("assets/sfx/magic0.wav")
mixer.Sound.set_volume(magicsfx, 0.03)

# monster hurt sound
monsterdmgsfx = mixer.Sound("assets/sfx/monsterdmg0.wav")
mixer.Sound.set_volume(monsterdmgsfx, 0.1)

# ui click sound
clicksfx = mixer.Sound("assets/sfx/click.wav")
mixer.Sound.set_volume(clicksfx, 0.1)

# WRITING DEFAULT ITEMS FOR FIRST PLAYTHROUGH
if os.stat("assets/txtfiles/config.txt").st_size == 0:  # checking if config is empty
    with open("assets/txtfiles/inventory.txt", "w") as invFile, open("assets/txtfiles/selected.txt", "w") as selectFile, \
            open("assets/txtfiles/skills.txt", "w") as skillsFile, open("assets/txtfiles/stats.txt", "w") as statFile, \
            open("assets/txtfiles/shop.txt", "w") as shopFile:
        invFile.write("Fist\nWeapon\n1\nfist0.png\n-\nKim Sahng-Sik's Sword\nWeapon\n10\nsword0.png\n-")
        selectFile.write("0,1\n0,1,2,3")
        skillsFile.write("sprint\nberserk\nheal\nghost")
        statFile.write("0\nE-Rank Hunter\n100\n100\n5\n5")
        shopFile.write("100")

# FONTS
# loading all fonts
fontMed = font.Font("assets/fonts/HIROMISAKE.ttf", 39)
fontSmall = font.Font("assets/fonts/hud.otf", 15)
fontStory = font.Font("assets/fonts/story.ttf", 17)
fontTitle = font.Font("assets/fonts/titlefont1.otf", 20)
fontButtons = font.Font("assets/fonts/zelda.ttf", 40)
fontButtonTitle = font.Font("assets/fonts/titlefont2.ttf", 100)
fontRewards = font.Font("assets/fonts/story.ttf", 30)
statFont = font.Font("assets/fonts/hud.otf", 30)

# MUSIC
# loading tracks, setting volume
trackList = ["assets/track0.wav", "assets/track1.wav", "assets/track2.wav"]
mixer.music.set_volume(0.1)

# LOGIN VARIABLES
login = False  # to check if player needs to log in
username = ""  # username string
password = ""  # password string
loginStep = 0  # tracks 'step' of login (username-0, password-1)

# DUNGEON VARIABLES
isBattle = False  # checks if player is currently in battle
enemyCount = 3  # starting enemycount
isWin = False  # variable to determine if dungeon win/lose

# SCENE VARIABLES
cutscene = False  # cutscenes (panels)
skip = False  # checking for user skip cutscene

# STORE AND STAT MENU VARS
points = 0  # skill points to upgrade skills in statmenu


# FUNCTION TO BLIT MULTILINE TEXT FOR STORY (not our work, got it from stack overflow)
def multiline_text(s, text, pos, f, colour=BLACK):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words
    space = f.size(' ')[0]  # The width of a space
    max_width, max_height = s.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = f.render(word, 0, colour)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x
                y += word_height  # Start on new row
            s.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x
        y += word_height  # Start on new row


# GETTING USERNAME
if os.stat("assets/txtfiles/config.txt").st_size != 0:
    with open("assets/txtfiles/config.txt", "r") as configFile:
        username = str(configFile.readline().strip())
        usernameText = statFont.render(username, True, WHITE)  # username text


# PLAYER ATTRIBUTE VARIABLES
with open("assets/txtfiles/stats.txt", "r") as statFile:
    stats = statFile.readlines()
    level = int(stats[0].strip())
    title = stats[1].strip()
    health = int(stats[2].strip())
    mana = int(stats[3].strip())
    strength = int(stats[4].strip())
    agility = int(stats[5].strip())

# MAIN SCREEN VARIABLES
mainbg = image.load("assets/menu/mainbg.png").convert()  # main screen background
statusPage = image.load("assets/menu/status.png").convert_alpha()  # status page - shows stats
shopPage = image.load("assets/menu/shop.png").convert_alpha()  # shop page - shows available items
# screen booleans - menu, stat, shop, inv, cred
isMenu, isStat, isShop, isInv, isCred, isGuide = False, False, False, False, False, False
# list of attribute variables
statVars = [level, title, health, mana, strength, agility]  # all atrributes
statVarNames = ["Level", "Title", "Health", "Mana", "Strength", "Agility"]
statVarText = []
# creating text for stat menu
for i in range(len(statVarNames)):
    statVarText.append(statFont.render(statVarNames[i], True, WHITE))
statTexts = []  # stats nums to be blitted onto screen
for s in statVars:  # loop through attributes and add text of each number to statTexts
    statTexts.append(statFont.render(str(s), True, WHITE))

# DUNGEON VARIABLES TO TRACK PROGRESS
currDungeon = 0  # tracking current dungeon
isDungeon = False  # track if currently in dungeon
if os.stat("assets/txtfiles/config.txt").st_size != 0:  # making sure files not empty
    with open("assets/txtfiles/progress.txt", "r") as initFile:
        progress = initFile.readlines()
        if progress[0].strip() == "True":  # if currently in dungeon
            isDungeon = True
            mixer.music.load(trackList[1])
            mixer.music.play(-1)
        if progress[2].strip() == "True":  # if currently in menu
            isMenu = True
            mixer.music.load(trackList[0])
            mixer.music.play(-1)
        # getting current dungeon number
        currDungeon = int(progress[1])
        # getting current point amount
        points = int(progress[3])
        # getting enemycount for current dungeon
        enemyCount = dungeonEnemies[currDungeon]

# initializing current weapon and skill lists
currWeapons = []
currSkills = []
# getting equiped items (weapons and skills)
with open("assets/txtfiles/selected.txt") as itemFile:
    currItems = itemFile.readlines()
    for sel in range(len(currItems)):
        currItems[sel] = currItems[sel].strip().split(",")
    for i in range(len(currItems[0])):
        currWeapons.append(currItems[0][i])
    for i in range(len(currItems[1])):
        currSkills.append(currItems[1][i])
        

# CURRENT CONSUMABLE AND ARMOUR
currConsumable = [None, "", 0]
currArmour = [None, 0]


# loading weapoons and skills
def loadItems(wList, txt, loadType):
    with open(txt, "r") as iFile:
        items = iFile.readlines()
        for j in range(len(items)):  # iterating and stripping content of file
            items[j] = items[j].strip()
        if loadType == "inventory":  # if file type is inventory then use below format to store info
            for i in range(0, len(items), 5):
                wList.append([items[i], items[i + 1], items[i + 2], items[i + 3], items[i + 4]])
        elif loadType == "skills":  # if file type is skills then use below format to store skills
            for i in range(len(items)):
                wList.append(items[i])


# lists to store weapons and dict to store images for those weapons
weaponList = []
weaponPics = {}

# similarly, list and dict to store skills
skillList = []
skillPics = {
    "0": image.load("assets/skills/sprint.png").convert(),
    "1": image.load("assets/skills/berserk.png").convert(),
    "2": image.load("assets/skills/heal.png").convert(),
    "3": image.load("assets/skills/ghost.png").convert()
}

# loading items for weapons and skills from txt files
loadItems(weaponList, "assets/txtfiles/inventory.txt", "inventory")
loadItems(skillList, "assets/txtfiles/skills.txt", "skills")
for i in range(len(weaponList)):
    weaponPics[str(i)] = (image.load("assets/shop/" + weaponList[i][3]).convert_alpha(),
                          image.load("assets/shop/" + weaponList[i][3][:-4] + "IG.png").convert_alpha())


# ENEMY CLASS - sprite
class Enemy(sprite.Sprite):
    def __init__(self, img, name, dmg, speed, reward, health):
        super().__init__()
        self.image = img[0][0]
        self.imageList = img
        # random position to be spawned at
        self.posx, self.posy = randint(300, 1000), randint(200, 1000)
        self.rect = (self.posx, self.posy, self.image.get_width(), self.image.get_height())
        # setting enemy info
        self.name = name
        self.dmg = dmg
        self.speed = speed
        self.reward = reward
        self.health = health
        self.randomTL = 16  # random time limit - to set intervals
        self.randomMove = 0  # rand 0-1 int to check if enemy will move or not move (0 = move, 1 = not move)
        self.hitLimit = True  # limit hits, no hit every frame
        self.damaged = False  # boolean for whether damaged
        self.fontSize = 0  # fontsize for dmg indicator
        self.dmgTL = 0  # time interval for dmg indicator
        self.moveFrame = 0  # frame of enemy sprite
        self.moveCap = 0  # to cap the movement to every x number of frames
        self.dir = [True, False]  # direction list - stores booleans that represent each direction
    
    # function to update enemy position and track player
    def update_pos(self):
        if self.randomTL > 15:  # checking for next decision (move or not move)
            self.randomTL = 0  # resetting timer for next decision
            self.randomMove = randint(0, 1)  # getting random num to determine
        self.randomTL += 1  # increase timer
        # check where enemy is in relation to player in order to determine where to move
        if self.posx > player.posx:
            if self.randomMove == 0:  # checking if decision is to move
                self.posx -= randint(self.speed - 1, self.speed)  # moving
                self.dir = [False, True]  # setting direction (left, right)
        elif self.posx < player.posx:  # check for enemy v player position
            if self.randomMove == 0:  # checking if move
                self.posx += randint(self.speed - 1, self.speed)  # moving
                self.dir = [True, False]  # setting direction
        if self.posy > player.posy:  # SAME AS PREVIOUS 2 BUT DIFFERENT MOVEMENT AXIS TO ALLOW FOR DIAGONAL MOVEMENT
            if self.randomMove == 0:
                self.posy -= randint(self.speed - 1, self.speed)
        elif self.posy < player.posy:
            if self.randomMove == 0:
                self.posy += randint(self.speed - 1, self.speed)  # move at certain speed
        
        if self.moveFrame == len(self.imageList[0]) - 1:  # frame for enemy animation
            self.moveFrame = 0  # reseting move frame for enemy based on how many frames it contains
        if self.moveCap > 2:  # only changing enemy frame if movecap is greater than 2 (changes moveframe every 2 frames)
            self.moveFrame += 1  # change moverframe
            self.moveCap = 0  # reset movecap
        else:
            self.moveCap += 1  # increase movecap
        if self.dir == [False, True]:  # checking for direction to blit correct facing sprites (left and right facing sprites)
            self.image = self.imageList[0][self.moveFrame]
        else:
            self.image = self.imageList[1][self.moveFrame]
        
        # setting rect for collision as well as blitting enemy onto screen
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posx, self.posy)
        dungeonSurf.blit(self.image, (self.posx, self.posy))
    
    # function to indicate enemy damage
    def damage_indicator(self):
        if self.damaged:  # checking for if enemy has been hit
            fontDmg = font.Font("assets/fonts/HIROMISAKE.ttf", self.fontSize)  # setting new fontsize for text
            if self.dmgTL < 10:  # checking if frame is less than 10, if so, increase fontsize
                self.fontSize += 3
            if self.dmgTL > 14:  # checking if frame greater than 15, degrease fontsize back to 0
                self.fontSize -= 4
            if self.fontSize <= 0:  # if fontsize back to 0, damage indicator done
                self.dmgTL = 0  # reset frame count
                self.damaged = False
            self.dmgTL += 1  # increasing frame count
            dungeonSurf.blit(fontDmg.render("-" + str(player.strength + strength), True, WHITE),
                             (self.posx + self.fontSize // 4 + 15, self.posy - 30))  # blitting text above sprite head
    
    # checking for player being hit, decrease player health if hit
    def player_hit(self):
        if Rect.colliderect(Rect(player.rect), Rect(self.rect)) and self.hitLimit:  # checking for rect collide
            if player.health > 0:
                self.hitLimit = False
                player.health -= self.dmg  # decrease player health
                player.damaged = True
                player.dmgtaken = self.dmg  # getting amount of dmg for player dmg indicator


# creating sprite groups for enemy and boss
enemygroup = sprite.Group()
bossgroup = sprite.Group()
enemySpawn = True


# function to spawn in enemies and add to sprite group - if number of spawned enemies is less than set amount
def spawn_enemy(enemyInfo):
    global spawned, enemySpawn  # need to access amount of spawned enemies
    if spawned < dungeonEnemies[currDungeon] and enemySpawn:
        enemySpawn = False
        spawned += 1  # increasing total amount of spawned enemies
        enemy = Enemy(enemyInfo[0], enemyInfo[1], enemyInfo[2], enemyInfo[3], enemyInfo[4], enemyInfo[5])  # initialize instance
        enemygroup.add(enemy)  # add to sprite group


# function to update enemies position and status
def update_enemy():
    global enemyCount, accumCoins, dead
    for e in enemygroup:  # iterating through all enemies in sprite group
        e.update_pos()  # updating position
        e.damage_indicator()  # indicating damage if damaged
        e.player_hit()  # checking for player collision
        # if enemy has been hit
        if ((e.rect.colliderect(player.atkRect) or e.rect.colliderect(player.rect)) and player.attacking) and e.hitLimit:
            mixer.Sound.play(monsterdmgsfx)  # play dmg grunt sound
            e.hitLimit = False  # disallow consecutive frame hits, resets every second
            e.health -= player.strength + strength  # takes away from health
            e.damaged = True  # sets damaged to true for dmg indicator
            if e.health <= 0:  # checking for death
                dead = (e.posx, e.posy)  # setting dead variable for death animation to play
                e.kill()  # killing sprite, and deleting from memory
                accumCoins += int(allEnemies[currDungeon][4])  # gaining coins from killing enemy
                enemyCount -= 1  # decrease enemy count


# PLAYER CLASS
class Player:
    def __init__(self, level, title, health, mana, strength, agility):
        super().__init__()
        self.posx, self.posy = 600, 400
        self.rect = (self.posx, self.posy, 40, 40)
        self.dir = [False, False, False, False]
        self.speed = agility
        self.moving = False
        self.moveFrame = 0
        self.moveCap = 0
        self.image = runRight[0]
        self.level = level
        self.title = title
        self.health = health
        self.mana = mana
        self.strength = strength
        self.damaged = False
        self.dmgTL = 0
        self.fontSize = 0
        self.selWeapon = currWeapons[0]
        self.weaponAngle = [50, 130]
        self.currWeaponImg = [transform.rotate(weaponPics.get(self.selWeapon)[1], self.weaponAngle[0]),
                              transform.rotate(transform.flip(weaponPics.get(self.selWeapon)[1], False, True),
                                               self.weaponAngle[1])]
        self.atkAnim = atkRight
        self.atkmoveframe = 0
        self.attacking = False
        self.atkcap = 0
        self.hitLimit = True
        self.atkRect = [0, 0, 0, 0]
        self.yoffset = 25
        self.dmgtaken = 0
        self.atkCooldown = True
    
    def move_player(self):
        global surfX, surfY
        self.dir[0], self.dir[1], self.dir[2], self.dir[3] = False, False, False, False
        if self.health > 0:
            keys = key.get_pressed()
            if keys[K_w] and hit_wall(self.rect[0], self.rect[1] - 5, walls) == -1:
                self.dir[2] = True
                self.moving = True
                self.posy -= self.speed
                surfY += self.speed
            if keys[K_a] and hit_wall(self.rect[0] - 5, self.rect[1], walls) == -1:
                self.dir[1] = True
                self.moving = True
                self.posx -= self.speed
                surfX += self.speed
            if keys[K_s] and hit_wall(self.rect[0], self.rect[1] + 45, walls) == -1:
                self.dir[3] = True
                self.moving = True
                self.posy += self.speed
                surfY -= self.speed
            if keys[K_d] and hit_wall(self.rect[0] + 40, self.rect[1], walls) == -1:
                self.dir[0] = True
                self.moving = True
                self.posx += self.speed
                surfX -= self.speed
    
    def update(self):
        if self.moveFrame == len(runRight) - 1:
            self.moveFrame = 1
        if self.moveCap > 2:
            self.moveFrame += 1
            self.moveCap = 0
        else:
            self.moveCap += 1
        if self.moving and self.dir[1]:
            self.image = runLeft[self.moveFrame]
        elif self.moving:
            self.image = runRight[self.moveFrame]
        
        if True not in self.dir:
            self.image = idleRight[0]
        
        if self.health > 0:
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.posx, self.posy)
            dungeonSurf.blit(self.image, (self.posx, self.posy))
    
    def damage_indicator(self):
        if self.damaged:
            fontDmg = font.Font("assets/fonts/HIROMISAKE.ttf", self.fontSize)
            if self.dmgTL < 10:
                self.fontSize += 3
            if self.dmgTL > 14:
                self.fontSize -= 4
            if self.fontSize <= 0:
                self.dmgTL = 0
                self.damaged = False
            self.dmgTL += 1
            dungeonSurf.blit(fontDmg.render("-" + str(self.dmgtaken), True, RED),
                             (self.posx + self.fontSize // 4 + 15, self.posy - 30))
    
    def equip_weapon(self):
        if not self.attacking and self.health > 0:
            if self.dir[1]:
                dungeonSurf.blit(self.currWeaponImg[1], (self.posx - 40, self.posy - 25))
            elif self.dir[0]:
                dungeonSurf.blit(self.currWeaponImg[0], (self.posx + 35, self.posy - 25))
            else:
                dungeonSurf.blit(self.currWeaponImg[0], (self.posx-10, self.posy - 30))
    
    def player_attack(self):
        keys = key.get_pressed()
        if keys[K_SPACE] and not self.attacking and self.atkCooldown and ghost[1]:
            mixer.Sound.play(swingsfx[randint(0, 2)])
            self.atkCooldown = False
            self.attacking = True
            self.yoffset = 25
            if self.dir[2]:
                self.atkAnim = atkUp
                self.yoffset = 50
            if self.dir[3]:
                self.atkAnim = atkDown
                self.yoffset = 0
            if self.dir[1]:
                self.atkAnim = atkLeft
            if self.dir[0]:
                self.atkAnim = atkRight
        if self.attacking:
            if self.atkmoveframe == len(self.atkAnim) - 1:
                self.atkmoveframe = 0
                self.attacking = False
            if self.atkcap > 5:
                self.atkmoveframe += 1
                self.atkcap = 0
            if self.attacking:
                self.atkcap += 2
                self.atkRect = (self.atkAnim[self.atkmoveframe]).get_rect()
                self.atkRect.topleft = (self.posx + (50 if self.dir[0] else -45), self.posy - self.yoffset)
                dungeonSurf.blit(self.atkAnim[self.atkmoveframe],
                                 (self.posx + (50 if self.dir[0] else -45), self.posy - self.yoffset))


# create instance of player class
player = Player(level, title, health, mana, strength, agility)


class Boss(sprite.Sprite):
    def __init__(self, imgList, name, dmg, reward, special, health, fireball):
        super().__init__()
        self.imageList = imgList
        self.image = imgList[0][0]
        self.fireball = fireball
        self.posx, self.posy = randint(700, 1000), randint(500, 1000)
        self.rect = (self.posx, self.posy, self.image.get_width(), self.image.get_height())
        self.permHealth = health
        self.health = health
        self.name = name
        self.dmg = dmg
        self.reward = reward
        self.special = special
        self.randomTL = 41
        self.hitLimit = True
        self.timerProt = 0
        self.fireB = 10
        self.moveFrame = 0
        self.moveCap = 0
        self.dir = [True, False]
        self.fireBalls = []
        self.isReady = True
        self.getCoords = False
        self.a = None
        self.b = None
        self.speed = 15
        self.bullets = []
        self.ang = 0
        self.vx, self.vy = 0, 0
        self.damaged = False
        self.fontSize = 0
        self.dmgTL = 0
        self.healthRect1 = Rect(98, 98, 1004, 24)
        self.healthRect2 = Rect(100, 1000, self.health, 20)
        self.healthScale = 1000 / self.health
    
    def health_bar(self):
        self.healthRect2 = Rect(100, 100, self.health * self.healthScale, 20)
        draw.rect(screen, WHITE, self.healthRect1)
        draw.rect(screen, RED, self.healthRect2)
    
    def update_pos(self):
        if self.posx > player.posx:
            if not player.posx - 10 < self.posx < player.posx + 10:
                self.posx -= 3
                self.dir = [True, False]
        elif self.posx < player.posx:
            if not player.posx - 10 < self.posx < player.posx + 10:
                self.posx += 3
                self.dir = [False, True]
        if self.posy > player.posy:
            self.posy -= 3
        elif self.posy < player.posy - 100:
            self.posy += 3
        
        if self.moveFrame == len(self.imageList[0]) - 1:
            self.moveFrame = 0
        if self.moveCap > 2:
            self.moveFrame += 1
            self.moveCap = 0
        else:
            self.moveCap += 1
        if self.dir[1]:
            self.image = self.imageList[0][self.moveFrame]
        elif self.dir[0]:
            self.image = self.imageList[1][self.moveFrame]
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posx, self.posy)
        dungeonSurf.blit(self.image, (self.posx, self.posy))
    
    def melee_atk(self):
        if self.rect.colliderect(player.rect) and player.hitLimit:
            player.damaged = True
            player.hitLimit = False
            player.health -= self.dmg
            player.dmgtaken = self.dmg
    
    def tusk_atk(self):
        if self.isReady:
            if player.health > 0 and isBattle:
                if self.getCoords == True:
                    self.getCoords = False
                    self.ang = atan2(player.posy - self.posy, player.posx - self.posx)
                    self.vx = cos(self.ang) * self.speed
                    self.vy = sin(self.ang) * self.speed
                    self.bullets.append([self.posx, self.posy, self.vx, self.vy])
            for b in self.bullets[:]:  # bullets[:] is a COPY of the bullets list
                b[0] += b[2]
                b[1] += b[3]
                if b[0] > 2090 or b[0] < 80 or b[1] > 2220 or b[1] < 200:  # off-screen
                    self.bullets.remove(b)
            for b in self.bullets:
                dungeonSurf.blit(self.fireball, (int(b[0])-22, int(b[1])-22))
                if Rect(int(b[0]), int(b[1]), 10, 10).colliderect(player.rect):
                    player.damaged = True
                    player.health -= 1
                    player.dmgtaken = 1
    
    def damage_indicator(self):
        if self.damaged:
            fontDmg = font.Font("assets/fonts/HIROMISAKE.ttf", self.fontSize)
            if self.dmgTL < 10:
                self.fontSize += 3
            if self.dmgTL > 14:
                self.fontSize -= 4
            if self.fontSize <= 0:
                self.dmgTL = 0
                self.damaged = False
            self.dmgTL += 1
            dungeonSurf.blit(fontDmg.render("-" + str(player.strength + strength), True, WHITE),
                             (self.posx + self.fontSize // 4 + 15, self.posy - 30))


bossOverTimer = 0


def update_boss():
    global isReward, accumCoins, dead, bossOverTimer
    for b in bossgroup:
        b.update_pos()
        b.tusk_atk()
        b.melee_atk()
        b.damage_indicator()
        b.health_bar()
        if Rect(player.atkRect).colliderect(b.rect) and b.hitLimit and player.attacking:
            b.damaged = True
            b.hitLimit = False
            b.health -= player.strength + strength
        if b.health <= 0:
            dead = (b.posx, b.posy)
            b.kill()
    if not bossgroup:
        if bossOverTimer > 50:
            bossOverTimer = 0
            dungeon_reset(True)
            isReward = True
            accumCoins += int(allBosses[currDungeon][3])
        bossOverTimer += 1


deathAnimCount = 0
deathAnimCountTL = 0


def death_anim(pos):
    global deathAnimCount, deathAnimCountTL, dead
    if deathAnimCount == 6:
        dead = (0, 0)
        deathAnimCount = 0
        deathAnimCountTL = 0
        return True
    elif deathAnimCountTL > 2:
        deathAnimCount += 1
        deathAnimCountTL = 0
    deathAnimCountTL += 1
    dungeonSurf.blit(deathAnim[deathAnimCount], pos)


# function to detect player-wall collision
def hit_wall(x, y, wallList):
    pRect = Rect(x, y, 25, 25)
    return pRect.collidelist(wallList)


# surface for status page
statusSurf = Surface((1200, 800))
buttonImg = image.load("assets/menu/buttonpurpleclicked.png").convert_alpha()
buttonHoverImg = image.load("assets/menu/buttonpurple.png").convert_alpha()
buttonText = [fontButtons.render("DUNGEON", True, WHITE), fontButtons.render("STATS", True, WHITE),
              fontButtons.render("STORE", True, WHITE), fontButtons.render("INVENTORY", True, WHITE),
              fontButtons.render("CREDITS", True, WHITE)]
logoImg = image.load("assets/menu/logo.png").convert_alpha()
mainButtonRects = [[80, i, 225, 70] for i in range(300, len(buttonText) * 100 + 201, 90)]
weaponPos = [[200, 20], [265, 20]]
skillPos = [[365, 20], [430, 20], [495, 20], [560, 20]]
replaceNum = 0


def hud_menu(s):
    global replaceNum
    draw.rect(s, BLACK, (0, 0, 1200, 100))
    s.blit(coinImg, (20, 33))
    s.blit(fontMed.render(str(coins), True, WHITE), (70, 35))
    s.blit(fontMed.render("Skill Points: " + str(points), True, WHITE), (850, 35))
    # selected weapons and skills (blitting)
    for i in range(len(currWeapons)):
        s.blit(transform.scale(weaponPics.get(str(currWeapons[i]))[0], (60, 60)), weaponPos[i])
        if Rect(weaponPos[i][0], weaponPos[i][1], 60, 60).collidepoint(mx, my):
            if clicked:
                replaceNum = i
    for i in range(len(currSkills)):
        s.blit(transform.scale(skillPics.get(str(currSkills[i])), (60, 60)), skillPos[i])
    if currConsumable[0] is not None:
        s.blit(transform.scale(currConsumable[0], (60, 60)), [660, 20])
    if currArmour[0] is not None:
        s.blit(transform.scale(currArmour[0], (60, 60)), [760, 20])


wallFountainBasin = []
wallFountainBasinName = [("assets/tileset/Walls/fountain" + str(i) + ".png") for i in range(3)]
image_load(False, wallFountainBasin, wallFountainBasinName)

wallFountainMid = []
wallFountainMidName = [("assets/tileset/Walls/f" + str(i) + ".png") for i in range(3)]
image_load(False, wallFountainMid, wallFountainMidName)


def draw_fountain(ds, count):
    count[0] += 1
    if count[0] == 5:
        count[1] = (count[1] + 1) % 3
        count[0] = 0
    for x in range((1008 // 7) + 35, (1008 + 1) + 35, (1008 // 7) + 35):
        ds.blit(wallFountainBasin[count[1]], (x, 165))
        ds.blit(wallFountainMid[count[1]], (x, 165 + 16))


fountainCount = [0, 0]

mainBlit = True
settingsButton = image.load("assets/menu/settings.png").convert_alpha()
settingsButtonRect = Rect(settingsButton.get_rect())
settingsButtonRect.topleft = (1080, 20)


def main_menu():
    global isDungeon, isMenu, isStat, isShop, isInv, isCred, mainBlit, isGuide
    if mainBlit:
        screen.blit(mainbg, (0, 0))
        screen.blit(logoImg, (44, 10))
        screen.blit(settingsButton, (1080, 20))
        mainBlit = False
    # blitting battle button
    for i in range(len(mainButtonRects)):
        screen.blit(transform.scale(buttonImg, (250, 72)), (mainButtonRects[i][0] - 12, mainButtonRects[i][1] - 2))
        if Rect(mainButtonRects[i]).collidepoint(mx, my):
            mainBlit = True
            screen.blit(transform.scale(buttonHoverImg, (250, 72)),
                        (mainButtonRects[i][0] - 12, mainButtonRects[i][1] - 2))
        screen.blit(buttonText[i], (mainButtonRects[i][0] + 20, mainButtonRects[i][1] + 15))
    # going to next dungeon
    if Rect(mainButtonRects[0]).collidepoint(mx, my) and clicked:
        isMenu = False
        isDungeon = True
        mixer.Sound.play(clicksfx)
        mixer.music.load(trackList[randint(1, 2)])
        mixer.music.play(-1)
    if Rect(mainButtonRects[1]).collidepoint(mx, my) and clicked:
        mixer.Sound.play(clicksfx)
        isStat = True
    if Rect(mainButtonRects[2]).collidepoint(mx, my) and clicked:
        mixer.Sound.play(clicksfx)
        isShop = True
    if Rect(mainButtonRects[3]).collidepoint(mx, my) and clicked:
        mixer.Sound.play(clicksfx)
        isInv = True
    if Rect(mainButtonRects[4]).collidepoint(mx, my) and clicked:
        mixer.Sound.play(clicksfx)
        isCred = True
    if settingsButtonRect.collidepoint(mx, my) and clicked:
        mixer.Sound.play(clicksfx)
        isGuide = True


statText = fontButtonTitle.render("STATUS", True, WHITE)
statbg = image.load("assets/menu/statbg.png").convert()
statRects = [[i + 1000, i * 80 + 255, 150, 40] for i in range(2, len(statTexts))]
statButton = transform.scale(buttonImg, (150, 40))
upgradeText = fontSmall.render("UPGRADE", True, WHITE)


# skillVars = [level, title, health, mana, strength, agility]  # all atrributes

def upgrade_stats():
    global statVars, clicked, points, mana, health
    for i in range(len(statTexts) - 2):
        if Rect(statRects[i]).collidepoint(mx, my) and clicked and points > 0:
            clicked = False
            if i == 0:
                player.health += 2
                health += 2
                statVars[i + 2] += 2
                points -= 1
            if i == 1:
                player.mana += 2
                mana += 2
                statVars[i + 2] += 2
                points -= 1
            if i == 2:
                player.strength += 2
                statVars[i + 2] += 2
                points -= 1
            if i == 3 and player.speed < 10:
                player.speed += 1
                statVars[i + 2] += 1
                points -= 1
            statTexts[i + 2] = statFont.render(str(statVars[i + 2]), True, WHITE)


statTextSurf = Surface((330, 200))
statDescript = "Upgrade and View your stats here. If you have skill points, you can upgrade your skills." \
               "   NOTE: agility has a max level of 10."


# main screen w/ status panel, shop
def stat_menu():
    global isStat
    keys = key.get_pressed()
    if keys[K_ESCAPE]:
        isStat = False
    screen.blit(statusSurf, (0, 0))
    statusSurf.blit(statbg, (0, 30))
    statusSurf.blit(invtransbg, (365, 140))
    statusSurf.blit(statTextSurf, (18, 250))
    multiline_text(statTextSurf, statDescript, (10, 50), fontStory, WHITE)
    hud_menu(statusSurf)
    statusSurf.blit(statText, (65, 130))
    statusSurf.blit(usernameText, (400, 155))
    for i in range(len(statTexts)):
        screen.blit(statVarText[i], (i + 400, i * 80 + 255))
        screen.blit(statTexts[i], (i + 600, i * 80 + 255))
        if i < len(statTexts) - 2:
            statusSurf.blit(statButton, (statRects[i][0], statRects[i][1]))
            statusSurf.blit(upgradeText, (statRects[i][0] + 35, statRects[i][1] + 10))
            upgrade_stats()
    back_button()


shopbg = image.load("assets/menu/shopbg.png").convert()
shopText = fontButtonTitle.render("GAME SHOP", True, WHITE)
shopTextSurf = Surface((330, 200))
shopDescript = "Purchasing Items: Click on item > Click preview of item to " \
               "confirm purchase > Item arrives in your inventory       " \
               "                                                Don't go broke!"


def shop_menu():
    global isShop
    keys = key.get_pressed()
    if keys[K_ESCAPE]:
        isShop = False
    screen.blit(shopSurf, (0, 0))
    shopSurf.blit(shopbg, (0, 0))
    shopSurf.blit(invtransbg, (365, 140))
    shopSurf.blit(shopText, (10, 130))
    shopSurf.blit(shopTextSurf, (18, 250))
    multiline_text(shopTextSurf, shopDescript, (10, 50), fontStory, WHITE)
    hud_menu(shopSurf)
    item_shop()
    back_button()


accumCoins = 0

with open("assets/txtfiles/shop.txt") as shopFile:
    coins = shopFile.readlines()[0].strip()
itemPreview = False
itemPN = 0
previewImg = image.load("assets/shop/preview.png").convert_alpha()
coinImg = image.load("assets/shop/coins.png").convert_alpha()
itemImgs = []
itemRects = []
itemNames = ["manapotion.png", "dagger.png", "armprotector.png", "helmet.png", "knightkiller.png",
             "demonmonarchdagger.png", "demonkinglongsword.png", "chestprotector.png"]  # name of shop files
itemPos = [[i, j] for j in range(150, 651, 100) for i in range(376, 20 * 100, 100)]  # position of shop things
for i in range(len(itemNames)):
    itemImgs.append((image.load("assets/shop/" + itemNames[i]).convert(),
                     image.load("assets/shop/" + itemNames[i][:-4] + "IG.png").convert_alpha()))
shopSurf = Surface((1200, 800))
previewSurf = Surface((previewImg.get_width(), previewImg.get_height()))
itemDict = {
    # id: (name of item, item class, img, stat, statname amount of boost, cost)
    "0": ("Mana Potion", "Consumable", itemImgs[0][0], player.mana, "Mana", 50, 60),
    "1": ("Rasaka's Fang", "Weapon", itemImgs[1][0], player.strength, "Strength", 20, 100),
    "2": ("Knight Gauntlet", "Armour", itemImgs[2][0], player.health, "Health", 50, 70),
    "3": ("Red Knight's Helmet", "Armour", itemImgs[3][0], player.health, "Health", 60, 80),
    "4": ("Knight Killer", "Weapon", itemImgs[4][0], player.strength, "Strength", 40, 150),
    "5": ("Demon Monarch Dagger", "Weapon", itemImgs[5][0], player.strength, "Strength", 150, 300),
    "6": ("Demon King's Longsword", "Weapon", itemImgs[6][0], player.strength, "Strength", 80, 200),
    "7": ("High Knight's Chestplate", "Armour", itemImgs[7][0], player.health, "Health", 80, 100)
}
for i in range(len(itemPos)):
    itemRects.append((itemPos[i][0], itemPos[i][1], 83, 83))


def item_shop():
    global itemPreview, itemPN, clicked, invPreview
    for i in range(len(itemImgs)):
        shopSurf.blit(itemImgs[i][0], itemPos[i])
        if itemPreview:
            if clicked and Rect(itemPos[itemPN][0] - 370, itemPos[itemPN][1], 364, 200).collidepoint(mx, my):
                mixer.Sound.play(clicksfx)
                buy_item(itemPN)
            tempItem = itemDict.get(str(itemPN))
            shopSurf.blit(previewSurf, (itemPos[itemPN][0] - 370, itemPos[itemPN][1]))
            previewSurf.blit(previewImg, (0, 0))
            previewSurf.blit(itemDict.get(str(itemPN))[2], (33, 35))
            previewSurf.blit(fontSmall.render(tempItem[0], True, WHITE), (140, 29))
            previewSurf.blit(fontSmall.render(tempItem[1], True, WHITE), (215, 57))
            previewSurf.blit(fontSmall.render("Cost: " + str(tempItem[6]) + " coins", True, WHITE), (140, 84))
            previewSurf.blit(
                fontSmall.render("+" + str(tempItem[5]) + " " + tempItem[4], True, WHITE), (140, 110))
        if clicked:
            if itemPreview:
                if Rect(itemRects[i]).collidepoint(mx, my) or not Rect(itemRects[itemPN]).collidepoint(mx, my):
                    mixer.Sound.play(clicksfx)
                    clicked = False
                    itemPreview = False
                    continue
            else:
                if Rect(itemRects[i]).collidepoint(mx, my):
                    mixer.Sound.play(clicksfx)
                    clicked = False
                    itemPreview = True
                    invPreview = False
                    itemPN = i


def buy_item(itemid):
    global coins, weaponList
    coins = int(coins)
    if coins >= itemDict.get(str(itemid))[6]:
        coins -= itemDict.get(str(itemid))[6]
        weaponList.append([itemDict.get(str(itemid))[0], itemDict.get(str(itemid))[1],
                           str(itemDict.get(str(itemid))[5]), itemNames[itemid], "-"])
        weaponPics[str(len(weaponPics))] = (itemImgs[itemid][0], itemImgs[itemid][1])
        return True
    return False


invText = fontButtonTitle.render("INVENTORY", True, WHITE)
invbg = image.load("assets/menu/invbg.png").convert()
invtransbg = image.load("assets/menu/transparentbg.png").convert_alpha()
invTextSurf = Surface((330, 200))
invDescript = "Shows ALL player owned items. To get items, visit the store. To equip a purchased item: " \
              "Click on item to replace (in HUD) > right click on the item you want to select" \
              "         NOTE: You can only do this with weapons. Potions and Armour will equip to their own" \
              "slots."


def inventory_menu():
    global isInv
    keys = key.get_pressed()
    if keys[K_ESCAPE]:
        isInv = False
    screen.blit(invSurf, (0, 0))
    invSurf.blit(invbg, (0, 0))
    invSurf.blit(invtransbg, (365, 140))
    invSurf.blit(invText, (18, 130))
    invSurf.blit(invTextSurf, (18, 250))
    multiline_text(invTextSurf, invDescript, (10, 20), fontStory, WHITE)
    hud_menu(invSurf)
    inventory()
    back_button()


invSurf = Surface((1200, 800))
row1Height = 510
invPos = [[i, j] for j in range(150, 651, 100) for i in range(376, len(weaponList) + 11 * 100, 100)]
invRects = []
invPreview = False
invPN = 0
for i in range(len(invPos)):
    invRects.append((invPos[i][0], invPos[i][1], 83, 83))


def inventory():
    global invPreview, invPN, itemPreview, currArmour, currConsumable
    for i in range(len(weaponList)):
        screen.blit(weaponPics.get(str(i))[0], invPos[i])
        if clicked:
            if (Rect(invRects[i]).collidepoint(mx, my) or not Rect(invRects[invPN]).collidepoint(mx,
                                                                                                 my)) and invPreview:
                mixer.Sound.play(clicksfx)
                invPreview = False
                continue
            if Rect(invRects[i]).collidepoint(mx, my) and not invPreview:
                mixer.Sound.play(clicksfx)
                invPreview = True
                itemPreview = False
                invPN = i
        if mb[2]:
            itemPreview = False
            invPreview = False
            if Rect(invRects[i]).collidepoint(mx, my) and str(i) not in currWeapons:
                if weaponList[i][1] == "Weapon":
                    currWeapons[replaceNum] = str(i)
                elif weaponList[i][1] == "Armour":
                    currArmour[0] = weaponPics.get(str(i))[0]
                    currArmour[1] = weaponList[i][2]
                elif weaponList[i][1] == "Consumable":
                    currConsumable[0] = weaponPics.get(str(i))[0]
                    currConsumable[1], currConsumable[2] = weaponList[i][0], weaponList[i][2]
    if invPreview:
        screen.blit(previewSurf, (invPos[invPN][0] - 370, invPos[invPN][1]))
        previewSurf.blit(previewImg, (0, 0))
        previewSurf.blit(image.load("assets/shop/" + weaponList[invPN][3]).convert(), (33, 35))
        # add more item info
        previewSurf.blit(fontSmall.render(weaponList[invPN][0], True, WHITE), (140, 29))
        previewSurf.blit(fontSmall.render(weaponList[invPN][1], True, WHITE), (215, 57))
        weaponClass = weaponList[invPN][1]
        if weaponClass == "Weapon":
            weaponClass = "Strength"
        elif weaponClass == "Armour":
            weaponClass = "Vitality"
        else:
            weaponClass = "Attribute"
        previewSurf.blit(fontSmall.render(weaponClass + " + " + str(weaponList[invPN][2]), True, WHITE), (140, 84))


# CREDITS SCENE
creditsbg = image.load("assets/menu/creditsbg.png").convert()
creditsFont = font.Font("assets/fonts/credits.otf", 30)
creditsText = [image.load("assets/menu/credits" + str(i) + ".png").convert_alpha() for i in range(3)]
creditPos = [[190, 500], [90, 580], [143, 660]]


def game_credits():
    global isCred
    keys = key.get_pressed()
    if keys[K_ESCAPE]:
        isCred = False
    screen.blit(creditsbg, (0, 0))
    for i in range(len(creditsText)):
        screen.blit(creditsText[i], creditPos[i])
    back_button()
    

guideimg = image.load("assets/menu/guidebg.png").convert()
    

def guide_menu():
    global isGuide
    keys = key.get_pressed()
    if keys[K_ESCAPE]:
        isGuide = False
    screen.blit(guideimg, (0, 0))


# BACK BUTTON FOR STATS, SHOP, INVENTORY, CREDITS
backText = fontButtons.render("BACK", True, WHITE)
backRect = Rect(2, 742, 95, 50)


def back_button():
    global isStat, isShop, isInv, isCred, isGuide
    screen.blit(transform.scale(buttonImg, (105, 55)), (2, 740))
    screen.blit(backText, (backRect[0] + 12, backRect[1] + 7))
    if backRect.collidepoint(mx, my) and clicked:
        mixer.Sound.play(clicksfx)
        isStat, isShop, isInv, isCred, isGuide = False, False, False, False, False


# PANELS & TEXT FOR SCENE 0 (INTRO)
s1text = [fontMed.render("He reached his breaking point", True, BLACK),
          fontMed.render("Death was imminent.", True, BLACK)]
s1TextLoc = [(300, 360), (390, 550)]

s1alpha = 0
shot0 = 0
s0panels = [image.load("assets/panelimgs/death1.png").convert_alpha(),
            image.load("assets/panelimgs/death2.png").convert_alpha()]


def scene0():
    global cutscene, skip, s1alpha, login, shot0
    cutscene = True
    if skip and shot0 < len(s0panels):
        skip = False
        shot0 += 1
        s1alpha = 0
        welcome = image.load("assets/panelimgs/welcome.png").convert_alpha()
        if shot0 == len(s0panels):
            screen.fill(BLACK)
            screen.blit(welcome, (320, 220))
            display.update()
            ttime.sleep(3)
            screen.fill(BLACK)
            login = True  # starting login phase
    for i in range(len(s0panels)):
        if shot0 == i:
            cutscene = True
            if s1alpha < 255:
                s1alpha += 8
            panelbg.set_alpha(int(s1alpha))
            s0panels[i].set_alpha(int(s1alpha))
            screen.blit(panelbg, (-200, 0))
            screen.blit(s0panels[i], (250, -10))
            screen.blit(s1text[i], s1TextLoc[i])


d0alpha = 0
shot1 = 0
shotList1 = [image.load("assets/panelimgs/dungeon1.png").convert_alpha()]
d0text = [fontMed.render("Enter the first dungeon...", True, (55, 115, 177))]
panelbg = image.load("assets/panelimgs/panelbg.png").convert()
d0TextLoc = [(330, 650)]


def dungeon0():
    global cutscene, d0alpha, skip, isBattle, accumCoins
    if skip:
        isBattle = True
        accumCoins = 0
    for i in range(len(shotList1)):
        if shot1 == i:
            cutscene = True
            if d0alpha < 255:
                d0alpha += 5
            panelbg.set_alpha(int(d0alpha))
            shotList1[i].set_alpha(int(d0alpha))
            screen.blit(panelbg, (-200, 0))
            screen.blit(shotList1[i], (250, -10))
            screen.blit(d0text[i], d0TextLoc[i])


panelList = []
with open("assets/txtfiles/panels.txt", "r") as panelFile:
    panels = panelFile.readlines()
for i in range(len(panels)):
    panels[i] = panels[i].strip()
    panelList.append(image.load("assets/panelimgs/" + panels[i]).convert_alpha())
newPanel = panelList[currDungeon]
alphaval = 0


def make_scene():
    global cutscene, skip, panelList, alphaval, newPanel, isBattle, accumCoins
    cutscene = True
    if skip:
        skip = False
        if currDungeon < 9:
            newPanel = panelList[currDungeon + 1]
        alphaval = 0
        isBattle = True
        accumCoins = 0
        player.strength = int(weaponList[int(player.selWeapon)][2]) + strength
    if alphaval < 255:
        alphaval += 8
    newPanel.set_alpha(int(alphaval))
    screen.blit(panelbg, (-200, 0))
    screen.blit(newPanel, (250, -10))


dungeonDict = {
    "0": dungeon0,
    "1": make_scene,
    "2": make_scene,
    "3": make_scene,
    "4": make_scene,
    "5": make_scene,
    "6": make_scene,
    "7": make_scene,
    "8": make_scene,
    "9": make_scene,
}

fontTitle = font.Font("assets/fonts/titlefont1.otf", 300)

rewardSurf = surface.Surface((1200, 800))
winbg = image.load("assets/menu/winscreen.png").convert()
losebg = image.load("assets/menu/losescreen.png").convert()
wintext = fontTitle.render("VICTORY", True, WHITE)
losetext = fontTitle.render("DEFEAT", True, WHITE)


def give_rewards(win):
    global coins, points
    coins = int(coins)
    points = int(points)
    if win:
        coins += int(accumCoins)
        points += int((currDungeon + 1) * 3)
    else:
        coins += int(accumCoins) // 2
        points += int((currDungeon + 1) * 2) // 2


coinIncrease = 0
pointIncrease = 0


def reward_screen():
    global coinIncrease, pointIncrease, isReward, isWin
    screen.blit(rewardSurf, (0, 0))
    rewardSurf.blit(winbg, (0, 0))
    rewardSurf.blit(wintext, (10, 530))
    rewardSurf.blit(invtransbg, (400, -100))
    screen.blit(fontMed.render("REWARDS", True, WHITE), (420, 20))
    screen.blit(fontRewards.render(str(coinIncrease) + " GOLD COINS", True, WHITE), (420, 70))
    screen.blit(fontRewards.render(str(pointIncrease) + " SKILL POINTS", True, WHITE), (420, 100))
    if coinIncrease < int(accumCoins):
        coinIncrease += 1
    if pointIncrease < (currDungeon + 1) * 3:
        pointIncrease += 1
    if clicked:
        mixer.Sound.play(clicksfx)
        isReward = False
        isWin = False
        coinIncrease = 0
        pointIncrease = 0
        give_rewards(True)


def lose_screen():
    global coinIncrease, pointIncrease, isReward
    screen.blit(rewardSurf, (0, 0))
    rewardSurf.blit(losebg, (0, 0))
    rewardSurf.blit(losetext, (10, 530))
    rewardSurf.blit(invtransbg, (400, -100))
    screen.blit(fontMed.render("REWARDS", True, WHITE), (420, 20))
    screen.blit(fontRewards.render(str(coinIncrease) + " GOLD COINS", True, WHITE), (420, 70))
    screen.blit(fontRewards.render(str(pointIncrease) + " SKILL POINTS", True, WHITE), (420, 100))
    if coinIncrease < int(accumCoins) // 2:
        coinIncrease += 1
    if pointIncrease < ((currDungeon + 1) * 2) // 2:
        pointIncrease += 1
    if clicked:
        mixer.Sound.play(clicksfx)
        isReward = False
        coinIncrease = 0
        pointIncrease = 0
        give_rewards(False)


def end_screen(win):
    screen.blit(rewardSurf, (0, 0))
    if win:
        reward_screen()
    else:
        lose_screen()


def player_login():
    global username, password, login
    screen.fill(BLACK)
    if loginStep == 0:
        asknametext = fontMed.render("What is your name?", True, WHITE)
        screen.blit(asknametext, (410, 300))
        usernametext = fontMed.render(username, True, WHITE)
        screen.blit(usernametext, (610 - len(username) * 10, 350))
    else:
        askpasstext = fontMed.render("What is your code?", True, WHITE)
        screen.blit(askpasstext, (415, 300))
        passwordtext = fontMed.render(password, True, WHITE)
        screen.blit(passwordtext, (610 - len(password) * 10, 350))


# dungeonTile = image.load("assets/dungeontile1.jpg").convert()
dungeonSize = 128
wall2d = [[0 for i in range(dungeonSize)] for j in range(dungeonSize)]
dungeonSurf = Surface((2400, 1600))

for i in range(dungeonSize - 63):
    wall2d[0][i] = 1
    wall2d[i][0] = 1
    wall2d[dungeonSize - 64][i] = 1
    wall2d[i][dungeonSize - 64] = 1


def make_walls(mywalls):
    myRects = []
    for row in range(len(mywalls)):
        for col in range(len(mywalls)):
            if mywalls[row][col] == 1:
                myRects.append(Rect(col * 16 + 35, row * 16 + 165, 16, 16))
    return myRects


walls = make_walls(wall2d)
surfX, surfY = 0, 0

wall = []
wallName = [("assets/tileset/walls/wall" + (str(i)) + ".png") for i in range(3)]
image_load(False, wall, wallName)

wallTop = []
wallTopName = [("assets/tileset/walls/walltop" + (str(i)) + ".png") for i in range(3)]
image_load(False, wallTop, wallTopName)

wallSide = []
wallSideName = [("assets/tileset/walls/wallsidemid" + (str(i)) + ".png") for i in range(2)]
image_load(False, wallSide, wallSideName)

wallSideTop = []
wallSideTopName = [("assets/tileset/walls/wallsidetop" + (str(i)) + ".png") for i in range(2)]
image_load(False, wallSideTop, wallSideTopName)

floorTiles = []
floorTilesName = [("assets/tileset/Floors/floor" + str(i) + ".png") for i in range(8)]
image_load(False, floorTiles, floorTilesName)


def define_walls(wallList, ws):
    for w in wallList:
        if w[1] == 165:
            if w[0] == 35:
                ws.blit(wallSideTop[0], (w[0], w[1] - 16))
            elif w[0] == 1059:
                ws.blit(wallSideTop[1], (w[0], w[1] - 16))
            if w[0] < 1043:
                ws.blit(wall[1], (w[0] + 16, w[1]))
                ws.blit(wallTop[1], (w[0] + 16, w[1] - 16))
        elif w[1] == 1189:
            if w[0] < 1043:
                ws.blit(wall[1], (w[0] + 16, w[1]))
                ws.blit(wallTop[1], (w[0] + 16, w[1] - 16))
        if w[0] == 35:
            ws.blit(wallSide[0], w.topleft)
        elif w[0] == 1059:
            ws.blit(wallSide[1], w.topleft)


wallSurf = Surface((2400, 1600))
define_walls(walls, wallSurf)
wallSurf.set_colorkey(BLACK)


def define_floor(bg):
    for x in range(0, 1008, 16):
        for y in range(0, 1008, 16):
            isBroken = randint(0, 10)
            randTile = 0
            if isBroken == 1:
                randTile = randint(1, 7)
            bg.blit(floorTiles[randTile], (x, y))


backgroundSurf = Surface((1008, 1008))
define_floor(backgroundSurf)
levelOverTimer = 0


def dungeon_battle(ds):
    global isDungeon, levelOverTimer, dead
    isDungeon = True
    screen.blit(ds, (surfX, surfY))
    ds.fill((0, 0, 0))
    ds.blit(backgroundSurf, (51, 181))
    ds.blit(wallSurf, (0, 0))
    draw_fountain(ds, fountainCount)
    spawn_enemy(allEnemies[currDungeon])
    update_enemy()
    player.move_player()
    player.equip_weapon()
    player.update()
    player.player_attack()
    player.damage_indicator()
    stat_bar()
    skillbar(screen)
    storybar()
    if dead != (0, 0):
        death_anim(dead)
    if activeSkill != -1:
        screen.blit(transform.scale(skillPics.get(str(currSkills[activeSkill])), (83, 83)), (1100, 700))
        skillDict.get(str(activeSkill))()
    if enemyCount <= 0:
        update_boss()
    if player.health <= 0:
        dead = [player.posx, player.posy]
        if levelOverTimer > 50:
            levelOverTimer = 0
            player.damaged = False
            return False
        levelOverTimer += 1
    if gg == False:
        display.flip()


boss = Boss(allBosses[currDungeon][0], allBosses[currDungeon][1], allBosses[currDungeon][2],
            allBosses[currDungeon][3], allBosses[currDungeon][4], allBosses[currDungeon][5], allBosses[currDungeon][6])
bossgroup.add(boss)

rankList = ["E-rank Hunter", "D-rank Hunter", "C-rank Hunter", "B-rank Hunter", "A-rank Hunter",
            "S-rank Hunter", "SS-rank Hunter", "SSS-rank Hunter", "National-rank Hunter", "Shadow Monarch",
            "Shadow Monarch"]
gg = False


def dungeon_reset(complete=False):
    global currDungeon, isMenu, isBattle, isDungeon, surfX, \
        surfY, mainBlit, enemyCount, spawned, currStory, \
        strength, isWin, title, level, gg, activeArmour, activePotion
    if currDungeon < 9 or complete == False:
        if complete:
            isWin = True
            currDungeon += 1
            title = rankList[currDungeon]
            statTexts[1] = statFont.render(title, True, WHITE)
            level = currDungeon
            statTexts[0] = statFont.render(str(level), True, WHITE)
        else:
            isWin = False
        
        for e in enemygroup:
            e.kill()
        for b in bossgroup:
            b.kill()
        
        isMenu = True
        mainBlit = True
        isBattle = False
        isDungeon = False
        player.posx, player.posy = 600, 400
        player.rect = (player.posx, player.posy, 40, 40)
        player.dir = [True, False, False, False]
        player.selWeapon = currWeapons[0]
        player.currWeaponImg[0] = transform.rotate(weaponPics.get(player.selWeapon)[1], player.weaponAngle[0])
        player.currWeaponImg[1] = transform.rotate(transform.flip(weaponPics.get(player.selWeapon)[1], False, True),
                                                   player.weaponAngle[1])
        player.strength = 0
        player.health = health
        player.mana = mana
        player.damaged = False
        player.attacking = False
        activeArmour, activePotion = False, False
        surfX, surfY = 0, 0
        enemyCount = dungeonEnemies[currDungeon]
        spawned = 0
        with open("assets/txtfiles/story.txt") as storyFile:
            storyList = storyFile.readlines()
            currStory = str(storyList[currDungeon])
        boss = Boss(allBosses[currDungeon][0], allBosses[currDungeon][1], allBosses[currDungeon][2],
                    allBosses[currDungeon][3], allBosses[currDungeon][4], allBosses[currDungeon][5], allBosses[currDungeon][6])
        bossgroup.add(boss)
        mixer.music.load(trackList[0])
        mixer.music.play(-1)
    elif complete:
        gg = True


healthText = fontSmall.render("Health", True, WHITE)
manaText = fontSmall.render("Mana", True, WHITE)


def stat_bar():
    draw.rect(screen, paletteList[0], (0, 0, 297, 75))
    # health
    draw.rect(screen, paletteList[1],
              (10, 10, 201 / (health / player.health if player.health != 0 else 1) if health != player.health else 200, 20))
    # mana
    draw.rect(screen, paletteList[2], (10, 40, 201 / (mana / player.mana if player.mana != 0 else 200), 20))
    # health and mana text
    screen.blit(healthText, (220, 10))
    screen.blit(manaText, (220, 38))


# SPRINT SKILL
def skill0():
    player.speed = agility + 8-(currDungeon//2) + 3
    player.mana -= 1


# BERSERK SKILL
def skill1():
    player.strength = int((int(weaponList[int(player.selWeapon)][2]) + strength) * 1.5)
    player.mana -= 1


# HEAL SKILL
def skill2():
    global activeSkill
    if player.health < health:
        player.health += 1
        player.mana -= 2
    else:
        activeSkill = -1


# GHOST SKILL
ghost = [0, True]


def skill3():
    if ghost[1]:
        ghost[0] = player.health
    ghost[1] = False
    player.health = 99999999999999999
    player.mana -= 1


skillDict = {
    "0": skill0,
    "1": skill1,
    "2": skill2,
    "3": skill3
}


activeSkill = -1


skillRects = [(20, 705, 83, 83), (110, 705, 83, 83),
              (200, 705, 83, 83), (290, 705, 83, 83)]
skillsText = fontSmall.render("Skills", True, WHITE)
weaponRects = [(420, 705, 83, 83), (510, 705, 83, 83)]
weaponText = fontSmall.render("Weapons", True, WHITE)
consumableRects = [(640, 705, 83, 83)]
consumableText = fontSmall.render("Consumable", True, WHITE)
armourRects = [(765, 705, 83, 83)]
armourText = fontSmall.render("Armour", True, WHITE)

activeArmour, activePotion = False, False
targetDmg = 0


def skillbar(win):
    global activeSkill, clicked, activeArmour, activePotion, targetDmg
    draw.rect(win, paletteList[0], (0, 670, 1200, 180))
    # skills
    win.blit(skillsText, (170, 675))
    if player.mana <= 0:
        if activeSkill == 0:
            player.speed = agility
        elif activeSkill == 1:
            player.strength = int(weaponList[int(player.selWeapon)][2]) + strength
        elif activeSkill == 3:
            player.health = ghost[0]
        activeSkill = -1
        ghost[1] = True
    if player.health > 0:
        for i in range(len(skillRects)):
            if Rect(skillRects[i]).collidepoint(mx, my) and clicked:
                if activeSkill != -1:
                    if activeSkill == 0:
                        player.speed = agility
                    elif activeSkill == 1:
                        player.strength = int(weaponList[int(player.selWeapon)][2]) + strength
                    elif activeSkill == 3:
                        player.health = ghost[0]
                    activeSkill = -1
                    ghost[1] = True
                else:
                    activeSkill = i
    for s in range(len(currSkills)):
        win.blit(transform.scale(skillPics.get(str(currSkills[s])), (83, 83)), skillRects[s][:2])
    # weapons
    win.blit(weaponText, (467, 675))
    for i in range(len(weaponRects)):
        if Rect(weaponRects[i]).collidepoint(mx, my) and clicked:
            player.selWeapon = currWeapons[i]
            player.currWeaponImg[0] = transform.rotate(weaponPics.get(player.selWeapon)[1], player.weaponAngle[0])
            player.currWeaponImg[1] = transform.rotate(transform.flip(weaponPics.get(player.selWeapon)[1], False, True),
                                                       player.weaponAngle[1])
            player.strength = int(weaponList[int(player.selWeapon)][2]) + strength
            mixer.Sound.play(equipsfx[randint(0, 4)])
    for w in range(len(currWeapons)):
        win.blit(weaponPics.get(str(currWeapons[w]))[0], weaponRects[w][:2])
    # consumables
    win.blit(consumableText, (628, 675))
    if currConsumable[0] is not None:
        win.blit(currConsumable[0], consumableRects[0][:2])
        if Rect(consumableRects[0]).collidepoint(mx, my) and clicked and activePotion == False:
            if player.mana < mana - 50:
                activePotion = True
                player.mana += int(currConsumable[2])
    # armour
    win.blit(armourText, (771, 675))
    if currArmour[0] is not None:
        win.blit(currArmour[0], armourRects[0][:2])
        if Rect(armourRects[0]).collidepoint(mx, my) and clicked and activeArmour == False:
            activeArmour = True
            targetDmg = int(allEnemies[currDungeon][2]) // 2
        if activeArmour:
            for e in enemygroup:
                if e.dmg > targetDmg:
                    e.dmg -= 1


with open("assets/txtfiles/story.txt") as storyFile:
    storyList = storyFile.readlines()
    currStory = str(storyList[currDungeon])


def storybar():
    draw.rect(screen, paletteList[0], (330, 0, 870, 74))
    multiline_text(screen, currStory, (333, 3), fontStory, WHITE)


ggtext = [fontMed.render("", True, BLACK),
          fontMed.render("", True, BLACK)]

ggalpha = 0
ggshot = 0
ggpanels = [image.load("assets/panelimgs/gg0.png").convert_alpha(),
            image.load("assets/panelimgs/gg1.png").convert_alpha(),
            image.load("assets/panelimgs/gg2.png").convert_alpha(),
            image.load("assets/panelimgs/gg3.png").convert_alpha(),
            image.load("assets/panelimgs/gg4.png").convert_alpha(),
            image.load("assets/panelimgs/gg5.png").convert_alpha(),
            image.load("assets/panelimgs/gg6.png").convert_alpha(),
            image.load("assets/panelimgs/gg7.png").convert_alpha()]


def GGscene():
    global cutscene, skip, ggalpha, ggshot, running, isDungeon
    if gg:
        cutscene = True
        if skip and ggshot < len(ggpanels):
            isDungeon = False
            skip = False
            ggshot += 1
            ggalpha = 0
            if ggshot == len(ggpanels):
                running = False
        for i in range(len(ggpanels)):
            if ggshot == i:
                cutscene = True
                if ggalpha < 240:
                    ggalpha += 8
                ggpanels[i].set_alpha(int(ggalpha))
                screen.blit(panelbg, (-200, 0))
                screen.blit(ggpanels[i], (250, -10))


def typing():
    global username, password, login, isDungeon, loginStep, usernameText
    if login:
        if evt.key == K_BACKSPACE:  # slicing string if backspace
            if loginStep == 0 and len(username) > 0:
                username = username[:-1]
            elif loginStep == 1 and len(password) > 0:
                password = password[:-1]
        elif loginStep == 0 and len(username) < 12:  # take normal keyboard input
            username += evt.unicode
        elif loginStep == 1 and len(password) < 12:
            password += evt.unicode
        if evt.key == K_RETURN:
            if loginStep == 0:
                loginStep = 1
            else:
                with open("assets/txtfiles/config.txt", "w") as loginFile:
                    loginFile.write(username)
                    loginFile.write(password)
                    usernameText = statFont.render(username, True, WHITE)
                login = False
                ttime.sleep(1)
                screen.fill(BLACK)
                isDungeon = True


running = True
isReward = False
event.set_allowed([QUIT, MOUSEBUTTONUP, KEYDOWN, KEYUP, cooldown])

while running:
    clicked = False
    skip = False
    oldHealth = player.health
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONUP:
            clicked = True
            if cutscene:
                skip = True
                mixer.Sound.play(clicksfx)
        if evt.type == KEYDOWN:
            typing()
            if evt.key == K_ESCAPE and (isInv or isShop or isStat or isGuide or isCred):
                mainBlit = True
        if evt.type == cooldown:
            player.hitLimit = True
            player.atkCooldown = True
            enemySpawn = True
            if player.mana <= mana - 10 and activeSkill == -1:
                player.mana += 10
            for e in enemygroup:
                e.hitLimit = True
            if enemyCount <= 0:
                for b in bossgroup:
                    b.isReady = True
                    b.getCoords = True
                    b.hitLimit = True
                    mixer.Sound.play(magicsfx)
                    
    if os.stat("assets/txtfiles/config.txt").st_size == 0:
        scene0()
        if login:
            player_login()
    
    if isDungeon:
        if isBattle:
            if dungeon_battle(dungeonSurf) == False:
                dungeon_reset()
                isReward = True
        else:
            dungeonDict[str(currDungeon)]()
    
    if isMenu:
        if isReward:
            end_screen(isWin)
        elif isStat:
            stat_menu()
        elif isShop:
            shop_menu()
        elif isInv:
            inventory_menu()
        elif isCred:
            game_credits()
        elif isGuide:
            guide_menu()
        else:
            main_menu()
    
    GGscene()
    
    display.flip()
    clock.tick(FPS)

with open("assets/txtfiles/progress.txt", "w") as progressFile:
    progressFile.write(str(isDungeon) + "\n" + str(currDungeon) + "\n" + str(isMenu) + "\n" + str(points))
with open("assets/txtfiles/selected.txt", "w") as selectFile:
    selectFile.write(str(currWeapons[0]) + "," + str(currWeapons[1]))
    selectFile.write("\n")
    for i in range(len(currSkills)):
        selectFile.write(str(currSkills[i]) + ("," if i != len(currSkills) - 1 else ""))
with open("assets/txtfiles/stats.txt", "w") as statFile:
    for i in range(len(statVars)):
        statFile.write(str(statVars[i]) + "\n")
with open("assets/txtfiles/shop.txt", "w") as shopFile:
    shopFile.write(str(coins))
with open("assets/txtfiles/inventory.txt", "w") as invFile:
    for i in range(len(weaponList)):
        for j in range(len(weaponList[i])):
            invFile.write(weaponList[i][j] + "\n")
quit()
