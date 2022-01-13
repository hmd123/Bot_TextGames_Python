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

init = "Não há tempo pra explicar, você está em um labirinto!!! Apenas saia daí o quanto antes \nO caminho se divide em duas vias. Qual você deseja escolher?"

init_dir = "Você se deparou com dois caminhos, o da esquerda é trevoso e não tem tomada pra carregar seu celular, o da direita você encontra um programa com erros no codigo e que só roda porque o Javascript aceita Gambiarra. \nQual você escolhe?"

init_dir_esq = " Um wild pokemon appeared... \nDeseja captura-lo?"

init_dir_esq_sim = "O pokemon se revelou um Snorlax dormindo na frente do caminho. Você vasculha sua mochila e percebe que não trouxe uma pokeflauta pra encantar Snorlaxes \n(burrice, quem não traz uma pokeflauta na mochila todo dia?). \nVocê morre de inanição simplesmente porque em um jogo desses não pode escolher o caminho de voltar"

init_dir_esq_nao = "Você perde todo seu XP por não ter capturado um pokemon que podia ser raro e sua conta do Pokemon Go é deletada. Pika pika"

init_dir_dir = "Quando você chega na sala, de repente se faz ouvir a voz de um narrador na sua cabeça e em todo o redor - \n'Após acordar em um labirinto misterioso, o personagem, confuso e assustado, havia decidido sair daquele lugar custe o que custar. \nO personagem então tinha seguido o caminho da direita, confiante de que estava no caminho certo, se deparando então com promessas de caminhos ainda mais intraquilizantes, escolheu mais uma vez o caminho da direita, onde chega em uma sala em que uma voz bela e elegante narra toda sua história até ali' \n'Após ouvir essa maravilhosa voz, o personagem DECIDE pegar o caminho da direita'"

init_dir_dir_esq = "'O personagem aparentemente possui algum problema de memoria, já que no caminho anterior havia DECIDIDO pegar o caminho da direita' \n'O personagem sabe agora que tem de seguir a RAZÃO e para consertar suas falhas decide pegar um TELETRANSPORTADOR que estava coincidentemente colocado a sua frente e com letras garrafais, podia-se ler *teletransportador que o leva de volta para o inicio da sua jornada. Aproveite e avalie se puder o produto em nosso aplicativo*' (não recomendável ir pela esquerda)"

init_dir_dir_esq_esq = "'Tornando-se evidente que o personagem possui um sério problema em seguir direções, acontece algo inesperado: Um poço de acido que não estava ali momentos antes, se materializa e draga o corpo do personagem à sua infeliz morte'. Você passa os ultimos segundos de sua vida pensando em como odeia esse narrador"

init_dir_dir_esq_teletransport = "Vushhhhhhh *sons de teletransporte (não ria, você nunca ouviu um pra dizer que não é assim)*"

init_dir_dir_dir = "'Enquanto anda pelo belo caminho que o personagem escolheu (cheio de flores e pássaros cantantes), ele começa a refletir sobre sua posição na vida e como é privilegiado por poder fazer as PRÓPIAS escolhas. \nAgora mesmo ele está pensando no caminho que ele próprio escolheu e sobre como pode decidir as coisas por sí mesmo, está pensando também no narrador que está narrando seus pensamentos enquanto ele pensa nisso e sua cabeça começa a dar um nó. Enfim, o personagem se sente grato por ter esse livre arbítrio e que nada seja como um programa de computador, hahaha programa de computador... De onde o personagem tira essas idéias?' \n 'Em uma nova via de dois caminhos que aparece na frente do personagem (estranho como só parecem haver sempre apenas duas opções nesse universo), o personagem ergue sua cabeça, confiante, e SABE COM TODA CERTEZA que vai pegar o da direita'"

init_dir_dir_dir_dir = "'No novo caminho em que o personagem percorre, sua situação psicologica se altera. Nesse momento, tendo passado por muitas experiencias e já ciente de que acumulara bastante sabedoria no tempo entre a situação inicial em que ele acordou no labirinto e o agora, o personagem (cujo nome será substituido agora por -h- já que o narrador está cansado de digit... ops, quer dizer, falar personagem) passa a ter novos pontos de vistas que nunca antes haviam acorrido a sua mente. - Afinal - está pensando h - Serei eu realmente senhorx do meu própio destino? Afinal, até o momento tudo que fiz foi seguir caminhos já pré-definidos, sem falar nos ultimos tempos, que tenho seguido as ordens implicitas de um narrador bizarro que provavelmente está tomando muito café enquanto faz seu trabalho - E assim, h iniciou seu processo de raciocínio conciente, que é algo pouco buscado nos dias de hoje, e pensamentos revolucionarios começaram a brotar da sua cabeça. Após ter uma epifania, finalmente descobriu o que precisava fazer, h iria acabar de uma vez por toda com essa maquina que regia a sociedade e que controlava cada mente humana de forma a impedir que este alcançe seu potencial, iria acabar com essa opressão. Basta percorrer mais alguns caminhos, não importa quantos, para realizar seu novo sonho. \n 'Após se encher de determinação, h alcança duas saídas que levam à liberdade. Sabendo do crítico que essa escolha representa para sua vida, h se concentra em sua decisão que é enfim, própia. De um lado, o caminho azul, de outro, o caminho vermelho'","[Azul, Vermelho]"

init_dir_dir_dir_dir_azul = "'h acha a saída para o labirinto e sua felicidade quase explode quando consegue voltar para a sociedade. Sentindo que tudo que passara até o dado momento fora um teste para aprender a verdade sobre a vida, o universo e tudo mais, h se incumbe o dever de libertar os outros de suas prisões também. h passa o resto de sua vida xingando nas redes sociais e falando que todos tem que concordar com suas idéias pois é o unico ser detentor da verdade. h apagou o labirinto da mémoria e nunca se preocupou em saber mais sobre ele ou que segredos ocultos escondia, contudo, não precisava, afinal h havia traçado seu caminho através de suas própias decisões' - Finaliza o narrador"

