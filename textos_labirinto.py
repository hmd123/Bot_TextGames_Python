class lab_arvore:
    def _init_(self):

        self.val = None
        self.esq = None
        self.dir = None
        opcoes = None

    def insere_arvore(self,val):
        self.val = val

    def arruma_arvore(self):
        self.val = init

        #constroi filhos
        self.esq = lab_arvore()
        self.esq.esq = lab_arvore()
        self.esq.dir = lab_arvore()
        self.esq.dir.esq = lab_arvore()
        self.esq.dir.esq.esq = lab_arvore()
        self.esq.dir.esq.dir = lab_arvore()
        self.esq.dir.esq.dir.esq = lab_arvore()
        self.esq.dir.esq.dir.dir = lab_arvore()
        self.esq.dir.dir = lab_arvore()
        self.dir = lab_arvore()
        self.dir.esq = lab_arvore()
        self.dir.esq.esq = lab_arvore()
        self.dir.esq.dir = lab_arvore()
        self.dir.dir = lab_arvore()
        self.dir.dir.esq = lab_arvore()
        self.dir.dir.esq.esq = lab_arvore()
        self.dir.dir.esq.dir = lab_arvore()
        self.dir.dir.dir = lab_arvore()
        self.dir.dir.dir.esq = lab_arvore()
        self.dir.dir.dir.esq.esq = lab_arvore()
        self.dir.dir.dir.esq.dir = lab_arvore()
        self.dir.dir.dir.dir = lab_arvore()
        self.dir.dir.dir.dir.esq = lab_arvore()
        self.dir.dir.dir.dir.dir = lab_arvore()


        #atribui valores
        self.esq.val = init_esq
        self.esq.esq.val = init_esq_sim
        self.esq.dir.val = init_esq_nao
        self.esq.dir.esq.val = init_esq_nao_sim
        self.esq.dir.esq.esq.val = init_esq_nao_sim_seqmmmepau
        self.esq.dir.esq.dir.val = init_esq_nao_sim_nao
        self.esq.dir.esq.dir.esq.val = init_esq_nao_sim_nao_carinho
        self.esq.dir.esq.dir.dir.val = init_esq_nao_sim_nao_chuta
        self.esq.dir.dir.val = init_esq_nao_nao
        self.dir.val = init_dir
        self.dir.esq.val = init_dir_esq
        self.dir.esq.esq.val = init_dir_esq_sim
        self.dir.esq.dir.val = init_dir_esq_nao
        self.dir.dir.val = init_dir_dir
        self.dir.dir.esq.val = init_dir_dir_esq
        self.dir.dir.esq.esq.val = init_dir_dir_esq_esq
        self.dir.dir.esq.dir.val = init_dir_dir_esq_teletransport
        self.dir.dir.dir.val = init_dir_dir_dir
        self.dir.dir.dir.esq.val = init_dir_dir_dir_esq
        self.dir.dir.dir.esq.esq.val = init_dir_dir_dir_esq_cqnp
        self.dir.dir.dir.dir.val = init_dir_dir_dir_dir
        self.dir.dir.dir.dir.esq.val = init_dir_dir_dir_dir_ver
        self.dir.dir.dir.dir.dir.val = init_dir_dir_dir_dir_azul

        #atribui se nao tem = 0, esq/dir = 1, sim/nao = 2, ver/azul = 3, car/chuta = 4, seq/nao = 5, esq/telet = 6, cqnp/dir = 7
        self.opcoes = 1
        self.esq.opcoes = 2
        self.esq.esq.opcoes = 0
        self.esq.dir.opcoes = 2
        self.esq.dir.esq.opcoes = 5
        self.esq.dir.esq.esq.opcoes = 0
        self.esq.dir.esq.dir.opcoes = 4
        self.esq.dir.esq.dir.esq.opcoes = 0
        self.esq.dir.esq.dir.dir.opcoes = 0
        self.esq.dir.dir.opcoes = 0
        self.dir.opcoes = 1
        self.dir.esq.opcoes = 2
        self.dir.esq.esq.opcoes = 0
        self.dir.esq.dir.opcoes = 0
        self.dir.dir.opcoes = 1
        self.dir.dir.esq.opcoes = 6
        self.dir.dir.esq.esq.opcoes = 0
        self.dir.dir.esq.dir.opcoes = 0
        self.dir.dir.dir.opcoes = 1
        self.dir.dir.dir.esq.opcoes = 7
        self.dir.dir.dir.esq.esq.opcoes = 0
        self.dir.dir.dir.dir.opcoes = 3
        self.dir.dir.dir.dir.esq.opcoes = 0
        self.dir.dir.dir.dir.dir.opcoes = 0

    #percorre arvore
    def avanca_arvore(self, num):
        if num == 1 and self.esq != None:
            return self.esq
        elif num == 2 and self.dir != None:
            return self.dir


