import pygame
import sys

pygame.init()

# 게임 창 크기
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("2D Pixel-style Game")

# 배경 이미지 로드
background_image = pygame.image.load("background.png")  # 배경 이미지 파일 경로에 맞게 수정

# 배경 이미지의 위치
background_x = -1600
background_y = 0

# 캐릭터 초기 위치
player_x, player_y = window_width // 2, 360

# 캐릭터 이동 속도
player_speed = 5

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
    """
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    """
    
    #화면 움직임
    if player_x <= 100 and keys[pygame.K_LEFT] and background_x < 0:
        background_x += 4
    if player_x >= 700 and keys[pygame.K_RIGHT]:
        background_x -= 4
    """
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        background_x += 4
    if keys[pygame.K_RIGHT]:
        background_x -= 4
    if keys[pygame.K_UP]:
        background_y += 4
    if keys[pygame.K_DOWN]:
        background_y -= 4
    """
 
    # 캐릭터 그리기 사각형
    pygame.draw.rect(window, (255, 0, 0), (player_x, player_y, 20, 20))

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 설정
    pygame.time.Clock().tick(60)