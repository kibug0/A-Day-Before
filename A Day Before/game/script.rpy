define Ano = Character("???")

define Mari = Character("Marinheiro")

define Revo = Character("Revolucionario")

define Mafioso = Character("Politico")

define Red = Character("Red Chowders")

define Chef = Character("chefe")

define Ravi = Character("Ravidias")

define Lade = Character("Lade")

define Helen = Character("Helen")

define Hacker = Character ("Hacker")

define Mur = Character("Murrey")

define Marduck = Character("Marduck")

define Dn = Character("Narrador")

define Aten = Character ("Atendente")

define Soldado = Character ("soldado")

define Max = Character ("Maxuel")

define Cape = Character ("capitão")

default codigo = ""

default revolucao = 0

default Final = 0

default Raiva = 0

default estresse = 0

default cuzao = 0

default Mentira = False

default verdades = False

default trair = 0

default morte = 0

default dinheiro = 0

default danca = 0
default Traicao = False



# The game starts here.



label start:

    scene preto4 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene porto with dissolve

    show mury



    "Um dos marinheiros. chega."



    Mari "Ae você pode ajudar lá. Eu não vou poder ajudar agora."



    Ano "O que? por que você não pode ajudar?"



    Mari "É que tem um soldado lá."



    Ano "E o que isso tem haver? Você tem problema com os soldados?"



    Mari "Não, Não. É só que eu prefiro não chegar perto."



    Ano "Afff. Tá bom."



    "O marinheiro vai para os fundos."



    Ano "Agora quem eu devo ajudar?"





    menu NPC:

        "O que aquele cara está amarrando?":



            Ano "Eu não sei o porquê, mas aquilo parece importante."

            Ano "Ei Posso te ajudar?"

            Mari "Claro. Uma ajuda seria bem-vinda."

            Ano "Pronto acabei desse lado."

            Mari "Ah obrigado, mas desse lado não precisava amarrar."

            Ano "A entendi desculpa."

            Mari "Ha não se preocupa com isso não."









        "Aquela caixa parece pesada.":



            Ano "Eu deveria ajuda-lo. Se não ele pode derrubar as caixas e ferrar tudo."

            Ano "Oi. Me pediram para ajudar."

            Mari "Ah claro então me ajuda a levantar essa caixa. ela ta muito pesada."

            Ano "Sim eles devem estar pesados mesmo já que tão cheias..."

            Mari "Mas, então pega desse lado que eu pego do outro."

            "Eles levam a caixa para fora do barco."

            Mari "Aqui já está bom. Obrigado amigo."







        "Eu deveria ajuda-lo a recolher aquelas gaiolas.":



            "Essas gaiolas de caranguejos estão espalhadas por todo lado."

            Ano "Ae você está precisando de alguma ajuda?"

            Mari "Sim por favor, vai ser mais fácil com mais de uma pessoa."

            Ano "Sim eu vou começar por aquele lado e você vai por aquele."

            Mari "Ta bom."

            Mari "Obrigado pela ajuda."









    Mari "Mas então você acha que os outros estão prontos."



    menu verdades:

        "Eles têm que estar.":

            "Se não serão só um peso morto."

            $ cuzao += 1

            $ verdades = True



        "Espero que estejam.":

            "Se não serão só um estorvo."





    "O marinheiro se assusta com a resposta dele e não consegue segurar uma expressão de

    leve espanto."

label Detetive1:

    scene preto5 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene apartamento with dissolve

    show lad





    "Trin, trin, trin."







    "No celular aparece que é o chefe da polícia do distrito sul."







    Lade "Bom dia senhor."







    Chef "Detetive Lade. Primeiro de tudo parabéns pela promoção para o cargo de

    detetive. Agora para sua primeira missão você vai ter que investigar um corpo

    de um soldado que foi assassinado no condomínio sequoia que fica perto da

    ponte sul."







    Chef "Já como é seu primeiro caso foi designado um detetive veterano para você

    auxilia-lo na investigação. O nome dele é Marduck Vanny, ele é um ótimo detetive,

    mas o jeito dele pode ser meio extremo e não muito sociável."





    menu procrastinar:

        "Eu não estou afim de me juntar a alguém desse tipo.":



            Lade "(Não, Não. Eu não posso pensar assim esse tipo de pensamentos

            fracos podem acarretar em erros cruciais.)"



            Lade "Entendido senhor eu não me importo com isso se ele fizer o seu

            trabalho corretamente então não tem problema. Desligando."

            $ revolucao +=1



        "Entendido senhor.":



            Lade "Eu não me importo com isso se ele fizer o seu trabalho

            corretamente então não tem problema. Desligando."



            $ revolucao -=1