#lista de textos

init = "N??o h?? tempo pra explicar, voc?? est?? em um labirinto!!! Apenas saia da?? o quanto antes \nO caminho se divide em duas vias. Qual voc?? deseja escolher?"

init_dir = "Voc?? se deparou com dois caminhos, o da esquerda ?? trevoso e n??o tem tomada pra carregar seu celular, o da direita voc?? encontra um programa com erros no codigo e que s?? roda porque o Javascript aceita Gambiarra. \nQual voc?? escolhe?"

init_dir_esq = " Um wild pokemon appeared... \nDeseja captura-lo?"

init_dir_esq_sim = "O pokemon se revelou um Snorlax dormindo na frente do caminho. Voc?? vasculha sua mochila e percebe que n??o trouxe uma pokeflauta pra encantar Snorlaxes \n(burrice, quem n??o traz uma pokeflauta na mochila todo dia?). \nVoc?? morre de inani????o simplesmente porque em um jogo desses n??o pode escolher o caminho de voltar"

init_dir_esq_nao = "Voc?? perde todo seu XP por n??o ter capturado um pokemon que podia ser raro e sua conta do Pokemon Go ?? deletada. Pika pika"

init_dir_dir = "Quando voc?? chega na sala, de repente se faz ouvir a voz de um narrador na sua cabe??a e em todo o redor - \n'Ap??s acordar em um labirinto misterioso, o personagem, confuso e assustado, havia decidido sair daquele lugar custe o que custar. \nO personagem ent??o tinha seguido o caminho da direita, confiante de que estava no caminho certo, se deparando ent??o com promessas de caminhos ainda mais intraquilizantes, escolheu mais uma vez o caminho da direita, onde chega em uma sala em que uma voz bela e elegante narra toda sua hist??ria at?? ali' \n'Ap??s ouvir essa maravilhosa voz, o personagem DECIDE pegar o caminho da direita'"

init_dir_dir_esq = "'O personagem aparentemente possui algum problema de memoria, j?? que no caminho anterior havia DECIDIDO pegar o caminho da direita' \n'O personagem sabe agora que tem de seguir a RAZ??O e para consertar suas falhas decide pegar um TELETRANSPORTADOR que estava coincidentemente colocado a sua frente e com letras garrafais, podia-se ler *teletransportador que o leva de volta para o inicio da sua jornada. Aproveite e avalie se puder o produto em nosso aplicativo*' (n??o recomend??vel ir pela esquerda)"

init_dir_dir_esq_esq = "'Tornando-se evidente que o personagem possui um s??rio problema em seguir dire????es, acontece algo inesperado: Um po??o de acido que n??o estava ali momentos antes, se materializa e draga o corpo do personagem ?? sua infeliz morte'. Voc?? passa os ultimos segundos de sua vida pensando em como odeia esse narrador"

init_dir_dir_esq_teletransport = "Vushhhhhhh *sons de teletransporte (n??o ria, voc?? nunca ouviu um pra dizer que n??o ?? assim)*"

init_dir_dir_dir = "'Enquanto anda pelo belo caminho que o personagem escolheu (cheio de flores e p??ssaros cantantes), ele come??a a refletir sobre sua posi????o na vida e como ?? privilegiado por poder fazer as PR??PIAS escolhas. \nAgora mesmo ele est?? pensando no caminho que ele pr??prio escolheu e sobre como pode decidir as coisas por s?? mesmo, est?? pensando tamb??m no narrador que est?? narrando seus pensamentos enquanto ele pensa nisso e sua cabe??a come??a a dar um n??. Enfim, o personagem se sente grato por ter esse livre arb??trio e que nada seja como um programa de computador, hahaha programa de computador... De onde o personagem tira essas id??ias?' \n 'Em uma nova via de dois caminhos que aparece na frente do personagem (estranho como s?? parecem haver sempre apenas duas op????es nesse universo), o personagem ergue sua cabe??a, confiante, e SABE COM TODA CERTEZA que vai pegar o da direita'"

