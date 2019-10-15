import pygame

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMEHLO = (255, 0, 0)

cenario = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2],
    [2, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2],
    [2, 0, 2, 0, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2],
    [2, 0, 2, 0, 0, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2],
    [2, 0, 2, 0, 0, 0, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2],
    [2, 0, 2, 0, 0, 0, 1, 2, 2, 1, 1, 1, 1, 2, 1, 2],
    [2, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2],
    [2, 0, 2, 0, 0, 0, 1, 2, 2, 1, 1, 1, 1, 2, 1, 2],
    [2, 0, 2, 0, 0, 0, 2, 0, 0, 2, 1, 1, 1, 2, 1, 2],
    [2, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 1, 1, 2, 1, 2],
    [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]

pygame.init()
screen = pygame.display.set_mode((800, 600), 0)
corpo_x = 400
corpo_y = 300
tamanho = int(600 / 16)
corpo_linha = 2
corpo_coluna = 1
corpo_x1 = 300
corpo_y1 = 400
corpo_linha1 = 5
corpo_coluna1 = 5
tamanho1 = int(600 / 16)
intencao_linha = 1
intencao_coluna = 1
pontos = 0
abertura = 0
vel_abertura = 0.1
VELOCIDADE_BOCA = 0.2



def desenhar_pacman(tela):
    global abertura, vel_abertura, VELOCIDADE_BOCA
    raio = int(tamanho / 2)
    corpo_x = corpo_coluna * tamanho + raio
    corpo_y = corpo_linha * tamanho + raio
    fundo_boca = (corpo_x, corpo_y)
    labio_inferior = (corpo_x + raio, corpo_y + abertura)
    labio_superior = (corpo_x + raio, corpo_y - abertura)
    abertura += vel_abertura
    if abertura > raio:
        abertura = VELOCIDADE_BOCA
    if abertura <= 0:
        abertura = VELOCIDADE_BOCA

    olho_raio = int(raio / 10)
    olho_x = corpo_x + int(raio / 6)
    olho_y = corpo_y - int(2 * raio / 3)
    pygame.draw.circle(tela, AMARELO, (corpo_x, corpo_y), raio, 0)
    pontos_boca = [fundo_boca, labio_inferior, labio_superior]
    pygame.draw.polygon(tela, PRETO, pontos_boca, 0)
    pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

def cenario_calcular_regras(cen):
    global corpo_coluna, corpo_linha, intencao_coluna, intencao_linha, pontos
    if 0<= intencao_linha < 16 and 0<= intencao_coluna < 16 and cen[intencao_linha][intencao_coluna] != 2:
        corpo_linha = intencao_linha
        corpo_coluna = intencao_coluna
        if cen[intencao_coluna][intencao_linha] == 1:
            pontos += 1
            print(pontos)
            cen[corpo_linha][corpo_coluna] = 0
    else:
        intencao_coluna = corpo_coluna
        intencao_linha = corpo_linha

'''PAC DOISS
    def desenhar_pacman1(tela):
    raio1 = int(tamanho / 2)
    corpo_x1 = corpo_coluna1 * tamanho1 + raio1
    corpo_y1 = corpo_linha1 * tamanho1 + raio1
    fundo_boca1 = (corpo_x1, corpo_y1)
    labio_inferior1 = (corpo_x1 + raio1, corpo_y1)
    labio_superior1 = (corpo_x1 + raio1, corpo_y1 - raio1)
    olho_raio1 = int(raio1 / 10)
    olho_x1 = corpo_x1 + int(raio1 / 6)
    olho_y1 = corpo_y1 - int(2 * raio1 / 3)
    pygame.draw.circle(tela, VERMEHLO, (corpo_x1, corpo_y1), raio1, 0)
    pontos_boca1 = [fundo_boca1, labio_inferior1, labio_superior1]
    pygame.draw.polygon(tela, PRETO, pontos_boca1, 0)
    pygame.draw.circle(tela, PRETO, (olho_x1, olho_y1), olho_raio1, 0)
'''
def desenhar_cenario(tela, cena, tamanho):
    for linha, linha_conteudo in enumerate(cena):
        for coluna, coluna_conteudo in enumerate(linha_conteudo):
            x = coluna * tamanho
            y = linha * tamanho
            cor = PRETO
            if coluna_conteudo == 2:
                cor = AZUL
            r = pygame.Rect((x, y), (tamanho, tamanho))
            pygame.draw.rect(tela, cor, r, 0)
            pygame.draw.circle(tela, AMARELO, (50, 50), 4,0)
            if coluna_conteudo == 1:
                ponto_x = int(x + tamanho/2)
                ponto_y = int(y + tamanho/2)
                ponto_raio = int(tamanho/10)
                pygame.draw.circle(tela, AMARELO, (ponto_x, ponto_y), ponto_raio, 0)


while True:
    #calcular REgras
    cenario_calcular_regras(cenario)
    # Desenha tela
    screen.fill(PRETO)
    desenhar_cenario(screen, cenario, tamanho)
    desenhar_pacman(screen)
    #desenhar_pacman1(screen)
    pygame.display.update()

    # Captura eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                intencao_coluna += 1
            if e.key == pygame.K_LEFT:
                intencao_coluna -= 1
            if e.key == pygame.K_UP:
                intencao_linha -= 1
            if e.key == pygame.K_DOWN:
                intencao_linha += 1

            if e.key == pygame.K_d:
                corpo_coluna1 += 1
            if e.key == pygame.K_a:
                corpo_coluna1 -= 1
            if e.key == pygame.K_w:
                corpo_linha1 -= 1
            if e.key == pygame.K_s:
                corpo_linha1 += 1



