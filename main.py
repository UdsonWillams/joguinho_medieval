"""
Criado por :Dhiego Viana Machado
            Diego da Cunha
            Udson Willams

DIAMONDS FROM THE KING

"""
import pygame
import sys
from random import randint

pygame.init()
janela = pygame.display.set_mode((640, 480))
pygame.display.set_caption("DIAMONS OF THE KING")
clock = pygame.time.Clock()

velocidade_personagem = 5
x_doPersonagem = 120
y_doPersonagem = 250
vidas = 2

velocidade1_esqueleto = 4
velocidade2_esqueleto = 4
x_esqueleto0 = 125
y_esqueleto0 = 230

x_esqueleto1 = 200
y_esqueleto1 = 140

x_esqueleto2 = 300
y_esqueleto2 = 230

x_esqueleto3 = 400
y_esqueleto3 = 140

x_esqueleto4 = 470
y_esqueleto4 = 230

x_esqueleto5 = 550
y_esqueleto5 = 140

velocidade_monstro1 = 10
xMonstro1 = 200
yMonstro1 = 280

magox = 550
magoy = 240
vidasmago = 5

# Personagens ------------------------------------------------------------------------
# heroi
personagem = pygame.image.load("heroi//personagemdireira1.png")
personagem_direita = [pygame.image.load("heroi//personagemdireira1.png"),
                      pygame.image.load("heroi//personagemdireira2.png"),
                      pygame.image.load("heroi//personagemdireira3.png"),
                      pygame.image.load("heroi//personagemdireira4.png"),
                      pygame.image.load("heroi//personagemdireira5.png"),
                      pygame.image.load("heroi//personagemdireira6.png"),
                      pygame.image.load("heroi//personagemdireira7.png"),
                      pygame.image.load("heroi//personagemdireira8.png"),
                      pygame.image.load("heroi//personagemdireira9.png")]

personagem_esquerda = [pygame.image.load("heroi//personagemesquerda1.png"),
                       pygame.image.load("heroi//personagemesquerda2.png"),
                       pygame.image.load("heroi//personagemesquerda3.png"),
                       pygame.image.load("heroi//personagemesquerda4.png"),
                       pygame.image.load("heroi//personagemesquerda5.png"),
                       pygame.image.load("heroi//personagemesquerda6.png"),
                       pygame.image.load("heroi//personagemesquerda7.png"),
                       pygame.image.load("heroi//personagemesquerda8.png"),
                       pygame.image.load("heroi//personagemesquerda9.png")]

personagem_cima = [pygame.image.load("heroi//personagemcima1.png"),
                   pygame.image.load("heroi//personagemcima2.png"),
                   pygame.image.load("heroi//personagemcima3.png"),
                   pygame.image.load("heroi//personagemcima4.png"),
                   pygame.image.load("heroi//personagemcima5.png"),
                   pygame.image.load("heroi//personagemcima6.png"),
                   pygame.image.load("heroi//personagemcima7.png"),
                   pygame.image.load("heroi//personagemcima8.png"),
                   pygame.image.load("heroi//personagemcima9.png")]

personagem_baixo = [pygame.image.load("heroi//personagembaixo1.png"),
                    pygame.image.load("heroi//personagembaixo2.png"),
                    pygame.image.load("heroi//personagembaixo3.png"),
                    pygame.image.load("heroi//personagembaixo4.png"),
                    pygame.image.load("heroi//personagembaixo5.png"),
                    pygame.image.load("heroi//personagembaixo6.png"),
                    pygame.image.load("heroi//personagembaixo7.png"),
                    pygame.image.load("heroi//personagembaixo8.png"),
                    pygame.image.load("heroi//personagembaixo9.png")]
# Outros personagens
mago = pygame.image.load("personagens//mago.png")
princesa = pygame.image.load("personagens//princesa.png")
esqueleto0 = pygame.image.load("personagens//esqueletocima1.png")
esqueleto1 = pygame.image.load("personagens//esqueletobaixo1.png")
esqueleto2 = pygame.image.load("personagens//esqueletocima1.png")
esqueleto3 = pygame.image.load("personagens//esqueletobaixo2.png")
esqueleto4 = pygame.image.load("personagens//esqueletocima2.png")
esqueleto5 = pygame.image.load("personagens//esqueletobaixo2.png")
pequeno_monstro1 = pygame.image.load('personagens//monstrinho.png')
guarda1 = pygame.image.load("personagens//guarda1.png")
guarda2 = pygame.image.load("personagens//guarda2.png")

