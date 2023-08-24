import pygame
import sys
import time

pygame.init()
pygame.display.set_caption("2D Pixel-style Game")

## 변수 ##

# 게임 창 크기
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))

# 배경 로드
bg_1 = pygame.image.load("배경/bg_1.jpg")
bg_2 = pygame.image.load("배경/bg_2.jpg")
bg_3 = pygame.image.load("배경/bg_3.jpg")
bg_4 = pygame.image.load("배경/bg_4.jpg")
bg_5 = pygame.image.load("배경/bg_5.jpg")
bg_6 = pygame.image.load("배경/bg_6.jpg")
bg_7 = pygame.image.load("배경/bg_7.jpg")
bg_8 = pygame.image.load("배경/bg_8.jpg")
bg_9 = pygame.image.load("배경/bg_9.jpg")
bg_10 = pygame.image.load("배경/bg_10.jpg")
bg_11 = pygame.image.load("배경/bg_11.jpg")
bg_12 = pygame.image.load("배경/bg_12.jpg")
bg_13 = pygame.image.load("배경/bg_13.jpg")
bg_14 = pygame.image.load("배경/bg_14.jpg")
bg_15 = pygame.image.load("배경/bg_15.jpg")
bg_16 = pygame.image.load("배경/bg_16.jpg")

# 이미지 로드
coin = pygame.image.load("광산/coin.png")
wood = pygame.image.load("벌목장/wood.png")
lumberCamp = pygame.image.load("벌목장/ruin.png")

# 배경 이미지의 위치
background_x = -1200
background_y = -900

# 건물의 위치 (앞으로 모든 건물의 위치는 다음의 변수를 기준으로 함)
camp_x = 360
camp_y = 260

# 캐릭터 초기 위치
player_x, player_y = window_width // 2, window_height // 2

# 캐릭터 이동 속도
player_speed = 8

# 폰트
font = pygame.font.SysFont(None, 20, False, False)

# 생산물
money = 100 # 광산
tree = 0 # 벌목장
startTime = time.time()

## 함수 ##

# 텍스트 넣기
def printText(contents, r, g, b, x, y): # 내용, 색깔(r, g, b), 좌표(x, y)
    text = font.render(contents, True, (r, g, b))
    window.blit(text, (x, y))

# 광산
def mine():
    global money
    global startTime
    window.blit(coin, (10, 10))
    if money < 103:
        time.time()
        if time.time() - 3 >= startTime:
            startTime += 3
            money += 1

# 벌목
def logging():
    global tree
    global startTime
    global lumberCamp
    lumberCamp = pygame.image.load("벌목장/Camp1.png")
    window.blit(wood, (90, 10))
    if tree < 3:
        time.time()
        if time.time() - 3 >= startTime:
            startTime += 3
            tree += 1

## 메인 코드 ##

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 배경
    window.blit(bg_1, (background_x, background_y))
    window.blit(bg_2, (background_x + 800, background_y))
    window.blit(bg_3, (background_x + 1600, background_y))
    window.blit(bg_4, (background_x + 2400, background_y))
    window.blit(bg_5, (background_x, background_y + 600))
    window.blit(bg_6, (background_x + 800, background_y + 600))
    window.blit(bg_7, (background_x + 1600, background_y + 600))
    window.blit(bg_8, (background_x + 2400, background_y + 600))
    window.blit(bg_9, (background_x, background_y + 1200))
    window.blit(bg_10, (background_x + 800, background_y + 1200))
    window.blit(bg_11, (background_x + 1600, background_y + 1200))
    window.blit(bg_12, (background_x + 2400, background_y + 1200))
    window.blit(bg_13, (background_x, background_y + 1800))
    window.blit(bg_14, (background_x + 800, background_y + 1800))
    window.blit(bg_15, (background_x + 1600, background_y + 1800))
    window.blit(bg_16, (background_x + 2400, background_y + 1800))

    # 건물
    window.blit(lumberCamp, (camp_x, camp_y))

    mine()
    printText(str(money) + "/103", 255, 255, 255, 30, 12)

    if money >= 103:
        logging()
        printText(str(tree) + "/3", 255, 255, 255, 110, 12)    

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 100:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 700:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 100:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < 500:
        player_y += player_speed
    
    #화면 움직임
    if player_x <= 100 and keys[pygame.K_LEFT] and background_x < 0:
        background_x += 8
        camp_x += 8
    if player_x >= 700 and keys[pygame.K_RIGHT] and background_x > -2400:
        background_x -= 8
        camp_x -= 8
    if player_y <= 100 and keys[pygame.K_UP] and background_y < 0:
        background_y += 8
        camp_y += 8
    if player_y >= 500 and keys[pygame.K_DOWN] and background_y > -1800:
        background_y -= 8
        camp_y -= 8
 
    # 캐릭터 그리기 사각형
    pygame.draw.rect(window, (255, 0, 0), (player_x, player_y, 20, 20))

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 설정
    pygame.time.Clock().tick(60)