from graphics import*
from ctypes import*
import random

## abrindo arquivo 
bibli = CDLL("./bibli.dll")

## Contando qual fase
qualfase = 1
velocinimigo = 0
inimigostotais = 0
## Qual a fase máxima?
try:
    fasearq = open("ultimafase.txt","r+")
    fasearq.close()
except FileNotFoundError:
    fasearq = open("ultimafase.txt","w")
    fasearq.close()
    fasearq = open("ultimafase.txt","r+")
    fasearq.write("0")
    fasearq.close()

def main():
    ## Início
    win = GraphWin("ReiDaPradaria", 900, 600, autoflush=False)
    win.setBackground("sienna4")

    ## Tutorial
    def tutorial():
        tutor = Text(Point(450,100),"TUTORIAL")
        tutor.setSize(36)
        tutor.draw(win)
        setas = Text(Point(500,200),"Use as setas ← ↑ → ↓ para \nmovimentar seu personagem, \ne Espaço para atirar!")
        setas.draw(win)
        bonequinho = Image(Point(300,200),"boneco.gif")
        bonequinho.draw(win)
        cofretexto = Text(Point(300,300),"Não deixe que os inimigos\n encostem no cofre, se não\n o jogo acaba e você perde.")
        cofretexto.draw(win)
        cofre = Image(Point(470,300),"cofre.gif")
        cofre.draw(win)
        tiro = Text(Point(500,400),"Para isso, atire e\n derrote todos os inimigos! \n Cuidado que a cada três fases, aparece um \n inimigo novo (max. 3).")
        tiro.draw(win)
        bonequinho1 = Image(Point(200,400),"boneco.gif")
        bonequinho1.draw(win)
        tiro1 = Circle(Point(230,400),3)
        tiro1.setFill("black")
        tiro1.draw(win)
        inimigo = Image(Point(260,400),"inimigo.gif")
        inimigo.draw(win)
        sair = Text(Point(450,500),"Sair.")
        sair.setSize(16)
        sair.draw(win)
        seta = Polygon(Point(410,500),Point(400,495),Point(400,505))
        seta.setFill("black")
        seta.draw(win)
        while True:
            a = win.getKey()
            if a=="Return":
                tutor.undraw()
                setas.undraw()
                bonequinho.undraw()
                bonequinho1.undraw()
                cofretexto.undraw()
                cofre.undraw()
                tiro.undraw()
                tiro1.undraw()
                inimigo.undraw()
                sair.undraw()
                seta.undraw()
                break
        menu()

    ## Jogo
    def inicio():
        global qualfase
        global velocinimigo
        global inimigostotais

        #Fundo
        fundo = Image(Point(400,300),"fundo.gif")
        fundo.draw(win)

        ## Perder/ganhar o jogo
        cofre = Rectangle(Point(380,280),Point(420,320))
        cofreimg = Image(Point(400,300),"cofre.gif")
        cofreimg.draw(win)
        ## Jogador 
        bonecocabeca = Circle(Point(400,250),15)
        bonecodesenho = Image(Point(400,250),"boneco.gif")
        bonecodesenho.draw(win)
        bonecoarma = Line(Point(415,250),Point(420,250))
        bonecoarmacima = Line(Point(400,235),Point(400,230))
        bonecoarmabaixo = Line(Point(400,265),Point(400,270))
        bonecoarmaesquerda = Line(Point(385,250),Point(380,250))
        boneco = [bonecocabeca, bonecoarma, bonecoarmacima, bonecoarmabaixo, bonecoarmaesquerda, bonecodesenho]
        bonecocirc = [bonecocabeca, bonecoarma, bonecoarmacima, bonecoarmabaixo, bonecoarmaesquerda]
        bonecoarmas = [bonecoarma]

        
        ## Menu ao lado direito da tela
        titulo1 = Image(Point(852,45),"ReidaPradaria2.gif")
        titulo1.draw(win)
        linha = Rectangle(Point(801,94),Point(900,600))
        linha.setFill("sienna4")
        linha.draw(win)
        vidas2 = Text(Point(830,120),"VIDAS")
        vidas2.setStyle("bold")
        vidas2.draw(win)
        vidasboneco =[]
        oi = 0
        quantinimigos = 10+inimigostotais
        inimigosrestantes = Text(Point(850,300),"INIMIGOS\nRESTANTES\n{}".format(quantinimigos))
        inimigosrestantes.setStyle("bold")
        inimigosrestantes.draw(win)
        fase = Text(Point(850,500),"FASE\n{}".format(qualfase))
        fase.setStyle("bold")
        fase.draw(win)
        while oi<80:
            vidaboneco = Image(Point(820+oi,170),"boneco.gif")
            vidaboneco.draw(win)
            vidasboneco.append(vidaboneco)
            oi+=23
        ## Spawn inimigo
        a = 1
        b = 380
        c = 10
        ## NA LISTA xESTÃO TODOS OS SPAWNS POSSIVEIS PROS INIMIGOS (LEMBRAR!!!!!!)
        spawns = []
        while a<=12:
            b = b + bibli.criaspawnx(a)
            c = c + bibli.criaspawny(a)
            spawn = Circle(Point(b,c),2)
            spawns.append(spawn)
            a+=1


        ## INIMIGO (por enquanto uma bola)
        spawnaleatorio = random.randint(0, len(spawns))
        spawninimigo = spawns[spawnaleatorio-1]
        inimigosvelo = []
        inimigo = Circle(spawninimigo.getCenter(),15)
        inimigoimagem = Image(spawninimigo.getCenter(),"inimigo.gif")
        inimigoimagem.draw(win)
        inimigosvelo.append(inimigo)
        inimigoscomimagem = [inimigo,inimigoimagem]
        if qualfase>=3:
            spawnaleatorio = random.randint(0, len(spawns))
            spawninimigo = spawns[spawnaleatorio-1]
            inimigosvelo2 = []
            inimigo2 = Circle(spawninimigo.getCenter(),15)
            inimigoimagem2 = Image(spawninimigo.getCenter(),"inimigo2.gif")
            inimigoimagem2.draw(win)
            inimigosvelo2.append(inimigo2)
            inimigoscomimagem2 = [inimigo2,inimigoimagem2]
        if qualfase>=6:
            spawnaleatorio = random.randint(0, len(spawns))
            spawninimigo = spawns[spawnaleatorio-1]
            inimigosvelo3 = []
            inimigo3 = Circle(spawninimigo.getCenter(),15)
            inimigoimagem3 = Image(spawninimigo.getCenter(),"inimigo2.gif")
            inimigoimagem3.draw(win)
            inimigosvelo3.append(inimigo3)
            inimigoscomimagem3 = [inimigo3,inimigoimagem3]


        ## Movimento do boneco (é um def pra simplificar)
        def movimentoboneco():
            for i in boneco:
                if tecla == "Up":
                    i.move(0,-10)
                    try:
                        bonecoarma.undraw()
                        bonecoarmabaixo.undraw()
                        bonecoarmaesquerda.undraw()
                        bonecoarmacima.draw(win)
                        ## Isso é para saber de onde o tiro irá sair, em qual lado.
                        bonecoarmas.clear()
                        bonecoarmas.append(bonecoarmacima)
                    except GraphicsError:
                        continue
                if tecla =="Down":
                    i.move(0,10)
                    try:
                        bonecoarma.undraw()
                        bonecoarmacima.undraw()
                        bonecoarmaesquerda.undraw()
                        bonecoarmabaixo.draw(win)
                        bonecoarmas.clear()
                        bonecoarmas.append(bonecoarmabaixo)
                    except GraphicsError:
                        continue
                if tecla == "Left":
                    i.move(-10,0)
                    try:
                        bonecoarma.undraw()
                        bonecoarmacima.undraw()
                        bonecoarmabaixo.undraw()
                        bonecoarmaesquerda.draw(win)
                        bonecoarmas.clear()
                        bonecoarmas.append(bonecoarmaesquerda)
                    except GraphicsError:
                        continue
                if tecla == "Right":
                    i.move(10,0)
                    try:
                        bonecoarmabaixo.undraw()
                        bonecoarmacima.undraw()
                        bonecoarmaesquerda.undraw()
                        bonecoarma.draw(win)
                        bonecoarmas.clear()
                        bonecoarmas.append(bonecoarma)
                    except GraphicsError:
                        continue
        
        ## While True (onde o jogo inteiro acontece)
        while True:
            try:
                inimigos = [inimigo, inimigo2, inimigo3]
                inimigoindex = inimigos.index(inimigo)
                inimigoindex2 = inimigos.index(inimigo2)
                inimigoindex3 = inimigos.index(inimigo3)
            except UnboundLocalError:
                try:
                    inimigos = [inimigo,inimigo2]
                    inimigoindex = inimigos.index(inimigo)
                    inimigoindex = inimigos.index(inimigo2)
                except UnboundLocalError:
                    inimigos = [inimigo]
                    inimigoindex = inimigos.index(inimigo)

            update(100)
            tecla = win.checkKey()
        ## Movimento do Inimigo
            def movimentoinimigo():
                global velocinimigo
                for i in inimigosvelo:
                    praqueladoX = i.getCenter().getX()
                    praqueladoY = i.getCenter().getY()
                oioi = 0
                oioi = oioi + bibli.movinimigo(c_double(praqueladoX),c_double(praqueladoY))
                if oioi == 1:
                    for j in inimigoscomimagem:
                        j.move(0,0.1+velocinimigo)
                    oioi = 0
                elif oioi == 2:
                    for j in inimigoscomimagem:
                        j.move(0,-0.1-velocinimigo)
                    oioi = 0
                elif oioi == 3:
                    for j in inimigoscomimagem:
                        j.move(0.1+velocinimigo,0)
                    oioi = 0
                else:
                    for j in inimigoscomimagem:
                        j.move(-0.1-velocinimigo,0)
                    oioi = 0
                try:
                    for k in inimigosvelo2:
                        praqueladoX2 = k.getCenter().getX()
                        praqueladoY2 = k.getCenter().getY()
                    oioi1 = 0
                    oioi1 = oioi1 + bibli.movinimigo(c_double(praqueladoX2),c_double(praqueladoY2))
                    if oioi1 == 1:
                        for m in inimigoscomimagem2:
                            m.move(0,0.1+velocinimigo)
                        oioi1 = 0
                    elif oioi1 == 2:
                        for m in inimigoscomimagem2:
                            m.move(0,-0.1-velocinimigo)
                        oioi1 = 0
                    elif oioi1 == 3:
                        for m in inimigoscomimagem2:
                            m.move(0.1+velocinimigo,0)
                        oioi1 = 0
                    else:
                        for m in inimigoscomimagem2:
                            m.move(-0.1-velocinimigo,0)
                        oioi1 = 0
                except NameError:
                    pass
                try:
                    for l in inimigosvelo3:
                        praqueladoX3 = l.getCenter().getX()
                        praqueladoY3 = l.getCenter().getY()
                    oioi2 = 0
                    oioi2 = oioi2 + bibli.movinimigo(c_double(praqueladoX3),c_double(praqueladoY3))
                    if oioi2 == 1:
                        for n in inimigoscomimagem3:
                            n.move(0,0.1+velocinimigo)
                        oioi2 = 0
                    elif oioi2 == 2:
                        for n in inimigoscomimagem3:
                            n.move(0,-0.1-velocinimigo)
                        oioi2 = 0
                    elif oioi2 == 3:
                        for n in inimigoscomimagem3:
                            n.move(0.1+velocinimigo,0)
                        oioi2 = 0
                    else:
                        for n in inimigoscomimagem3:
                            n.move(-0.1-velocinimigo,0)
                        oioi2 = 0
                except NameError:
                    pass

        ##
            movimentoboneco()
            movimentoinimigo()
        
        ## Perdendo(talvez)
        
        ## def() para ajudar na simplificação do código
            def apagar():
                for i in boneco:
                    i.undraw()
                for j in spawns:
                    j.undraw()
                for k in vidasboneco:
                    k.undraw()
                for l in inimigosvelo:
                    l.undraw()
                for m in inimigoscomimagem:
                    m.undraw()
                try:
                    for n in inimigoscomimagem2:
                        n.undraw()
                    for o in inimigoscomimagem3:
                        o.undraw()
                except NameError:
                     pass
            def apagar2():
                linha.undraw()
                apagar()
                fundo.undraw()
                inimigo.undraw()
                inimigoimagem.undraw()
                cofre.undraw()
                cofreimg.undraw()
                titulo1.undraw()
                vidas2.undraw()
                inimigosrestantes.undraw()
                fase.undraw()
            
            for im in inimigos:
                um = im.getCenter().getX()+15
                dois = im.getCenter().getY()+15
                umneg = im.getCenter().getX()-15
                doisneg = im.getCenter().getY()-15
            teste = 0
            teste = teste + bibli.resumocodigo(c_double(um),c_double(dois),c_double(umneg),c_double(doisneg))
            if teste == 1:
                apagar2()
                qualfase = 1
                teste = 0            
                perdeu()
                break
        
        ## Boneco Perdendo vida
            boneco1 = bonecocabeca.getCenter().getX()
            boneco2 = bonecocabeca.getCenter().getY()
            if umneg<=boneco1<=um and doisneg<=boneco2<=dois:
                for i in boneco:
                    i.undraw()
                bonecocabeca = Circle(Point(400,250),15)
                bonecodesenho = Image(Point(400,250),"boneco.gif")
                bonecodesenho.draw(win)
                bonecoarma = Line(Point(415,250),Point(420,250))
                bonecoarmacima = Line(Point(400,235),Point(400,230))
                bonecoarmabaixo = Line(Point(400,265),Point(400,270))
                bonecoarmaesquerda = Line(Point(385,250),Point(380,250))
                boneco = [bonecocabeca, bonecoarma, bonecoarmacima, bonecoarmabaixo, bonecoarmaesquerda, bonecodesenho]
                bonecocirc = [bonecocabeca, bonecoarma, bonecoarmacima, bonecoarmabaixo, bonecoarmaesquerda]
                bonecoarmas = [bonecoarma]
                for i in bonecocirc:
                    i.setOutline("black")
                try:
                    ultimavidaboneco = vidasboneco[-1]
                    ultimavidabonecoindex = vidasboneco.index(ultimavidaboneco)
                    ultimavidaboneco.undraw()
                    vidasboneco.pop(ultimavidabonecoindex)
                except IndexError:
                    apagar2()
                    qualfase = 1            
                    perdeu()
                    break
        ## Atirando
            if tecla == "space":
                for j in bonecoarmas:
                    j
                tiro = Circle(Point(j.getP2().getX(),j.getP2().getY()),3)
                tiro.setFill("black")
                tiro.draw(win)
                ## E agora para o tiro sair para o lado certo? *thinking*
                ## CONSEGUI!!!!!!!
                tempo=0
                while tempo<170:
                    movimentoinimigo()
                    update(100)
                    ##
                    if j == bonecoarmaesquerda:
                        tiro.move(-5,0)
                        tempo+=1
                    elif j == bonecoarma:
                        tiro.move(5,0)
                        tempo+=1
                    elif j == bonecoarmacima:
                        tiro.move(0,-5)
                        tempo+=1
                    else:
                        tiro.move(0,5)
                        tempo+=1
                    ## tiro pegando
                    if inimigo.getCenter().getX()-15<=tiro.getCenter().getX()<=inimigo.getCenter().getX()+15:
                        if inimigo.getCenter().getY()-15<=tiro.getCenter().getY()<=inimigo.getCenter().getY()+15:
                            inimigo.undraw()
                            inimigoimagem.undraw()
                            inimigos.pop(inimigoindex)
                            tiro.undraw()
                            inimigosrestantes.undraw()
                            quantinimigos -=1
                            inimigosrestantes = Text(Point(850,300),"INIMIGOS\nRESTANTES\n{}".format(quantinimigos))
                            inimigosrestantes.setStyle("bold")
                            inimigosrestantes.draw(win)
                            spawnaleatorio = random.randint(0, len(spawns))
                            spawninimigo = spawns[spawnaleatorio-1]
                            inimigo = Circle(spawninimigo.getCenter(),15)
                            inimigoimagem = Image(spawninimigo.getCenter(),"inimigo.gif")
                            inimigoimagem.draw(win)
                            inimigoscomimagem = [inimigo,inimigoimagem]
                            inimigos.append(inimigo)
                            inimigosvelo.append(inimigo)
                            inimigoindex = inimigos.index(inimigo)
                            break
                    try:
                        if inimigo2.getCenter().getX()-15<=tiro.getCenter().getX()<=inimigo2.getCenter().getX()+15:
                            if inimigo2.getCenter().getY()-15<=tiro.getCenter().getY()<=inimigo2.getCenter().getY()+15:
                                inimigo2.undraw()
                                inimigoimagem2.undraw()
                                tiro.undraw()
                                spawnaleatorio = random.randint(0, len(spawns))
                                spawninimigo = spawns[spawnaleatorio-1]
                                inimigo2 = Circle(spawninimigo.getCenter(),15)
                                inimigoimagem2 = Image(spawninimigo.getCenter(),"inimigo2.gif")
                                inimigoimagem2.draw(win)
                                inimigos.append(inimigo2)
                                inimigosvelo2.append(inimigo2)
                                inimigoscomimagem2 = [inimigo2,inimigoimagem2]
                                break
                        if inimigo3.getCenter().getX()-15<=tiro.getCenter().getX()<=inimigo3.getCenter().getX()+15:
                            if inimigo3.getCenter().getY()-15<=tiro.getCenter().getY()<=inimigo3.getCenter().getY()+15:
                                inimigo3.undraw()
                                inimigoimagem3.undraw()
                                tiro.undraw()
                                spawnaleatorio = random.randint(0, len(spawns))
                                spawninimigo = spawns[spawnaleatorio-1]
                                inimigo3 = Circle(spawninimigo.getCenter(),15)
                                inimigoimagem3 = Image(spawninimigo.getCenter(),"inimigo2.gif")
                                inimigoimagem3.draw(win)
                                inimigos.append(inimigo3)
                                inimigosvelo3.append(inimigo3)
                                inimigoscomimagem3 = [inimigo3, inimigoimagem3]
                                break
                    except UnboundLocalError:
                        continue

                ##Otimização do jogo
                if tempo>=170:
                    tiro.undraw()

                ##Próxima fase
            if quantinimigos == 0:
            ##Ganhar
                t = 0
                apagar()
                fundo.undraw()
                inimigo.undraw()
                inimigoimagem.undraw()
                cofre.undraw()
                cofreimg.undraw()
                titulo1.undraw()
                vidas2.undraw()
                inimigosrestantes.undraw()
                fase.undraw()
                linha.undraw()

                # checando se deve escrever a nova fase como a mais alta atingida
                fasearq = open("ultimafase.txt","r+")
                fasedoarquivo = fasearq.readline()
                fasearq.close()
                qualfase+=1
                if int(qualfase)>int(fasedoarquivo):
                    fasearq = open("ultimafase.txt","w")
                    fasearq.write(str(qualfase))
                    fasearq.close()
                velocinimigo+=0.1
                inimigostotais+=5
                ganhar = Text(Point(450,300),"Você ganhou!")
                ganhar.setSize(24)
                ganhar.draw(win)
                continuar = Text(Point(450,350),"Continuar para a proxima fase: {}".format(qualfase))
                continuar.setSize(14)
                continuar.draw(win)
                seta = Polygon(Point(305,350),Point(295,345),Point(295,355))
                seta.setFill("black")
                seta.draw(win)
                ponto = Circle(Point(300,350),1)
                sair = Text(Point(490,400),"Voltar ao Menu (NÃO recomeçará do zero!)")
                sair.setSize(14)
                sair.draw(win)
                while True:
                    chave = win.getKey()
                    if chave == "Down" and ponto.getCenter().getY()==350:
                        seta.move(0,50)
                        ponto.move(0,50)
                    elif chave == "Up" and ponto.getCenter().getY()==400:
                        seta.move(0,-50)
                        ponto.move(0,-50)
                    elif chave == "Return" and ponto.getCenter().getY()==350:
                        ganhar.undraw()
                        seta.undraw()
                        ponto.undraw()
                        continuar.undraw()
                        sair.undraw()
                        inicio()
                        break
                    elif chave == "Return" and ponto.getCenter().getY()==400:
                        ganhar.undraw()
                        seta.undraw()
                        ponto.undraw()
                        continuar.undraw()
                        sair.undraw()
                        menu()
                        break
    ## Menu
    def menu():
        titulo1 = Image(Point(450,600),"ReidaPradaria.gif")
        titulo1.draw(win)
        titulocima = 0
        while titulocima<250:
            update(100)
            titulo1.move(0,-1.5)
            titulocima+=1
        def undraws():
            titulo1.undraw()
            jogo.undraw()
            comojogar.undraw()
            seta.undraw()
            sair.undraw()
            fasetexto.undraw()
        jogo = Text(Point(411,350),"JOGAR")
        jogo.setSize(14)
        jogo.draw(win)
        comojogar = Text(Point(450,400),"COMO JOGAR?")
        comojogar.setSize(14)
        comojogar.draw(win)
        sair = Text(Point(400,450),"SAIR")
        sair.setSize(14)
        sair.draw(win)

        ## Mostrando a fase máxima atingida
        fasearq = open("ultimafase.txt","r+")
        qfase = fasearq.readline()
        if qfase=="0":
            fasetexto = Text(Point(450,500),"Maior fase atingida: 0")
            fasetexto.setTextColor("green")
            fasetexto.draw(win)
            fasearq.close()
        else:
            fasetexto = Text(Point(450,500),"Maior fase atingida: {}".format(int(qfase)))
            fasetexto.setTextColor("green")
            fasetexto.draw(win)
            fasearq.close()
        seta = Polygon(Point(375,350),Point(365,345),Point(365,355))
        ponto = Circle(Point(370,350),1)
        seta.setFill("black")
        seta.draw(win)
        while True:
            tecla = win.checkKey()
            if tecla == "Down" and (ponto.getCenter().getY()==350 or ponto.getCenter().getY()==400):
                seta.move(0,50)
                ponto.move(0,50)
            elif tecla == "Up" and (ponto.getCenter().getY()==450 or ponto.getCenter().getY()==400):
                seta.move(0,-50)
                ponto.move(0,-50)
            elif tecla == "Return" and ponto.getCenter().getY()==350:
                undraws()
                inicio()
            elif tecla == "Return" and ponto.getCenter().getY()==400:
                undraws()
                tutorial()
            elif tecla == "Return" and ponto.getCenter().getY()==450:
                win.close()
                break
    ## Perdeu
    def perdeu():
        global inimigostotais
        global velocinimigo
        perder = Text(Point(450,300),"Você perdeu...\n Voltando ao menu.")
        perder.setSize(24)
        perder.draw(win)
        inimigostotais = 0
        velocinimigo = 0
        tempo = 0
        while True:
            tempo+=1
            update(25)
            if tempo>=100:
                perder.undraw()
                menu()
                break

    menu()


if __name__ == "__main__":
    main()