# FUNDO E HISTORIA
inicio = pygame.image.load("historias_fundos//teladeinicio.png")
fundo = inicio
historia1 = pygame.image.load("historias_fundos//historia1.png")
historia2 = pygame.image.load("historias_fundos//historia2.png")
historia3 = pygame.image.load("historias_fundos//historia3.png")
historia4 = pygame.image.load("historias_fundos//historia4.png")
historia5 = pygame.image.load("historias_fundos//historia5.png")
historia6 = pygame.image.load("historias_fundos//historia6.png")
historia7 = pygame.image.load("historias_fundos//historia7.png")
historiacastelo = pygame.image.load("historias_fundos//historiacastelo.png")
historiaprincesa = pygame.image.load("historias_fundos//historiaprincesa.png")
jogadorvenceu = pygame.image.load("historias_fundos//jogadorvenceu.png")
fimdejogo = pygame.image.load("historias_fundos//fimdejogo.png")
fundo1 = pygame.image.load("historias_fundos//fundo1.png")
fundo2 = pygame.image.load("historias_fundos//fundo2.png")
fundo3 = pygame.image.load("historias_fundos//fundo3.png")
fundo4 = pygame.image.load("historias_fundos//fundo4.png")
fundo5 = pygame.image.load("historias_fundos//fundo5.png")
abismo = pygame.image.load("historias_fundos//abismo.png")
entradacastelo = pygame.image.load("historias_fundos//entradacastelo.png")
taverna = pygame.image.load("historias_fundos//taverna.png")

flechaX = 599
flechaY = - 30
flecha = pygame.image.load("flecha.png")
velocidade_flecha = 10
movimentoflecha = False

font = pygame.font.SysFont(('arial black'), 10)
txt_vida = font.render("VIDAS:   ", True, (255, 255, 255), (0, 0, 0))
pos_texto_vida = txt_vida.get_rect()
pos_texto_vida = (20, 20)

esquerda = False
direita = False
cima = False
baixo = False
andar = 0

pygame.mixer.init()
pygame.mixer.music.load('Flagonlord.wav')
pygame.mixer.music.play(-1)


