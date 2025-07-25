import pygame

# 1. init (contohnya: map mobile legends)
# 2. user input, database input (contohnya: tombol atas atau bawah)
# 3. update asset
# 3. render ke display
# ----------------------------------

## 1. init
pygame.init()
# variable running game
isRun = True

# membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang)) 

# object game
# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 10

while isRun:
	pygame.time.delay(10)
	# 2. user input, database input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRun = False
			
	# ambil semua keyboard press
	keys = pygame.key.get_pressed()
	
	# ambil ke kiri
	if keys[pygame.K_LEFT] and x > 0:
			x -= speed
			
	# ambil ke kanan		
	if keys[pygame.K_RIGHT] and x < window_lebar - lebar:
			x += speed
			
	# ambil ke atas
	if keys[pygame.K_UP] and y > 0:
			y -= speed
			
	# ambil ke bawah
	if keys[pygame.K_DOWN] and y < window_panjang - panjang:
			y += speed
			
	# 3. update asset
	window.fill((255,255,255))
	pygame.draw.rect(window,(255,120,0),(x,y,lebar,panjang))
	
	# 4. render ke display
	pygame.display.update()

pygame.quit()



































