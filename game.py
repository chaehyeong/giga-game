import pygame
import sys

pygame.init()

# 게임 창 크기
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("2D Pixel-style Game")

# 배경 이미지 로드
background_image = pygame.image.load("bg_img.png")  # 배경 이미지 파일 경로에 맞게 수정

# 배경 이미지의 위치
background_x = -1200
background_y = -900

# 캐릭터 초기 위치
player_x, player_y = window_width // 2, window_height // 2

# 캐릭터 이동 속도
player_speed = 8

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.blit(background_image, (background_x, background_y))

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
    if player_x >= 700 and keys[pygame.K_RIGHT] and background_x > -2400:
        background_x -= 8
    if player_y <= 100 and keys[pygame.K_UP] and background_y < 0:
        background_y += 8
    if player_y >= 500 and keys[pygame.K_DOWN] and background_y > -1800:
        background_y -= 8
 
    # 캐릭터 그리기 사각형
    pygame.draw.rect(window, (255, 0, 0), (player_x, player_y, 20, 20))

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 설정
    pygame.time.Clock().tick(60)