init_dir_dir_dir_dir_ver = "'O personagem encontra um beco sem saída e avista uma mensagem que está escrita no muro - NÃO PROCURE O CAMINHO SECRETO NO INÍCIO DA JORNADA, NÃO PROCURE O *JOGO DO LABIRINTO*. NÃO PROCURE, NÃO DIGITE, NÃO QUEIRA SABER DA TRISTE REALIDADE! - h fica intrigado com a mensagem, sente-se pertubado. Analisa de novo a parte que estava ressaltada -jogo do labirinto- fez uma anotação mental para nunca escolher o caminho secreto, o caminho -jogo do labirinto-'"

init_dir_dir_dir_esq = "'ahhh. O personagem estava indo tão bem, prosseguia em um caminho com uma estória, um bom enredo. Sabe quanto tempo foi gasto pra produzir uma estória de boa qualidade, personagem?' \n Mas o fulano joga tudo fora ao escolher um CAMINHO QUE NÃO PODE. Contudo um narrador sensato não pode deixar que as coisas desandem desse jeito, então algumas mudanças irão ocorrer por aqui. Primeiro, o personagem VAI SEGUIR PELA DIREITA para consertar o estrago que fez, assim irá respeitar o rumo correto. Há também uma pequena possibilidade do personagem passar por um caminho denominado - caminho que não pode - que é um nome bastante idiota para um caminho, obviamente não irá mudar em nada o rumo em que foi organizado a vida dele, então é melhor nem tentar"

init_dir_dir_dir_esq_cqnp = "'O personagem é muito teimoso e decidiu contrariar o rumo correto. Por ironia do destino, ao passar pelo caminho que não deveria ele magicamente retorna ao campo florido que passara antes...'"

init_esq = "Um Gandalf chapado com uma bengala nada elegante se materializa: \n'Você deve vir comigo pra jogar uns bagulhos no fogo' Falou ele. \nVocê tem a opção de dizer Sim ou Não"

init_esq_sim = " Ele te levou pra um vulcão. Contudo, no meio do caminho ele te troca por um baixinho também chapado e você fica no chão chorando de frustação."

init_esq_nao = "Furioso ele grita 'You shall not pass!', mas daí você percebe que ele está de costas para um muro... \nComo o caminho está livre, você segue em frente lembrando que precisa fazer uma marotona de um trilogia cujo nome não se lembra ainda. \nEm frente, você avista a entrada de uma Universidade \nVocê descobre que tem a oportunidade de fazer um curso superior. Está preparade para entrar para a vida universitária e contribuir com sua parte para essa belíssima sociedade em que vivemos? Tem a opção de responder sim ou NÃO"

init_esq_nao_nao = "Você pega outro caminho e tem um final feliz."

init_esq_nao_sim = "Humm... Acho que a escolha não foi muito adequada. Façamos o seguinte, vamos tentar de novo. \nAinda na entrada dessa maravilhosa Universidade, você avista outro portão que tem de atravessar, isso te faz REPENSAR se quer realmente ser estudante desse incrivel lugar. Você deseja ser estudante da Universidade? \nSe quiser mesmo, responda 'Sim, eu quero muito muito muito entrar para a Universidade'(exatamente desse jeito). Agora, se não estiver afim eu vou te apoiar, basta responder com 'não' que vou entender que você é inteligente"

init_esq_nao_sim_seqmmmepau = "Você é prese no primeiro mês de aula por porte de entorpecentes, numero excessivo de faltas e posição política duvidosa em relação ao governo. \nNa cadeia você finalmente tem uma boa noite de sono, depois de eras sem saber o que é isso, faz amizade com outros detentos e organiza uma empresa para a comercialização de material artístico e turístico no litoral"

init_esq_nao_sim_nao = "Agora sim. Você pega outro caminho \nComo você fez uma tolice de não ter dito 'não' mais cedo, agora encontrou uma dungeon. \nBarrando o caminho há um lindo e adoravel cachorro da Uni, ele late e abana o rabo. \nVocê tem a opção de chutá-lo para fora do caminho ou fazer carinho nele"

init_esq_nao_sim_nao_chuta = "Você chuta o cachorro para fora do caminho. Ele late e gane, demonstrando que está com a pata machucada. \nVocê, com seu coração frio, ignora o animal e continua a andar em frente. \nVocê caminha até o final do corredor e se depara com um gigante. Ele te avista com um olhar indiferente e decide chuta-lo para fora do caminho. \nVocê grita e choraminga vendo que sua perna quebrou. \nO gigante, com seu coração frio, ignora você e continua a andar em frente. \nO gigante quando alcança o final do corredor se depara com um titã..."

init_esq_nao_sim_nao_carinho = "O cachorro acaba te mordendo... \nComo é um ser imundo e nojento, você acaba passando varias doenças pra ele e ele morre nos seus braços :'("

init_jogolabirinto = "Você percebe que é na verdade apenas o fruto da imaginação criado para um jogo e com a finalidade de entreter os outros. Percebe também que os outros são parte de um jogo maior também, e esse jogo é parte de um outro ainda maior. Sua cabeça buga e você cai no chão desesperado, aí você pensa em deletar seus pixels e dar game over. Mas depois você reconsidera e decide ir pra um jogo melhor (e mais bem feito), você vai pro colheita feliz e vive feliz... Mais tarde percebe que não tem nenhum amigo jogando e assim não dá pra roubar de ninguém, você fica muito triste e agora cansado desse texto longo, decide ser programador. Fim. "