init_dir_dir_dir_dir = "'No novo caminho em que o personagem percorre, sua situa????o psicologica se altera. Nesse momento, tendo passado por muitas experiencias e j?? ciente de que acumulara bastante sabedoria no tempo entre a situa????o inicial em que ele acordou no labirinto e o agora, o personagem (cujo nome ser?? substituido agora por -h- j?? que o narrador est?? cansado de digit... ops, quer dizer, falar personagem) passa a ter novos pontos de vistas que nunca antes haviam acorrido a sua mente. - Afinal - est?? pensando h - Serei eu realmente senhorx do meu pr??pio destino? Afinal, at?? o momento tudo que fiz foi seguir caminhos j?? pr??-definidos, sem falar nos ultimos tempos, que tenho seguido as ordens implicitas de um narrador bizarro que provavelmente est?? tomando muito caf?? enquanto faz seu trabalho - E assim, h iniciou seu processo de racioc??nio conciente, que ?? algo pouco buscado nos dias de hoje, e pensamentos revolucionarios come??aram a brotar da sua cabe??a. Ap??s ter uma epifania, finalmente descobriu o que precisava fazer, h iria acabar de uma vez por toda com essa maquina que regia a sociedade e que controlava cada mente humana de forma a impedir que este alcan??e seu potencial, iria acabar com essa opress??o. Basta percorrer mais alguns caminhos, n??o importa quantos, para realizar seu novo sonho. \n 'Ap??s se encher de determina????o, h alcan??a duas sa??das que levam ?? liberdade. Sabendo do cr??tico que essa escolha representa para sua vida, h se concentra em sua decis??o que ?? enfim, pr??pia. De um lado, o caminho azul, de outro, o caminho vermelho'","[Azul, Vermelho]"

init_dir_dir_dir_dir_azul = "'h acha a sa??da para o labirinto e sua felicidade quase explode quando consegue voltar para a sociedade. Sentindo que tudo que passara at?? o dado momento fora um teste para aprender a verdade sobre a vida, o universo e tudo mais, h se incumbe o dever de libertar os outros de suas pris??es tamb??m. h passa o resto de sua vida xingando nas redes sociais e falando que todos tem que concordar com suas id??ias pois ?? o unico ser detentor da verdade. h apagou o labirinto da m??moria e nunca se preocupou em saber mais sobre ele ou que segredos ocultos escondia, contudo, n??o precisava, afinal h havia tra??ado seu caminho atrav??s de suas pr??pias decis??es' - Finaliza o narrador"

init_dir_dir_dir_dir_ver = "'O personagem encontra um beco sem sa??da e avista uma mensagem que est?? escrita no muro - N??O PROCURE O CAMINHO SECRETO NO IN??CIO DA JORNADA, N??O PROCURE O *JOGO DO LABIRINTO*. N??O PROCURE, N??O DIGITE, N??O QUEIRA SABER DA TRISTE REALIDADE! - h fica intrigado com a mensagem, sente-se pertubado. Analisa de novo a parte que estava ressaltada -jogo do labirinto- fez uma anota????o mental para nunca escolher o caminho secreto, o caminho -jogo do labirinto-'"

init_dir_dir_dir_esq = "'ahhh. O personagem estava indo t??o bem, prosseguia em um caminho com uma est??ria, um bom enredo. Sabe quanto tempo foi gasto pra produzir uma est??ria de boa qualidade, personagem?' \n Mas o fulano joga tudo fora ao escolher um CAMINHO QUE N??O PODE. Contudo um narrador sensato n??o pode deixar que as coisas desandem desse jeito, ent??o algumas mudan??as ir??o ocorrer por aqui. Primeiro, o personagem VAI SEGUIR PELA DIREITA para consertar o estrago que fez, assim ir?? respeitar o rumo correto. H?? tamb??m uma pequena possibilidade do personagem passar por um caminho denominado - caminho que n??o pode - que ?? um nome bastante idiota para um caminho, obviamente n??o ir?? mudar em nada o rumo em que foi organizado a vida dele, ent??o ?? melhor nem tentar"

init_dir_dir_dir_esq_cqnp = "'O personagem ?? muito teimoso e decidiu contrariar o rumo correto. Por ironia do destino, ao passar pelo caminho que n??o deveria ele magicamente retorna ao campo florido que passara antes...'"

