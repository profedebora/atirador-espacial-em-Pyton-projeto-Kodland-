import pygame
import random

# Inicializa o PyGame
pygame.init()

# Configurações da tela
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Space Shooter')

# Carrega os assets
imagem_jogador = pygame.image.load('assets/spaceship.png')
imagem_inimigo = pygame.image.load('assets/enemy.png')
imagem_bala = pygame.image.load('assets/bullet.png')
imagem_fundo = pygame.image.load('assets/background.jpg')

# Variáveis do jogador
jogador_x, jogador_y = largura_tela // 2, altura_tela - 100
velocidade_jogador = 5
balas = []

# Variáveis dos inimigos
inimigos = []
velocidade_inimigo = 2
numero_inimigos = 5

# Função para adicionar inimigos
def adicionar_inimigos():
    global inimigos
    inimigos = []
    for _ in range(numero_inimigos):
        x = random.randint(0, largura_tela - imagem_inimigo.get_width())
        y = random.randint(-150, -50)
        inimigos.append({'x': x, 'y': y})

# Funções do jogo
def movimentar_jogador():
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador_x -= velocidade_jogador
    if teclas[pygame.K_RIGHT] and jogador_x < largura_tela - imagem_jogador.get_width():
        jogador_x += velocidade_jogador
    tela.blit(imagem_jogador, (jogador_x, jogador_y))

def movimentar_inimigos():
    for inimigo in inimigos:
        inimigo['y'] += velocidade_inimigo
        if inimigo['y'] > altura_tela:
            inimigo['x'] = random.randint(0, largura_tela - imagem_inimigo.get_width())
            inimigo['y'] = random.randint(-150, -50)
        tela.blit(imagem_inimigo, (inimigo['x'], inimigo['y']))

def atirar_bala():
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        balas.append({'x': jogador_x + imagem_jogador.get_width() // 2 - imagem_bala.get_width() // 2, 'y': jogador_y})

def movimentar_balas():
    for bala in balas[:]:
        bala['y'] -= 10
        if bala['y'] < 0:
            balas.remove(bala)
        tela.blit(imagem_bala, (bala['x'], bala['y']))

def verificar_colisao():
    global inimigos
    for bala in balas[:]:
        for inimigo in inimigos[:]:
            if (inimigo['x'] < bala['x'] < inimigo['x'] + imagem_inimigo.get_width() and
                inimigo['y'] < bala['y'] < inimigo['y'] + imagem_inimigo.get_height()):
                inimigos.remove(inimigo)
                balas.remove(bala)
                break

# Adiciona inimigos iniciais
adicionar_inimigos()

# Loop principal do jogo
rodando = True
while rodando:
    tela.blit(imagem_fundo, (0, 0))  # Limpa a tela com o fundo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    movimentar_jogador()
    movimentar_inimigos()
    atirar_bala()
    movimentar_balas()
    verificar_colisao()

    pygame.display.update()

pygame.quit()