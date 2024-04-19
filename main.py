from pyautogui import press, typewrite, pixel
from PIL import ImageGrab
from time import sleep

# Machine Settings OS: Windows 11 Resolution: 2560 x 1440
GAMELINK = "https://elgoog.im/dinosaur-game/"
OBJ_COLOR_LIGHT = (83, 83, 83)
OBJ_COLOR_DARK = (172, 172, 172)
# BG_COLOR_LIGHT = (255, 255, 255)
# BG_COLOR_DARK = (32, 33, 36)
CACTUS_BBOX = (750, 800, 950, 840) # (left_x, top_y, right_x, bottom_y)
BIRD_BBOX = (670, 660, 820, 685)

game_on = True


def object_detected(bird_object, cactus_object):
    for x in range(0,150):
        for y in range(0, 15):
            if bird_object.getpixel((x, y)) == (OBJ_COLOR_LIGHT) or bird_object.getpixel((x, y)) == (OBJ_COLOR_DARK):
                press("down")
                return
    for x in range(0,200):
        for y in range(0, 40):
            if cactus_object.getpixel((x, y)) == (OBJ_COLOR_LIGHT) or cactus_object.getpixel((x, y)) == (OBJ_COLOR_DARK):
                press("up")
                return
    return


## Open Chrome and navigate to game link
press("win")
sleep(2)
typewrite("Google Chrome")
sleep(2)
press("enter")
sleep(2)
typewrite(GAMELINK)
press("enter")

sleep(5)
press("up")
sleep(2)

## Play dinasour game
while game_on:
    cactus_box = ImageGrab.grab(bbox=CACTUS_BBOX)
    bird_box = ImageGrab.grab(bbox=BIRD_BBOX)

    object_detected(bird_object=bird_box, cactus_object=cactus_box)
    
    if pixel(x=893 ,y=483) == (83, 83, 83) or pixel(x=893 ,y=483) == (172, 172, 172):
        game_on = False
        print("Game Over")
        # press("up") # Keep replaying game


# Get Color at curser location - Ctrl+C to exit
# while True:
#     sleep(5)
#     current_position = position()
#     print(position())
#     print(pixel(x=current_position.x, y=current_position.y))