def desenhos():
    global andar

    janela.blit(fundo, (0, 0))
    if andar + 1 >= 25:
        andar = 0
    if esquerda:
        janela.blit(personagem_esquerda[andar // 3], (x_doPersonagem, y_doPersonagem))
        andar += 1
    elif direita:
        janela.blit(personagem_direita[andar // 3], (x_doPersonagem, y_doPersonagem))
        andar += 1
    elif cima:
        janela.blit(personagem_cima[andar // 3], (x_doPersonagem, y_doPersonagem))
        andar += 1
    elif baixo:
        janela.blit(personagem_baixo[andar // 3], (x_doPersonagem, y_doPersonagem))
        andar += 1
    else:
        janela.blit(personagem, (x_doPersonagem, y_doPersonagem))
        andar = 0
    if fundo == fundo2:
        janela.blit(guarda1, (253, 54))
        janela.blit(guarda2, (332, 54))
    janela.blit(txt_vida, pos_texto_vida)
    pygame.display.update()


def desenhar_esqueletos(esqueleto1, x_esqueleto, y_esqueleto):
    janela.blit(esqueleto1, (x_esqueleto, y_esqueleto))
    pygame.display.update()


def textos(txt, localx, localy, tamanhofonte):
    txt = txt  ##### armazena o texto
    fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
    fontesys = pygame.font.SysFont(fonte, tamanhofonte)  ##### usa a fonte padrão
    txttela = fontesys.render(txt, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
    janela.blit(txttela, (localx, localy))  ##### coloca na posição 50,900 (tela FHD)
    pygame.display.update()

    # def textodiferente():
    font = pygame.font.SysFont(('arial black'), 20)
    txt_casa2 = font.render("APERTE F PARA ENTRAR", True, (255, 255, 255), (0, 0, 0))
    pos_texto_casa2 = txt_vida.get_rect()
    pos_texto_casa2 = (20, 90)
    janela.blit(txt_casa2, pos_texto_casa2)
    pygame.display.update()


janela_aberta = True
while janela_aberta:
    clock.tick(27)
    # laço para fechar a janela caso o jogador clique no X da tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_a]:
        x_doPersonagem -= velocidade_personagem
        esquerda = True
        direita = False
        cima = False
        baixo = False

    elif comandos[pygame.K_d]:
        x_doPersonagem += velocidade_personagem
        direita = True
        esquerda = False
        cima = False
        baixo = False

    elif comandos[pygame.K_w]:
        y_doPersonagem -= velocidade_personagem
        direita = False
        esquerda = False
        baixo = False
        cima = True

    elif comandos[pygame.K_s]:
        y_doPersonagem += velocidade_personagem
        direita = False
        esquerda = False
        baixo = True
        cima = False

    else:
        esquerda = False
        direita = False
        cima = False
        baixo = False
        walkCount = 0
    desenhos()

    if y_doPersonagem > 479:
        fundo = abismo  # if para que se o jogador sair por baixo da tela ele morra
        vidas = 0
        pygame.display.update()

    if fundo == fundo1:
        if comandos[pygame.K_f]:
            movimentoflecha = True
            flechaX = x_doPersonagem + 30
            flechaY = y_doPersonagem + 20
        if movimentoflecha:
            janela.blit(flecha, (flechaX, flechaY))
            flechaX += velocidade_flecha
        if flechaX > 600:  # movimento da flecha
            movimentoflecha = False
            pygame.display.update()
        pygame.display.update()
        if y_doPersonagem < 230:  # colisao com a cerca
            y_doPersonagem = 229

        if x_doPersonagem > 65 and x_doPersonagem < 180:
            if y_doPersonagem < 238:
                font_casa1 = pygame.font.SysFont(('arial black'), 15)
                txt_casa1 = font_casa1.render("NAO POSSO IR PRA CASA TENHO DE PROCURAR A PRINCESA!", True,
                                              (255, 255, 255), (0, 0, 0))
                pos_texto_casa1 = txt_vida.get_rect()
                pos_texto_casa1 = (100, 200)
                janela.blit(txt_casa1, pos_texto_casa1)
                pygame.display.update()

    if fundo == fundo2:
        if comandos[pygame.K_f]:
            movimentoflecha = True
            flechaX = x_doPersonagem + 30
            flechaY = y_doPersonagem + 20
        if movimentoflecha:
            janela.blit(flecha, (flechaX, flechaY))
            flechaX += velocidade_flecha
        if flechaX > 600:  # movimento da flecha
            movimentoflecha = False
            pygame.display.update()
        pygame.display.update()
        if y_doPersonagem < 90:  # colisao com a casa e o castelo
            y_doPersonagem = 94
        if x_doPersonagem > 4 and x_doPersonagem < 60:
            if y_doPersonagem < 98:
                fonte1casa = pygame.font.SysFont(('arial black'), 20)
                txt_casa2 = fonte1casa.render("APERTE F PARA ENTRAR", True, (255, 255, 255), (0, 0, 0))
                pos_texto_casa2 = txt_vida.get_rect()
                pos_texto_casa2 = (20, 90)
                janela.blit(txt_casa2, pos_texto_casa2)
                pygame.display.update()

                if comandos[pygame.K_f]:
                    fundo = taverna
                    y_doPersonagem = -200

        # if x_doPersonagem < 245 and y_doPersonagem > 150: #
        #    x_doPersonagem == 240
        if x_doPersonagem > 260 and x_doPersonagem < 332:  # ativa o texto dos guardas
            if y_doPersonagem < 135:
                fonte = pygame.font.SysFont(('arial black'), 30)
                txt_castelo = fonte.render("ENTRADA PROIBIDA", True, (255, 255, 255), (0, 0, 0))
                pos_texto_castelo = txt_vida.get_rect()
                pos_texto_castelo = (220, 50)
                janela.blit(txt_castelo, pos_texto_castelo)
                pygame.display.update()
                # txt = 'ENTRADA PROIBIDA'
                # tamanhofonte = 33
                # localx = 220  # if para mostrar entrada proibida na frente da entrada do castelo
                # localy = 50
                # textos(txt, localx, localy, tamanhofonte)
            if y_doPersonagem < 110:
                fundo = entradacastelo
                y_doPersonagem = -2000
                pygame.display.update()
        if x_doPersonagem > 330 and x_doPersonagem < 550:
            if y_doPersonagem > 140 and y_doPersonagem < 250:  # este if é para colisao com as casas do meio da segunda tela
                x_doPersonagem = x_doPersonagem - 5
                y_doPersonagem = y_doPersonagem - 5
        if x_doPersonagem > 380 and x_doPersonagem < 600:
            if y_doPersonagem > 330 and y_doPersonagem < 480:  # este if é para colisao com as casas de baixo da segunda tela
                x_doPersonagem = x_doPersonagem - 5
                y_doPersonagem = y_doPersonagem - 5

    if fundo == fundo3:
        if comandos[pygame.K_f]:
            movimentoflecha = True
            flechaX = x_doPersonagem + 30
            flechaY = y_doPersonagem + 20
        if movimentoflecha:
            janela.blit(flecha, (flechaX, flechaY))
            flechaX += velocidade_flecha
        if flechaX > 600:  # movimento da flecha
            movimentoflecha = False
            pygame.display.update()
        pygame.display.update()
        if y_doPersonagem < 140:
            y_doPersonagem = y_doPersonagem + 5  # colisao do personagem com a mata
        if y_doPersonagem > 230:
            y_doPersonagem = y_doPersonagem - 5

        desenhar_esqueletos(esqueleto0, x_esqueleto0, y_esqueleto0)
        desenhar_esqueletos(esqueleto1, x_esqueleto1, y_esqueleto1)
        desenhar_esqueletos(esqueleto2, x_esqueleto2, y_esqueleto2)  # desenha os esqueletos
        desenhar_esqueletos(esqueleto3, x_esqueleto3, y_esqueleto3)
        desenhar_esqueletos(esqueleto4, x_esqueleto4, y_esqueleto4)
        desenhar_esqueletos(esqueleto5, x_esqueleto5, y_esqueleto5)
        # esqueleto0
        if y_esqueleto0 > 139:
            y_esqueleto0 -= velocidade1_esqueleto
        if y_esqueleto0 < 141:
            y_esqueleto0 = 230
            # esqueleto 1
        if y_esqueleto1 < 230:
            y_esqueleto1 += velocidade1_esqueleto
        if y_esqueleto1 > 229:
            y_esqueleto1 = 140
        # esqueleto2
        if y_esqueleto2 > 139:
            y_esqueleto2 -= velocidade1_esqueleto
        if y_esqueleto2 < 141:
            y_esqueleto2 = 230  # MOVIMENTAÇÃO DOS ESQUELETOS
        # esqueleto3
        if y_esqueleto3 < 230:
            y_esqueleto3 += velocidade2_esqueleto
        if y_esqueleto3 > 229:
            y_esqueleto3 = 140
        # esqueleto4
        if y_esqueleto4 > 139:
            y_esqueleto4 -= velocidade2_esqueleto
        if y_esqueleto4 < 141:
            y_esqueleto4 = 230
        # esqueleto5
        if y_esqueleto5 < 230:
            y_esqueleto5 += velocidade2_esqueleto
        if y_esqueleto5 > 229:
            y_esqueleto5 = 140
            # colisao com o esqueleto 0
        if x_doPersonagem > 100 and x_doPersonagem < 140:
            if y_doPersonagem > y_esqueleto0:
                x_doPersonagem = 35
                y_doPersonagem = 200
                vidas = vidas - 1
            # colisao com o esqueleto 1
        if x_doPersonagem > 185 and x_doPersonagem < 225:
            if y_doPersonagem < y_esqueleto1:
                x_doPersonagem = 35
                y_doPersonagem = 200
                vidas = vidas - 1
            # colisão com o esqueleto 2
        if x_doPersonagem > 270 and x_doPersonagem < 315:
            if y_doPersonagem > y_esqueleto1:
                x_doPersonagem = 35
                y_doPersonagem = 200
                vidas = vidas - 1
            # colisão com o esqueleto 3
        if x_doPersonagem > 365 and x_doPersonagem < 425:
            if y_doPersonagem < y_esqueleto1:
                x_doPersonagem = 35
                y_doPersonagem = 200
                vidas = vidas - 1
            # colisao com o esqueleto 4
        if x_doPersonagem > 445 and x_doPersonagem < 480:
            if y_doPersonagem > y_esqueleto1:
                x_doPersonagem = 35
                y_doPersonagem = 200
                vidas = vidas - 1
            # colisao com o esqueleto 5
        if x_doPersonagem > 530 and x_doPersonagem < 580:
            if y_doPersonagem < y_esqueleto1:
                x_doPersonagem = 35
                y_doPersonagem = 200
                vidas = vidas - 1
    if fundo == fundo4:
        velocidade_personagem = 4
        janela.blit(pequeno_monstro1, (xMonstro1, yMonstro1))
        pygame.display.update()
        if xMonstro1 > 199 and xMonstro1 < 400:
            xMonstro1 += velocidade_monstro1
            if xMonstro1 > 398:
                xMonstro1 = 200
        if x_doPersonagem < 10 + xMonstro1:
            if y_doPersonagem > 265 and y_doPersonagem < 300:
                x_doPersonagem = 300
                y_doPersonagem = 430
                vidas = vidas - 1
        if x_doPersonagem < 200:
            x_doPersonagem = 199
        if x_doPersonagem > 430:
            x_doPersonagem = 449
        if y_doPersonagem < 160:
            y_doPersonagem = 161
        if x_doPersonagem > 200 and x_doPersonagem < 430:
            if y_doPersonagem > 360 and y_doPersonagem < 390:
                y_doPersonagem = 391
                fontemago = pygame.font.SysFont(('arial black'), 20)
                txt_casamago = fontemago.render("APERTE F PARA ENTRAR", True, (255, 255, 255), (0, 0, 0))
                pos_texto_casamago = txt_vida.get_rect()
                pos_texto_casamago = (300, 395)
                janela.blit(txt_casamago, pos_texto_casamago)
                pygame.display.update()
                if comandos[pygame.K_f]:
                    y_doPersonagem = 340
        if x_doPersonagem > 360 and x_doPersonagem < 430:
            if y_doPersonagem < 180:
                fonteportacasamago = pygame.font.SysFont(('arial black'), 20)
                txt_casamagoentrar = fonteportacasamago.render("APERTE F PARA ENTRAR", True, (255, 255, 255), (0, 0, 0))
                pos_texto_casamagoentrar = txt_vida.get_rect()
                pos_texto_casamagoentrar = (330, 160)
                janela.blit(txt_casamagoentrar, pos_texto_casamagoentrar)
                pygame.display.update()
                if comandos[pygame.K_f]:
                    fundo = historia6
                    x_doPersonagem = 2000
    if fundo == fundo5:
        janela.blit(princesa, (320, 10))
        fonteprin = pygame.font.SysFont(('arial black'), 10)
        txt_daprin = fonteprin.render("Por favor, me ajude!!", True, (255, 255, 255), (0, 0, 0))
        pos_texto_prin = txt_vida.get_rect()
        pos_texto_prin = (360, 10)
        janela.blit(txt_daprin, pos_texto_prin)
        pygame.display.update()
        janela.blit(mago, (magox, magoy))
        pygame.display.update()
        if comandos[pygame.K_f]:
            movimentoflecha = True
            flechaX = x_doPersonagem + 30
            flechaY = y_doPersonagem + 20
        if movimentoflecha:
            janela.blit(flecha, (flechaX, flechaY))
            flechaX += velocidade_flecha
        if flechaX > 600:  # movimento da flecha
            movimentoflecha = False
            pygame.display.update()
        pygame.display.update()

        if flechaX > magox:
            if magoy - 5 < flechaY and magoy + 5 > flechaY:
                vidasmago = vidasmago - 1
                if vidasmago == 4:
                    magoy = randint(100, 200)
                if vidasmago == 3:
                    magoy = randint(380, 440)
                if vidasmago == 2:
                    magoy = randint(100, 200)
                if vidasmago == 1:
                    magoy = randint(300, 440)
                if vidasmago == 0:
                    fundo = jogadorvenceu
                    x_doPersonagem = 2000

    # para fazer a quantidade de vidas aparecer
    txt_vida = font.render("VIDAS:   " + str(vidas), True, (255, 255, 255), (0, 0, 0))
    # ifs com as mensagens ou entradas de lugares
    if fundo == inicio:
        x_doPersonagem = 50
        y_doPersonagem = 350
        if x_doPersonagem < 10:
            x_doPersonagem = 9
        if x_doPersonagem > 600:
            x_doPersonagem = 599
        if y_doPersonagem < 375:
            y_doPersonagem = 376
        if y_doPersonagem > 420:
            y_doPersonagem = 419
    # se fundo for igual ao inicio do jogo e se apertar Direita
    if fundo == inicio and comandos[pygame.K_RIGHT]:
        fundo = historia1
        x_doPersonagem = 2000
        pygame.display.update()
    # se fundo for igual a historia 1 e se apertar espaço
    if fundo == historia1 and comandos[pygame.K_SPACE]:
        x_doPersonagem = 2000
        fundo = historia2
        pygame.display.update()
    # se fundo for igual a historia 2 e se apertar Direita
    if fundo == historia2 and comandos[pygame.K_RIGHT]:
        x_doPersonagem = 2000
        fundo = historia3
        pygame.display.update()
    # se fundo for igual a historia 3 e se apertar espaço
    if fundo == historia3 and comandos[pygame.K_SPACE]:
        x_doPersonagem = 120
        y_doPersonagem = 250
        fundo = fundo1
        pygame.display.update()
    # entrada na taverna
    if fundo == taverna and comandos[pygame.K_SPACE]:
        fundo = fundo2
        pygame.display.update()
    # Entrada no castelo
    if fundo == entradacastelo and comandos[pygame.K_SPACE]:
        y_doPersonagem = 250
        fundo = fundo2
        pygame.display.update()
    # se fundo for igual a fim de jogo e se apertar a tecla R
    if fundo == fimdejogo and comandos[pygame.K_r]:
        fundo = fundo1
        x_doPersonagem = 120
        y_doPersonagem = 250
        vidas = 2
        pygame.display.update()
    # se fundo for igual a historia 4
    if fundo == historia4:
        x_doPersonagem = 2000
        if comandos[pygame.K_SPACE]:
            fundo = fundo3
            x_doPersonagem = 6
            y_doPersonagem = 220
            pygame.display.update()
    # se fundo for igual a historia 5
    if fundo == historia5:
        if comandos[pygame.K_SPACE]:
            fundo = fundo4
            x_doPersonagem = 300
            y_doPersonagem = 430
    # SE FUNDO FOR IGUAL A HISTORIA 6
    if fundo == historia6:
        if comandos[pygame.K_SPACE]:
            fundo = fundo5
            x_doPersonagem = 20
            y_doPersonagem = 240
    if fundo == jogadorvenceu:
        if comandos[pygame.K_SPACE]:
            fundo = historia7
    if fundo == historia7:
        if comandos[pygame.K_LEFT]:
            fundo = historiacastelo
        elif comandos[pygame.K_RIGHT]:
            fundo = historiaprincesa
    # se fundo for igual a fundo 1
    if fundo == fundo1:
        if x_doPersonagem < 4:
            x_doPersonagem = 5
        if x_doPersonagem > 600:
            fundo = fundo2
            x_doPersonagem = 6
            y_doPersonagem = 250
            flechaX = x_doPersonagem
    # se fundo for igual a fundo 2
    if fundo == fundo2:
        if x_doPersonagem < 3:
            fundo = fundo1
            x_doPersonagem = 600
        if x_doPersonagem > 610:
            fundo = historia4
            x_doPersonagem = 2000
    # se fundo for igual a fundo 3
    if fundo == fundo3:
        if x_doPersonagem < 3:
            fundo = fundo2
            x_doPersonagem = 600
        if x_doPersonagem > 610:
            fundo = historia5
            x_doPersonagem = 2000
    # se fundo for igual a abismo e voce estiver sem vidas
    if vidas < 1 and fundo != abismo:
        fundo = fimdejogo
        x_doPersonagem = 2000
        pygame.display.update()

pygame.quit()