init_esq = "Um Gandalf chapado com uma bengala nada elegante se materializa: \n'Voc?? deve vir comigo pra jogar uns bagulhos no fogo' Falou ele. \nVoc?? tem a op????o de dizer Sim ou N??o"

init_esq_sim = " Ele te levou pra um vulc??o. Contudo, no meio do caminho ele te troca por um baixinho tamb??m chapado e voc?? fica no ch??o chorando de frusta????o."

init_esq_nao = "Furioso ele grita 'You shall not pass!', mas da?? voc?? percebe que ele est?? de costas para um muro... \nComo o caminho est?? livre, voc?? segue em frente lembrando que precisa fazer uma marotona de um trilogia cujo nome n??o se lembra ainda. \nEm frente, voc?? avista a entrada de uma Universidade \nVoc?? descobre que tem a oportunidade de fazer um curso superior. Est?? preparade para entrar para a vida universit??ria e contribuir com sua parte para essa bel??ssima sociedade em que vivemos? Tem a op????o de responder sim ou N??O"

init_esq_nao_nao = "Voc?? pega outro caminho e tem um final feliz."

init_esq_nao_sim = "Humm... Acho que a escolha n??o foi muito adequada. Fa??amos o seguinte, vamos tentar de novo. \nAinda na entrada dessa maravilhosa Universidade, voc?? avista outro port??o que tem de atravessar, isso te faz REPENSAR se quer realmente ser estudante desse incrivel lugar. Voc?? deseja ser estudante da Universidade? \nSe quiser mesmo, responda 'Sim, eu quero muito muito muito entrar para a Universidade'(exatamente desse jeito). Agora, se n??o estiver afim eu vou te apoiar, basta responder com 'n??o' que vou entender que voc?? ?? inteligente"

init_esq_nao_sim_seqmmmepau = "Voc?? ?? prese no primeiro m??s de aula por porte de entorpecentes, numero excessivo de faltas e posi????o pol??tica duvidosa em rela????o ao governo. \nNa cadeia voc?? finalmente tem uma boa noite de sono, depois de eras sem saber o que ?? isso, faz amizade com outros detentos e organiza uma empresa para a comercializa????o de material art??stico e tur??stico no litoral"

init_esq_nao_sim_nao = "Agora sim. Voc?? pega outro caminho \nComo voc?? fez uma tolice de n??o ter dito 'n??o' mais cedo, agora encontrou uma dungeon. \nBarrando o caminho h?? um lindo e adoravel cachorro da Uni, ele late e abana o rabo. \nVoc?? tem a op????o de chut??-lo para fora do caminho ou fazer carinho nele"

init_esq_nao_sim_nao_chuta = "Voc?? chuta o cachorro para fora do caminho. Ele late e gane, demonstrando que est?? com a pata machucada. \nVoc??, com seu cora????o frio, ignora o animal e continua a andar em frente. \nVoc?? caminha at?? o final do corredor e se depara com um gigante. Ele te avista com um olhar indiferente e decide chuta-lo para fora do caminho. \nVoc?? grita e choraminga vendo que sua perna quebrou. \nO gigante, com seu cora????o frio, ignora voc?? e continua a andar em frente. \nO gigante quando alcan??a o final do corredor se depara com um tit??..."

init_esq_nao_sim_nao_carinho = "O cachorro acaba te mordendo... \nComo ?? um ser imundo e nojento, voc?? acaba passando varias doen??as pra ele e ele morre nos seus bra??os :'("

init_jogolabirinto = "Voc?? percebe que ?? na verdade apenas o fruto da imagina????o criado para um jogo e com a finalidade de entreter os outros. Percebe tamb??m que os outros s??o parte de um jogo maior tamb??m, e esse jogo ?? parte de um outro ainda maior. Sua cabe??a buga e voc?? cai no ch??o desesperado, a?? voc?? pensa em deletar seus pixels e dar game over. Mas depois voc?? reconsidera e decide ir pra um jogo melhor (e mais bem feito), voc?? vai pro colheita feliz e vive feliz... Mais tarde percebe que n??o tem nenhum amigo jogando e assim n??o d?? pra roubar de ningu??m, voc?? fica muito triste e agora cansado desse texto longo, decide ser programador. Fim. "