label detetive2:

    scene preto6 with dissolve



    scene condominio with dissolve

    show mard at Move((1.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)

    show lad at Move((0.0, 0.5), (0.5, 0.5), 3, xanchor=0.5, yanchor=0.5)



    Lade "Bom dia senhor Vanny você está 5 minutos atrasado. Eu já peguei todas

    as informações."





    Marduck "Primeiro de tudo não me chame de Vanny nunca mais. Segundo repasse

    todas as informações para mim."







    Lade "Desculpe senhor. Então pelo que já foi dito a vítima é um soldado do

    exército imperial, ele foi morto a facadas e o mais curioso é que com o

    sangue dele foi escrito uma mensagem na parede: O dia está chegando."



    Lade "Outro fato é que as câmeras se desligaram nesse momento do assassinato

    então não temos imagens do acontecimento."







    Marduck "Entendo. então vamos ver se tem alguma impressão digital na parede."







    Lade "Já fiz. ele deixou varias."







    Marduck "Humm também. Então você já checou o implante neural."







    Lade "Sim parece que ele foi quebrado numa possível queda."







    Marduck "Agora só falta pesquisar pelas digitais."







    Lade "Já fiz e acabou de chegar o nome dele. Henrique Batista e o endereço

    dele já foi confirmado."







    Marduck "Então vamos para lá rápido."





label detetive3:

    scene preto7 with dissolve

    "Eles chegam na casa do suspeito."

    scene favelafora with dissolve

    show mardin at Move((0.0, 0.5), (0.8, 0.5), 2, xanchor=0.5, yanchor=0.5)

    show lad at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



    Lade " Okay, estamos no Local. Marduck você vai pela janela e eu pela porta."



    Marduck "Pera porque eu tenho que ir pela janela e por que você está dando



    ordens? você vai pela janela e eu pela porta."



    menu desavenca:

        "Eu não confio em você.":

            Lade "Até agora você não se mostrou apto e até se atrasou no começo da investigação."

            Marduck "O que!! Foram só 5 minutos! E você é só um novato inexperiente."

            Lade "5 minutos podem ser cruciais no nosso ramo de trabalho e se você

            não consegue notar isso. Mostra ainda mais como você é inapto."

            Marduck "BAH!!! Eu vou pela janela então seu pentelho."

            "Marduck entra pela janela."

            Marduck "PARADO!!!!"

            "Depois entra Lade."

            Marduck "Droga!!"

            Lade "O que aconteceu?"

            scene faveladentro

            $ estresse += 1

            $ revolucao +=1

            show mard at Move((1.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)

            show lad at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)





        "Entendido.":

            Lade "Você irá pela porta e eu vou na janela. Vou checar primeiro caso ele esteja armado."

            Marduck "Ta bom. Então você vai primeiro."

            "Lade vai pela janela."

            Lade "Policia do distrito Sul. Se mantenha parado."

            "Em seguida entra Marduck."

            Lade "Meu deus."

            Marduck "O que foi?"

            scene faveladentro

            show mard at Move((1.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)

            show lad at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)

            $ revolucao -=1



    "Eles vêm o corpo do suposto suspeito sentado em uma cadeira com um buraco no

    céu da boca."



    Marduck "Merda! eu achei que esse seria um caso fácil."

    Marduck "Eai Garoto, encontrou alguma coisa?"

    Lade "Vou começar a olha ao redor."



    menu investigar:

        "Investigar pilha de roupas.":

            Lade "Marduck, encontrei uma carta aqui no meio dessas roupas."



            Lade "Venha dar uma olhada nisso."



            "Marduck então pega a carta e ler ela por Completo."



            Marduck "Ora Ora, parece que tínhamos um romancista aqui."



            Lade "O que está escrito aí??, isso nos dá alguma pista??"



            "Marduck entrega a carta para o Lade."



            "Carta: Oh querida torradinha, eu venho por meio dessa carta agradece-la

            do fundo do meu ser por me salvar do seu impiedoso pai, mas ele é um

            grande perigo para você então irei fazer com que você não caia em

            tremendo caos."



            Marduck "Parece que esse cara aí tinha um caso bem complicado com seu

            sogro."



            Lade "Mas isso não importa pra gente e nem nos ajuda muito, vamos

            investigar o resto."



            $ morte += 1

            if morte == 5:

                jump morte



            jump investigar



        "Investigar maleta.":

            Lade "Marduck, olha isso, tem uma maleta ali jogada no chão."



            Marduck "Será que tem dinheiro dentro??"



            Lade "Provavelmente não, ta muito leve isso aqui."



            "Lade abre a maleta e se decepciona."



            Lade "Está vazio."



            Marduck "Pera lá, TA VAZIA? QUE DECEPÇÃO!"



            "Marduck Pega a maleta e começa a examina-la."



            Marduck "Aqui olha, essa parte da maleta está amaçada e tem sangue seco nessa região."



            Marduck "Provavelmente foi usada durante algum confronto com a vítima."



            Lade "Okay, talvez seja melhor ir ver o corpo."

            $ estresse += 1

            $ dinheiro += 1

            if dinheiro == 5:

                jump ricos



            jump investigar



        "Investigar o corpo.":



            Lade "Hum... Entendo."



            Marduck "O que você descobriu?"



            Lade "Ele não se matou. alguém fez isso."



            Marduck "Como?"



            Lade "Olhando pelas marcas de feridas no céu da boca aparentemente alguém



            forçou uma arma."



            Marduck "Tá, mas pode ter sido só o recuo da arma."



            Lade "Esse não é o caso. Da para ver sinais de lutas pelo quarto e no corpo."









    Marduck "ta bom isso já deve ter sido tudo."



    Lade "Sim, eu já liguei para central e aparentemente a única loja de armas perto

    dessa região é um tal de toca do tatu."



    Marduck "Lá deve ter um possível comprador dessa arma."



    Lade "Então já vamos indo."





label Helen1:

    hide lad

    scene preto with dissolve

    $ renpy.pause(0.5, hard=True)

    scene fogo with dissolve





    Helen "Socorro!! SOOcoooorro!!! Coff, coff."



    show helenmao with dissolve



    Helen "Paaaaiii!!!! Socoorrrooo!!"



    Ano "Ei garotinha. Eu vou te ajudar."

    show murymao with dissolve



    Helen "Por Favor, me ajude!! Socorro onde está o papai?"



    Ano "Desculpe garotinha, mas agora precisamos fugir daqui."







label Helen2:

    scene preto9 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene preto with dissolve



    scene preto with dissolve

    show helen



    "Helen acorda em seu quarto."







    "Ela repara que seu alarme estava quebrado e tinha uma arma com silenciador



    na sua mão."



    Helen "Eu to atrasada!!!"

    hide helen

    scene toca



    Ravi "Heleeeeeeeeeen!!"

    show rav

    show helen at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



    Helen "Aaah eai Ravidias, o que ta pegando???"



    Ravi "Vem nos ajudar a levar essas caixas."



    "Helen então se depara com várias pessoas transportando uma caixa pra dentro de sua loja."



    Ravi "Todos vocês, coloquem essas caixas no armazém dos fundos."



    Helen "Nossa, vocês são bem rápidos mesmo."



    Ravi  "Claro, com as coisas que a gente ta carregando nessas caixas. A

    gente não pode dar mole."



    "Helen então ajuda o resto do povo com as caixas na última caixa ela repara

    algo."



    Helen "Ei o Ravidias essa caixa aqui está meio aberta. Se não consegue nem

    fechar uma caixa direito."



    Ravi "Hahahah. Eu não fechei essa caixa garota."



    "Ravidias leva essa última caixa para o armazém e depois volta."



    Ravi "Helen..."



    Helen "O que foi Ravidias."



    Ravi "Depois preciso conversar com você."







label Helen3:

    scene preto94 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene toca with dissolve

    hide helen

    show helen at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



    Helen "Então eu to saindo o Ravidias."



    show rav at Move((2.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



    Ravi "Onde você vai garota??"



    Helen "Comprar um lanche naquela barraquinha de sempre."



    Ravi "Entendo. Então quando você voltar a gente conversa."



    Helen "Okay. Até daqui a pouco!!!"

    show helen at Move((0.5, 0.5), (0.0, 0.5), 2, xanchor=0.5, yanchor=0.5)



    scene lachonete

    "Helen então sai em direção até a lanchonete que fica localizada perto da

    praça central, ao chegar lá, ela encontra um atendente trabalhando normalmente."





    show helen at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)







    $ code = renpy.input ("Atendente | Bom dia Helen, o de sempre??")

    $ code = code.strip()

    if code == "":

        $ code = "nada"





    Helen "Sim, vou querer %(code)s"

    if code == "dancing burger":

        Aten "Perai?? %(code)s???"



        "Os Dois começam a se olhar estranhamente até que..."



        Aten "chaka chaka chaka, entendi."

        "Ele dança enquanto prepara o lanche."



        "Ele vai e prepara o %(code)s"



        Aten "Então pode entrar."

        $ danca = True





    if code == "nada":



        Aten "Perai?? nada???"



        Helen "huummm."



        Aten "Como assim nada???"



        Helen "huummm!!!"



        Aten "A tá!!"



        Aten "então toma nada, pode entrar."



    else:

        Aten "Perai?? %(code)s???"



        "Os Dois começam a se olhar estranhamente até que..."



        Aten "Aaaaaah Ta, entendi."



        "Ele vai e prepara o %(code)s"



        Aten "Então pode entrar."







    Aten "Aqui está seu lanche, PRÓOOOOOXIMOOOOOO!"



    Helen "Obrigada então."

    show helen at Move((0.5, 0.5), (1.5, 0.5), 2, xanchor=0.5, yanchor=0.5)

    scene porão

    show hacker





    show helen at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



    Helen "Aaahn Oi??"



    "Helen é totalmente ignorada pela desconhecida, então ela vai até ela e tira

    seus fones de ouvido."



    Helen "TA ME OUVINDOOOOOOO!!"



    Hacker "MEU DEUS, PRA QUE GRITAAAAAR??"



    Helen "Bom, porque você não me ouviu talvez."



    Hacker "Ooh sinto muito minha senhorita, o que posso fazer por você??"



    Helen "Seguinte, o esquema das câmeras já está pronto??"



    Hacker "Claro Senhorita, está tudo nos conformes como você pediu."



    Helen "Certo, descanse hoje porque amanhã será um longo dia."





    "Então ela vai embora."

    show helen at Move((0.5, 0.5), (0.0, 0.5), 2, xanchor=0.5, yanchor=0.5)



label Helen4:

    scene preto11 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene toca with dissolve

    show rav

    show helen at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



    "Helen chega na toca do tatu e encontra Ravidias com um olhar preocupado."



    Helen "Ravidias. Aconteceu alguma coisa?"



    Ravi "Então. Eu tava querendo conversar com você sobre o seu pai."

    "(Ele fala meio receoso.)"



    Helen "Meu pai? o que tem ele?"



    Ravi "Então ele vem andando meio estranho. Provavelmente seja por causa

    de amanhã, parece que isso está desgastante para ele e eu estou ficando

    preocupado com ele."







    menu confianca:



       "Você está duvidando do meu pai.":



            Helen "Por acaso você não confia nele??"



            Ravi "Não é isso, mas ele tem estado meio desequilibrado nesses últimos

            dias."



            Helen "Só vou lhe falar uma coisa, o que meu pai está fazendo não é só por

            ele, e sim por todos nós, então não há do que duvidar dele."



       "Eu confio em você.":



            Helen "Mas você tem certeza do que está falando."



            Ravi "Não completamente, mas ele tem estado bem violento recentemente."



            Helen "Você acha melhor adiar o dia de amanhã?"

            $ trair += 1



    "Som de cliente entrando."



    Ravi "Chegou um cliente agora, é melhor ir atende-lo e depois terminamos."

    show helen at Move((0.5, 0.5), (0.0, 0.5), 2, xanchor=0.5, yanchor=0.5)





label helen5:

    scene preto12 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene toca with dissolve

    show mardin at Move((0.0, 0.5), (0.8, 0.5), 2, xanchor=0.5, yanchor=0.5)

    show lad at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)

    show helenin at Move((1.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



    Helen "Boa Tarde, posso ajudar vocês em alguma coisa, aqui temos as melhores

    armas do bairro."



    Marduck "Ora, que loja interessante essa aqui, nem parece que é favela isso."



    "Lade então mostra seu distintivo para Helen e todas ao redor da loja olham

    feio para eles."



    Marduck "ABAIXA ISSO MERDA!!! isso aí Lade, não quero morrer nesse lugar."



    Lade "Mas esse é o protocolo, devemos sempre o seguir."



    Marduck "É garoto, mas tem certos locais que a gente não mostra, se não a

    gente morre."



    Helen "Oooh vocês são da Polícia, o que desejam??"



    Lade "Queremos dar uma olhada no histórico de vendas da loja."



    Helen "Ué, porque??"



    Marduck "Relaxa garota, isso é pra nossa investigação, só nos dê o histórico."



    Lade "Seja mais educado, senhor Vanny."



    Marduck "JÁ DISSE PRA NÃO ME CHAMAR ASSIM MULEKE, lembre se que EU SOU seu superior."



    Helen "Okay então, só aguardem um pouco que eu irei pegar pra vocês."



    Helen "(Não tem muitas coisas importantes nesses históricos, maaas... )"

    show helenin at Move((0.5, 0.5), (1.0, 0.5), 2, xanchor=0.5, yanchor=0.5)

    hide mardin

    hide lad

    show helen at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)







    menu Enganacao:







        "Ainda assim tem um certo risco mostra-lo.":



            Helen "(Não vale a pena arriscar a operação com esses idiotas.)"

            hide helen



            show mardin at Move((0.0, 0.5), (0.8, 0.5), 2, xanchor=0.5, yanchor=0.5)

            show lad at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



            show helenin at Move((1.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



            Helen "Bem, aqui está o histórico de compras mais recente da nossa loja."



            Lade "Hum, entendo, bom acho que com isso já temos o suficiente."



            Marduck "É, aparentemente ele não passou por aqui, vamos indo garoto."

            $ Mentira = True

            show mardin at Move((0.8, 0.5), (-1.0, 0.5), 2, xanchor=0.5, yanchor=0.5)

            show lad at Move((0.5, 0.5), (-1.0, 0.5), 2, xanchor=0.5, yanchor=0.5)

            $ estresse += 1

            $ revolucao -=1











        "Não é bom tentar engana-los, pode ser perigoso.":



            Helen "(Bom, o histórico está aqui, melhor mostrar isso logo para eles.)"

            hide helen



            show mardin at Move((0.0, 0.5), (0.8, 0.5), 2, xanchor=0.5, yanchor=0.5)

            show lad at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



            show helenin at Move((1.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



            Helen "Ta aqui, o histórico das compras mais recentes."



            Lade "Parece que o nosso suspeito não passou por aqui."



            Marduck "Merda!"



            Marduck "Ta, vamos indo garoto, não tem mais nada por aqui que vai ajudar a gente."

            show mardin at Move((0.8, 0.5), (-1.0, 0.5), 2, xanchor=0.5, yanchor=0.5)

            show lad at Move((0.5, 0.5), (-1.0, 0.5), 2, xanchor=0.5, yanchor=0.5)

            $ revolucao +=1

            $ trair += 1





    "Os Detetives então saem da loja e vão embora, enquanto isso,

    Helen volta para os fundos para terminar sua conversa com Ravidias."



    Helen "Então Ravidias, vamos continuar nossa conversa."

    show rav at Move((2.0, 0.5), (-2.0, 0.5), 5, xanchor=0.5, yanchor=0.5)



    Ravi "Desculpe Helen, parece que minha perna Robótica ta com algum defeito,

    acho que vou pra minha oficina consertar."



    Helen "Ta bom, depois que você resolver isso aí, a gente se encontra a noite."



    Ravi "Claro."



    Ravi "Bom, eu já vou indo garota, até mais tarde."











    "Ravidias vai pra oficina consertar a sua Perna Robótica."







label detetive4:

    scene preto122 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene toca with dissolve

    show mardin at Move((0.0, 0.5), (0.8, 0.5), 2, xanchor=0.5, yanchor=0.5)

    show lad at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



    Lade "É, parece que essa loja não nos ajudou muito, senhor Vanny."



    Marduck "Até quando você vai me chamar assim em??"



    Marduck "Bom, como essa arma não é daqui, provavelmente ela veio transportada de algum outro país."



    Lade "Faz sentido nos estamos numa ilha e ainda mais a capital do pais, mas
    eles não devem ter vindo com aviões por conta dos parâmetros de segurança."



    Marduck "Ah única pista que resta para nós então é o porto mais próximo, até que você é inteligente novato."



    Lade "Então vamos indo, Senhor Vanny."



    Marduck "CALA A BOCAA!!"



label detetive5:

    scene preto123 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene porto with dissolve

    show mardin at Move((0.0, 0.5), (0.8, 0.5), 2, xanchor=0.5, yanchor=0.5)

    show lad at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



    "Eles chegam no porto de piracema."



    Lade "Olha senhor Van... Marduck... Um soldado em patrulha. Ele deve ter um registro de passagens."



    Marduck "Se ia me chamar de Vanny né? Bah esquece vamos interrogar o soldado."



    "Eles abordam o soldado."



    "Lade mostra o distintivo."



    Lade "Eu sou o detetive do distrito sul no primeiro dia de trabalho."



    Soldado "Haaaa Parabéns? Posso ajuda-los em alguma coisa?"



    Marduck "Ignora esse cara. Nós queremos ver seu histórico de cargas."



    Soldado "Claro ele fica lá na sala de câmeras."



    show mardin at Move((0.8, 0.5), (-1.0, 0.5), 2, xanchor=0.5, yanchor=0.5)

    show lad at Move((0.5, 0.5), (-1.0, 0.5), 2, xanchor=0.5, yanchor=0.5)

    "Eles vão até a sala de câmeras."



    show mardin at Move((0.0, 0.5), (0.8, 0.5), 2, xanchor=0.5, yanchor=0.5)

    show lad at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)

    Lade "Nesse histórico não tem nenhum carregamento de armas. Só de peixes em sua maioria."



    Marduck "É claro que não seria tão fácil assim."





    Marduck  "Ta. Então liga os vídeos aí."

    hide mardin

    hide lad







    "Eles ligam as câmeras e vem Ravidias e várias outras pessoas transportando caixas de pesca."



    show rav

    Ravi "Ei tomem cuidado com essas caixas."

    hide rav



    show lad at Move((0.5, 0.5), (-1.0, 0.5), 1, xanchor=0.5, yanchor=0.5)

    show mardin at Move((0.8, 0.5), (-1.0, 0.5), 2, xanchor=0.5, yanchor=0.5)

    Soldado "Esses são os caras."



    Lade "Só um minuto senhor Vanny."



    "Lade sai correndo e pega com uma pinça entre a madeira do porto."



    Marduck "Arff Arff. O que você está fazendo saindo correndo assim do nada? E eu já falei para você não me..."



    Lade "Eu vi caindo de uma das caixas e tive que ter certeza. Aqui Esse e um cartucho compatível com a arma que temos."



    Marduck "Huuum Caralho como você viu esse cartucho caindo pelo vídeo Você tem um olho biônico?"



    Lade "Não temos tempo para as suas piadas. Vamos investigar onde o cara do vídeo mora e depois interroga-lo."



label detetive6:

    scene preto13 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene oficina with dissolve

    show rav



    Marduck "Então esse é o local?"



    Lade "Sim. Ravideas Delore, um mecânico que mora aqui no anel inferior da

    região sul e essa é a oficina do suspeito."

    show mardin at Move((0.0, 0.5), (0.8, 0.5), 2, xanchor=0.5, yanchor=0.5)

    show lad at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)







    show rav





    menu abordagem:



        "Parado polícia!!!":



            "Ravideas sai correndo."

            hide rav

            show ravin at Move((1.0, 0.5), (2.0, 0.5), 2, xanchor=0.5, yanchor=0.5)



            $ trair += 1



        "Essa é a oficina do senhor Ravideas?":



            Ravi "Ele mesmo falando. Como posso ajudar os senhores do anel superior."



            Marduck "Por que você acha isso?"



            Ravi "Você nem tanto, mas o seu amigo ele tem roupas muito bonitas algo

            que não se vê por aqui."



            Lade "Obrigado."



            Marduck "Ele não te elogiou porra."



            Lade "Mas enfim senhor nós somos detetives e gostaríamos de fazer algumas

            perguntas."



            "Quando lade mostra o distintivo Ravideas fica com um olhar assustado e

            corre em desespero."



            hide rav

            show ravin at Move((1.0, 0.5), (2.0, 0.5), 2, xanchor=0.5, yanchor=0.5)













    Lade "Parado!!!"

    hide lad

    hide mardin



    show ravin at Move((-1.5, 0.5), (2.0, 0.5), 2, xanchor=0.5, yanchor=0.5)



    "Ravideas ignora e continua correndo."







    "Lade saca sua arma."







    Lade "Eu disse parado porra!!!!!"



    "Enquanto Lade grita, Marduck saca a arma e dá um tiro na perna normal do

    Ravideas o derrubando."



    "bang!"



    Ravi "Drogaaa!!"

    show rav-me at Move((0.0, 0.75), (0.5, 0.95), 2, xanchor=0.5, yanchor=0.5):

        subpixel True

        rotate 0

        linear 1 rotate 450



    Marduck "Se você não vai atirar então nem devia ter sacado a arma, seu idiota."







    "Eles vão até o corpo caído de Ravideas."







    Ravi "Merda!!!"

    show mardin at Move((0.0, 0.5), (0.8, 0.5), 2, xanchor=0.5, yanchor=0.5)

    show lad at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



    Marduck "Agora pegamos você. Me fale para que servia todos aqueles

    carregamentos de armas."



    Ravi "Vai se fuder seu merda."



    Marduck "Entendi. Ei Lade, eu tenho um fio condutor??"



    Lade "Espera Marduck isso vai contra o protocolo."



    Marduck "QUE SE FODA O PROTOCÓLO, nós temos que fazer isso, AGORA!!!"







    "Lade se assusta com o grito de Marduck."



    Lade "Entendi..."







    "Lade pega um fio e o conecta com seu chip-neural e depois conecta com o

    chip de Ravideas."







    "Lade pega um fio e o conecta com seu chip-neural e depois conecta com o



    chip de Ravideas."







    "Lade então descobre tudo sobre o plano da revolução, e acaba descobrindo a

    identidade do Líder, como também acaba sabendo seu nome e se assusta com seus

    atos de violência."

    "Enquanto  Ravidias ainda conectado com Lade, ele usa um dente falso com
    veneno para se matar. isso deu um estouro na coneção entre eles, mas lade sai
    ileso e Ravdias morre."





    Lade "Marduck, temos um problema, parece que esse cara aqui iria participar

    de uma espécie de Revolução."



    Marduck "Merda, então a gente precisa avisar isso pra central agora mesmo."





    "Marduck então liga para a central e fala sobre os acontecimentos e o que

    descobriram."





    Chef "Entendo, então vamos preparar uma emboscada pra esses desgraçados,

    avise ao Lade que isso irá alavancar muito a carreira dele."



    Marduck "Okay, eu aviso Senhor."



    Marduck "Ai o Novato, se liga, parece que você deu sorte mesmo em."



    Lade "Sorte Porque??"



    Marduck "A Central quer fazer uma emboscada pra esses caras, como você contém

    as informações, é só levar isso para eles e montaremos um plano."















    menu mudar:



        "Uma Emboscada parece ser bom.":



            Lade "Certo, parece um bom plano pra pegar esses bandidos."



            Marduck "Hahaha, é assim que se fala garoto, a partir de amanhã seu

            nome ficara bem conhecido no nosso setor."



            Marduck "Beleza, bora pra Central."



            "Marduck e Lade vão até a central e lá eles fazem uma reunião pra

            acabar de vez com a Revolução, O nome do Líder finalmente foi

            Revelado: Murrey Whintonsser."



            Marduck "Cacete, essa Reunião foi exaustiva."



            Lade "Sim, também estou meio cansado."



            Marduck "Vai pra casa garoto, amanhã será um dia bem cansativo."



            Lade "Certo."

            $ revolucao -=1





        "Eu preciso parar esse cara o quanto antes.":



            Lade "(Se eu esperar até a hora da emboscada, quanto mais pessoas esse cara vai matar??)"



            Marduck "Ei Lade, vamos para a central, o chefe quer um relatório do

            que a gente conseguiu."



            Lade "Certo!"





            "Marduck e Lade vão até a central e lá, Lade passa algumas

            informações sobre a Revolução."





            Lade "Então foi apenas isso que eu descobri, Senhor!"



            Chef "Entendo, você não encontrou nada relacionado ao Líder??"



            Lade "Não Senhor, parece que o suspeito não tinha tanto envolvimento

            com o Líder."



            Chef "Uma Pena mesmo, mas fiquem tranquilos pois vamos pegar o líder

            não importa quem seja!"





            "A Reunião então acaba com eles armando um plano para acabar com a

            Revolução."





            Marduck "Isso foi exaustivo mesmo, mas então Lade, melhor você ir

            pra casa descansar um pouco."



            Lade "Certo!"



            Marduck "Quer uma carona pra casa??"



            Lade "Não, eu preciso passar em um lugar antes."



            Marduck "Okay."





            "Marduck então vai pra casa e deixa Lade sozinho, mas Lade apenas

            pensava em uma coisa."





            Lade "(Eu Irei parar o Murrey, não importa como!)"

            $ revolucao +=1



label helen6:

    scene preto14 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene toca with dissolve

    show helen



    "trin, trin."



    "Um número anônimo está ligando para Helen."







    Helen "Alo?"



    Hacker "Olá Senhorita Helen."



    Helen "Você. O que você quer?"



    Hacker "Eu vi aqueles detetives te interrogando pela câmera de segurança."



    Helen "Ta e daí?"







    if Mentira == True:



        Hacker "Eu vi você mentindo e você é péssima nisso senhorita, não combina

        com seu charme."



        Helen "Merda. Será que eles me descobriram?"



        Hacker "Eles são detetives e não crianças na quinta série, mas não se preocupe

        senhorita, pois sua lindeza e seu charme devem ter desnorteado eles de sua

        missão."







    Hacker "Então depois deles terem saído eu decidi segui-los."



    Hacker "Eles acabaram descobrindo sobre os carregamentos de armas e que o

    ravidias estava envolvido. Eles já foram para a oficina dele."



    Hacker "Se eu fosse você, iria pra lá agora mesmo Senhorita."







    Helen "Merda to indo para lá agora."





label helen7:

    scene preto145 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene oficina with dissolve



    show helen at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



    "Helen chega na oficina do Ravidias."







    Helen "Não..."







    "Ela se depara com o corpo morto de Ravidias."

    show rav-me at Move ((2.0, 1.0), (0.5, 1.0), 2, xanchor=0.5, yanchor=0.5):

        subpixel True

        rotate 90





    Helen "Não, Não, Não, Não!!!!"







    "Helen pega o celular."







    Helen "...Pai...Pai, pelo amor de Deus, você ta ai??"



    Mur "Fala Helen, o que aconteceu?"



    Helen "Pai... o Ra-Ra-Ravidias, mataram ele!!"



    Mur "Entendo me encontre na toca do tatu."



    Helen "... Está bem."



    Mur "E Helen."



    Helen "O Que??"



    Mur "Não me ligue pelo telefone. Eles poderiam ter nos rastreado.

    Eu esperava mais de você."







    "Ele desliga o celular."







    menu Reviravolta:



        "Ir para a toca do tatu encontrar o Murrey.":



            "Helen então volta para a toca do tatu, com apenas com um pensamento

            em mente, fazer com que a revolução acontece a qualquer custo."

            hide rav



            jump murrey1





        "Investigar a casa do Ravidias.":



            Helen "Eu não vou embora assim de mãos abanando."



            Helen "Talvez tenha algo que possa me ajudar a descobrir quem vez

            essa merda."

            hide rav


            show helen at Move((0.0, 0.5), (-2.0, 0.5), 2, xanchor=0.5, yanchor=0.5)



            jump helen8



label helen8:

    scene preto146 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene oficina with dissolve

    show helen at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



    "Ao entrar Helen encontra um computador ligado nos fundos."







    Helen "Talvez esse computador possa ter alguma coisa, mas não sou muito boa

    com isso."







    "Helen então tem a ideia de ligar para a Hacker."







    Helen "Eai, to precisando de um favor seu."



    Hacker "Claro, por você eu faço qualquer coisa Senhorita."



    Helen "Ta, Ta, agora foca, eu preciso que você procure alguma prova de quem

    fez isso."



    Hacker "Deixa comigo Madame."







    "O Hacker então consegue acessar as informações no computador e acaba

    encontrando algo que seria horrível para Helen."







    Hacker "Tem um vídeo que eu achei aqui, posso liberar ele pra gente assistir,

    só mandar a ordem que eu reproduzo pra você."



    Helen "E o que você está esperando, aperta logo nisso aí."







    "Nesse momento, a verdade é revelada."







    Helen "Pai?... Não! Porque está fazendo isso?!"







    "Ela vê uma coisa horrível nesse vídeo."







    menu pai:



        "Eu tenho que impedir meu pai.":



            Helen "Porque??, porque um vídeo como esse está no computador do Ravidias??"



            Hacker "Isso é um Problemão e tanto em Senhorita, e agora, o que vamos fazer??"



            Helen "(Então era isso que o Ravidias queria me mostrar.)"



            Helen "Meu pai vai precisar de uma boa explicação pra isso."



            Hacker "Concordo Plenamente com você Senhorita."





            $ trair += 1
            $ Traicao = True



        "Eu vou ignorar isso.":



            Hacker "Isso parece um Problema senhorita."



            Helen "Isso não é nada, apenas apaga isso."



            Hacker "Pera, mas porque, isso é extremamente horri..."



            Helen "APENAS APAGA ESSA MERDA!!"





    "Helen desliga o telefone e sai do local sem falar nada, com uma atmosfera misteriosa."





label murrey1:

    scene preto415 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene porto with dissolve

    show mury




    Mari "Mas então você acha que os outros estão prontos."


    if verdades == True:



        menu:



            "Eles têm que estar.":



                "Se não serão só um peso morto."





    else:

        menu:

            "Espero que estejam.":



                "Se não serão só um estorvo."











    Dn "O marinheiro se assusta com a resposta dele e não segurar uma expressão de

        leve expando."



    Ravi "Ei Murrey, você parece cansado, você está bem?? "



    Mur "Estou bem Ravidias, não se preocupe, como estão as coisas??"



    Ravi "Os rapazes estão agilizando as coisas já, mas então, quando você vai

    visitar a Helen??"



    Mur "A Helen ficará bem, preciso focar na nossa missão."



    Mur "Mais Tarde irei visitar os Red Chowders, precisamos demonstrar as armas

    pra eles antes de nos ajudarem com a Revolução."



    Ravi "Okay, irei juntos com os rapazes para a loja, dar uma passada lá depois."



    Mur "Tudo Bem!"







    "Murrey então parte em direção ao território dos Red Chowers."



label murrey2:

    scene preto6 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene guangue with dissolve

    show mury at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)









    Cape "Ora Ora, olhem só rapazes, o babaca que acha que vai mudar o país chegou."







    menu ira:



        "Vocês não mudaram nada mesmo.":



            Mur "Vocês continuam o mesmo de sempre, até quando vão continuar agindo assim??"



            Red "Ala Capitão, esse cara acha que pode dar sermão em nós."



            Cape "Não esquenta, já to acostumado com isso."



            Mur "Ta bom, chega de enrolação."







        "Eu não acho, eu VOU mudar o país.":



            Mur "Eu não acho, EU VOU mudar o país a qualquer custo, e ninguém irá ficar no meu caminho!!"



            Red "Ala Capitão, esse cara acha que bota medo na gente kkkkkk!!"



            Cape "Relaxa jovem, já estou acostumado com pessoas sonhadoras assim."



            Mur "Vamos direto pro assunto, sim??"







            $ Raiva +=1





    Mur "Trouxe essas armas para vocês, melhor vocês testarem elas antes de partimos amanhã."



    Cape "Claro que vamos testar, eu não confio em você, Revolucionário."



    Mur "Não quero confiança, apenas quero apoio de vocês no dia de amanhã pois serão bem util."



    Red "Pera Pera, não trate a gente como se fossem ferramentas. Provavelmente sem nós vocês irão falhar amanhã."







    menu furia:



        "Eu estou falando com o seu chefe. Agora cala a boca antes que eu cale.":



            Red "Não vai se achando só por que você tem algumas armas aí. Se eu quiser eu..."



            Cape "Já chega você."



            Red "Hurg... ta bom capitão."







            "Murrey começa a apresentar um olhar irritado."

            $ Raiva +=1







        "Mas então o que vocês acharam das armas?":



            Red "Ei não me ignore seu idiota!"



            Cape "Já chega!"



            Red "Hurg... ta bom capitão."







    Cape "Eu to gostando do que estou vendo aqui essas armas são de alto calibre."



    Mur "Obrigado."







    "Capitão pega uma das armas."







    Cape "Elas são tão boas que é um desperdício deixa-las com seu grupinho."



    "Ele aponta a arma para a cabeça de murrey."



    Cape "Será que eu deveria acabar com essa sua brincadeira de revolucionário e pegar essas armas para mim?"







    menu colera:



        "Eu não faria isso se fosse você.":



            Mur "Se fizer isso, vocês irão só arranjar pra cabeça, sabem disso né??"



            Cape "Infelizmente você tem razão, seus amiguinhos iriam vir atrás

            de mim com esse lance de vingança e bla bla bla."



            Mur "Bom, então vamos terminar essa demonstração por hoje."









        "Certo, vamos acabar com isso de uma vez.":



            Mur "Ta Legal, lembrem se no inferno que foram vocês que pediram por isso."



            Cape "Calma Calma, eu só tava brincando cara, relaxa."



            $ Raiva +=1







    if Raiva >= 2:



        "Murrey Saca uma Arma rapidamente e atira bem na cabeça do Capitão."







        Red "CAPITÃAAAAAAO!!"



        Red "Seu Desgraça..."







        "Murrey mira em um dos capangas e atira novamente."







        "Nesse momento, Murrey começa a fazer um massacre, por conta do seu ódio

        e fúria, sua velocidade em atirar superava todos os Capangas, mal dava

        tempo deles reagirem, até que sobra apenas um capanga vivo."







        Red "Se-seu desgraçado, isso não vai ficar ass..."







        "Murrey dá o ultimo tiro acabando de vez com os Red Chowders."

        $ cuzao += 1



    else:

        "O Capitão então abaixa a arma e aceita o acordo com Murrey,

        no final parece que deu tudo certo."



        Mur "Não é pra ser divertido, mas enfim, te espero amanhã no local

        combinado, agora preciso voltar."



        "Murrey então pede pra uns revolucionários trazerem o resto das armas

        para os Red Chowders, depois disso ele parte de volta pra toca do tatu."





        Cape "Bom, você sabe que essa sua ideia é suicida, mas mesmo assim eu

        vou ajudar você, vai ser divertido."











    Mur "Bom, acho melhor eu voltar pra base."







    "Murrey então parte em retorno para a toca do tatu."







    Mur "Bom, acho melhor me apressar pra ver como estão indo as coisas,

    melhor eu pegar um atalho nesse beco."







    "Murrey então recebe uma ligação de um Revolucionário."



    Mur "Alô."



    Ano "Senhor Murrey, está ouvindo??"



    Mur "Sim! Pode falar."



    Ano "Um dos nossos anda meio suspeito, talvez ele faça o nosso plano dar

    errado, o que devemos fazer??"



    Mur "Se Livrem dele, não quero mais problemas!"



    Ano "Sim Senhor!"



label murrey3:

    scene preto12 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene toca with dissolve

    show mury at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)

    show rav at Move((1.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



    if Raiva >= 2:



        Ravi "Mas que merda foi essa com Os Red Chowders??  Você matou todos eles!!!"



        Mur "Eles mereceram aquilo. E aquele bando de macacos não iriam ajudar em nada."



        Ravi "Meu deus você está ficando insano!!"

        $ revolucao -=1

        $ trair += 1



    else:



        Ravi "Murrey! Como foi as negociações?"



        Mur "Complicado como sempre, mas deu tudo certo pelo que parece."



        Ravi "Certo, e aquele esquema daquele cara???"



        Mur "Não se preocupe com isso Ravidias, eu já resolvi isso."



        Ravi "Certo!"

        $ revolucao +=1



    "Outro Problema Surge para Murrey!"







    Ravi "Murrey, temos um novo problema."



    Ravi "Lembra daqueles caras corruptos que estão financiando nossas armas?

    Então, parece que eles querem dar pra trás no plano."



    Mur "Puta que Pariu!! Quando eu acho que está tudo pronto, sempre vem outro

    pra fuder o nosso objetivo."



    Mur "Onde eles estão agora???"



    Ravi "Bem, pelo que eu soube, eles vão ir naquele restaurante popular que

    tem no centro da cidade."



    Ravi "O que você vai fazer??"







    menu Mafia:



        "Vou ter uma conversa com eles.":



            Mur "Vou Conversar um pouco com eles, talvez estejam com medo de alguém descobrir."



            Ravi "Não faça nenhuma estupidez."



            Mur "Pode Deixar!"







        "Botar Medo nesses caras vai fazer repensarem suas idéias.":



            Mur "Acho que vou precisar pressionar eles um pouco pra não fazerem merda."



            Ravi "Isso só vai piorar a situação não acha??"



            Mur "Se Piorar, resolvo da maneira que eu sempre faço."

            $ cuzao += 1







    "Murrey então sai em direção ao encontro dos Corruptos."





label murrey4:

    scene preto1300 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene restaurante with dissolve

    show mury at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)





    "Murrey chega no grande restaurante acompanhando de um revolucionário."







    Mur "Ei você, me espera aqui na entrada."







    "Murrey entra no Restaurante, mas ele parece vazio."







    Mur "Ué, não sabia que iria ta tão vazio assim."







    "Murrey então avista os Corruptos sentado em uma das mesas do restaurante

    comendo e se divertindo, algo vai acontecer."







    Max "Ei Murrey, que bom que está aqui, se junte a nós."



    Mur "Acho que você sabe porque eu estou aqui não é mesmo Max??"



    Max "Uol, você está com Raiva??"







    menu Irritado:



        "Raiva?? O que você acha Porra???":



            Mafioso "Melhor alguém como você não falar assim com a gente."



            Mur "A gente? Você ta falando de políticos corruptos que

            vieram do anel superior."



            Mafioso "Hora seu... não ouse falar assim comigo."



            Mur "Cala a boca. Vocês estão ferrados. Todos já sabem que vocês

            estão sendo investigados pelos desvios de verbas e outros crimes

            políticos."



            Mur "Sem mim o de vocês está na reta."



            Mafioso "Vai se fuder, seu merda."



            Max "Vamos acalmar os ânimos senhores. Nós somos pessoas civilizadas.

            Então vamos voltar ao tópico."



            $ Raiva += 1





        "Não estou com raiva, mas vocês vão amarelar agora??":



            Max "Amarelar é meio forte. Eu prefiro chamar de saída estratégica a

            custa de vocês."



    Mur "Então vocês vão nos vender. Mas de qualquer jeito os seus podres estão

    sendo investigados e vocês vão pra cadeia."



    Max "Entenda a nossa situação Murrey, ao contrário de você, nós estamos em

    maior destaque então caso o seu plano de errado você tem até chance de

    escapar, mas nossas cabeças serão cortadas na hora."







    Mur "E o que isso tem a ver comigo, eu só pedir pra vocês me ajudarem com

    as armas, eu disse que nada ia dar errado."



    Max "Desculpa, mas sabe como é, crime político é prisão mas uma revolução

    pode acarretar numa execução. Eu não vou arriscar minha vida por meros

    cidadãos do anel inferior."











    menu Paciencia:



        "Não se preocupem.":



            Mur "Apenas sejam pacientes, vocês não serão pegos pelos policiais tão

            facilmente, eu to ajudando vocês."



            Max "Ta Legal Homem, eu entendo esse seu sonho louco ai, mas nós

            políticos pensamos de uma maneira lógica, só falar isso não vai nos ajudar."





        "Não vão se achando por só ter nascido no anel superior.":



            Mur "Essa arrogância de vocês me enoja, isso já ta testando minha paciência."



            Max "Hahaha! Não fique tão raivoso homem, como você irá liderar sua

            revolução sendo um Homem impulsivo desse jeito??"





            $ Raiva += 1





    "Murrey então tenta sua última chance de convence-los a não trair a causa."







    Mur "Eu disse que se me ajudassem, vocês iriam ter um bom cargo na Política,

    não disse??"



    Mafioso "E Quem garante que você vai cumprir com a Palavra??"







    menu Decisao:



        "Eu vou cumprir a palavra, confiem em mim.":



            Mur "A Gente vai seguir com plano, e vocês vão conseguir sair

            intocáveis da polícia, vão viver suas vidas do jeito que estão depois."



            Max "Sinceramente, espero que você realmente esteja falando a verdade."



            Mur "Eu sou um homem de palavra, apenas isso!"





        "Ja chega não aguento mais falar com vocês.":



            Mur "Só uma coisa é melhor não nos dedurarem."



            Max "E se eu quiser??"



            Mur "Bem, arrisque e você verá!"



            "Murrey olha para Maximillian com puro ódio e desgosto."



            $ Raiva += 1

















    Mur "Então, não se esqueçam do trato."






    if Raiva >= 4:

        if Raiva != 6:







            Mur "Ja não basta aqueles merdas dos Red Chowders, agora tenho que lidar com

            vocês também."







            "Murrey então saca sua arma e da 3 tiros em direção do Max."



            Mafioso "Mas que porra foi essa??"



            Mur "Quem é o próximo??"



            Mafioso "..."







            "Murrey então é interrompido pelo Revolucionário."







            Revo "Senhor Murrey, telefone pra você."



            Mur "Okay, passa pra cá."







            "Os outros políticos ficaram paralisados com a situação, com medo de morrer

            também."



            Mur "Alô, Helen??"



            Mur "Fala Helen, o que aconteceu??"



            Helen "..."



            Mur "Entendo, me encontre na toca do tatu."







            "Murrey fica extremamente raivoso com a situação, mas ele se segura e

            deixa os outros políticos viverem."







            Mur "Ei você, precisamos voltar pra Toca, vamos!"

            $ revolucao +=1







        else:



            Mur "Vocês já acabaram com mina paciência!!"



            "Murrey então pega sua arma e começa a atirar em todos os políticos

            que estavam ali."



            Mafioso "Mas que porr..."





            "Após matar todos que estavam ali, Murrey é interrompido pelo

            Revolucionário, mas algo acontece."





            Revo "Senhor Murr..."





            "Murrey dar um tiro no Próprio Revolucionário, o celular que estava na

            mão dele cai no chão tocando, então Murrey atende o Telefone."





            Mur "Alô, quem é??"



            Mur "Helen?? O que aconteceu??"



            Mur "O QUE??"



            Mur "Ta ta, me encontra na toca do tatu."





            "Murrey então sai do local e volta para a toca do tatu."

            $ revolucao +=1

            $ cuzao += 1













    else:

        "Murrey então parte pra cima do Max e começa dar várias porradas na cara

        dele, mas uma coisa o interrompe."

        Revo "Senhor Murrey, telefonema pra você."

        Mur "Espera um momento."

        "Murrey da mais cinco socos por segundo na cara de Max e então se levanta

        para atender o telefone."

        "Os outros políticos ficaram paralisados com a situação, com medo de

        apanhar também."

        Mur "Alô, Helen??"

        Mur "Fala Helen, o que aconteceu??"

        Helen "..."

        Mur "Entendo, me encontre na toca do tatu."

        "Murrey então fica com uma cara triste e decide voltar para a toca do tatu"

        Mur "Então, não se esqueçam do trato.."
        $ revolucao -=1



    "Então murrey vai para a toca do tatu."





label final1:

    scene preto

    if revolucao <= 1 :



        Dn "No dia seguinte logo de madrugada ouve várias tropas de soldados detendo

        associados dos revolucionários apagando as chamas da revolução. várias

        pessoas presas e várias vidas foram perdidas e a cidade continuou

        lentamente sucumbindo a desigualdade e pobreza."



        Dn "Isso tornou essa a pior

        cidade do mundo. Eles até trocaram a capital do país e Lade até hoje

        acha que a revolução poderia ter mudado isso e se culpa até hoje."





    if revolucao > 1 and Traicao == false :

        if revolucao > 1 and cuzao >= 3 :



            Dn "Murrey consegue assumir na sua revolução e lidera com mão de ferro,

            assim ele alavancou a economia de seu país. Agora ele está mais

            Ambicioso, ele começou uma guerra com os países envolta onde varias

            vidas já foram perdidas e ainda não tem um final visível."



        if revolucao > 1 and cuzao < 3 :



            Dn "Murrey consegue fazer sua revolução. Ele consegue assumir como um

            imperador de punho de aço, mas isso acarretou numa grande queda na

            economia, no país e para ele mesmo. Assim o país destruído teve seu

            território repartido entre os países envolta."





    if revolucao > 1 and trair >=2 and trair != 5 and Traicao == True :



        Dn "No dia seguinte nada de mais aconteceu e parece que as chamas da revolução

        nunca existiram, mas isso foi só uma pausa estratégica para a mudança

        para seu novo líder."



        Dn "Helen agora nova líder dos revolucionários depois

        de ter impedido seu pai louco. Agora seu plano está sendo posto em

        pratica e as chamas da revolução crescem."



    if revolucao > 1 and trair == 5 and Traicao == True:



        Dn "Helen confronta seu pai e o prende na toca do tatu dizendo que ele

        está desequilibrado demais então ela assume a frente da revolução e

        tem uma vitória absoluta. O seu pai aparentemente ainda esta

        desequilibrado então infelizmente ela tem que assumir o comando do país."









label falhas:

    Dn "veja tambem os erros de gra... quero dizer."

    Dn "Os erros de programação."

    menu cenas:

        "ravidias voador inverso.":

                scene preto145 with dissolve

                $ renpy.pause(0.5, hard=True)

                scene oficina with dissolve



                show helen at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



                "Helen chega na oficina do Ravideas."







                Helen "Não..."







                "Ela se depara com o corpo morto de Ravideas."

                $ renpy.pause(0.5, hard=True)

                show rav-me at Move ((2.0, 1.0), (0.5, 0.1), 0.5, xanchor=0.5, yanchor=0.5):

                    subpixel True

                    rotate 90





                Helen "Não, Não, Não, Não!!!!"

                Helen "se ingeriu helio?! ravidias?!"

                jump cenas

        "ravidias voador.":

            scene preto145 with dissolve

            $ renpy.pause(0.5, hard=True)

            scene oficina with dissolve

            "Ela se depara com o corpo morto de Ravideas."

            show rav-me at Move ((-1.0, 0.1), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5):

                subpixel True

                rotate 90





            Helen "Não, Não, Não, Não!!!!"

            Helen "se ingeriu helio de novo ravidias?!"

            jump cenas

        "Helen e ravideas.":

            scene preto145 with dissolve

            $ renpy.pause(0.5, hard=True)

            scene oficina with dissolve



            show helen at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)



            "Helen chega na oficina do Ravideas."







            Helen "Não..."







            "Ela se depara com o corpo morto de Ravideas."

            show ravin at right:

                subpixel True

                rotate 180





            Helen "Não, Não, Não, Não!!!!"

            Ravi "kekekek ela nunca vai me encontrar aqui."

            jump cenas

        "Ravidias cenas epicas.":

            scene preto13 with dissolve

            $ renpy.pause(0.5, hard=True)

            scene oficina with dissolve

            show rav

            Ravi "Drogaaa!!"

            show rav-me at Move((0.0, 0.75), (0.5, 0.75), 2, xanchor=0.5, yanchor=0.5):

                subpixel True

                rotate 0

                linear 1 rotate 350



            Marduck "carai o cara deu um mortal."

            Lade "Oxi mas nesa cena era para voce cair morto."

            Ravi "Foi mal erro meu."
            Ravi "Porra cara se é meu duble mas ainda esse mortal foi epico."

            jump cenas



        "cena completamente errada.":

            scene preto13 with dissolve

            $ renpy.pause(0.5, hard=True)

            scene oficina with dissolve

            show rav



            Marduck "Então esse é o local?"



            Lade "Sim. Ravideas Delore, um mecânico que mora aqui no anel inferior da

            região sul e essa é a oficina do suspeito."

            show lad at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)







            show rav







            menu isso:



                "Parado polícia!!!":



                    "Ravideas sai correndo."

                    show rav

                    show ravin at Move((1.0, 0.5), (2.0, 0.5), 2, xanchor=0.5, yanchor=0.5)



                    $ trair += 1



                "Essa é a oficina do senhor Ravideas?":



                    Ravi "Ele mesmo falando. Como posso ajudar os senhores do anel superior."



                    Marduck "Por que você acha isso?"



                    Ravi "Você nem tanto, mas o seu amigo ele tem roupas muito bonitas algo

                    que não se vê por aqui."



                    Lade "Obrigado."



                    Marduck "Ele não te elogiou porra."



                    Lade "Mas enfim senhor nós somos detetives e gostaríamos de fazer algumas

                    perguntas."



                    "Quando lade mostra o distintivo Ravideas fica com um olhar assustado e

                    corre em desespero."



                    show rav

                    show ravin at Move((1.0, 0.5), (2.0, 0.5), 2, xanchor=0.5, yanchor=0.5)













            Lade "Parado!!!"

            hide lad



            show ravin at Move((-1.5, 0.5), (2.0, 0.5), 2, xanchor=0.5, yanchor=0.5)



            "Ravideas ignora e continua correndo."







            "Lade saca sua arma."







            Lade "Eu disse parado porra!!!!!"



            "Enquanto Lade grita Marduck saca a arma e dá um tiro na perna normal do

            Ravideas o derrubando."



            "bang"



            Ravi "Drogaaa!!"

            show ravin at Move((0.0, 0.75), (0.85, 0.75), 2, xanchor=0.5, yanchor=0.5):

                subpixel True

                rotate 0

                linear 1 rotate 180



            Marduck "Se você não vai atirar então nem devia ter sacado a arma, seu idiota."







            "Eles vão até o corpo caído de Ravideas."







            Ravi "Merda!!!"

            show lad at Move((0.0, 0.5), (0.5, 0.5), 2, xanchor=0.5, yanchor=0.5)

            jump cenas













        "sair.":
            "obrigado por ter jogado nosso jogo."

            return



label morte:

    scene preto

    "Parabéns você morreu do único jeito possível nesse jogo sendo um idiota repetitivo"

    "Se quiser culpar alguém culpe Rodrigo Cardoso Corsi ou Poze."

    return



label ricos:

    scene preto

    "Depois de tanto abrir e fechar a maleta magicamente um gazilhão de dinheiros

    apareceu na maleta."

    Lade "Meu deus."

    Marduck "Estamos ricos!!!!!!!"

    "Lade e Marduke desistem da investigação e viajam para as Baransmas e tem uma

    vida feliz como gazilionarios com suas camisas brancas. FIM."

    return
