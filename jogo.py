import ficha
import inventario
import combate
import dado
personagem = {}
cap1 = (f"O clamor dos espectadores excitados some gradualmente atrás de você, que se aventura cada vez mais fundo na penumbra do túnel da caverna.Grandes cristais pendem do teto do túnel a intervalos de 20 metros, irradiando uma luz suave, apenas suficiente para que se veja por onde anda. À medida que seus olhos vão pouco a pouco se acostumando à quase escuridão, você começa a ver movimentos à sua volta. Aranhas e besouros sobem e descem pelas paredes entalhadas, desaparecendo em frestas e gretas ao sentir sua aproximação; ratazanas e ratos correm pelo chão à sua frente. Pingos de água caem em pequenas poças com um sinistro som gotejante que ecoa pelo túnel. O ar é frio, úmido e pesado. Depois de caminhar lentamente pelo túnel por uns cinco minutos, você chega a uma mesa de pedra encostada contra a parede à sua esquerda. Nela há seis caixas, uma das quais tem o seu nome pintado na tampa. Se você quiser abrir a caixa, digite 270. Se preferir continuar caminhando para o norte, digite 66.")
cap2="O Escorpião consegue prendê-lo nas garras por tempo suficiente para mover a cauda segmentada para frente, por sobre a cabeça, e cravar em você o ferrão venenoso. O efeito é fatal, e você desaba no chão da Arena da Morte, imaginando se Throm conseguirá vencer."
cap3="O Gnomo sacode a cabeça e diz: Temo que você não tenha passado pela Prova dos Campeões. Os segredos do Calabouço da Morte do Barão Sukumvit ficarão guardados por mais um ano, pois você não terá permissão para sair daqui. Você foi indicado para ser meu servo pelo resto dos seus dias; preparará e modificará o subterrâneo para competidores futuros. Talvez em outra vida você tenha sucesso..."
cap4="Na escuridão total, você não vê a curva do cano para baixo. Escorrega e, incapaz de se segurar no cano cheio de limo, desliza pela borda. Seus gritos ecoam pelo tubo, enquanto você cai 50 metros até o fundo. Você fracassou na Prova dos Campeões."
cap5="Você se arrasta pelo chão e se vê no covil de uma tribo de TROGLODITAS. Ao engatinhar passando por eles, sua bainha bate em uma pedra. "
cap6="Sabendo que o Mantécora disparará os espinhos da cauda, Você corre para se proteger atrás de um dos pilares. Antes que consiga chegar lá, uma saraivada de espinhos voa pelo ar, e um deles penetra-lhe o braço. Você perde 2 pontos de ENERGIA. Se ainda estiver vivo, não perca tempo e ataque o Mantécora com espada, antes que ele possa disparar mais espinhos.\nMANTÉCORA	\nHABILIDADE 11	\nENERGIA 11 \nSe você vencer, vá para 364."
cap7="Antes que você tenha tempo de chegar a uma porta, o rochedo já está sobre você, que grita de dor e medo quando ele o esmaga no chão. Sua aventura termina aqui."
cap8="O Demônio do Espelho agarra-o pelo pulso. Imediatamente, ele começa a puxá-lo na direção do espelho. A força dele é incrível, e, apesar de todos os seus esforços, você não consegue evitar que o arraste progressivamente na direção do espelho. Quando ele toca o espelho, parece desaparecer diretamente através dele. Horrorizado, você vê seu próprio braço desaparecer, seguido pelo resto do corpo. Você está agora em um mundo de espelhos de outra dimensão, do qual jamais retornará."
cap9="Os Hobgoblins não têm nada que lhe seja útil, por isso você resolve abrir o saco no chão. Dentro, acha uma moringa de barro arrolhada. Você a desarrolha e cheira o líquido que contém. O odor é penetrante e acre. Se quiser beber um pouco do líquido, vá para 158. Se quiser mergulhar um pedaço de pano nele, vá para 375."
cap10="Ainda correndo o mais rápido possível, você enfia a mão na mochila e tira o tubo de madeira. Seu plano é ficar sob a água, respirando pelo tubo. Com sorte, os Trogloditas pensarão que você será arrastado até a morte rio abaixo, pois a torrente desaparece nas profundezas da montanha. Você segura o tubo entre os dentes e mergulha na água. Segurando-se em um dos pilares da ponte embaixo d'água, você fica absolutamente imóvel por 10 minutos. Quando finalmente acha que os Trogloditas foram embora, você sobe à superfície e olha em volta. Não há ninguém à vista, e você sai do rio e atravessa a ponte para a margem norte. Quaisquer Provisões restantes que você possa ter estão agora encharcadas e imprestáveis. Risque-as de sua Folha de Aventuras. Você segue pela vasta caverna até que, finalmente, vê um túnel na parede do outro lado. Você caminha até uma pesada porta de madeira, que está trancada. Se você tiver uma chave de ferro, vá para 86. Se não tiver, vá para 276."
cap11="Você olha para baixo e vê os corpos esparramados dos Guardiões Voadores imóveis no chão. Então, começa a forçar o olho de esmeralda do ídolo para retirá-lo com a ponta da espada. Finalmente, ele se solta, e você fica surpreso com o peso da jóia. Esperando que possa ser útil mais tarde, você o coloca na mochila. Se quiser agora retirar o olho direito, vá para 140. Se preferir descer do ídolo, vá para 46."
cap12="A porta abre para um grande aposento iluminado por velas, repleto das mais extraordinárias estátuas, de aparência real, representando guerreiros e cavaleiros. Um velho de cabelos brancos, trajando trapos esfarrapados, salta de trás de uma das estátuas e começa a dar risinhos. Uma centelha nos olhos dele faz com que você pense que algo se esconde por trás daquela aparência de idiota. Numa voz estridente, ele diz: Bom, mais uma pedra para meu jardim. Fico feliz que você tenha vindo se juntar a seus amigos. Sou um homem justo, e por isso vou lhe fazer uma pergunta. Se responder corretamente, ficará livre - mas, se sua resposta estiver errada, eu o transformarei em pedra! Ele volta a dar risadinhas, obviamente feliz com sua chegada. Você:\nEsperará pela pergunta?(Vá para 382) \nVai atacá-lo com sua espada?(Vá para 195) \nCorrerá para a porta?(Vá para 250)"
cap13="O túnel faz uma curva abrupta para a esquerda e se dirige para o norte, tanto quanto a sua vista alcança. As pegadas que você está seguindo começam a sumir à medida que o túnel vai ficando mais seco. Logo não vê mais o teto gotejante e as poças no chão. Você repara que o ar está se tornando mais quente, e se vê ofegante, embora esteja andando bem devagar. Em uma pequena reentrância da parede da esquerda, você vê um pedaço de bambu na vertical. Levantando-o, repara que ele está cheio de um líquido claro. Sua garganta está dolorosamente seca, e você se sente um pouco tonto por causa do calor no túnel. Se quiser beber o líquido, vá para 141. Se não quiser se arriscar a beber e preferir continuar para o norte, vá para 182."
cap14="O túnel conduz a uma câmara escura, coberta de espessas teias de aranha. Abrindo caminho entre elas, você tropeça em um pequeno cofre de madeira. Se quiser tentar abrir o cofre, vá para 157. Se preferir continuar para o norte, vá para 310."
cap15="Uma sensação de cócegas desce pela sua espinha enquanto você se arrasta cuidadosamente para fora do aposento. De volta ao túnel, você solta um suspiro de alívio e fecha a porta com força. Feliz com sua boa sorte, parte para o oeste mais uma vez. Vá para 74."
cap16="Você só teve tempo de ouvir o Gnomo dizer: Três crânios, antes que um raio branco de energia disparasse da fechadura e o atingisse no peito, derrubando-o inconsciente. Jogue um dado, some 1 ao número obtido e reduza este total da sua ENERGIA. Se você ainda estiver vivo, recupera a consciência e o Gnomo manda que tente de novo. Você escolheu as gemas erradas da outra vez; portanto, não tentará aquela combinação novamente.\nEsmeralda	Diamante	Safira	(Fique em 16)\nDiamante	Safira	Esmeralda	(Vá para 392)\nSafira	Esmeralda	Diamante (Vá para 177)\n Esmeralda	Safira	Diamante	(Vá para 287)\nDiamante  Esmeralda	Safira	(Vá para 132)\nSafira	Diamante	Esmeralda	(Vá para 249)"
cap17="Você não é forte o bastante para forçar e abrir a pesada porta. A água já está na cintura agora, e você está exausto por causa dos esforços. O nível da água sobe rapidamente, e você se vê boiando cada vez mais alto. Até que seu rosto fica imprensado contra o teto. Logo fica completamente imerso e não tem como prender a respiração por mais tempo. Sua aventura termina aqui."
cap18="Para sorte sua, os dentes da naja se cravam na munhequeira de couro que você está usando. A serpente se enrosca de novo bem depressa, pronta para lançar outro ataque, quando o Anão ordena que você faça mais uma tentativa. Jogue dois dados. Se o total for igual ou menor que sua HABILIDADE, vá para 55. Se o total for maior que sua HABILIDADE, vá para 202"
cap19="Você não consegue resistir ao olhar hipnótico da Medusa quando seus olhares se encontram. Sente os membros enrijecerem e entra em pânico, indefeso, enquanto se transforma em pedra. Sua aventura termina aqui."
cap20="Somente sua incrível força poderia resistir à mordida da aranha venenosa. Contudo, você está enfraquecido e repara que sua mão está tremendo ao colocar a Peça de Ouro no bolso. Reduza sua HABILIDADE em 1 ponto. Você amaldiçoa a pessoa que largou a mochila e parte para o norte de novo. Vá para 279."
cap21="O ferimento não teve qualquer efeito sobre a Besta Sangrenta, que continua a atacá-lo tão furiosamente quanto antes. Continue o combate e, logo que vença uma Série de Ataques." 
cap22="Embora vocês fiquem um pouco perturbados na companhia um do outro, sabendo que só pode haver um vencedor na Prova dos Campeões, ambos estão contentes por compartilhar os benefícios de uma aliança temporária. Contam um ao outro as explorações que fizeram até agora, falam dos monstros e armadilhas que encontraram e dos perigos que venceram. Caminhando em frente, vocês logo chegam à borda de um poço largo. É profundo e escuro demais para verem-lhe o fundo. O Bárbaro se oferece para ajudá-lo descer ao fundo com a corda dele, dizendo que tem uma tocha com a qual você poderá iluminar o caminho. Você:\nAceitará a oferta do Bárbaro?	(Vá para 63)\nOferece-se para ajudar a descida dele, já que ele está tão ansioso para investigar o poço?	(Vá para 184)\nSugerirá que, em vez disso, ambos pulem por cima do poço?	(Vá para 311)"
cap23="O papel traz uma advertência simples, escrita em sangue seco: Cuidado com os Juízes da Prova. Você recoloca o papel no prego e corre de volta pelo túnel para se reunir ao Bárbaro. Vá para 154."
cap24="Colocada em uma alcova em arco na parede do túnel, você vê uma cadeira de madeira ornamentada, esculpida na forma de uma ave de rapina de aparência demoníaca. Se você quiser se sentar na cadeira, vá para 324. Se preferir continuar seguindo para o norte, vá para 188."
cap25="Embora a temperatura no túnel esteja mais alta do que você conseguiria normalmente tolerar, o líquido do bambu mantém-no vivo. Vá para 197."
cap26="A pílula faz com que você se sinta mole e letárgico. Você perde 2 pontos de HABILIDADE. O Anão diz que agora você pode prosseguir para o segundo estágio do teste. Ele pega uma cesta de vime e lhe diz que ela contém uma serpente. Vira a cesta e a serpente cai no chão. É uma naja, e se ergue no ar, pronta para dar o bote. O Anão diz que pretende testar suas reações. Você deverá agarrar a naja, com as mãos nuas, pelo pescoço, evitando as presas mortais. Você se agacha, tensionando os músculos para o momento decisivo. Jogue dois dados. Se o total for igual ou menor que sua HABILIDADE, vá para 55. Se o total for maior que sua HABILIDADE, vá para 202."
cap27="Você caminha até o apavorado homem e corta a corrente com sua espada. Ele cai de joelhos e se inclina, agradecendo, repetidamente. Diz que, há quatro anos, entrou na Prova dos Campeões, mas fracassou. Ele caiu em um poço e teve que ser resgatado por um Juiz da Prova, um dos administradores do calabouço do Barão Sukumvit. Foi-lhe, então, oferecida a opção de morrer ou servir como lacaio no Calabouço da Morte. Para sobreviver, ele trabalhou como escravo, até que não pôde mais suportar e tentou escapar. Lástima, não teve êxito e foi capturado pelos Orcas, os guardas volantes do Juiz da Prova. Como corretivo, cortaram-lhe uma das mãos e condenaram-no a um ano de prisão nessa cela. Você pergunta se ele tem alguma informação que lhe possa ser útil. Ele coça a cabeça: “Bem, não cheguei a me sair exatamente bem aqui, mas, de fato, sei que você precisa juntar gemas e pedras preciosas, se espera escapar. Não sei por que, mas é isso.” Sem mais dizer, o esfarrapado prisioneiro dispara para fora do aposento, virando à esquerda no túnel. Você resolve prosseguir para o norte e vira à direita no túnel. Vá para 78."
cap28="A cota de malha do Anão é de ferro da melhor qualidade, obviamente feita por um mestre armeiro. Você a tira do corpo dele e a coloca sobre sua cabeça. Acrescente 1 ponto de HABILIDADE. Não há mais nada de útil na câmara, portanto você decide investigar o novo túnel. Vá para 213."
cap29="O túnel conduz ao norte por alguma distância, antes de chegar a um beco sem saída. A entrada de um escorrega se projeta da parede leste do túnel. Parece ser a única maneira de sair. Você resolve se arriscar e sobe no escorrega. Deslizando suavemente, você desce em um aposento, onde aterrissa de costas. Vá para 90."
cap30="Dando um passo à frente, você salta para a borda do outro lado do poço. Teste sua Sorte. Se você tiver sorte, vá para 160. Se não tiver sorte, vá para 319."
cap31="O Gnomo sorri e diz: “Bom. Agora, você possui uma safira?” Se você de fato tiver uma safira, vá para 376. Se não, vá para 3."
cap32="Você logo chega a uma outra encruzilhada no túnel. Um braço leva para o leste, mas as pegadas úmidas que você vem seguindo continuam para o norte, e você resolve continuar na trilha delas. Vá para 37."
cap33="Foi um erro ter tateado no interior do buraco com o braço da espada. Está coberto de marcas de sucção e dá a sensação de ter sido esmagado. Você perde 3 pontos de HABILIDADE. Você dá uma espiada para dentro do buraco e vê o toco do tentáculo ensanguentado que pende inerte. Cuidadosamente, retira o gancho e a bolsa de couro, na qual encontra um minúsculo sino de latão. Você guarda suas novas posses na mochila e segue para o norte. Vá para 292."
cap34="Você tenta forçar por baixo da esmeralda com a ponta da espada. Para sua grande surpresa, a esmeralda se despedaça com o contato, soltando um jato de gás venenoso diretamente no seu rosto. O gás o faz desmaiar, e você solta a corda, despenca do ídolo e cai no chão de pedra. Sua aventura termina aqui."
cap35="O túnel continua para o oeste por várias centenas de metros, terminando finalmente em alguns degraus que conduzem a um alçapão fechado. Você sobe os degraus lentamente, ouvindo vozes abafadas acima. Na penumbra, você pode ver que o alçapão não está trancado. Se quiser bater na porta do alçapão, vá para 333. Se preferir irromper pela porta com a espada desembainhada, vá para 124."
cap36="Embora você jamais tenha corrido tanto em toda a sua vida, o rochedo chega cada vez mais perto. Jogue dois dados. Se o total for igual ou menor que os seus índices tanto de HABILIDADE quanto de ENERGIA, vá para 340. Se o total for maior que qualquer um dos seus índices de HABILIDADE ou ENERGIA, volte para 7."
cap37="A passagem se alarga em uma ampla caverna, mais escura, mas muito mais seca. As pegadas desaparecem gradualmente à sua frente. Há um grande ídolo no centro da caverna, com cerca de seis metros de altura. Os olhos da estátua são jóias, cada uma do tamanho do seu punho. Duas criaturas empalhadas, com aparência de pássaros, encontram-se de pé em cada lado do ídolo. Se você quiser subir no ídolo para pegar as jóias, vá para 351. Se preferir atravessar a caverna para o túnel na parede do outro lado, vá para 239."
cap38="Em silêncio, o homem fica de lado enquanto você engole a água e devora o pão. Uma dor aguda lhe invade o estômago, e você cai de joelhos. O velho olha para você com desprezo e diz: “Bem, o que pode esperar quem come comida envenenada?”. Você perde 3 pontos de ENERGIA. Ele se afasta, arrastando os pés, e o deixa se contorcendo em dores no chão. Se ainda estiver vivo, você acaba recuperando força bastante para continuar para o oeste. Vá para 109."
cap39="Você consegue se desviar das pernas estendidas da Mosca Gigante que mergulha sobre você. Recuando, você desembainha a espada e se prepara para lutar contra o horroroso inseto, quando ele se volta para atacá-lo outra vez.\n MOSCA GIGANTE:	HABILIDADE 7	ENERGIA 14\nSe você vencer, vá para 111. Você pode Fugir, correndo de volta para o túnel, para prosseguir para o norte. Vá para 267."
cap40="Você chama o Anão, dizendo que está pronto para lutar contra o MINOTAURO. A porta de madeira se ergue lentamente, e você vê a assustadora fera, meio homem, meio touro, entrar na arena. Ele bufa e expele vapor pelas narinas, enquanto vai ficando mais e mais furioso, pronto para atacar. Súbito, arranca adiante, girando uma acha de dois gumes.\nMINOTAURO	HABILIDADE 9	ENERGIA 9\nSe você vencer, vá para 163."
cap41="Você caminha lentamente para a alcova, verificando cuidadosamente o chão para não cair em outras armadilhas ocultas. Você vê que a taça contém um líquido vermelho efervescente. Você:\nBeberá o líquido vermelho?	(Vá para 98) \nDeixará a taça e caminhará de volta para procurar o Bárbaro (se você ainda não tiver feito isso)?	(Vá para 126)\n Deixará a câmara para continuar para o oeste?	(Vá para 83)"
cap42="Os dentes da naja se cravam fundo no seu pulso e você sente o veneno se alastrando pelo corpo. Você perde 5 pontos de ENERGIA. Se você ainda estiver vivo, o Anão não tem pena, e lhe diz para tentar outra vez. Jogue dois dados. Se o total for igual ou menor que sua HABILIDADE, vá para 55. Se o total for maior, vá para 202."
cap43="O túnel vira abruptamente para a direita e continua para o norte, até onde a vista alcança. Há uma porta entreaberta na parede do lado esquerdo. Você ouve alguém gritando por socorro, a voz vindo do outro lado da porta. Se você quiser abrir a porta, vá para 200. Se preferir continuar para o norte, vá para 316."
cap44="Você está a apenas alguns metros da porta quando ouve o velho atrás de si enunciar umas palavras estranhas. Instantaneamente, sente os músculos endurecerem e a pele esticar. Você entra em pânico, mas não há nada que possa fazer para impedir a petrificação do seu corpo. Sua aventura termina aqui."
cap45="O disco, afiado como uma navalha, atinge-lhe as costas com terrível efeito. Você perde 1 ponto de HABILIDADE e 4 pontos de ENERGIA. Se ainda estiver vivo, você luta para se tirar o disco das costas, enquanto o Ninja lhe atira mais um. Vá para 312"
cap46="Você desce cuidadosamente do ídolo e, sem perder mais tempo na caverna, corre para o túnel adiante na parede norte. Vá para 239."
cap47="Você tem um tubo oco de madeira? Se tiver, volte para 10. Se não tiver, vá para 335."
cap48="Somente sua força imensa e determinação inquebrantável evitam que você caia inconsciente ao solo. Você aperta os dentes e, resoluto, segue adiante. Vá para 197."
cap49="Você dá uma espiada, virando a esquina, e vê duas pequenas criaturas correndo de você. Vestem roupas largas e usam chapéus pontudos e desengonçados. São os travessos LEPRECHAUNS. Se você quiser segui-los, vá para 205. Se preferir caminhar de volta para a última encruzilhada e seguir para o norte, vá para 241."
cap50="Você acorda e vê Throm puxando o anel do seu dedo. Ele joga o anel no chão e o esmaga com a acha de guerra. Em seguida, grunhindo para expressar que desaprova sua atitude, sai caminhando para o leste. Com esforço, você se levanta e o segue cambaleante. Vá para 221."
cap51="Os Hobgoblins não estão preparados para o seu ataque, e você consegue matar o primeiro antes que ele possa puxar da espada. Você se volta para enfrentar o outro Hobgoblin, que rosna de ódio. HOBGOBLIN	HABILIDADE 6	ENERGIA 5Se você vencer, volte para 9."
cap52="Ao abrir o livro, você vê que ele começa a se desintegrar. As páginas se transformando em poeira nas suas mãos. Mas você consegue salvar alguns fragmentos e ler o manuscrito. O livro parece ser sobre monstros, e, do que você pode concluir, contém uma descrição completa de um ser chamado Besta Sangrenta. É uma horrível criatura inchada, com pele grossa e coberta de espinhos e úlceras faciais que se abrem para se tornar falsos olhos, cujo objetivo é esconder o único ponto fraco da Besta Sangrenta - seus olhos verdadeiros. Essas monstruosidades geralmente habitam poços de lodo fétido que exalam gás venenoso, tão forte que pode facilmente deixar uma pessoa inconsciente. A Besta Sangrenta, embora pesada demais para sair da poça de lodo, tem uma língua longa e poderosa que se enrosca em torno de suas vítimas para arrastá-las para o interior da poça. Quando a carne das vítimas começa a apodrecer no lodo abjeto, a Besta Sangrenta a devora. Você conta a Throm sobre a grotesca Besta Sangrenta, mas ele simplesmente sacode os ombros e lhe diz para seguir adiante. Se você ainda não o fez, poderá abrir o livro preto - vá para 138. Do contrário, você deve prosseguir para o norte com Throm - vá para 369."
cap53="A Besta Sangrenta é inchada demais para sair da poça, mas, com a longa e poderosa língua, varre as cercanias e tenta alcançar a sua perna. Felizmente, você caiu fora do seu alcance. O ar, ao nível do chão, não contém nenhum dos vapores venenosos, mas você acorda com dor na garganta. Você cobre a boca com a manga da camisa para poder respirar através dela, e decide o que fazer. Se você quiser correr, contornando a poça, na direção do túnel, vá para 370. Se preferir atacar a Besta Sangrenta com sua espada, vá para 348."
cap54="O laço se solta e você consegue tirá-lo do pescoço do ídolo com uma sacudidela. Ele cai ao chão com um ruído alto. Você enrola a corda rapidamente e a coloca na mochila. Sem perder mais tempo na caverna, corre para o túnel na parede norte. Vá para 239."
cap55="Com a velocidade de um raio, você estica a mão e segura a naja logo abaixo da boca aberta. Você a ergue e, como braço estendido, sacode-a na frente do Anão. Ele fica impassível, mas, com seu jeito calmo e sem expressão, diz: “Por favor, coloque a naja de volta na cesta e prepare-se para a parte final do teste. Siga-me.” Você faz o que ele disse e o segue de volta para a câmara, onde Throm está andando de um lado para o outro, evidentemente nervoso. Você acena para ele, enquanto o Anão abre uma segunda porta secreta e manda que você entre por ela e espere por ele. Outra vez você obedece, e se vê em outro aposento circular, embora este se assemelhe a uma pequena arena. O chão é coberto de areia, e uma pequena sacada circunda a parede da arena. No lado oposto ao da porta secreta pela qual você entrou, há uma porta de madeira de aparência agourenta. De repente, você ouve um grito, e olha para cima, vendo o Anão sorridente na sacada. Ele joga dois pedaços de papel para você. Num deles, estão escritas as palavras SEI PORCÃO, e no outro, RUIM NO ATO. Com a voz sempre calma, ele diz: “Se você rearrumar as letras das palavras, descobrirá os nomes de duas criaturas. Você pode escolher com qual delas quer lutar na minha Arena da Morte.” Se você puder identificar a criatura rearrumando as letras de SEI PORCÃO, vá para 143. Se puder identificar a criatura rearrumando as letras de RUIM NO ATO, volte para 40. Se você não puder identificar nenhuma das duas criaturas, vá para 347."
cap56="Você vê que a obstrução é causada por um objeto grande e marrom, parecendo um rochedo. Você o toca com a mão e fica surpreso ao descobrir que é macio e esponjoso. Se você quiser tentar subir por cima dele, vá para 373. Se preferir cortá-lo ao meio com sua espada, vá para 215."
cap57="Embora você já tenha examinado a arca cuidadosamente, em busca de quaisquer mecanismos ocultos, não consegue ver a armadilha dentro dela. Ao levantar a tampa, uma bola de ferro pendente de uma corda é lançada para trás, partindo a cápsula de vidro fixada no lado de dentro da tampa. Uma nuvem de gás venenoso é instantaneamente liberado no ar, e você cambaleia, recuando, enquanto tosse e se engasga. Você perde 4 pontos de ENERGIA. Se ainda estiver vivo, vá para 198."
cap58="Você caminha lentamente entre os postes, tomando cuidado para não tocar em nenhum deles. Jogue dois dados. Se o total for igual ou menor que seu índice de HABILIDADE, vá para 80. Se o total for maior que seu índice de HABILIDADE, vá para 246."
cap59="Adiante, a distância, você ouve o som de passos lentos vindo na sua direção. Sem saber o que ou quem poderia estar se aproximando, você olha em volta, em busca de um lugar para se esconder. Encontra uma fenda grande na parede do túnel onde não bate luz. Se você quiser defrontar-se com o recém-chegado de espada na mão, vá para 341. Se preferir esconder-se nas sombras, vá para 283."
cap60="O túnel termina em uma grande porta de carvalho. Throm não perde tempo e vai logo testando a maçaneta, ficando algo admirado ao descobrir que a porta não está trancada. Ele a empurra e vocês se deparam com uma câmara iluminada por tochas. Sentado sozinho em uma cadeira ornamentada, há um ANÃO, que os convida a entrar na câmara. Ao fazê-lo, a porta de carvalho se fecha atrás de vocês. “Aventureiros, vocês se saíram muito bem até agora”, diz o Anão com voz profunda. “Contudo, como vocês dois sabem, só pode haver um vencedor na Prova dos Campeões. Como Juiz da Prova, é minha obrigação para com o Barão Sukumvit só permitir que o mais capaz continue. Portanto, tenho que preparar um teste de inteligência e força para eliminar um de vocês. Por favor, não tentem livrar-se de mim. Seria completamente estúpido, pois, como vocês podem ver, não há nenhuma maneira óbvia de sair desta câmara, e somente eu sei onde está a saída oculta. Agora, se vocês não se importassem de decidir entre vocês quem irá primeiro, eu tratarei de fazer as preparações necessárias.” Você olha para Throm, subitamente com raiva de que a eficaz associação de vocês pudesse ter que terminar. Ele se inclina e sussurra no seu ouvido que vocês deveriam tentar matar o Anão e preocupar- se com a saída depois. Se você quiser unir-se a Throm no ataque ao Anão, vá para 179. Se você preferir convencer Throm seguir em frente com o teste do Anão, vá para 365."
cap61="Apesar do terrível ruído de campainha nos seus ouvidos, você ouve passos descendo pelo túnel. Seus gritos altos atraíram um guardião do túnel. Há um HOBGOBLIN de pé junto a você. Ele sorri doentiamente enquanto pressiona a ponta da espada contra seu pescoço. Você não tem como se defender e impedir que ele o trespasse. Sua aventura termina aqui."
cap62="O Gnomo pula no ar, gritando: “Belo trabalho – ninguém jamais conseguiu encontrar todas as três gemas antes! Agora, prepare-separa o teste final, o qual eu explicarei uma vez e somente uma vez. Como você pode ver, a fechadura desta porta tem três ranhuras, com as etiquetas A, B e C, cada uma delas construída para aceitar uma gema específica. Você tem porque pôr uma das suas três gemas em cada uma das ranhuras na ordem certa. Se conseguir isso na primeira tentativa, ótimo. Porém, se puser as gemas nas ranhuras erradas, você será atingido por um raio de energia da fechadura, o que lhe causará ferimentos. De qualquer maneira, como eu disse, tenho permissão para ajudá-lo um pouco. Se você colocar uma gema em sua ranhura correta, mas puser as outras duas erradas, eu gritarei: ‘Uma coroa e dois crânios.’ Se você colocar todas as três gemas incorretamente, eu gritarei: ‘Três crânios.’ Você terá permissão para tentar repetidamente até que tenha êxito ou morra. Está pronto?” Você faz um aceno de cabeça e caminha adiante para colocar as três gemas nas ranhuras. Resolva que gemas colocará nas ranhuras com etiquetas:\nEsmeralda	Diamante	Safira	(Fique em 16)Diamante	Safira	Esmeralda	(Vá para 392)\nSafira	Esmeralda	Diamante	(Vá para 177)\nEsmeralda	Safira	Diamante	(Vá para 287)\nDiamante	Esmeralda	Safira	(Vá para 132)\nSafira	Diamante	Esmeralda	(Vá para 249)"
cap63="Você amarra a corda na cintura e segura a tocha que Throm, seu aliado Bárbaro, lhe dá, já acesa. Segurando a corda frouxa, Throm o vai descendo-o lentamente por sobre a borda do poço até as profundezas escuras. Você pode ver, com a luz da tocha, que os lados do poço são extremamente lisos. Você desce por uns 20 metros antes de chegar ao fundo do poço. Ali, vê um outro túnel que segue para o norte, e chama Throm para contar-lhe a descoberta. Ele responde, dizendo que vai amarrar a corda em uma rocha proeminente na borda do poço e descerá. Você ouve o Bárbaro descendo, e logo estão juntos de novo. Throm recupera a corda, sacudindo-a para soltá-la da rocha, e vocês partem para o norte pelo novo túnel. Vá para 194."
cap64="Logo que você põe o anel no dedo, todo seu corpo começa a tremer. Jogue dois dados. Se o total for igual ou menor que o seu índice de HABILIDADE, vá para 115. Se o total for maior que o seu índice de HABILIDADE, vá para 190."
cap65="Você bebeu uma Poção encontrada dentro de um livro de couro preto? Se beber, vá para 345. Se não, vá para 372."
cap66="Depois de caminhar pelo túnel por alguns minutos, você chega a uma encruzilhada. Uma seta branca pintada na parede aponta para o oeste. No chão, você vê pegadas molhadas, feitas por aqueles que entraram antes de você. É difícil ter certeza, mas parece que três deles seguiram a direção da seta, enquanto um resolveu ir para o leste. Se você quiser ir para o oeste, vá para 293. Se preferir ir para o leste, vá para 119."
cap67="Você se agarra a um dos pilares submersos da ponte e gruda nele, prendendo a respiração. Enquanto isso, os Trogloditas chegam à margem e concluem que você deve ter sido arrastado rio abaixo para morte certa, já que o rio desaparece nas profundezas da montanha. A essa altura, seus pulmões estão estourando de falta de ar. Teste sua Sorte outra vez. Se você tiver sorte, vá para 146. Se não tiver sorte, vá para 219."
cap68="Você desce a passagem e logo se encontra de pé na borda de um poço profundo e escuro. A passagem continua para o leste, do outro lado do poço. Você pensa que provavelmente conseguirá pular por cima do poço, mas não tem certeza. Há uma corda que pende do teto e desce sobre o centro do poço. Você:\n Jogará seu escudo por cima do poço e depois pulará?//	Vá para 271\nPulará por cima do poço carregando todas as suas posses?// Volte para 30\nUsará a espada para trazer a corda até você, de modo a poder usá-la para atravessar até a outra margem?	Vá para 212"
cap69="Erva não nota que você abriu a porta. Você se esgueira para fora do aposento, fecha a porta silenciosamente e se vê no fim de um outro túnel. Vá para 305."
cap70="Você consegue mergulhar para o lado, por pouco, antes que o rochedo despenque sobre o chão do túnel, rachando a pedra. Enquanto se limpa, nota que há luz do sol no fim do túnel. Você corre para lá, alegre com a bela visão do céu azule das árvores verdes. Ao correr para fora do túnel, você espera ser cumprimentado por multidões vibrantes, mas fica horrorizado com o que vê. Não há recepção de herói que possa vir das pessoas à sua volta. Estão todos mortos. Você está, na realidade, de pé em uma câmara fria, o chão coberto de cadáveres e esqueletos com armaduras - a saída para a vitória era apenas uma ilusão! Só os restos dos aventureiros do passado são reais. Você corre de volta para o túnel, mas colide com uma barreira invisível. Você caiu na armadilha e está condenado a terminar seus dias na câmara dos mortos."
cap71="Mais uma vez, você estica a mão para o pergaminho, só que dessa vez ele está em meio a uma pilha de ossos quebrados. Ao desenrolá-lo, você vê o mapa de um aposento com o desenho de uma criatura pavorosa dentro. Embaixo da figura do monstro, há uma rima que diz://\n“Se você encontrar o Mantécora, É bom de sua cauda cuidar. Proteja-se dos espinhos Que irão voar pelo ar.” //\nVocê enrola o pedaço de pergaminho e o coloca na mochila. Repetindo a rima muitas vezes para si mesmo, você caminha para o outro lado, em direção à alcova. Vá para 128."
cap72="O Espelho se quebra, lançando fragmentos de vidro por toda parte. As quatro faces do Demônio do Espelho gritam de agonia, e aparecem rachaduras em todas elas. Em seguida, elas também se partem e caem ao chão numa pilha de cacos de vidro. Infelizmente ao quebrar o espelho, você cortou seriamente o braço com que segura a espada. Embora sua força não tenha sido afetada, sua habilidade com as armas foi prejudicada. Você perde 2 pontos de HABILIDADE antes de continuar na sua jornada para o norte. Vá para 122"
cap73="Se você ainda não o tiver feito, poderá caminhar de volta à procura do Bárbaro - vá para 126. Do contrário, saia da câmara para continuar para o oeste - vá para 83."
cap74="O túnel faz uma curva fechada para a direita, e você se vê em uma espécie de galeria, coberta de espelhos por uns 20 metros. Um esqueleto humano parece estar sendo arrastado a meio caminho através de um espelho da parede da direita. Súbito, um ser grotesco, com quatro braços e quatro faces que gritam, emerge do espelho, barrando-lhe a passagem. Caminha lentamente na sua direção, todos os braços estendidos para agarrá-lo. É o DEMÔNIO DO ESPELHO, de outro plano dimensional, que veio para levar seu, espírito. Você:\nFará um desejo (se estiver usando um Anel dos Desejos)?	Vá para 265\nTentará quebrar os espelhos?	Vá para 300\nAtacará o Demônio do Espelho com sua espada?	Vá para 327"
cap75="Você esfrega o líquido nos seus ferimentos, mas eles não saram. Olhando fixamente para a garrafa vazia, você fica se perguntando o que o líquido seria exatamente. Se você ainda não o tiver feito, poderá abrir o livro vermelho - volte para 52. Do contrário, você deve continuar para o norte com Throm - vá para 369."
cap76="Você dá a volta pela enorme massa morta do Verme da Rocha e dá uma espiada dentro da escuridão de seu buraco perfurado. Você só consegue ver alguns metros, mas pode notar que ele se inclina levemente e é tímido por causa da gosma secretada pelo Verme da Rocha. Se você quiser explorar o buraco de broca, vá para 317. Se preferir caminhar para o oeste pelo túnel, vá para 117."
cap77="Você cambaleia pela porta aberta para outro túnel, no fim do qual está a visão bem-vinda da luz do dia. Com grande surpresa, você vê o Gnomo caído, morto, na metade do caminho do túnel, com uma seta de besta cravada na cabeça. O Gnomo, no esforço por libertar-se, caiu na armadilha final do Barão Sukumvit. Você passa por ele rumo à luz do sol brilhante. Vá para 400."
cap78="Há um cano com cerca de um metro de diâmetro aberto na parede da direita. Está escuro demais para se ver muito abaixo nele. Você grita dentro do cano de ferro e ouve sua voz ecoar por alguns instantes até desaparecer. Se você quiser engatinhar pelo cano, vá para 301. Se preferir continuar para o norte, vá para 142."
cap79="Você segura os braços da cadeira firmemente, esperando que uma onda de energia se espalhasse pelo seu corpo. Teste sua Sorte. Se você tiver sorte, vá para 106. Se não tiver sorte, vá para 383."
cap80="Você vai com calma e consegue passar pelo último poste sem ter tocado em nenhum deles. Corre para o leste, ainda seguindo os dois pares de pegadas. Vá para 313."
cap81="A única mobília no quarto do Goblin consiste em uma mesa, duas cadeiras e um armário de parede. Há duas portas fechadas, uma na parede oeste, outra na parede norte. Você:\nAbrirá o armário?	Vá para 307\nAbrirá a porta do oeste?	Vá para 263\nAbrirá a porta do norte?	Vá para 136"
cap82="Quando o Diabo do Poço bate como corpo contra a parede, você solta a corda e cai em segurança no chão. Você corre na direção das portas duplas e fica aliviado ao senti-las se abrirem quando as empurra; deixa que elas se fechem atrás de si e segue para o norte pelo túnel. Vá para 214."
cap83="A passagem logo conduz a uma encruzilhada. Você repara em mais pegadas no chão, possivelmente uns três pares, dirigindo-se ao norte pela passagem do sul. Resolve segui-las. Volte para 37."
cap84="Jogue dois dados. Se o total for maior que 8, vá para 152. Se for 8 ou menos, vá para 121."
cap85="Antes que você possa fazer qualquer outra coisa, o velho murmura umas palavras estranhas. Você sente os músculos se enrijecerem e a pele se esticar. Começa a entrar em pânico, mas não há nada que possa fazer para impedir a petrificação do seu corpo. Sua aventura termina aqui"
cap86="A chave gira na fechadura, e a porta se abre para um cruzamento de quatro caminhos do túnel. Não há nada a ser visto a leste ou a oeste, a não ser os já conhecidos cristais do teto que continuam a produzir luz fraca. Subitamente, você ouve um chamado: 'Por aqui, por aqui, você está no caminho certo.' A voz parece estar vindo de algum lugar bem à sua frente. Não resistindo à curiosidade, você resolve atender ao chamado. Vá para 187."
cap87="A porta se abre para um aposento grande. Vá para 381."
cap88="Logo que os TROGLODITAS o vêem pegam os arcos e correm para cercá-lo. Para seu horror, o líder dá um passo adiante e declara que você é prisioneiro deles e terá que se submetera uma prova, segundo o rito milenar, a Corrida da Flecha. Se você estiver disposto a participar da Corrida da Flecha, vá para 343. Se preferir tentar lutar para fugir, vá para 268."
cap89="De volta à solidez do chão da caverna, você tenta sacudir a corda para que saia do pescoço do ídolo. Teste sua Sorte. Se você tiver sorte, volte para 54. Se não tiver sorte, vá para 261."
cap90="Logo que se levanta, você se defronta com o quadro mais repulsivo que seus olhos jamais viram. Ali, na sua frente, chafurda numa poça circular de lodo fétido uma criatura inchada, inacreditavelmente horrível. O corpo é verde e coberto de ameaçadores espinhos. A cara é um amontoado de feridas vermelhas, uma das quais subitamente se abre para revelar mais um dos muitos olhos sinistros que tudo vêem. Um caminho estreito contorna a borda da poça e leva a um outro túnel na parede do outro lado. Se você já tiver lido detalhes sobre a abjeta BESTA SANGRENTA em um livro encadernado em couro, vá para 172. Se você não tiver lido o livro, vá para 357."
cap91="A maça de ferro do Orca atinge-lhe o braço, jogando sua espada no chão. Você terá que lutar com as mãos nuas, o que lhe reduz a HABILIDADE em 4 pontos enquanto durar o combate. Felizmente, o túnel é estreito demais para os dois Orcas atacarem-no ao mesmo tempo. Lute com um de cada vez. HABILIDADE	ENERGIA Primeiro ORCA 5// 5// Segundo ORCA// 6// 4 // Se você vencer, vá para 257."
cap92="Reunindo todas as suas forças, você desfere um golpe final no Demônio do Espelho com sua espada. Com um som de estourar os tímpanos, abrem-se rachaduras no rosto e membros do monstro. As várias bocas gritam de agonia nos estertores da morte, antes do Demônio se despedaçar completamente numa pilha de minúsculos cacos. Você solta um enorme suspiro de alívio e depois se apressa a seguir em frente. Vá para 122."
cap93="A porta se abre para um pequeno e escuro aposento, contendo apenas, na parede do lado oposto, uma robusta arca de madeira em cima de uma prateleira. No chão, coberto de poeira espessa, você pode ver claramente pegadas frescas que vão até a arca e retornam à porta. Você se pergunta se um dos seus rivais está à sua frente na “Caminhada” ou se a arca só foi posta na prateleira recentemente por um dos Juízes da Prova. Se você quiser entrar no aposento e abrir a arca, vá para 284. Se preferir continuar percorrendo o túnel, vá para 230."
cap94="Respirando fundo, você se debruça sobre o poço e mergulha o braço na massa de vermes que se contorcem. Eles são frios e viscosos, e o contato é extremamente desagradável, mas, pelo menos, são inofensivos, e você consegue pegar o punhal pelo cabo. Ao sacudi-lo firmemente, ele sai da rachadura em que a ponta estava cravada. Admirando-lhe a beleza, e imaginando se ele teria um dia pertencido a um competidor de pouca sorte, você põe o punhal ornamentado de opala firmemente no cinto e sai da caverna. Vá para 174."
cap95="O anel de ferro está preso a um pequeno alçapão. É fácil □uxa□-lo, e, dentro de um pequeno compartimento, você encontra um escudo, finamente trabalhado, feito do mais puro ferro. Maravilhado com o esplendor da peça, você a amarra ao seu braço. Acrescente 1 ponto de HABILIDADE. Você caminha na direção das portas duplas e as empurra. Vá para 248."
cap96="Seu segundo golpe também não consegue partir o espelho. O Demônio do Espelho estica um braço, agarra-lhe o pulso e começa a puxá-lo na direção do espelho. A força é incrível, e, apesar de todos os seus esforços, você não consegue resistir. A cada segundo, você chega mais perto do espelho. Quando o Demônio do Espelho toca o espelho, desaparece através dele. Com horror, você vê seu próprio braço desaparecer também através do espelho, e o resto do corpo logo tem o mesmo destino. Você está agora em um mundo de espelhos de outra dimensão, do qual jamais retornará."
cap97="Você não sabe, mas a Besta Sangrenta só tem um ponto fraco: seus olhos reais. Mais por sorte do que por propósito, você crava sua lâmina profundamente em um deles, e a Besta Sangrenta desaba de volta na poça. Depois de medonhas convulsões, ela afunda sob a superfície oleosa da poça. Sem esperar para ver se ela vai se recuperar, você corre e entra no túnel, ansioso por se afastar da câmara tóxica da Besta Sangrenta o mais rápido possível. Vá para 134."
cap98="Erguendo a taça, você aciona um mecanismo de mola, e um dardo é disparado da perna da mesa de madeira. Teste sua Sorte. Se você tiver sorte, vá para 105. Se não tiver sorte, vá para 235."
cap99="Sorrindo, você diz a Erva que a acha muito parecida com Barriga Azeda. Então, enquanto ela olha com admiração para a pintura, você pega um banco quebrado, aproxima-se silenciosamente por trás dela e golpeia-lhe a cabeça com toda a força. Para seu imenso alívio, Erva cai sem sentidos. Se você quiser revistar-lhe o quarto, vá para 266. Se não, saia pela porta da parede leste. Você se encontrará no final de um túnel. Vá para 305."
cap100 = "Alguns metros adiante, descendo a passagem, você vê uma outra porta fechada na parede da esquerda. Há uma letra X na placa central da porta. Colocando o ouvido na porta, você escuta atentamente, mas não consegue ouvir nada. Se você quiser abrir a porta, volte para 87. Se preferir continuar caminhando para o norte, vá para 217."
cap101 = "A correnteza do rio é bastante forte, e, atrapalhado pela armadura e a mochila, você não está em condição de nadar contra ela. Em poucos segundos, é arrastado por baixo da ponte. De pé na margem do rio, os Trogloditas olham, riem e gracejam, enquanto você desce o rio para encontrar a morte nas profundezas da montanha"
cap102 = "Você entra em um aposento pequeno e completamente vazio. Logo a porta se fecha atrás de você. Repentinamente, uma voz ressoa, vinda de lugar nenhum: Bem vindo ao Calabouço da Morte, o engenhoso labirinto assassino do meu senhor. Aventureiro, creio que você apresentará seus respeitos ao meu senhor, gritando seu nome? Você gritará:"
cap103 = "Você respira o gás venenoso e começa a se engasgar. Você perde 3 pontos de ENERGIA. Se ainda estiver vivo, volte para 77.\n Salve, Sukumvit?	Vá para 133\n Sukumvit é um verme?	Vá para 251"
cap104 = "Reagindo rapidamente, você consegue saltar por cima da língua estendida e correr para o túnel, deixando a Besta Sangrenta a afurdar na poça à espera de outra vítima. Vá para 134."
cap105 = "Seus reflexos são precisos, e você rapidamente pula de lado. O dardo passa assobiando, por pouco não o atingindo, e se choca contra a parede do outro lado. Você vê a taça jogada no chão, e o líquido vermelho escorrendo pela pedra cinzenta como pequenos riachos. Pelo menos a taça pode ser de alguma utilidade, portanto você a põe na mochila. Se você ainda não o tiver feito, poderá caminhar de volta para revistar o Bárbaro - vá para 126. Do contrário, saia da câmara para continuar para o oeste - volte para 83."
cap106 = "Ao apertar o braço da cadeira, você aciona a mola de um painel secreto, que salta no ar. Você encontra um frasco de vidro e lê o rótulo: Poção da Réplica - uma dose apenas. Este líquido fará com que seu corpo tome a forma de qualquer ser que esteja próximo. Você coloca a estranha poção na mochila e continua para o norte. Vá para 188."
cap107 = "Você chega a uma porta em arco localizada na parede à direita do túnel. A pesada porta de pedra está fechada, mas há um trinco de ferro e uma maçaneta redonda. Se você quiser tentar a porta, vá para 168. Se, em vez disso, quiser continuar pelo túnel, vá para 267."
cap108 = "Há um grande painel de vidro na parede à esquerda do túnel. Através dele, você pode ver um aposento intensamente iluminado por tochas com INSETOS GIGANTES de todas as formas possíveis. Abelhas, vespas, besouros, carrapatos  até os bichos do queijo têm mais de seis centímetros de comprimento. O ruído é ameaçador. No meio do aposento, uma coroa cravejada de jóias está colocada sobre uma pequena mesa. No meio da coroa, há uma jóia, parece um grande diamante. Você: Quebrará o vidro e tentará apanhar a coroa?	Vá para 394 Continuará para o oeste?	Volte para 59 Retornará à encruzilhada para seguir para o norte?	Volte para 14"
cap109 = "Você chega a uma outra encruzilhada no túnel. Se quiser continuar seguindo para o oeste, volte para 43. Se quiser seguir para o norte, volte para 24"
cap110 = "O túnel logo faz uma outra curva fechada para a direita. Seguindo para o leste, você chega a uma estranha obstrução: uma linha de 12 postes de madeira atravessados no túnel. Eles estão fixos às paredes a cerca de meio metro do chão, com um espaço de um metro entre eles. Se você quiser caminhar entre os postes, volte para 58. Se preferir subir pelos postes e passar por sobre a obstrução, vá para 223."
cap111 = "Você limpa o viscoso lodo amarelo da lâmina de sua espada e caminha rapidamente para a porta, de volta para o túnel, e segue para o norte. Vá para 267."
cap112 = "A não ser pelas Provisões, que ficaram encharcadas e não servem mais para serem comidas, todas as suas outras posses permanecem intactas. Você as recoloca cuidadosamente na mochila e parte para o norte de novo. Vá para 356."
cap113 = "A bola de madeira passa assobiando pelo crânio, atingindo a parede do outro lado com um estrondo. Se você quiser tentar outra vez com a outra bola, vá para 371. Se já tiver jogado duas vezes, ou não quiser tentar de novo, você pode fechar a porta e continuar pelo túnel – volte para 74"
cap114 = "O Homem da Caverna está usando uma munhequeira de couro com quatro pequenos crânios de rato pendurados. Se você quiser coloca-la no seu próprio pulso, vá para 336. Se preferir prosseguir para o norte, vá para 298."
cap115 = "Seu corpo continua a vibrar intensamente, e você se sente como se estivesse prestes a desmaiar. Mas sua força é grande, e você consegue resistir ao tremendo choque sofrido. Finalmente, você se acalma e começa a sentir a ação dos poderes benéficos do anel. Some 3 pontos de ENERGIA. Throm o olha ansioso, e você o tranquiliza, dizendo que está plenamente recuperado. Ele caminha para o leste, você o segue prontamente. Vá para 221."
cap116 = "Você não consegue acreditar que a Besta Sangrenta não tenha sido afetada pela nova ferida. Você hesita uma fração de segundo demais, e a fera dá um bote, partindo-lhe o crânio com as mandíbulas. Em seguida, arrasta-o para a poça, onde seu corpo, depois de decomposto, será devorado pela pavorosa criatura."
cap117 = "Depois de longa caminhada túnel abaixo, você chega a um beco sem saída. Um grande espelho, que vai do chão até o teto, está colocado na parede do fundo e, na penumbra, você só consegue visualizar vagamente o seu próprio reflexo. Se quiser olhar o espelho mais de perto, vá para 329. Se preferir fazer a longa caminhada de volta para a última encruzilhada no túnel, a fim de prosseguir para o leste, vá para 135"
cap118 = "Apesar das estalactites que caem por toda parte, você consegue passar ileso pelo arco. Você olha ao redor e vê Throm disparando na sua direção, um braço por cima da cabeça para protegê-la. Ele corre para o túnel e se encosta na parede fria, a respiração ofegante. Desculpa- se por ter iniciado o desabamento das rochas e lhe oferece a mão. Você diz a Throm que talvez fosse melhor ele usar a linguagem dos sinais no futuro, mesmo para rir! Os dois sorriem e partem para o leste mais uma vez. Volte para 60."
cap119 = "Adiante, você pode ver um grande obstáculo no chão do túnel, embora esteja escuro demais para saber exatamente o que é. As pegadas molhadas que você vem seguindo continuam até a obstrução. Se você quiser continuar para o leste, volte para 56. Se preferir voltar para a encruzilhada e seguir para o oeste, vá para 293."
cap120 = "Jogados num buraco de mais ou menos um metro de profundidade, você vê um gancho de ferro e uma bolsa de couro. Se quiser esticar a mão para apanhá-los, vá para 228. Se preferir ignorar os objetos e continuar para o norte, vá para 292."
cap121 = "O Anão olha para os dados. “Você não é muito bom nesse jogo, é?”, graceja. “Lamento, mas você terá que sofrer uma penalidade antes de continuar.” Ele retira duas pílulas do bolso. Uma está marcada com a letra S e a outra com a letra L. Pede que você escolha uma e engula. Se você escolher a pílula marcada com a letra S, volte para 26. Se quiser engolir a outra, vá para 354."
cap122 = "À sua frente, há dois lances de escadas de pedra, separados por um corrimão de crânios de ratazana. Você pode subir pelo lance de escadas da esquerda - vá para 176 - ou pelo da direita- vá para 384."
cap123 = "O colar é um amuleto de força. Some 1 ponto de HABILIDADE e 1 ponto de ENERGIA e continue na sua missão. Vá para 282"
cap124 = "Você abre o alçapão e sobe os degraus correndo, chegando a um aposento profundamente iluminado por lanternas. Dois GOBLINS afiam espadas curtas em uma pedra colocada no meio do chão. Você os pega desprevenidos, mas eles logo se recuperam e se projetam para frente a fim de atacá-lo.	HABILIDADE	ENERGIA \nPrimeiro GOBLIN	5	4 \nSegundo GOBLIN	5	5\nOs Goblins o atacarão separadamente em cada Série de Ataque, mas você deve escolher com qual dos dois vai lutar. Ataque o Goblin escolhido como numa batalha normal. Contra o outro, você tem que jogar os dados para determinar sua Força de Ataque da maneira usual, mas, mesmo que sua Força de Ataque seja maior, você não ferirá o Goblin. Compute isso simplesmente como se tivesse se defendido de um golpe dele. Porém, se a Força de Ataque dele for maior, ele o ferirá, da forma costumeira. Se você vencer, volte para 81."
cap125 = "Você caminha para a porta na ponta dos pés, enquanto Erva segue tagarelando. Teste sua Sorte. Se você tiver sorte, volte para 69. Se não tiver sorte, vá para 139."
cap126 = "Comerá a carne seca?	Vá para 226 Deixará a carne e caminhará para a alcova(se ainda não tiver feito isso)?	Volte para 41 Deixará a câmara e seguirá para o oeste?	Volte para 83"
cap127 = "A única maneira possível de sair do salão, tanto quanto você pode ver, é usando um escorrega na parede norte. Você resolve arriscar e sobe no escorrega. Desce deslizando suavemente e aterrissa de costas em outro aposento. Volte para 90."
cap128 = "Na parte de trás da alcova, há uns degraus que conduzem a uma adega abaixo. Teias de aranha tocam-lhe o rosto enquanto você desce. O teto da adega é bastante baixo, e o chão está coberto de lixo e detritos. No meio da parede do outro lado, uma passagem em arco leva a outro túnel iluminado por cristais. Grandes cogumelos crescem no lixo à sua direita. Se você quiser atravessar a passagem em arco, volte para 35. Se preferir parar para comer alguns cogumelos, vá para 233."
cap129 = "Você amarra a corda ao gancho e o atira por cima da muralha. O gancho se prende na pedra, e você começa a se içar. De cima da muralha, vê um monstro gigantesco, semelhante a um dinossauro, circulando em um poço coberto de areia. O grosso couro da criatura é verde malhado, e de pé nas fortes pernas traseiras, deve atingir uns 10 metros de altura. As enormes mandíbulas deixam ver filas de dentes afiados como navalhas ao se abrirem e fecharem com força suficiente para triturar-lhe os ossos. Uma grande porta dupla na parede do outro lado do poço parece ser a única maneira de sair desta parte do calabouço. Você: Descerá pela corda para dentro do poço, a fim de enfrentar o DIABO DO POÇO?	Vá para 349 Jogará seu amuleto de osso de macaco no poço (se você tiver um)?	Vá para 361 Tentará, de cima da muralha, fisgar O DIABO DO POÇO com o gancho de ferro?	Vá para 167"
cap130 = "Os Hobgoblins param de lutar imediatamente. Eles não entendem o que você está dizendo e rosnam agressivamente. Em seguida, desembainham as espadas curtas e avançam para ataca- lo. Lute com um de cada vez. HABILIDADE	ENERGIA Primeiro HOBGOBLIN	7	5 Segundo HOBGOBLIN Se você vencer, volte para 9.	6	5"
cap131 = "Os dardos da besta voam por cima de sua cabeça e se cravam na parede; felizmente, você ainda está agachado. Agora que a armadilha já disparou, você pode sair do aposento pela mesma porta pela qual entrou. De volta no túnel, você segue para o oeste. Volte para 74"
cap132 = "Você só tem tempo de ouvir o Gnomo dizer: 'Uma coroa e dois crânios', antes de ser atingido no peito por um raio branco de energia disparado da fechadura. Você cai sem sentidos. Jogue um dado, some 1 ao número obtido e reduza esse total de sua ENERGIA. Se você ainda estiver vivo, recupera a consciência e o Gnomo manda que tente de novo. Você sabe que colocou uma gema na ranhura certa, mas qual? Você suspira e tenta uma nova combinação. /\n/Esmeralda - Diamante - Safira - Volte 16/\n/Diamante - Safira - Esmeralda - Vá para 392/\n/Safira - Esmeralda - Diamante - Vá para 177/\n/Esemeralda - Safira - Diamante - Vá para 287/\n/Diamante - Esmeralda - Safira - Fique em 132/\n/Safira - Diamante - Esmeralda - Vá para 249"
cap133 = "Mais uma vez, a voz misteriosa ecoa, só que agora num tom cheio de desprezo e escárnio. 'Então, temos uma erva daninha em nosso meio, não?', zomba a voz. 'Meu senhor tem um presente especial para você, verme abjeto.' Súbito, começa a entrar água no aposento por um buraco no teto. Logo sobe até a altura dos seus tornozelos, e não parece haver qualquer meio de escapar. Você caminha na água até a porta. Está firmemente trancada, mas, no desespero, você tenta arrombá-la, batendo com o ombro. Jogue dois dados. Se o total for igual ou menor que o seu índice de HABILIDADE, vá para 178. Se o total for maior que o seu índice de HABILIDADE, volte para 17"
cap134 = "O túnel leva a um amplo aposento cujo teto é sustentado por diversos pilares de mármore. Ao entrar no aposento, você depara com uma estranha fera à sua direita. Tem corpo de leão, asas de dragão, rabo de escorpião e cabeça de velho barbudo. Se você tiver lido o poema escrito no Pergaminho do Guerreiro Esqueleto, vá para 222 Se não tiver lido esse poema, vá para 247."
cap135 = "Passando pelo buraco perfurado do Verme da Rocha, à sua esquerda, você logo chega à encruzilhada. Dá uma olhada rápida no túnel que conduz ao sul, mas não vê ninguém se aproximando. Apressando o passo, você segue velozmente para o leste. Volte para 68."
cap136 = "A porta abre para um outro túnel, que se inclina numa subida ao longe. Depois de percorrer essa subida por algum tempo, você chega a uma parte plana, onde numa porta na parede da direita encontra-se pregada uma mão já decomposta. Se você quiser abrir a porta, vá para 210. Se preferir continuar para o norte, volte para 78."
cap137 = "Caminhando pelo túnel, você se surpreende com um grande sino de ferro pendurado no teto. Se quiser tocar o sino, vá para 220. Se preferir contorná-lo e prosseguir para o oeste, vá para 362"
cap138 = "As páginas do livro estão unidas com lacre, mas um pequeno orifício foi cortado no meio delas, de tamanho suficiente para conter uma pequena garrafa arrolhada, na qual há um líquido de cor clara. Você mostra isso a Throm, que levanta a mão, indicando não querer que você sequer chegue perto dele com aquilo; a desconfiança que ele sente em relação às coisas desconhecidas fica evidente. Você:/\n/Beberá o Líquido? - Vá para 393/\n/Esfregará o líquido nos seus ferimentos? - Volte para 75/\n/Abrirá o livro vermelho (se ainda não fez isso) - Volte para 52/\n/Deixará a garrafa de lado e seguirá para o norte com Throm - Vá para 369"
cap139 = "Ao tentar escapar, você é atacado ferozmente por Erva, que, com raiva, vira-se rapidamente, pega um banco quebrado e o atinge com ele. Você perde 2 pontos de ENERGIA. Se ainda estiver vivo, você consegue desembainhar a espada e lutar ERVA	HABILIDADE 9	ENERGIA 9 Se você vencer, vá para 201."
cap140 = "Você tenta forçar o olho de esmeralda com a ponta da espada, procurando enfiá-la por baixo dele. Para sua grande surpresa, ele se despedaça com o contato, soltando um jato de gás venenoso direto no seu rosto. Você desmaia e cai para trás, chocando-se contra o ídolo várias vezes até parar no chão de pedra. Sua aventura termina aqui."
cap141 = "O Demônio do Espelho está quase em cima de você quando, reunindo todas as suas forças, você desfere um golpe decisivo contra o espelho com a espada. Jogue dois dados. Se o total for igual ou menor que a sua HABILIDADE, volte para 72. Se o total for maior que a sua HABILIDADE, volte para 96."
cap142 = "Há uma nova ramificação no túnel à sua esquerda, e, à frente, você vê dois corpos estendidos no chão. Você para e dá uma espiada no novo túnel, mas, não vendo nem portas nem criaturas, resolve seguir por ele. Com a espada na mão, você caminha na direção dos corpos estendidos. Vá para 338."
cap143 = "Você chama o Anão, dizendo-lhe para mandar vir o ESCORPIÃO, pois você está pronto para lutar. Lentamente, a porta de madeira é erguida, e um enorme e grotesco escorpião negro se esgueira por baixo dela e entra no aposento. Você desembainha a espada em guarda e se prepara para enfrentar a sinistra criatura com pinças gigantescas e ferrão mortal. ESCORPIÃO GIGANTE	HABILIDADE 10	ENERGIA 10 O Escorpião o ataca com ambas as pinças, e você terá que considerar cada uma das pinças como uma entidade separada, como se lutasse contra duas criaturas. Ambas as pinças possuem HABILIDADE 10 e o atacarão separadamente em cada Série de Ataque, mas você terá que escolher qual delas enfrentará. Ataque uma pinça como numa batalha normal. Contra a outra pinça, você joga os dados para determinar sua Força de Ataque da forma costumeira, mas você não causará ferimentos ao Escorpião, mesmo que sua Força de Ataque seja maior; conte isso como se você tivesse apenas conseguido se defender de um golpe. É claro que, se a Força de Ataque da pinça for maior que a sua, você será ferido da maneira usual. Se, durante qualquer das Séries de Ataque, a Força de Ataque do Escorpião totalizar 22, volte para 2. Se você conseguir matar o Escorpião sem que ele atinja uma Força de Ataque de 22, vá para 163."
cap144 = "Ainda sorrindo, o velho olha para você e diz em voz baixa: 'Errado.' Volte para 85."
cap145 = "O Anão estava esperando seu movimento. Além disso, você não é tão rápido quanto deveria, devido ao sofrimento recente, por isso ele evita seu golpe facilmente, dizendo: “Eu poderia matá-lo agora, se quisesse, mas estou com saudades de uma luta corpo a corpo.” Em seguida, ele larga a besta no chão e puxa uma acha do cinto. Apesar da fadiga, você só pensa em vingança. ANÃO	HABILIDADE 8	ENERGIA 6 Durante cada Série de Ataque, você terá que reduzir sua Força de Ataque em 2, por causa da sua condição física. Se você vencer, volte para 28."
cap146 = "A dor nos pulmões força-o a subir à superfície para respirar. Felizmente, nenhum dos Trogloditas o vê e todos se dispersam. Você sai do rio e atravessa a ponte para a margem norte. Quaisquer Provisões restantes que você possa ter estão agora imprestáveis. Você segue pela vasta caverna até que, finalmente, vê um túnel na parede do outro lado. Você anda até ele e chega a uma pesada porta de madeira, que está trancada. Se você tiver uma chave de ferro, volte para 86. Se não tiver a chave, vá para 276."
cap147 = "A água no tubo de bambu é agradavelmente refrescante. Você ganha 1 ponto de ENERGIA. A água contém também uma solução mágica que lhe permite expor-se a temperaturas altíssimas sem sofrer danos. Jogando fora o bambu, você segue para o norte de novo com excelente disposição. Vá para 182."
cap148 = "Nada há a fazer senão descer as escadas, na direção dos cachorros que latem. Você chega ao pé da escada com a espada na mão e enfrenta os dois gigantescos CÃES DE GUARDA, que saltam sobre você, um de cada vez./\n/Primeiro CÃO DE GUARDA HABILIDADE - 7 ENERGIA - 7 /\n/Segundo CÃO DE GUARDA	HABILIDADE - 7 ENERGIA - 8  /\n/Se você vencer, vá para 175. Você pode Fugir depois de matar o primeiro Cão de Guarda, correndo para leste pelo túnel. Vá para 315."
cap149= "Você solta a corda e ouve ela cair no fundo do poço. O Bárbaro o amaldiçoa, prometendo matá-lo se seus caminhos se cruzarem outra vez. Você recua, toma distância e salta. Cai em segurança do outro lado do poço e continua para o oeste. Mais adiante no túnel, você pisa em uma parte do chão de pedra que se inclina para frente, disparando uma armadilha que solta um rochedo preso frouxamente no teto. Você olha para cima bem no momento em que o rochedo está prestes a cair sobre você. Teste sua Sorte. Se você tiver sorte,volte para 70. Se não tiver sorte, vá para 353"
cap150 = "Tendo tido a boa idéia de não pôr o seu braço da espada dentro do buraco, os efeitos do tentáculo não são muito graves. Você perde 1 ponto de HABILIDADE. Enfiando novamente o braço no buraco, de lá retira o gancho e a bolsa de couro. Dentro da bolsa, você encontra um minúsculo sino de metal. Guarda suas novas posses na mochila e continua para o norte. Vá para 292."
cap151 = "Quando toca o olho de esmeralda do ídolo, você ouve um rangido abaixo. Ao olhar, fica abismado ao ver os dois pássaros empalhados voando. As asas das criaturas batem aos arrancos, mas logo estão acima de você e parecem prontos para atacar. Lute com um dos GUARDIÃES VOADORES de cada vez, mas reduza sua HABILIDADE em 2 pontos durante este combate, pois a posição restringe-lhe os movimentos.\n/Primeiro GUARDIÃOVOADOR HABILIDADE - 7 ENERGIA - 8 /\n/Segundo GUARDIÃO VOADOR HABILIDADE - 8 ENERGIA - 8 /\n/Se você vencer, vá para 240."
cap152 = "O Anão o cumprimenta por ter adivinhado corretamente. Ele diz que agora você deverá seguir para a segunda fase do teste. Apanhando uma cesta de vime, ele lhe diz que há uma cobra dentro dela. Vira a cesta e a cobra cai ao chão; é uma naja, que se ergue no ar, pronta para o bote. O Anão diz que quer testar suas reações. De mãos vazias, você deverá segurar a naja pelo pescoço, evitando-lhe os dentes mortais. Você se agacha, tensionando os músculos para o momento decisivo. Jogue dois dados. Se o total for igual ou menor que a sua HABILIDADE, volte para 55. Se o total for maior que a sua HABILIDADE, vá para 202."
cap153 = "A porta abre para um pequeno aposento, no qual há um crânio humano cujos olhos são jóias, pousado sobre um pedestal de mármore. Uma bateria de bestas com dardos está fixada à parede da esquerda, e duas pequenas bolas de madeira estão no chão, bem perto da porta. Você: /\n/Entrará no aposento e apanhará o crânio? - Vá para 390 /\n/Jogará, da porta, uma das bolas de madeira no crânio? - Vá para 371/\n/ Fechará a porta e continuará para o oeste, levando as bolas de madeira? - Volte para 74"
cap154 = "Correndo pelo túnel, você logo alcança o Bárbaro e diz a ele que a passagem do leste conduz a um beco sem saída. Ele faz um aceno com a cabeça, num entendimento silencioso, e ambos partem para o oeste. Volte para 22."
cap155 = "As palavras do poema dela cruzam velozmente a sua mente: “Quando o corredor a água encontrar, não se apresse em recuar...” Está claro, é aqui que ela quer que você mergulhe na água. Agora, você deve decidir. Se quiser mergulhar na água, vá para 378. Se preferir caminhar de volta para o túnel, vá para 322."
cap156 = "A pequena placa desliza e se abre facilmente, e você divisa um aposento com um poço profundo no chão atrás da porta. Na parede do outro lado, há dois ganchos de ferro, num dos quais está pendurado um rolo de corda. Se você quiser abrir a porta, pular por cima do poço e pegar a corda, vá para 208. Se preferir continuar para o norte pelo túnel, vá para 326."
cap157 = "O pequeno cofre se abre facilmente; dentro, uma bolsa de veludo negro contém uma pérola grande. Some 1 ponto de SORTE. Depois de pôr a pérola no bolso, você avança em meio às teias de aranha. Vá para 310."
cap158 = "Você leva a moringa aos lábios e toma um gole. O líquido queima tanto que você larga a moringa e segura a garganta em agonia. Você engoliu ácido! Perde 1 ponto de HABILIDADE e 4 de ENERGIA. Se ainda estiver vivo, vá para 275."
cap159 = "Suas reações ainda estão lentas por causa do veneno em seu organismo, e, embora você tente pular por cima da língua estendida, suas pernas o traem. A língua pegajosa se enrosca em torno da sua perna, derrubando-o, e começa a □uxa-lo na direção da poça. A espada escorregou da sua mão, e você começa a entrar em pânico. Se você tiver um punhal, vá para 294.Se não tiver um punhal, vá para 334."
cap160 = "Sua armadura e sua espada são pesadas e dificultam o salto, mas você aterrissa em segurança, por um triz, na borda do outro lado do poço. Você não perde tempo e se encaminha para o leste. Vá para 237."
cap161 = "Você passa sem parar pelos dois Leprechauns e segue para o norte, os risos e a gozação ainda ecoando nos seus ouvidos. Mais adiante no túnel, você pára para descansar e verificar seus pertences. Se você tinha gemas, elas agora sumiram. O Leprechaum que caiu sobre as suas costas roubou-as da mochila. Você amaldiçoa os Leprechauns ladrões e prossegue para o norte. Volte para 29."
cap162 = "Retirando a tampada caixa na luz do túnel, você encontra uma chave de ferro e uma gema grande. É uma safira. Some 1 ponto de SORTE. Colocando as coisas cuidadosamente na mochila, você parte para o norte mais uma vez. Volte para 142."
cap163 = "O Anão o chamada sacada, congratulando-o pela vitória. Ela joga um saco na arena e lhe diz para relaxar e recuperar as forças para a parte final do teste. Depois, ele sai, dizendo que estará de volta em 10 minutos. Você abre o saco e encontra uma moringa com vinho e galinha cozida. Se você quiser comer o que o Anão ofereceu, vá para 363. Se preferir simplesmente ficar sentado, esperando que ele volte, vá para 302."
cap164 = "Enquanto você caminha, pingos de água voltam a cair do teto do túnel. Você vê pegadas úmidas, feitas pelas mesmas botas que você havia seguido anteriormente, se dirigindo para o oeste. As pegadas conduzem a uma porta de ferro fechada na parede do lado direito do túnel, mas não parecem continuar a partir dali. Se quiser abrir a porta, vá para 299. Se preferir continuar em frente para o oeste, volte para 83."
cap165 = "Há uma ranhura no cadeado, na qual você coloca a moeda. Imediatamente, o cadeado se abre, e você consegue desacorrentar as pernas-de-pau. Você as coloca nos ombros e, mais uma vez, parte para o norte. Vá para 234."
cap166 = "Ao tocar o olho de esmeralda do ídolo, você ouve um rangido abaixo de si. Olhando na direção do ruído. Você fica abismado ao ver os dois pássaros empalhados voando. As asas dele batem aos arrancos, mas logo estão sobre você e parecem prontos para atacar. Lute com um dos GUARDIÕESVOADORES de cada vez, mas reduza a sua HABILIDADE em 3 pontos durante este combate, pois a posição restringe-lhe os movimentos./\n/Primeiro GUARDIÃO VOADOR HABILIDADE - 7 ENERGIA - 8 /\n/Segundo GUARDIÃO VOADOR HABILIDADE - 8 ENERGIA - 8 /\n/ Se você vencer, volte para 11.	"
cap167 = "Você gira o gancho de ferro em torno da cabeça e o atira na fera lá embaixo. As enormes mandíbulas do Diabo do Poços e fecham firmemente sobre o gancho, e, em seguida, ele joga a cabeça para trás. Ainda segurando a corda, você é puxado do alto da muralha e despenca no fundo do poço. Você perde 4 pontos de ENERGIA. Se ainda estiver vivo, vá para 203."
cap168 = "Levantando o trinco e empurrando a pesada porta de pedra, você se vê em uma grande caverna. A luz é fraca e sombria, mas seus olhos logo se adaptam e você vê que as paredes são úmidas e revestidas de algas verdes. O chão está coberto de palha. A atmosfera é quente, úmida e fétida, e um zumbido suave enche o ar. Com cautela, você avança pela palha na direção de um dos cantos da caverna, onde parece haver um poço raso. Espiando com cuidado para dentro do poço, você fica enojado ao ver uma massa de vermes esbranquiçados que se contorcem, alguns deles chegando a meio metro de comprimento. Nauseado, você está prestes a ir embora quando repara que os corpos ondulantes dos vermes estão amontoados em torno de um punhal, cuja ponta está firmemente presa a uma fenda no fundo do poço. O cabo é envolto em couro negro com incrustações de opalas, e a lâmina é feita de um estranho metal lustrado preto-avermelhado. Você fica doido para pegar a arma, mas isso significaria enfiar a mão no meio daqueles vermes. Você tenta apanhar o punhal - volte para 94 - ou recua enojado e sai da caverna - vá para 267."
cap169 = "Ele olha desconfia do quando você lhe oferece uma parte das suas Provisões. Mas a fome é mais forte que o medo, e ele acaba pondo a comida na boca. Você pergunta o que ele está fazendo nos túneis, e ele explica que é servo de um dos Juízes da Prova, os controladores de seções do calabouço designados pelo Barão Sukumvit. Diz que gostaria de escapar, mas ninguém pode sair do calabouço, a fim de impedir que o segredo da construção seja revelado. Você diz-se um dos concorrentes na Prova dos Campeões e que apreciaria qualquer tipo de ajuda. Esfregando o queixo, ele vira-se para você e diz: “Tudo o que lhe posso dizer é que, em um dos túneis setentrionais, há uma cadeira esculpida na forma de um pássaro demoníaco; um painel secreto no braço da cadeira contém uma poção em um frasco de vidro. É uma Poção de Réplica. Agora, preciso realizar minhas tarefas. Boa sorte. Espero que nos encontremos de novo fora destes túneis infernais.” O homem sai se arrastando e você continua sua jornada para o oeste. Volte para 109."
cap170 = "Ao se aproximar da figura prostrada, você vê que é um dos seus rivais na Prova dos Campeões. É, na realidade, a Mulher-elfo. Ela luta tenazmente pela vida, envolta no abraço de uma enorme JIBÓIA que lhe esmaga os ossos. Se você quiser ajudá-la, vá para 281. Se preferir deixá-la à própria sorte e retornar pelo túnel para seguir para o norte, vá para 192."
cap171 = "A porta abre para um pequeno aposento, mas, antes que saiba o que está acontecendo, você despenca no vazio havia um poço atrás da porta e você não o viu. Você cai pesadamente no fundo e se contorce em dores. Perde 4 pontos de ENERGIA. As paredes do poço são rugosas e têm muitos pontos onde apoiar os pés e as mãos; por isso, você consegue fazer a escalada e sair com bastante facilidade. Você amaldiçoa sua própria ansiedade e diz a si mesmo que doravante será mais cuidadoso. No interior do aposento, você vê dois ganchos de ferro numa das paredes. Há um rolo de corda pendurado em um deles; você o coloca na mochila, salta de volta por cima do poço e sai do aposento, dirigindo-se ao norte. Vá para 326."
cap172 = "Lembrando da descrição da abjeta Besta Sangrenta, e da advertência quanto aos gases tóxicos que exalam da poça da fera, você cobre a boca com a manga da camisa e, atento, avança, espada na mão, para a língua do monstro. Enquanto você contorna a poça, a fera se projeta para frente e estica a língua, mas você está prevenido e a perfura com um golpe da espada. A fera urra de dor e se estica, frenética, para fora da poça, tentando abocanhá-lo com as mandíbulas inundadas de sangue. Você golpeia-lhe a carantonha com a espada, na tentativa de atingir-lhe os olhos verdadeiros. BESTA SANGRENTA -	HABILIDADE 12 /	ENERGIA 10 Quando você vencer a sua segunda Série de Ataque, vá para 278."
cap173 = "A água fresca é revigorante e vem de uma fonte que foi salpicada com poeira de Duende. Se você ainda não o fez, poderá beber da outra fonte - vá para 337 - ou continuar para o norte - vá para 368."
cap174 = "Quando você está retornando para a porta, o zumbido aumenta de intensidade, e você procura desesperadamente descobrir de onde ele vem. Ao olhar para o alto, você vê num relance a imensa e grotesca forma negra de uma MOSCA GIGANTE surgindo de uma reentrância no alto da parede da caverna. Ao se aproximar, você se dá conta de que ela tem pelo menos um metro e meio de comprimento. As asas opacas vibram, produzindo o abominável zumbido que você vem ouvindo; as seis pernas peludas estão posicionadas para agarrá-lo; abaixo dos olhos multifacetados, há uma longa probóscida, negra e lustrosa, que se movimenta malignamente para dentro e para fora. Você retirou o tesouro da Mosca Gigante do ninho de larvas, e agora deve enfrentar as consequências. Teste sua Sorte. Se você tiver sorte, volte para 39. Se não tiver sorte, vá para 350."
cap175 = "Presa à coleira de um dos Cães de Guarda, há uma cápsula de metal. Você retira a parte de cima da cápsula e encontra um pequeno dente lá dentro. É um dente de Leprechaum, que lhe trará boa sorte. Some 2 pontos de SORTE. Você põe o dente no bolso e parte para o leste pelo túnel. Vá para 315."
cap176 = "Caminhando cuidadosamente, você vai subindo os degraus devagar. Logo chega ao topo sem problemas. Continue pelo túnel e vá para 277"
cap177 = "Você só tem tempo para ouvir o Gnomo gritar: “Três coroas!”, antes que a fechadura estale e abra. Quando a pesada porta gira lentamente para fora, o Gnomo corre na direção dela, jogando a bola de vidro a seus pés. Um gás verde escapa do vidro quebrado, e você tenta não o inspirar. Teste sua Sorte. Se você tiver sorte, vá para 243. Se não tiver sorte, volte para 103."
cap178 = "A porta não resiste às violentas pancadas que  você desfere. A placa central racha e se despedaça; você abre a pontapés um buraco grande o bastante para por ele se esgueirar. Molhado, mas feliz por ter sobrevivido a essa ameaça, você parte para o norte de novo. Vá para 344."
cap179 = "Quando você parte na direção do Anão, ele tira do cinto dois dardos de mão e os atira contra você e Throm, atingindo-os nas pernas. Ambos ficam instantaneamente paralisados pelo veneno existente na ponta dos dardos. Você perde 2 pontos de ENERGIA. Como que pregado ao chão, você vê o Anão se aproximar e retirar-lhe o dardo coxa. Ele pergunta se agora você está disposto a entrar da em seu campeonato. Você se esforça para balançar a cabeça afirmativamente. Aos poucos, os efeitos do veneno se dissipam, e a mobilidade retorna. O Anão ordena que você o siga e que Throm espere o retorno dele. Ele abre uma porta secreta na parede da câmara, e vocês entram em um pequeno aposento circular. Ele fecha a porta atrás de você e lhe dá dois dados de osso, mandando que os jogue no chão. Você tira um seis e um dois, total oito. O Anão ordena um novo lançamento, mas desta vez você tem que adivinhar o total: será igual, maior ou menor que oito? Se você preferir igual a oito, vá para 290. Se optar por maior que oito, volte para 84. Se escolher menor que oito, vá para 191."
cap180 = "Você avança na direção da Besta Sangrenta; de repente, sente-se fraco. O gás que emana da poça é altamente tóxico, e você vai ao chão, inconsciente. Teste sua Sorte. Se você tiver sorte, volte para 53. Se não tiver, vá para 272."
cap181 = "O túnel conduz a um salão com piso de mármore e pilares que se erguem até o teto. Ao atravessar o piso, suas passadas ecoam pelo salão. Os cabelos da sua nuca começam a ficar em pé, pois você pressente que está sendo observado. Sem que você saiba, um dos seus rivais se esconde atrás de um pilar. É o NINJA, o terrível assassino vestido com o manto negro. Sem qualquer ruído, ele sai do esconderijo e joga um disco estrelado nas suas costas. Uma voz interior manda que você se abaixe. Teste sua Sorte. Se você tiver sorte, vá para 312. Se não tiver sorte, volte para 45."
cap182 = "A temperatura continua a subir, e você começa a pingar suor. Adiante, o calor se intensifica. Parece que você está numa fornalha. A situação é tão insuportável que você começa a desfalecer. Se você tiver bebido o líquido do tubo de bambu, volte para 25. Se não tiver parado para beber o líquido, vá para 242"
cap183 = "Você sobe nas pernas-de-pau e dá alguns passos experimentais. Sua confiança aumenta, e logo você se sente capaz de enfrentar a caminhada pelo lodo. A fumaça sobe da base das pernas-de-pau: o lodo começa a corroê-las. Você segue em frente com firmeza e acaba atingindo terreno sólido de novo. Infelizmente, as pernas-de-pau ficam cobertas de lodo, e você é forçado a abandoná-las. Se quiser ir para o oeste, vá para 386. Se preferir continuar para o norte, vá para 218."
cap184 = "O Bárbaro, que se diz chamar Throm, amarra a corda em volta da cintura, dando-lhe a outra ponta. Ao acender a tocha, você nota um ar de desconfiança nos olhos do Bárbaro. Lentamente, ele sobe na borda do poço, enquanto você se firma no chão e segura a corda tensa. Ao abaixá-lo aos poucos, você vê os lados lisos do poço iluminados pela tocha de Throm. Ele finalmente chega ao fundo e grita que há um outro túnel rumo ao norte. Manda que você prenda a corda em uma rocha saliente na borda do poço e desça. Se você quiser ficar com o Bárbaro e seguir para o norte pelo túnel inferior, vá para 323. Se desejar abandoná-lo, pulando por cima do poço para se dirigir ao oeste, volte para 149"
cap185 = "Os Trogloditas estão tão concentrados na dança tribal que não ouvem o ruído da sua espada, e você engatinha e passa. Quando acha que está suficientemente longe, você se levanta e corre pelo piso da caverna. À sua frente, corre um rio subterrâneo de leste para oeste através da caverna; sobre ele, uma ponte de madeira. Ao ouvir um barulho, você olha para trás e toma consciência de que foi descoberto. Os Trogloditas estão vindo atrás de você. Se quiser correr pela ponte, vá para 318. Se preferir mergulhar no rio, volte para 47"
cap186 = "Lenta e cuidadosamente, você começa a escalar o ídolo. Quando está prestes a segurar na grande orelha, seu pé escorrega, Teste sua Sorte. Se você tiver sorte, vá para 260. Se não tiver sorte, vá para 358."
cap187 = "O túnel faz uma curva fechada para a direita, depois da qual você vê um velhinho de barba longa encolhido atrás de uma grande cesta de vime. A cesta está amarrada a uma corda cuja ponta desaparece no teto. Com aparência preocupada,o velho diz: “Não me ataque, estranho. Não sou nenhuma ameaça para você. Estou aqui simplesmente para ajudá-lo. Se você fizesse a gentileza de me oferecer algum tipo de remuneração, eu ficarei feliz em içá-lo na cesta para o nível superior. E, acredite-me, você deveria estar lá.” Se você quiser dar ao homem alguma coisa da sua mochila pelo serviço, vá para 360. Se preferir passar por ele e seguir pelo túnel, vá para 280."
cap188 = "O túnel começa a declinar e termina numa poça profunda. Se você conseguir se lembrar do poema da garota-espírito, volte para 155. Se não tiver encontrado a garota-espírito, vá para 224."
cap189 ="As pontas da maça do Orca penetram dolorosamente na sua coxa esquerda. Você perde 3 pontos de ENERGIA. Você cambaleia para trás, mas consegue recuperar o equilíbrio a tempo de se defender. Felizmente, o túnel é estreito demais para que ambos os Orcas ataquem-no a um só tempo. Lute com um de cada vez. /\n/Primeiro ORCA HABILIDADE - 5 ENERGIA - 5/\n/ Segundo ORCA HABILIDADE - 6 ENERGIA - 4/\n/ Se você vencer, vá para 257."
cap190 = "Seu corpo vibra desenfreadamente, e você não consegue evitar o desmaio. Você perde 3 pontos de ENERGIA. Se ainda estiver vivo, volte para 50."
cap191 = "Jogue dois dados. Se o total for menor que oito, volte para 152. Se o total for igual ou maior que oito, volte para 121."
cap192 = "Caminhando pelo túnel, você repara em uma grade de ferro no chão. Se quiser parar e levantá-la, volte para 120. Se preferir prosseguir, vá para 292"
cap193 = "O ácido queima a parede do seu estômago, penetrando nos seus órgãos vitais. Você tomba inconsciente para nunca mais se recuperar. Sua aventura termina aqui."
cap194 = "Em uma plataforma de pedra na parede do túnel, você vê dois livros empoeirados encadernado sem couro. Throm expressa seu desprezo pela palavra escrita com um grunhido, insistindo para que você deixe os livros de lado e siga adiante com ele. Você:/\n/ Abrirá o livro de couro vermelho? - Volte para 52/\n/ Abrirá o livro de como preto? -	Volte para 138/\n/ Continuará para o norte pelo túnel? - Vá para 369"
cap195 = "Você desembainha a espada e corre na direção do velho. Ele ergue o braço esquerdo e, subitamente, você esbarra em uma barreira invisível. “Não seja tolo, meus poderes são grandes!”, diz o velho calmamente. “Se você não acredita em mim, veja isto.” Saindo do nada, um punho voador lhe desfere um soco no rosto antes que você possa se esquivar.Você perde 1 ponto de ENERGIA. Você sacode a cabeça e esfrega o queixo. Parece que não tem alternativa senão tentar responder à pergunta do velho. Vá para 382."
cap196 = "Você levanta o escudo bem a tempo de se proteger de uma saraivada de espinhos lançados contra seu coração pela cauda do Mantécora. Ileso, com os espinhos cravados no escudo, você desembainha a espada e avança para o Mantécora.MANTÉCORA	HABILIDADE 11	ENERGIA 11 Se você vencer, vá para 364."
cap197 = "Graças aos céus, a temperatura agora começa a cair rapidamente, e logo parece quase fresca de novo. No lado esquerdo do túnel, há uma porta fechada e nela, uma pequena placa de ferro que talvez possa ser aberta. Você:/\n/ Tentará abrir a porta? - Volte para 171 /\n/Tentará fazer deslizar a placa de ferro? - Volte para 156 /\n/Continuará para o norte, subindo o túnel? - Vá para 326"
cap198 = "Quando o gás se dissipa, você caminha de volta para a arca e olha dentro dela. Há uma corrente com pingente jogada no fundo, mas alguém já retirou a pedra que estava incrustada nele. Isso o aborrece tanto que você o atira ao chão e sai furioso do aposento, subindo o túnel. Vá para 230"
cap199 = "Os dardos da besta são em número tão grande que é impossível evitá-los. Jogue um dado para determinar o número de dardos que lhe atingem o corpo, perdendo 2 pontos de ENERGIA para cada um deles. Se ainda estiver vivo, terá que descansar aqui por um longo tempo para se recuperar dos ferimentos. Perde 1 ponto de SORTE. Quando você, finalmente, se sente forte o bastante para seguir adiante, sai do aposento e continua para o oeste pelo túnel. Volte para 74."
cap200 = "A porta abre para um pequeno aposento como chão coberto de palha. No centro do aposento, há uma grande gaiola coberta de cerca de dois metros de altura; uma corda presa ao topo da cobertura de pano passa por um anel de ferro no teto e desce até o chão. Se você quiser levantar o pano, vá para 321. Se preferir sair do aposento e se dirigir para o norte pelo túnel, vá para 316."
cap201 = "Você revista os armários e caixas no quarto de Erva mas não encontra nada, a não ser um osso velho. Há uma porta na parede leste da câmara, e você resolve sair. Pode levar o osso velho, se quiser. Você agora está de pé no final de um outro túnel. Vá para 305."
cap202 = "As reações da naja são mais rápidas do que as suas, e a cabeça estufada do animal se projeta para mordê-lo. Teste sua sorte. Se você tiver sorte, volte para 18. Se não tiver sorte, volte para 42."
cap203 = "Você se levanta com dificuldade e desembainha a espada. Faz isso bem a tempo, pois a assustadora fera se aproxima velozmente. Esta vai ser uma das lutas mais difíceis de sua vida."
cap204 = "Há uma placa sensível à pressão no topo do pedestal, e, logo que o crânio é colocado de volta sobre ele, o mecanismo invisível é disparado. Imediatamente, uma chuva de dardos lançados pela besta atravessa o aposento. Teste sua Sorte. Se você tiver sorte, volte para 131. Se não tiver sorte, volte para 199."
cap205 = "Correndo atrás dos Leprechauns, você ouve mais risos, só que agora eles vêm de trás de você. Você se vira e vê mais seis Leprechauns saindo de uma porta oculta na parede do túnel. De repente, mais um Leprechaun salta de uma plataforma fixada no teto e cai sobre suas costas. Livrando-se dele com um safanão, você desembainha a espada, o que faz com que os Leprechauns riam ainda mais alto. Se você quiser atacá-los, vá para 306. Se preferir tentar passar por eles, volte para 161."
cap206 = "As estalactites continuam a cair ao redor, mas você não tem força suficiente para fazer mais do que se arrastar na direção do arco. De repente, sente um braço em volta da cintura e se dá conta, em estado de semi-inconsciência, de que Throm o está carregando. Ele o põe na segurança do túnel e cuida dos seus ferimentos. Você resolve comer parte das Provisões para ajudar a recuperar as forças, e dá também uma parte para Throm, como agradecimento por ele tê-lo salvado. Ele se desculpa por ter iniciado o desabamento das rochas e lhe oferece a mão. Apesar da dor, você consegue sorrir e apertar a mão dele. Quando você finalmente se recupera, levanta-se e segue para o leste, com Throm caminhando à sua frente. Volte para 60."
cap207 = "Você tira a camisa e a rasga ao meio, depois amarra cada um dos pedaços em volta de cada pé, a fim de se proteger em certa medida do lodo corrosivo, e dispara para cruzá-lo a passos largos. No terreno fume do outro lado do lodaçal, você tenta freneticamente, com a espada, arrancar a camisa que queima em seus pés. Porém, parte do lodo penetrou até seu tornozelo. Você perde 3 pontos de ENERGIA. Partindo para o norte de novo, você chega a uma encruzilhada. Se quiser ir para o oeste, vá para 386. Se preferir continuar para o norte, vá para 218."
cap208 = "A porta abre para o aposento; você toma distância e salta sobre o poço. Coloca a corda na mochila e salta de volta por sobre o poço para sair do aposento e prosseguir para o norte. Vá para 326."
cap209 = "Você fica desolado ao descobrir que não apenas todas as suas Provisões restantes estão encharcadas e imprestáveis para comer, mas também que um dos seus tesouros desapareceu. Risque um item da sua Lista de Equipamentos ou uma de suas jóias ou poções. Você guarda cuidadosamente na mochila as posses que lhe restam e parte para o norte outra vez. Vá para 356."

cap210 = "Você entra em um aposento no qual há um homem maltrapilho, de pé, acorrentado, à parede pelo braço esquerdo. Vendo que ele não tema mão direita, você se dá conta de que a mão pregada na porta deve ser dele. Implorando piedade, ele se encolhe para longe de você, tanto quanto as correntes permitem. Se você quiser libertá-lo das cadeias, volte para 27. Se preferir sair do aposento e se dirigir para o norte, volte para 78."
cap211 = "Você consegue se livrar do aperto de Erva e desembainha a espada. Apanhando um banco quebrado para lhe servir de arma, ela avança na sua direção // ERVA // HABILIDADE 9 // ENERGIA 9"
cap212 = "Segurando a corda firmemente, você toma distância para o salto. Contudo, sob a luz fraca, você não nota que alguém enfraqueceu a corda, a ponto de parti-la em duas, logo acima do local em que você está segurando. Quando se lança por sobre o poço, a corda rompe e você grita de medo ao despencar de cabeça nas profundezas. Vá para 285"
cap213 = "O túnel logo se divide em dois. Você ouve um zumbido que vem do ramo da direita. Se quiser caminhar para o oeste para investigar quem ou o que está fazendo o ruído, volte para 108. Se preferir continuar para o norte, volte para 14."
cap214 = "Caminhando em frente, você vê uma linha vermelha pintada no chão do túnel e nota um aviso na parede que diz: “Armas não são permitidas a partir deste ponto.” Se você quiser abandonar suas armas antes de continuar para o norte, vá para 389. Se preferir ignorar o aviso e prosseguir para o norte, volte para 181."
cap215 = "Sua espada arrebenta facilmente a fina casca externa da gigantesca bola de esporos. Uma espessa nuvem de esporos saída da bola se espalha e o envolve. Alguns dos esporos grudam- se à sua pele, que começa a coçar terrivelmente. Aparecem grandes caroços no seu rosto e braços, e sua pele parece estar em fogo. Você perde 2 pontos de ENERGIA. Coçando freneticamente os caroços, você passa por cima da bola de esporos, agora murcha, e segue para o oeste. Volte para 13."
cap216 = "Reconhecendo a cabeça de serpentes da Medusa, você fecha os olhos para evitar o olhar mortal da criatura que o transformaria em pedra. Se você quiser entrar na gaiola com os olhos fechados para enfrentá-la com sua espada, vá para 308. Se preferir recuar para sair do aposento com os olhos fechados e continuar para o norte, vá para 316."
cap217 = "A passagem começa a subir lentamente, conduzindo-o sempre para o norte. Você não passa por uma única encruzilhada. Não há portas ou mesmo uma alcova para ser investigada, e você vai ficando mais relaxado enquanto segue adiante. Depois de certo tempo, você se torna tão temerário que não repara em um fino arame estendido bem baixo de lado a lado da passagem. Somente quando o seu pé o toca, e você ouve um ronco distante, é que se dá conta do erro que cometeu. O ronco cresce até um nível ensurdecedor, e subitamente surge da penumbra do túnel à sua frente um gigantesco rochedo que vem rolando na sua direção, ganhando velocidade a cada segundo. Largando o escudo, se tiver um (você perde 1 ponto de HABILIDADE), você se volta para fugir do rochedo que se aproxima. Volte para 36."
cap218 = "Você logo chega a uma porta dupla na parede da esquerda. Apura os ouvidos, mas não percebe nada. Tenta a maçaneta, ela gira, você abre uma fresta na porta da esquerda e dá uma espiada. Um guerreiro armado jaz de bruços no chão de um aposento vazio, de paredes lisas e teto baixo. Ele deve estar morto, pois permanece inerte mesmo quando você grita por ele. Uma jóia grande, talvez um diamante, está caída logo adiante do braço esticado. Se você quiser entrar no aposento e pegar a jóia, volte para 65. Se preferir continuar para o norte, vá para 252."
cap219 = "A dor nos pulmões força-o a subir à tona para respirar. Infelizmente, um dos Trogloditas o vê e grita pelos companheiros. Indefeso, você vê os arqueiros fazerem pontaria, e uma saraivada de flechas cai sobre você com impacto fatal. Seu corpo sem vida desce o rio boiando, penetrando nas profundezas ocultas da montanha."
cap220 = "Um 'bong' sombrio soa como um toque de sino fúnebre. Tudo vibra à sua volta, e você aperta os dentes quando sua cabeça também estremece. Todo seu corpo está tremendo, e você cai. Você tirita e tem calafrios, contorcendo-se convulsivamente no chão, à medida que as vibrações se intensificam. Procura desesperadamente uma maneira de parar o sino. Você:\nGritará o mais alto possível? (Volte para 61)\nTentará abafar o sino com sua bota? (Vá para 346)"
cap221 = "O túnel conduz a uma caverna úmida de teto alto, como chão coberto de rochas. Estalactites em forma de dentes pendem ameaçadoramente, os pingos constantes criando poças leitosas no chão. O túnel prossegue atravessando a passagem em arco, a qual é talhada na forma de uma boca demoníaca. Se você quiser examinara caverna, vá para 374. Se preferir prosseguir direto pela passagem em arco, volte para 60."
cap222 = "Você reconhece a fera - é um MANTÉCORA. Levando a sério a advertência do poema, você fica atento para a cauda dele, de cuja ponta sai uma profusão de espinhos afiados, grossos e duros como dardos de ferro. Se você tiver um escudo, volte para 196. Se não estiver carregando um escudo, volte para 6."
cap223 = "Você pisa com confiança no primeiro poste e avança para o próximo. Ao tocar o terceiro poste, ele imediatamente solta uma chuva de farpas afiadas, cada uma com vários centímetros de comprimento. Você perde 2 pontos de SORTE. As farpas voam em todas as direções a grande velocidade, e você não consegue evitá-las. Jogue dois dados para saber o número de farpas que lhe penetram a pele. Cada uma delas reduz sua ENERGIA em 1 ponto. Se você ainda estiver vivo, consegue arrastar-se por sobre os postes restantes e se senta para a dolorosa tarefa de retirar as farpas do corpo. Depois de descansar um pouco, você segue para o leste. Vá para 313."
cap224 = "Parece não haver como continuar para o norte. Você dá meia-volta e retorna pelo túnel, passando pela cadeira de madeira. Logo chega à encruzilhada e vira à direita para seguir para o oeste. Volte para 43."
cap225 = "Você reage prontamente e, com um golpe de espada, consegue cortar a língua estendida da Besta Sangrenta. A fera urra de dor e se atira para frente, tentando prendê-lo nas mandíbulas ensangüentadas. Esta será uma luta até a morte. // BESTA SANGRENTA	// HABILIDADE 12 // ENERGIA 10 // Quando vencer a sua primeira Série de Ataque, Teste sua Sorte. Se você tiver sorte, volte para 97. Se não tiver sorte, volte para 21."
cap226 = "A carne contém ervas que lhe aumentarão a força. Some 3 pontos seu índice de ENERGIA. Você pode caminhar até a alcova, se ainda não o fez - volte para 41 - ou sair da câmara e continuar para o oeste - volte para 83."
cap227 = "Ainda sorrindo, o velho olha para você. “Errado”, ele diz em voz baixa. Volte para 85."
cap228 = "Você enfia o braço no buraco e sente seu sangue gelar quando uma coisa quente e pegajosa se enrosca nele. Você consegue tirar o braço de dentro do buraco, mas um horrendo tentáculo, com ventosas incrivelmente fortes, está pendurado nele. Quando você consegue se libertar, cortando o tentáculo, seu braço dói e lateja. Teste sua Sorte. Se você tiver sorte, volte para 150. Se não tiver sorte, volte para 33."
cap229 = "229 Logo que sua cabeça entra embaixo da luz azul, você ouve o som de vozes abafadas. Os rostos já não riem, e as expressões são agora máscaras de desespero e angústia. O rosto triste de uma menina paira à sua frente, ela começa a sussurrar um poema. Em transe, você ouve atentamente, acreditando que ela tem uma mensagem especial para você, enquanto ela recita:\n Quando o corredor a água encontrar, Não se apresse em recuar. Mergulhe depois dos pulmões encher, Se sua Prova espera vencer.\nGuardando de cor o poema da garota-espírito, você atravessa o raio de luz e se dirige rapidamente para o norte. Volte para 107."
cap230 = "O túnel começa a se alargar e abre para uma imensa caverna, de onde você pode ouvir o som de muitas vozes agudas. Você se aproxima silenciosamente da entrada e espia. Cerca de 20 minúsculos seres, com narizes e orelhas compridos, correm em círculo em volta de uma grande efígie de ouro. Você:\nAndará até eles para conversar? Volte para 88 \nTentará se esgueirar e passar por eles?  Volte para 5 \nBeberá a Poção da Réplica (se você a tiver) // Vá para 385"
cap231 = "Você encontra uma poça atrás dos Hobglobins mortos e toma grandes goles de água fresca o mais rápido possível. Isso neutraliza o ácido e, lentamente, você começa a se recuperar. Ainda com dor, você se levanta e parte para o norte. Volte para 110."
cap232 = "Se você estiver desarmado, vá para 286. Se ainda estiver com suas armas, vá para 320."
cap233 = "Você parte um pedaço grande do cogumelo e o mastiga ansiosamente. De imediato, seu estômago incha, e você pode mesmo vê-lo estufando por baixo do cinto. Todo o seu corpo começa a se expandir, rasgando-lhe ruidosamente as roupas. Você fica cada vez maior, e logo seu rosto está imprensado de encontro ao teto. Os cogumelos que você comeu são muito procurados por mágicos para as poções de crescimento, mas para você eles significam a morte. Você está grande demais para poder algum dia sair da adega. Sua aventura termina aqui."
cap234 = "Um pouco mais adiante, você chega a uma parte do túnel coberta de lodo verde e espesso. Parece ameaçador, por isso você resolve testá-lo primeiro com um pedaço de pano. A pasta corrosiva do lodo queima o pano instantaneamente, não deixando nem sinal dele. Se você estiver carregando um par de pernas-de-pau, volte para 183. Se não as tiver, volte para 207."
cap235 = "Você não tem tempo para reagir antes que o dardo se crave na sua coxa. Você perde 2 pontos de ENERGIA. Se ainda estiver vivo, volte para 73."
cap236 = "O punho recua e prepara um novo ataque. Com a mão livre, você puxa a espada e tenta cortar a maçaneta da porta. Embora não o reconheça, você está sendo atacado pela forma fluida de um IMITADOR. // IMITADOR // HABILIDADE 9 // ENERGIA 8 /// Quando vencer sua primeira Série de Ataque, vá para 314."
cap237 = "O túnel faz uma curva súbita para a esquerda e continua para o norte até onde a vista alcança. Você logo chega a uma porta de madeira, fechada, na parede do lado esquerdo. Se você quiser abrir a porta, volte para 12. Se preferir continuar seguindo para o norte, volte para 100"
cap238 = "Ao cair, você consegue agarrar a corda com as mãos. Lentamente, você se iça até o outro lado e sobe para o piso. Você retira o elmo do poste e o põe na cabeça. O elmo foi feito por um ferreiro altamente habilidoso. Some 1 ponto de HABILIDADE. Não querendo se arriscar a caminhar de volta pela corda bamba, você resolve engatinhar por ela. De volta ao terreno firme, em segurança, você atravessa a passagem em arco para seguir pelo túnel na direção norte. Vá para 291."
cap239 = "239. Não muito adiante, o túnel chega a uma porta fechada à sua esquerda. Colocando o ouvido na porta, você escuta, mas não ouve nada. Se você quiser abrir a porta, volte para 102. Se desejar prosseguir para o norte, vá para 344."
cap240 = "Você olha para baixo e vê esparramados no chão os corpos inertes dos Guardiães Voadores. Você começa a forçar o olho esquerdo de esmeralda do ídolo com a ponta da espada. Finalmente, ele se solta e cai na sua mão; o peso da pedra o deixa surpreso. Esperando que seja de utilidade mais tarde, você a guarda na mochila. Se quiser agora forçar o olho direito, volte para 34. Se preferir descer do ídolo, volte para 89."
cap241 = "Uma cortina de veludo marrom fecha uma passagem em arco na parede oriental do túnel. Se você quiser descerrar a cortina e atravessar a passagem em arco, vá para 393. Se preferir continuar para o norte, vá para 291."
cap242 = "Você sacode a cabeça, tentando desesperadamente manter a consciência, mas o calor é intenso demais, e você perde os sentidos. Jogue dois dados. Se o total for igual ou menor que a sua HABILIDADE, volte para 48. Se o total for maior que a sua HABILIDADE, vá para 366."
cap243 = "Cobrindo o nariz e a boca com a mão, a fim de evitar inalar o gás, você segue o Gnomo pela porta aberta. Você entra em outro túnel, ao fim do qual aparece a visão bem vinda da luz do dia. Para sua grande surpresa, o Gnomo está morto no meio do caminho com um dardo de besta cravado na cabeça. Na ânsia por liberdade, o Gnomo caíra vítima da última armadilha do Barão Sukumvit. Você passa pelo infeliz e sai na luz brilhante do sol. Vá para 400."
cap244 = "Ele pega sua Peça de Ouro e lhe diz que, em um túnel setentrional, há uma cadeira de madeira esculpida na forma de um pássaro demoníaco. No braço da cadeira, um painel secreto contém uma poção em um frasco de vidro. “É uma Poção de Réplica, se eu bem me lembro. Boa sorte. Espero que nos encontremos de novo fora destes túneis infernais.” O homem sai arrastando os pés, e você continua sua jornada. Volte para 109."
cap245 = "Você não tem outra alternativa senão abrir a porta, já que o muro é liso demais para ser escalado. Respirando fundo, você gira a maçaneta e entra em um poço coberto de areia. Ali, um monstro enorme com aparência de dinossauro, chegando a uns 10 metros de altura, está de pé nas imensas patas traseiras, diante de grandes portas duplas na parede do outro lado. Possui um couro grosso verde malhado e uma boca com filas de dentes afiados como navalhas. As mandíbulas da criatura se abrem e fecham com força capaz de pulverizar ossos. E mesmo você não consegue evitar o tremor ao se aproximar do Diabo do Poço com a espada na mão. // DIABO DO POÇO //HABILIDADE 12 // ENERGIA 15"
cap246 = "Apesar de toda a cautela, sua perna raspa em um dos postes, que imediatamente solta uma chuva de farpas afiadas, cada uma com vários centímetros de comprimento. Você perde 2 pontos de SORTE. Elas voam em todas as direções com grande velocidade, e você não consegue evitá-las. Jogue dois dados para determinar o número de farpas que se cravam na sua carne. Cada farpa reduz sua ENERGIA em 1 ponto. Se ainda estiver vivo, você senta para a dolorosa tarefa de retirar as farpas do corpo antes de partir para o leste. Vá para 313."
cap247 = "A fera diante de você é o temível MANTÉCORA. A ponta da cauda da criatura guarda uma profusão de espinhos pontudos, grossos e duros como dardos de ferro. Subitamente, ele sacode a cauda, lançando uma saraivada de espinhos na sua direção. Jogue um dado. O número obtido é a quantidade de espinhos que lhe penetrarão o corpo. Cada espinho custa-lhe 2 pontos de ENERGIA. Se você ainda estiver vivo, avança com dificuldade para atacar o Mantécora com sua espada, antes que ele tenha tempo de disparar mais espinhos. // MANTÉCORA // HABILIDADE 11 // ENERGIA 11 Se você vencer, vá para 364."
cap248 = "As portas abrem para um túnel que segue para o norte. Você fecha as portas atrás de si e parte mais uma vez. Volte para 214."
cap249 = "Você só tem tempo de ouvir o Gnomo dizer: “Uma coroa e dois crânios”, antes que um raio branco de energia parta da fechadura e atinja-lhe o peito, derrubando-o sem sentidos. Jogue um dado, some 1 ao número obtido e reduza esse total de sua ENERGIA. Se ainda estiver vivo, você se recupera e ouve o Gnomo lhe dizer que tente de novo. Você sabe que colocou uma gema na ranhura certa, mas qual delas? Você suspira e tenta uma nova combinação.\nEsmeralda	Diamante Safira (Volte para 16)\nDiamante Safira  Esmeralda  (Vá para 392)\n Safira  Esmeralda  Diamante (Volte para 177) \nEsmeralda Safira  Diamante  (Vá para 287)\nDiamante  Esmeralda  Safira  (Volte para 132)\n Safira  Diamante  Esmeralda  (Fique em 249)"
cap250 = "Quando você corre para a porta, o velho grita atrás de você: “Não corra, ninguém escapa de mim. Pare, ou eu o transformarei em pedra neste instante!” Você:\nContinua correndo?	(Volte para 44)\nVira-se para atacá-lo com a espada?	(Volte para 195)\nDiz a ele que responderá à pergunta?	(Vá para 382)"
cap251 = "Mais uma vez, ouve-se a voz misteriosa, só que agora, para sua grande surpresa, num tom bem menos ameaçador: “Bom, meu senhor gosta daqueles que demonstram ter espírito. Tome este presente para ajudá-lo. Isto lhe concederá um desejo, mas somente um desejo. Adeus.” Um anel de ouro, magicamente saído do nada, cai a seus pés com um tinido suave. Você o põe num dedo. A porta se abre e você entra de novo no túnel, rumo ao norte. Vá para 344."
cap252 = "O túnel continua para o norte por uma boa distância antes de chegar a um beco sem saída. A entrada de um escorrega é visível na parede do oeste, e essa parece ser a única alternativa, além da opção de retornar. Você resolve arriscar e sobe no escorrega. Desliza suavemente e aterrissa sobre as costas em um aposento. Volte para 90."
cap253 = "253 Você tira o osso da mochila e o atira escada abaixo. Os latidos ficam mais altos, transformando-se em rosnados e ranger de dentes quando o osso cai no chão. Lentamente, você desce os degraus com a espada na mão, e vê os dois enormes CÃES DE GUARDA disputando o osso. Você passa correndo por eles e segue em frente pelo túnel. Vá para 315."
cap254 = "Você desembainha a espada e avança lentamente na direção do imenso e viscoso Verme da Rocha: VERME DA ROCHA // HABILIDADE 7 // ENERGIA 11 /// Se você vencer, volte para 76. Você poderá fugir depois de duas Séries de Ataque, correndo para o oeste pelo túnel. Volte para 117."
cap255 = "Quando corre contornando o caminho estreito, você se sente tonto. O gás da poça está fazendo efeito: sua visão começa a ficar embaçada, e você perde o equilíbrio. Você só tem uma vaga consciência da língua da Besta Sangrenta, enquanto ela se enrosca na sua perna e o arrasta para a poça de lodo. Depois de decomposto no lodo abjeto, seu corpo será saboreado pela ignóbil Besta Sangrenta."
cap256 = "Lembrando do conselho do velho, você examina o braço da cadeira em busca de um painel secreto. Descobrindo uma fenda quase imperceptível, você a força e, súbito, um pequeno painel salta do braço. Ao perceber um pequeno frasco de vidro numa cavidade, você o apanha e lê o rótulo: “Poção de Réplica - uma dose apenas. Este líquido fará com que você assuma a forma de qualquer ser vivo que lhe esteja próximo.” Você põe a estranha poção na mochila e continua para o norte. Volte para 188."
cap257 = "Dentro dos bolsos de um dos Orcas, você acha uma Peça de Ouro e um tubo oco de madeira. Você guarda na mochila o que encontrou e parte para o oeste. Volte para 164."
cap258 = "Você está exausto e se senta para um descanso na cauda da fera morta. Olhando para baixo, a seus pés, você de repente nota um anel de ferro que se destaca na areia. Se você quiser puxar o anel, volte para 95. Se preferir sair do poço pelas portas duplas, volte para 248."
cap259 = "Ignorando a dor, você, continua a correr. À sua frente, vê um rio subterrâneo que corre de leste para oeste atravessando a caverna, com uma ponte de madeira que liga uma margem a outra. Você olha para trás e vê os Trogloditas no seu encalço. Se você quiser correr pela ponte, vá para 318. Se desejar mergulhar no rio, volte para 47."
cap260 = "Você mal consegue se agarrar à orelha do ídolo e recuperar um ponto de apoio para os pés. Você se desloca pelo rosto da estátua. Sentado no nariz do ídolo, você desembainha a espada e considera qual dos olhos dele arrancará primeiro para levar a jóia. Se quiser arrancar primeiro o olho esquerdo, volte para 166. Se preferir arrancar o olho direito, volte para 140."
cap261 = "Apesar de todos os esforços, você não consegue tirar o Laço do pescoço do ídolo. Finalmente, você desiste e o abandona para quem quer que venha depois de você. Não há nada mais de interesse na caverna, portanto você caminha até a parede norte e entra no túnel. Volte para 239."
cap262 = "A porta abre para um outro túnel que segue para o norte. Você topa com duas fontes de pedra, uma de cada lado do túnel, esculpidas na forma de querubins, de cujas bocas a água jorra e desce em cascata para pequenas conchas nos pés. Você:\nBeberá água na fonte da esquerda?	Vá para 337\nBeberá água na fonte da direita?	Volte para 173 \nContinuará caminhando para o norte?	Vá para 368"
cap263 = "A porta abre para um outro túnel. Caminhando para o oeste, você logo chega a uma porta na parede norte. Se quiser abrir a porta, volte para 153. Se preferir continuar para o oeste, volte para 74."
cap264 = "Adiante, na penumbra, você vê dois HOBGOBLINS se engalfinhando. Há uma bolsa de couro jogada no chão, e parece ser ela a razão da luta. Você:\nTentará conversar com eles?	Volte para 130\nVai atacá-los com sua espada?	Volte para 51 \nTentará passar sem ser percebido?	Vá para 355"
cap265 = "Você esfrega seu anel mágico e deseja que o Demônio do Espelho seja transportado de volta ao próprio mundo e nunca mais retome. Ainda avançando na sua direção, o ser começa a se esvair e desaparece aos poucos. Por fim, ele some completamente, e você pode continuar sua jornada para o norte. Volte para 122."
cap266 = "Você revista os armários e caixas no quarto de Erva, mas não encontra nada, exceto um osso velho, que pode levar com você, se quiser. Saindo da câmara pela porta do leste, você agora se encontra de pé no final de um outro túnel. Vá para 305."
cap267 = "O túnel logo termina em uma encruzilhada. Olhando para a esquerda e para a direita, você vê uma passagem estreita que desaparece na penumbra da distância. Se você quiser se dirigir para o oeste, vá para 352. Se preferir seguir para o leste, volte para 68."
cap268 = "Você salta para adiante e tenta agarrar o líder para usá-lo como refém. Contudo, os Trogloditas estavam prevenidos para sua tentativa, e seis dos arqueiros deles imediatamente disparam flechas em você. A pontaria deles é mortalmente precisa, e as seis flechas atingem o alvo. Você tomba sem vida. Os Trogloditas encerraram abruptamente sua jornada."
cap269 = "Você esvazia o conteúdo do vidro na mão e o aplica às suas feridas. Os efeitos curativos são imediatos, e você se sente mais forte a cada momento. Acrescente 3 pontos de ENERGIA. Se você ainda não o fez, poderá comer o arroz e beber a água – vá para 330 – ou sair do salão, levando apenas o diamante com você - volte para 127."
cap270 = "A tampa da caixa sai facilmente. Dentro, você acha duas Peças de Ouro e um bilhete, escrito num pequeno pedaço de pergaminho, endereçado a você. Depois de colocar o ouro no bolso, você lê a mensagem: Muito bem. Pelo menos você tem o bom senso de parar e tirar proveito da ajuda simbólica que lhe é dada. Agora, posso avisá-lo da necessidade de encontrar e usar diversos itens, se espera sair-se bem no meu Calabouço da Morte. Assinado “Sukumvit.” Guardando de cor o aviso do bilhete, você o rasga em pequenos pedaços e continua para o norte pelo túnel. Volte para 66."
cap271 = "Quando você está prestes a soltar o escudo e atirá-lo por cima do poço, ele escorrega de seus dedos e rola pelo chão. Você não consegue apanhá-lo antes que ele ultrapasse a borda, caindo ruidosamente, de lado, no fundo. A perda do escudo reduz-lhe a capacidade - você perde 1 ponto de HABILIDADE. Amaldiçoando sua própria falta de jeito, você dá um passo à frente, salta por sobre o poço e cai em segurança do outro lado. Você não perde tempo e se dirige para o leste. Volte para 237."
cap272 = "Embora a Besta Sangrenta seja pesada e estufada demais para sair da poça, a língua da fera se estica e se enrosca na sua perna. Ainda inconsciente, você é arrastado para a poça de lodo. Depois de decomposto pela ação do lodo abjeto, seu corpo será saboreado pela repugnante Besta Sangrenta."
cap273 = "A bola de madeira se choca contra o crânio, derrubando-o do pedestal. Para sua surpresa, as bestas não disparam os dardos mortais. Você entra no aposento com cautela e apanha o crânio do chão. Reconhece as jóias amarelas dos olhos como sendo topázios, e rapidamente os arranca das órbitas. Você os coloca na mochila, imaginando se ainda há uma cilada à sua espera no aposento. Você: Ficará de quatro e sairá engatinhando do aposento, segurando o crânio?	Volte para 15 // Recolocará o crânio no pedestal antes de sair do aposento?	Volte para 204"
cap274 = "Você pisa nervosamente na corda, sem se atrever a olhar para baixo. Na metade da travessia, você começa a entrar em pânico e perde o equilíbrio. Jogue dois dados. Se o total for igual ou menor que a sua HABILIDADE, volte para 238. Se o total for maior que sua HABILIDADE, vá para 359."
cap275 = "Uma fumaça espessa sobe do chão no lugar onde o ácido caiu da moringa quebrada. Você se arrasta desesperadamente, tentando encontrar água potável nas poças rasas do túnel gotejante. Teste sua Sorte. Se você tiver sorte, volte para 231. Se não tiver sorte, vá para 309."
cap276 = "Ao tentar arrombar a porta com uma pancada de ombro, você ouve as vozes esganiçadas dos Trogloditas que vêm descendo o túnel. Você está encurralado e desembainha a espada. Os Trogloditas se aproximam, os arcos prontos, e uma saraivada de flechas o atinge com impacto fatal. Seu corpo desaba sem vida nas profundezas do Calabouço da Morte."
cap277 = "O túnel faz uma curva fechada para a direita e depois, uns 100 metros adiante, chega a um cruzamento. Olhando para a esquerda, você vê dois corpos caídos no chão. Resolve chegar perto e investigar. Vá para 338."
cap278 = "Sua lâmina atinge um dos olhos verdadeiros da Besta Sangrenta. O efeito é devastador. Ela desaba na poça, debatendo-se freneticamente. Você aproveita a oportunidade e corre, contornando a poça, rumo à saída para o túnel. Volte para 134."
cap279 = "Você chega a um cruzamento no túnel. Uma nova ramificação leva para o oeste, mas as pegadas molhadas que você vem seguindo continuam para o norte. Você decide continuar seguindo as pegadas. Volte para 32"
cap280 = "O túnel continua para o leste por uma boa distância antes de chegar a um cruzamento. As paredes, o teto e o chão do túnel que leva para o sul estão cobertos por um limo verde e espesso. Você considera que é mais seguro dirigir-se para o norte. Volte para 218."
cap281 = "Com um golpe da sua espada de fé, você corta a cabeça da Jibóia. Você desenrola o corpo gigantesco, libertando a Mulher-elfo, e tenta ressuscitá-la. Os olhos dela se abrem um pouco, mas não há esperança. Ela olha para você e sorri, depois murmura: “Obrigada. Sei que é tarde demais para mim, mas lhe direi o que já pude aprender. A saída está adiante, mas você precisa de gemas para destrancar a última porta. Uma delas é um diamante, mas não sei quais são as outras. Pena, não encontrei um diamante, mas aconselho-o a procurar um. Boa sorte.” Os olhos dela se fecham, e ela tomba no chão frio. Você a olha entristecido enquanto ela solta o último suspiro. Sabendo que ela não se importaria, retira-lhe os dois punhais e examina a mochila de couro que trazia. Dentro, você acha um pedaço de pão ázimo, um espelho e um amuleto de osso com a forma de um macaco. Se você quiser comer o pão, vá para 399. Se preferir pegar apenas o espelho e o amuleto e retornar ao túnel para dirigir-se ao norte, volte para 192."
cap282 = "O túnel logo termina em uma encruzilhada. Parado lá sozinho e sem saber para que lado ir está um de seus rivais. É um dos Bárbaros. Você o chama, mas ele não responde; apenas olha fria e fixamente para você, segurando a acha com firmeza. Você anda até ele e pergunta para que lado está indo. Ele grunhe sua resposta, dizendo que está indo para o oeste, e, se quiser, você pode ir com ele. Se você quiser seguir para o oeste com o Bárbaro, volte para 22. Se preferir recusar a oferta e seguir para o leste sozinho, vá para 388."
cap283 = "Você precisa se espremer e entrar fundo na fenda para se esconder completamente. Dessa posição desajeitada, você não consegue ver o dono dos pés que se arrastam, passando lentamente. Um minuto depois, tudo está quieto de novo, por isso você se esgueira de volta para o túnel e prossegue para o oeste. Volte para 109."
cap284 = "Você bebeu uma poção encontrada em um livro de couro preto? Se você tiver bebido, vá para 398. Se não, volte para 57."
cap285 = "Você cai pesadamente de costas, mas, felizmente, sua mochila suaviza o impacto. Você perde 1 ponto de HABILIDADE e 2 pontos de ENERGIA. A escuridão é quase total no fundo do poço, e você se arrasta, tateando. Repentinamente, sua mão toca alguma coisa fria, dura e lisa. O objeto é pequeno e redondo, mas você não consegue imaginar o que pode ser. Você o põe na mochila, esperando saber o que é quando sair do poço. Você continua a engatinhar e, adiante, topa com a parede do poço. É lisa demais para ser escalada, e você tem que escavar apoios nela com a espada. Isso toma muito tempo, mas, finalmente, você chega à boca do poço e sai dele pelo lado leste. Imediatamente, verifica a mochila, e descobre que o objeto encontrado é uma esfera de rubi vermelho vivo. Você fica absolutamente deslumbrado e se dirige para o leste com excelente disposição, assobiando suavemente. Volte para 237."
cap286 = "Foi obviamente um erro ter largado suas armas, mas, pelo menos, agora você pode se apossar das do Ninja morto. Você escolhe uma das facas compridas e a longa espada curva. O fio da lâmina de aço é excepcionalmente duro, e você não consegue deixar de admirar-lhe a beleza terrificante. Acrescente 4 pontos de HABILIDADE e vá para 320."
cap287 = "Você só tem tempo de ouvir o Gnomo dizer: “Uma coroa e dois crânios”, antes que um raio branco de energia parta da fechadura e atinja-lhe o peito, derrubando-o sem sentidos. Jogue um dado, some 1 ao resultado e subtraia o total da sua ENERGIA. Se você ainda estiver vivo, recupera os sentidos e ouve o Gnomo lhe dizer que tente de novo. Você sabe que colocou uma gema na ranhura certa, mas qual delas? Você suspira e tenta uma nova combinação.\nEsmeralda	Diamante	Safira	Volte para 16\nDiamante	Safira	Esmeralda	Vá para 392\nSafira	Esmeralda	Diamante	Volte para 177\nEsmeralda	Safira	Diamante	Fique em 287\nDiamante	Esmeralda	Safira	Volte para 132\nSafira	Diamante	Esmeralda	Volte para 249"
cap288 = "Você olha para a esquerda e vê Throm de pé sobre o Troll da Caverna que ele liquidou. O sangue que escorre do corte profundo que tem no ombro não parece preocupá-lo. Vocês revistam os corpos dos Trolls da Caverna, mas não encontram nada além de um anel de osso em um cordão de couro no pescoço de um deles. O anel tem um símbolo entalhado. Throm o reconhece e explica que deve ter pertencido a druidas do norte; trata-se de um antigo e poderoso talismã, capaz de aumentar-lhe os poderes, se seu corpo puder aceitá-lo. Throm recusa-se a tocar nele, e aconselha que você também não o faça. Se você quiser pôr o anel, volte para 64. Se preferir continuar para o leste com Throm, volte para 221."
cap289 = "A cobertura de pano sobe para o topo da gaiola, e nela, para seu horror, você vê o rosto de uma mulher velha, cujo cabelo é uma massa de serpentes que silvam. É a terrível MEDUSA! Teste sua Sorte. Se você tiver sorte, volte para 216. Se não tiver sorte, volte para 19."
cap290 = "Jogue dois dados. Se o total for oito, volte para 152. Se o total for qualquer número diferente de oito, volte para 121."
cap291 = "O túnel continua para o norte por uma longa distância, antes de fazer uma curva fechada para a direita. Ao virá-la, você chega a um beco sem saída. Somente a entrada de um escorrega de madeira na parede oferece alguma esperança de continuidade no caminho. Você resolve se arriscar e sobe no escorrega. Desliza suavemente e aterrissa sobre as costas num aposento. Volte para 90."
cap292 = "Uma porta se torna visível na parede do lado esquerdo do túnel. Você escuta cuidadosamente junto à porta, mas não ouve nada. A porta não está trancada, e a maçaneta gira facilmente. Se você quiser abrir a porta, volte para 93. Se preferir prosseguir pelo túnel, volte para 230."
cap293 = "Seguindo os três pares de pegadas molhadas pela passagem oeste do túnel, você logo chega a uma encruzilhada. Se quiser continuar para o oeste, seguindo dois pares de pegadas, volte para 137. Se quiser se dirigir para o norte, seguindo o terceiro par de pegadas, vá para 387."
cap294 = "Você puxa o punhal do cinto com a mão livre e golpeia a língua da Besta Sangrenta. A fera urra de dor e rola para a frente, tanto quanto consegue, para tentar abocanhá-lo com as mandíbulas ensanguentadas. Do chão, você tem que lutar contra a fera como punhal. Reduza sua HABILIDADE em 2 pontos durante este combate, pois não está lutando com sua espada. // BESTA SANGRENTA	HABILIDADE 12	ENERGIA 10 // Tão logo você vença sua primeira Série de Ataque, Teste sua Sorte. Se você tiver sorte, volte para 97. Se não tiver sorte, volte para 21"
cap295 = "Correndo na direção da passagem em arco, você tropeça numa pedra e perde o equilíbrio. Você cai estatelado no chão, e, antes que tenha tempo de levantar-se, uma estalactite despenca, rasgando-lhe a perna com a ponta aguçada. Você perde 5 pontos de ENERGIA. Se ainda estiver vivo, volte para 206."
cap296 = "Você percebe que adiante o túnel faz uma curva e depois continua para o norte. Alertado pelo som de vozes esganiçadas que sussurram e riem baixo, você pára antes da curva. Se quiser desembainhar a espada e olhar depois da curva, volte para 49. Se preferir caminhar de volta para a encruzilhada e seguir para o norte, volte para 241."
cap297 = "A perda de suas posses, obtidas com tanta dificuldade, está se tornando um problema. Você perde 1 ponto de SORTE. Sem mesmo parar para agradecer, Erva o empurra para fora do quarto por uma porta na parede leste. Ei-lo parado no fim de um outro túnel. Vá para 305."
cap298 = "Há uma mochila encostada na parede do túnel. Você se pergunta se ela pertenceria a um de seus rivais. Se você quiser olhar dentro da mochila, vá para 304. Se preferir continuar para o norte, volte para 279."
cap299 = "A porta abre para uma grande câmara, onde você se choca ao ver que um de seus rivais obviamente encontrou morte súbita ao ser perfurado. É um dos Bárbaros, e ele está empalado em vários espigões de ferro bem longos, presos a uma tábua projetada de dentro do chão. O piso está coberto de lixo e detritos, escondendo um arame no qual ele deve ter pisado, disparando assim o mecanismo da tábua com espigões. Numa alcova na parede do outro lado, você pode ver uma taça de prata sobre uma pequena mesa de madeira. Você: \n Irá até o Bárbaro para revistá-lo?	Volte para 126 \n Caminhará na direção da alcova?	Volte para 41 \n Fechará a porta e continuará para o oeste?	Volte para 83"
cap300 = "Você golpeia o espelho com a espada, com toda sua força, mas isso de nada adianta: o espelho não quebra, e o Demônio do Espelho continua a avançar. Se você quiser tentar partir o espelho de novo, volte para 141. Se, em vez disso, preferir atacar o Demônio do Espelho, vá para 327."
 
cap301 = "O cano está úmido e cheio de limo, mas você segue engatinhando na escuridão abafada, escorregando e deslizando no caminho. Subitamente, sua mão toca em algo duro e quadrado; parece ser de madeira. Ao sacudi-la, a coisa chacoalha, e você conclui que deve estar segurando uma caixa. Se quiser engatinhar de volta e sair do cano para examinar o achado, volte para 162. Se preferir seguir em frente pelo cano, levando a caixa para examinar mais tarde, volte para 4"
cap302 = "Depois de cerca de 20 minutos, o Anão reaparece na sacada. Ele lhe grita: “Bem, eu realmente tenho um problema muito interessante nas mãos. Prepare-se para lutar contra seu próximo adversário.” A porta de madeira se ergue mais uma vez, e você se admira ao ver um rosto conhecido. É Throm! Ele está muito machucado e tem cortes pelo corpo todo, e não parece reconhecê-lo. Está claramente delirante enquanto cambaleia para frente com a acha erguida para atacá-lo. O Anão ri e lhe diz: “A naja o mordeu, mas ele tema força de um touro e conseguiu resistir, ao contrário da maioria dos homens. Agora você deve lutar com ele, para decidir finalmente qual dos dois continuará na Prova dos Campeões.” Você grita com o Anão, revoltado, denunciando a crueldade de um confronto desses. Ele simplesmente ri, e você não tem alternativas e não se defender do ataque do pobre Throm.\n THROM	HABILIDADE 10	ENERGIA 12 \n Apesar dos ferimentos, Throm é imensamente forte. Se você vencer, vá para 379."
cap303 = "Com sua mão livre, você busca a moringa na mochila. Desarrolhando-a com os dentes, derrama o ácido sobre a porta, que é na realidade a forma fluida de um IMITADOR. Um jato de fumaça sobe dela, com um alto som sibilante, enquanto o ácido começa a queimar o Imitador. Ela derrete rapidamente, e você consegue afastar-se sem se ferir. Não tendo outra alternativa, você, um tanto apreensivo, gira a maçaneta da outra porta. Volte para 262."
cap304 = "Há uma única Peça de Ouro no fundo da mochila. Quando você tenta pegá-la, sente um leve movimento que faz cócegas nas costas, da sua mão. Você retira a mão lentamente, tentando controlar o pânico crescente, e fica horrorizado ao ver uma ARANHA VIÚVA NEGRA. Antes que possa afastá-la, ela crava as presas venenosas profundamente no seu pulso. Você perde 6 pontos de ENERGIA. Se ainda estiver vivo, volte para 20."
cap305 = "O túnel termina em um lance de degraus de pedra. Do chão, abaixo, vêm latidos de cães. Você tem um osso velho? Se tiver, volte para 253. Se não tiver, volte para 148."
cap306 = "Antes que você possa dar um passo na direção dos Leprechauns, um deles joga uma poeira cintilante em você, que é imediatamente congelado no lugar, incapaz de mover um músculo. Você vê, indefeso, os Leprechauns revirarem sua mochila, fugindo com todas as suas posses e deixando a mochila vazia. Você perde 2 pontos de SORTE. Cerca de uma hora depois, o efeito congelante da poeira se desfaz, e as sensações retornam a seu corpo. Furioso com a perda, você ruma para o norte, determinado a se vingar. Volte para 29."
cap307 = "O armário contém uma marreta de madeira e 10 espigões de ferro, os quais você põe na mochila enquanto decide qual porta abrir. Se quiser abrir a porta do oeste, volte para 263. Se preferir abrir a porta do norte, volte para 136."
cap308 = "A Medusa berra quando você entra na gaiola, mantendo os olhos firmemente fechados e desferindo golpes furiosos de um lado para o outro com a espada. Você sente a lâmina penetrar profundamente na fera e ouve um baque alto quando ela desaba pesadamente no chão. Você abre os olhos de novo e se arrepia com a visão da Medusa prostrada. O manto dela está preso por um grande broche constituído por uma única gema grande; é uma granada. Você a arranca, põe no bolso e sai do aposento, rumo ao norte. Vá para 316."
cap309 = "Você cambaleia desnorteado em busca de uma poça de água, mas não encontra. O ácido queima com uma dor lancinante bem fundo na sua garganta. Você perde 3 pontos de ENERGIA. Se ainda estiver vivo, Teste sua Sorte. Se você tiver sorte, volte para 231. Se não tiver sorte, volte para 193"
cap310 = "Você chega à parede do outro lado da câmara e vê duas portas. Se quiser abrir a portada esquerda, vá para 339. Se quiser abrir a porta da direita, volte para 262"
cap311 = "Depois de muito relutar, o Bárbaro concorda com sua alternativa. Vocês dois tomam distância e saltam por sobre o poço. Aterrissando em segurança do outro lado, você continua descendo pelo túnel. O Bárbaro, que vai na frente, subitamente tropeça em uma pedra, que se inclina para frente e dispara o mecanismo de um rochedo preso precariamente ao teto. O rochedo despenca sobre ele, derrubando-o e esmagando-lhe o crânio. Você terá que continuar sua jornada sozinho. Vá para 325."
cap312 = "O disco, afiado como uma navalha, passa assobiando pela sua cabeça e crava-se profundamente em um dos pilares. Você se vira e põe-se em guarda para enfrentar o assassino, que avança com a espada longa desembainhada.\nNINJA	HABILIDADE 11	ENERGIA 9\nSe você vencer, volte para 232."
cap313 = "O túnel termina em uma encruzilhada. As pegadas que você vem seguindo viram para o norte, e você resolve manter-se na trilha delas. Volte para 32."
cap314 = "Sua espada corta a maçaneta e, separada do corpo de origem, a membrana murcha e cai ao chão. Não tendo outra alternativa, você gira, um tanto apreensivo, a maçaneta da outra porta. Volte para 262"
cap315 = "O túnel dá uma guinada brusca para a esquerda e chega ao fim em uma parede alta, na qual há uma porta. Você ouve um rugido feroz vindo do outro lado da porta e tenta imaginar quão gigantesca seria a fera capaz de tamanho ruído. Se você tiver um rolo de corda e um gancho de ferro, volte para 129. Se não tiver esses objetos, volte para 245."
cap316 = "O túnel continua por uma boa distância antes de chegar a um cruzamento. Se você quiser se dirigir para o oeste pelo novo túnel, volte para 296. Se preferir continuar para o norte, volte para 241."
cap317 = "Tateando nos lados do buraco perfurado com sua espada, você abre caminho cegamente pelo lodo viscoso. Você segue as curvas e reviravoltas do orifício por um tempo que parece ser uma eternidade e começa a imaginar onde poderia levar. De repente, você ouve o ruído de alguma coisa se arrastando à frente. Você fica gelado de medo, seus olhos tentando desesperadamente rasgar a escuridão impenetrável. Antes que você se dê conta do que está acontecendo, seu pescoço é abocanhado pelas fortíssimas mandíbulas de outro Verme da Rocha. E o companheiro daquele que você matou, o qual foi atraído pelo cheiro de sangue na sua espada. Ele aperta mais forte. Seu pescoço estala como um ramo seco. Sua aventura termina aqui."
cap318 = "Depois de cruzar a ponte, você atravessa a caverna correndo. Finalmente, vê um túnel na parede do outro lado, pelo qual você entra a toda. O túnel termina numa pesada porta de madeira, e ela está trancada. Se você tiver uma chave de ferro, volte para 86. Se não tiver uma chave, volte para 276."
cap319 = "A armadura e a espada pesam mais do que você pensa. No ar, você toma consciência, com horror, de que não vai conseguir chegar ao outro lado do poço. Você se choca contra o lado do poço, uns dois metros abaixo da borda, e despenca de cabeça para o fundo. Volte para 285."
cap320 = "Você resolve revistar o Ninja e, em meio às vestes dele, encontra um saco de pano. Dentro, há um frasco de água, um pouco de arroz enrolado em folha de palmeira, um vidro de unguento e um lindo diamante. Você:\nComerá o arroz e beberá a água?	Vá para 330\nEsfregará um pouco do unguento nos\nseus ferimentos?	Volte para 269\nPegará apenas o diamante e sairádo salão?	Volte para 127"
cap321 = "Você puxa o cordão e o pano sobe pelos lados da gaiola. A voz da mulher insiste para que você seja rápido, dizendo que o aposento está preparado para uma cilada, de forma que o piso desabará em um minuto por causa do seu peso extra. Se você ainda quiser ajudá-la, volte para289. Se preferir sair do aposento e se dirigir para o norte pelo túnel, Volte para 316."
cap322 = "Você passa pela cadeira de madeira e logo retorna ao cruzamento, virando à direita para o oeste. Volte para 43."
cap323 = "Depois de amarrar a corda em torno da rocha, você desce devagar para o fundo do poço. Throm recupera a corda dele, soltando-a da rocha com uma sacudidela, e vocês partem juntos pelo novo túnel. Volte para 194"
cap324 = "Você falou com o servo aleijado dos Juízes da Prova? Se falou, volte para 256. Se não, volte para 79."
cap325 = "Você se levanta e segue túnel abaixo. De repente, vê a luz do dia no fim do túnel. Enquanto corre na direção da visão mais bela que teve diante de si desde muito tempo, um céu claro e azul, árvores verdes, você sonha com o alegre cenário de pessoas vibrando. Mas não há recepção de herói da parte das pessoas à sua volta. Estão todas mortas. Você está dentro de uma câmara fria repleta de cadáveres e esqueletos com armaduras. A saída para a vitória era apenas uma ilusão. Somente os despojos de aventureiros do passado são reais. Profundamente deprimido, você caminha de volta para o túnel, mas se choca com uma barreira invisível. Você está aprisionado neste sinistro local, fadado a terminar seus dias na câmara dos mortos."
cap326 = "Adiante, o túnel faz uma curva fechada para a esquerda. Ao □obra-la, você quase bate de frente em dois ORCAS de aspecto feroz, armados de maças com pontas de ferro e usando armaduras de couro. Você está totalmente despreparado, e, enquanto desembainha a espada, um deles desfere-lhe um golpe de maça. Jogue um dado. Se você obtiver 1 ou 2, volte para91. Se obtiver 3 ou 4, volte para 189. Se obtiver 5 ou 6, vá para 380"
cap327 = "Exclusivamente voltado para agarrar-lhe o braço, o Demônio do Espelho não tenta defender- seu DEMÔNIO DO ESPELHO	HABILIDADE 10	ENERGIA 10 \nSe, durante uma Série de Ataque, a Força de Ataque do Demônio do Espelho for maior que a sua, volte para 8. Se você conseguir derrotar o Demônio do Espelho sem que ele ganhe qualquer Série de Ataque, volte para 92."
cap328 = "Você olha em torno do quarto de Erva. Ao ver o retrato de um outro Troll pendurado na parede, pergunta a ela se são parentes. Imediatamente, o humor e a expressão dela mudam. Ela afrouxa o aperto sobre você e sorri, dizendo: “Ah, sim. Este é meu amado e querido irmão Barriga Azeda. Ele tem-se saído muito bem lá no sul, em Port Blacksand. Está agora na Guarda Imperial, na tropa de elite de Lord Azzur. Estou muito orgulhosa dele.” Erva fica olhando para a pintura e continua a tecer elogios ao irmão. Se você quiser se esgueirar para fora do quarto, pela porta na parede do leste, volte para 125. Se preferir continuar a conversa, volte para 99."
cap329 = "Você caminha até o espelho e se diverte com a imagem distorcida. Sua cabeça parece tão grande quanto uma abóbora, o rosto, muito estranho... Sem qualquer sinal prévio, uma dor terrível martela-lhe a cabeça; você tenta desviar o olhar do espelho, mas não consegue. Alguma força do mal mantém seus olhos pregados ao próprio reflexo. Você segura a cabeça com as mãos e, horrorizado, se dá conta de que ela está se expandindo. Você não pode mais suportar a dor, e tomba sem sentidos para nunca mais acordar."
cap330 = "As rações do Ninja são modestas mas bem-vindas. Acrescente 1 ponto de ENERGIA. Se você ainda não o fez, poderá esfregar um pouco do unguento nos seus ferimentos – volte para 269– ou sair do salão, levando só o diamante – volte para 127."
cap331 = "Tocar o pergaminho tem precisamente o efeito que você temia. O esqueleto dá um impulso para frente e, levantando-se da cadeira numa série de movimentos aos arrancos, ergue a espada para golpeá-lo. Esquivando-se para o lado, você desembainha a sua espada para se defender.\nGUERREIRO-ESQUELETO	HABILIDADE 8	ENERGIA 6\nSe você vencer, volte para 71."
cap332 = "Sua gema cai na poça com um ‘plop’ surdo. Enquanto espera que alguma coisa aconteça, você começa a se sentir fraco. O gás que emana da poça é tóxico, e você tomba inconsciente. Teste sua Sorte. Se você tiver sorte, volte para 53. Se não tiver sorte, volte para 272."
cap333 = "Você ouve passos e, de repente, a porta do alçapão é jogada para trás. Por alguns segundos, você é cegado pela intensa luz que vem do aposento de cima, e não vê o Goblin desferir um golpe de lança, nem ouve o riso sádico quando a ponta rasga seu pescoço. Sua aventura termina aqui, nos degraus de pedra do túnel."
cap334 = "Você tenta se livrar da língua com as mãos nuas, mas não consegue. Lentamente, você é arrastado para a poça, onde, depois de decomposto pelo lodo, seu corpo será devorado pela pavorosa Besta Sangrenta."
cap335 = "Ainda correndo o mais rápido que pode, você mergulha no rio. Teste sua Sorte. Se você tiver sorte, volte para 67. Se não tiver sorte, volte para 101."
cap336 = "A munhequeira foi feita e amaldiçoada por uma Bruxa. Ela torna suas reações mais lentas e embota-lhe os sentidos. Reduza sua HABILIDADE em 4 pontos. Furioso, você chuta a parede do túnel e segue para o norte. Volte para 298."
cap337 = "A água fresca é revigorante, mas provém de uma fonte amaldiçoada por uma Bruxa. Some 1 ponto de ENERGIA, mas desconte 2 pontos de SORTE. Se ainda não o fez, você poderá beber da outra fonte - volte para 173 - ou continuar para o norte - vá para 368"
cap338 = "Os corpos são de dois guardas Orcas. Pelo menos um de seus rivais na Prova dos Campeões ainda deve estar à sua frente. De uma rápida revista aos corpos nada resulta senão um colar de dentes pendurado no pescoço de um dos Orcas. Se você quiser usar o colar, volte para 123. Se preferir partir para o norte sem o colar, volte para 282."
cap339 = "Quando você toca a maçaneta da porta, ela fica mole na sua mão, e, quando tenta tirar a mão, descobre que ela está grudada na maçaneta. Então, um punho gigantesco se forma no meio da porta e projeta-se na sua direção, atingindo-o no estômago. Você perde 1 ponto de ENERGIA. Se tiver uma moringa de ácido, volte para 303. Se não tiver, volte para 236."
cap340 = "O medo lhe dá uma nova injeção de energia, e, de alguma forma, suas pernas cansadas conseguem mantê-lo à frente do rochedo. Adiante, à direita, você vê a forma bem-vinda de uma porta. Você mergulha de encontro à porta e, por sorte, ela se abre. O rochedo passa estrondoso, e você fica deitado, exausto, no chão de um aposento grande. Vá para 381."
cap341 = "Um homem aleijado, com cadeias nos pés, arrasta-se na sua direção carregando uma bandeja de madeira cheia de pão e água. Ele parece cansado e desalentado, e tenta passar por você sem demonstrar reação à sua presença. Você:\nFalará com ele?	Vá para 367\nPegará pão e água da bandeja dele?	Volte para 38\nOferecerá a ele alguma provisão\n(se você ainda tiver alguma)?	Volte para 169"
cap342 = "Suas reações são lentas por causa do veneno e, embora você tente pular por cima da língua estendida, suas pernas não conseguem erguê-lo o bastante. A língua pegajosa se enrola na sua perna e começa a puxá-lo na direção da poça. Você é arrastado para o chão e não consegue desembainhar a espada. Se você tiver um punhal, volte para 294. Se não tiver um punhal, volte para 334"
cap343 = "Com vozes esganiçadas, os Trogloditas explicam as regras da Corrida da Flecha. Eles dispararão uma flecha e você poderá caminhar, sem ser atacado, até o ponto onde ela cair. Porém, você deverá ir descalço, e o chão da caverna, como pode ver, está coberto de pedras pontiagudas. Logo que você chegar à flecha, os Trogloditas começarão a persegui-lo; se o pegarem, você será morto. De repente, um dos Trogloditas dispara uma flecha bem alto no ar. Ela cai a grande distância, e, imediatamente, os Trogloditas forçam-no a caminhar na direção dela. Enquanto você anda devagar na direção da flecha, ouve os gritos excitados dos Trogloditas. Ao chegar à flecha você se volta e vê os Trogloditas agitarem os braços no ar e iniciarem a perseguição. Você corre o mais depressa que pode, os pés sangrando com os cortes sofridos nas pedras pontiagudas. Você perde 1 ponto de ENERGIA. Adiante, um rio subterrâneo, que corre de leste para oeste, cruza a caverna; uma ponte de madeira liga uma margem à outra. Se você quiser atravessar a ponte, volte para 318. Se quiser mergulhar no rio, volte para 47."
cap344 = "O túnel faz curvas e reviravoltas, mas continua sempre para o norte. À sua frente, um facho de luz azul desce do teto para o chão. Ele faísca e cintila, e você pode ver imagens de rostos que riem na luz. Se você quiser passar através da luz, volte para 229. Se preferir contornar o facho, volte para 107."
cap345 = "Você está prestes a entrar no aposento quando a Poção de Detecção de Cilada começa a fazer efeito, e você é dominado por uma terrível premonição. Há uma armadilha mortal neste aposento. Você resolve não entrar e continua para o norte pelo túnel. Volte para 252."
cap346 = "Você tira a bota do pé e se esforça para estendê-la até o sino e travar-lhe a vibração. Aos poucos, o sino vai parando de vibrar, e a dor no seu corpo diminui gradualmente. Você consegue se levantar, mas não afasta a bota do sino até que ele esteja completamente imóvel. Você calça a bota e continua a jornada para o oeste. Vá para 362."
cap347 = "O Anão sacode a cabeça, dizendo: “Só músculos, sem inteligência, não bastam para conquistar a Prova dos Campeões. Sinto dizer que você fracassou. Você não terá permissão para ir embora, pois poderá revelar os segredos do calabouço para outros. Todavia, você conseguiu muito chegando tão longe, e eu o indicarei para meu servo pelos anos futuros para preparar o calabouço para os novos competidores”."
cap348 = "Você avança sobre a Besta Sangrenta, tentando evitar a língua que se estende para agarrar-lhe a perna. Jogue dois dados. Se o total for igual ou menor que a sua HABILIDADE, volte para 225. Se o total for maior que a sua HABILIDADE, volte para 159"
cap349 = "Você desce pela corda para o interior do poço, segurando-se com uma das mãos, enquanto a outra leva a espada desembainhada. O Diabo do Poço é uma das feras mais terríveis que você já viu, e você sabe que esta será uma das lutas mais difíceis da sua vida.DIABO DO POÇO	HABILIDADE 12    ENERGIA 15 Se você vencer, volte para 258."
cap350 = "A Mosca Gigante mergulha na sua direção e agarra-o com quatro patas. Rapidamente ela retorna ao teto da caverna, e você se encontra indefeso pendurado no ar. Súbito, para seu horror, ela o solta. Você despenca de 10 metros de altura, estatelando-se no solo. Jogue um dado e deduza o número de seu índice de ENERGIA. Se ainda estiver vivo, você desembainha a espada; bem a tempo, pois a Mosca Gigante vem descendo para tentar capturá- lo mais uma vez. Volte para 39."
cap351 = "O ídolo é muito liso, e a escalada será difícil. Você tem corda? Se tiver, vá para 396. Se não tiver, volte para 186."
cap352 = "Você ouve o som de rochas sendo trituradas e esmagadas à sua frente. O ruído cresce e, subitamente, você se dá conta de que a parede do seu lado direito começa a desabar. Apavorado, você vê uma enorme e horrorosa criatura, com mandíbulas incrivelmente poderosas, deslizar por um buraco na parede. A enorme boca da criatura mastiga rocha enquanto ela vira a cabeça devagar de um lado para outro, sentindo o ar fresco do túnel. O VERME DA ROCHA parece ser cego, mas dá a impressão de estar ciente de sua presença, talvez sentindo o calor de seu corpo. Ele se arrasta na sua direção com as mandíbulas bem abertas, pronto para o ataque. Se você quiser lutar contra o Verme da Rocha, volte para 254. Se preferir correr de volta pelo túnel para o cruzamento e depois se dirigir para o leste, volte para 68."
cap353 = "Antes que você possa sair do caminho, o rochedo se choca contra seu ombro. Você perde 1 ponto de HABILIDADE e 4 pontos de ENERGIA. Se ainda estiver vivo, volte para 325."
cap354 = "A pílula faz com que você se sinta como se o mundo inteiro estivesse contra você. E perde 2 pontos de SORTE. O Anão lhe diz que agora você pode passar à segunda fase do teste. Ele apanha uma cesta de vime e lhe diz que ela contém uma serpente. Vira a cesta e a serpente cai no chão. É uma naja, e se ergue no ar, pronta para dar o bote. O Anão lhe diz que pretende testar suas reações. Você deverá agarrar a naja com as mãos nuas, pelo pescoço, evitando as presas mortais. Você se agacha, tensionando os músculos para o momento decisivo. Jogue dois dados. Se o total for igual ou menor que a sua HABILIDADE, volte para 55. Se o total for maior que a sua HABILIDADE, volte para 202."
cap355 = "Você se aproxima silenciosamente por trás dos Hobglobins que lutam e, saltando das sombras, empurra-os contra a parede e foge correndo. Você olha para trás e os vê esparramados no chão. Rindo, você segue depressa para o norte. Volte para 110."
cap356 = "Há uma abertura no lado esquerdo da parede do túnel. Você está de pé na entrada de uma caverna grande, quando ouve uma voz de mulher gritando por socorro. Você distingue apenas a forma de uma figura humana que rola pelo chão no fundo da caverna. Se você quiser entrar na caverna, volte para 170. Se preferir continuar para o norte pelo túnel, volte para 192."
cap357 = "A Besta Sangrenta chafurda na poça, e o cheiro dos gases venenosos, cujas bolhas sobem à tona e contaminam a atmosfera, provoca ânsias de vômito. Você:\nCorrerá contornando a poça da fera,na direção do túnel?	Volte para 255\nJogará uma gema na poça (se você tiver uma)?	Volte para 332\nAtacará a fera com sua espada?	Volte para 180"
cap358 = "Você perde o equilíbrio e despenca de cabeça no chão. Perde 2 pontos de ENERGIA. Você desiste de tentar escalar o ídolo e corre para seguir pelo túnel na parede norte. Volte para 239."
cap359 = "Você cai da corda e despenca de cabeça na fenda. Bate com a cabeça em uma saliência rochosa e morre antes de chegar ao fundo da fenda."
cap360 = "Depois de pagar, você sobe na cesta de vime. O velho grita, jogando a cabeça para trás: Puxa,Erva! A corda se retesa, e a cesta se ergue aos solavancos. Enquanto você está sendo içado cada vez mais alto, o velho lhe grita: “Você vai gostar de Erva, ela é uma ótima garota. Nós a chamamos de Erva Venenosa!” Ele ri descontrolado, e você, um tanto apreensivo, se pergunta quem o está içando. A cesta passa por um buraco no teto, e você se vê em um pequeno quarto, frente a frente com uma mulher TROLL feia e velha. Ela tem o rosto peludo e coberto de verrugas. Com uma enorme mão ela o puxa para fora da cesta, a qual deixa cair lá embaixo. Em seguida, agarra-o pela garganta e lhe diz, numa voz rouca: “Quero pagamento também!” Você:\nOferecerá a ela alguma coisa da sua mochila?	Volte para 297\nTentará convencê-la a não cobrar nada de você?	Volte para 328\nAtacará a mulher com sua espada?	Volte para 211"
cap361 = "As mandíbulas do Diabo do Poço dão um bote no amuleto de macaco e o apanham no ar, mas logo se abrem de novo, forçadas pelo amuleto, que se expandiu a ponto de ocupar toda a boca da fera. Enquanto o Diabo do Poço se debate, tentando livrar-se do amuleto, você desce até o fundo para chegar às portas duplas. Desvairado, o Diabo do Poço usa o imenso corpo na tentativa de esmagar você contra a parede. Teste sua Sorte. Se você tiver sorte, volte para 82. Se não tiver sorte, vá para 377."
cap362 = "O túnel dá uma guinada acentuada para a direita e continua para o norte até onde a vista alcança. A distância, você ouve uma tremenda comoção: grunhidos, rosnados, uivos. Você desembainha a espada e parte na direção do tumulto. Volte para 264."
cap363 = "A comida e a bebida são excelentes, e você se sente muito melhor. Acrescente 2 pontos de ENERGIA. Plenamente satisfeito, você senta e espera a volta do Anão. Volte para 302."
cap364 = "Enquanto remove o sangue do Mantécora de sua espada, você leva um susto ao ver um homenzinho com um nariz grande saltar detrás de um dos pilares de mármore. Ele veste uma túnica justa, verde, e parece inofensivo, embora você fique desconfiado do modo como ele segura uma bola de vidro opaco com uma luz verde cintilante. “Meus cumprimentos!”, ele diz animadamente. “Meu nome é Igbut, o Gnomo, e sou o Juiz da Prova para seu teste final. Não é preciso dizer que meus poderes mágicos são grandes, por isso você não deve tentar me atacar. Talvez você tenha sabido, durante a sua jornada, que as gemas desempenham um papel essencial na Prova dos Campeões. A porta de ferro à sua frente é a saída para a vitória, mas só há uma maneira de abri-la. É preciso pôr três gemas no mecanismo da fechadura, numa ordem específica. Cada gema irradia uma energia que acionará o mecanismo – se você as colocar corretamente, é claro. Eu o ajudarei de certa forma, mas primeiro precisamos das gemas certas. Você tem uma esmeralda?”. Se você tiver uma esmeralda, volte para 31. Se não tiver, volte para 3."
cap365 = "Você diz a Throm que matar o Anão não vai adiantar nada, pois vocês jamais acharão a saída da câmara sozinhos. Você argumenta que talvez surja uma chance de enganar o Anão mais tarde, quando tiverem descoberto a saída da câmara, por isso você pretende ir adiante com o teste do Anão. Você diz ao Anão que está pronto, e ele acena para que o siga. Throm deve aguardar a volta dele. Uma porta secreta abre-se na parede da câmara, e você segue o Anão até um pequeno aposento circular. Ele fecha a porta atrás de você e lhe entrega dois dados de osso, mandando que os jogue no chão. Você tira um seis e um dois: total, oito. O Anão pede que você os jogue mais uma vez, mas, agora, deve adivinhar se o total será igual, menor ou maior que oito. Se seu palpite for que será igual, volte para 290. Se achar que será menor que oito, volte para 191. Se optar por maior que oito, volte para 84"
cap366 = "A temperatura continua a subir, muito além dos limites de tolerância humanos. Estendido no chão quase derretido do túnel, você não consegue recuperar a consciência. Sua aventura termina aqui."
cap367 = "Ele o encara desconfiado quando você diz que é um competidor na Prova dos Campeões. Você pergunta a ele o que faz nos túneis, e ele lhe responde, um tanto relutante, que é servo de um dos Juízes da Prova, os controladores das diferentes partes do calabouço designados pelo Barão Sukumvit. Depois de alguma conversa, ele admite que gostaria de fugir, mas ninguém pode sair do calabouço, pois poderia revelar os segredos da construção. Ele espera conseguir sair dali mediante suborno, e, por uma Peça de Ouro, poderá dizer-lhe onde há um tesouro escondido. Se você quiser pagar pela orientação do velho, volte para 244. Se preferir simplesmente desejar-lhe o melhore continuar para o oeste, volte para 109"
cap368 = "Você vê um par de pernas-de-pau junto à parede do lado esquerdo do túnel. Elas estão firmemente acorrentadas, e num aviso preso a um cadeado lê-se: “O preço destas pernas-de- pau é uma Peça de Ouro. Coloque a moeda na ranhura para abrir o cadeado.” Se você quiser comprar as pernas-de-pau, volte para 165. Se preferir prosseguir para o norte, volte para 234."
cap369 = "O túnel faz uma curva fechada para a direita, continuando para o leste até onde a vista alcança. Throm pára e lhe diz que faça o mesmo. Ele vira a cabeça devagar de um lado para o outro: “Ouço passos descendo pelo túnel na nossa direção”, ele sussurra. “Desembainhe a espada.” Vocês se agacham para se esconder nas sombras, e bem a tempo: duas figuras armadas se aproximam. Throm salta e brada um grito de guerra. Dois TROLLS DA CAVERNA estão diante de vocês. Throm ataca o primeiro com a acha de guerra, e você corre para ajudá-lo, atacando o segundo Troll da Caverna.\nTROLL DA CAVERNA	HABILIDADE 10    ENERGIA 11\nSe você vencer, volte para 288."
cap370 = "Quando você contorna a poça correndo, a Besta Sangrenta estende a língua comprida mais uma vez. Jogue dois dados. Se o total for igual ou menor que o seu índice de HABILIDADE, volte para 104. Se o total for maior que o seu índice de HABILIDADE, volte para 342"
cap371 = "Você faz pontaria e joga a bola de madeira no crânio. Jogue dois dados. Se o número obtido for igual ou menor que o seu índice de HABILIDADE, volte para 273. Se o número obtido for maior que o seu índice de HABILIDADE, volte para 113."
cap372 = "Você finalmente chega ao corpo do guerreiro, mas, logo que toca na jóia, tanto ela quanto o guerreiro desaparecem como num passe de mágica. A porta bate atrás de você, e segue-se um estrondo agourento acima da sua cabeça. Você olha para o alto e vê o teto baixando. Corre para a porta na tentativa de escapar, mas ela está trancada e não há maçaneta do lado de dentro. O teto vai descendo, e você é obrigado a se deitar no chão, tentando impedir o movimento do teto comas mãos e os pés. Mas o esforço é inútil, e você é esmagado entre os blocos de pedra."
cap373 = "Você sobe pelo rochedo macio, temendo ser absorvido por ele a qualquer momento. É difícil passar por cima da coisa, pois seus membros afundam na casca mole, mas, por fim, você consegue chegar ao outro lado. Aliviado por estar de novo em terreno firme, você se dirige para o leste. Volte para 13."
cap374 = "Você caminha pela caverna, mas não acha nada interessante. Throm o chama lá de trás, dizendo que encontrou um saco de couro sob uma pilha de rochas. Abrindo o saco, Throm ri alto quando um minúsculo camundongo corre entre os dedos dele e foge para uma fresta entre dois rochedos. A súbitas, você ouve o som de rocha rachando: estalactites se desprendem do teto, como resultado da vibração causada pelo riso retumbante de Throm, que ainda ecoa pela caverna. Você berra para que Throm fuja pela passagem em arco, enquanto as estalactites desabam. Teste sua Sorte. Se você tiver sorte, volte para 118. Se não tiver sorte, volte para 295."
cap375 = "Uma fumaça acre emana da moringa quando você enfia o pano nela. O líquido é indubitavelmente ácido. Você arrolha a moringa de novo e a coloca na mochila, esperando que venha a ter utilidade mais tarde. Você recoloca a espada na bainha e prossegue rumo ao norte. Volte para 110."
cap376 = "O Gnomo, ainda sorrindo, lhe diz, excitado: “Excelente! Só falta uma. Você possui um diamante?” Se você tiver encontrado um diamante, volte para 62. Se não tiver encontrado um diamante, volte para 3"
cap377 = "A imensa fera atira o corpo contra o seu braço, e você solta a corda. Gritando de dor, você despenca no fundo do poço e perde 5 pontos de ENERGIA. Se ainda estiver vivo, volte para 203."
cap378 = "Um tanto nervoso, você respira fundo e mergulha na poça escura. A parede norte não se projeta muito longe, sob a superfície da água, e você resolve se arriscar e nadar por baixo dela. Logo começa a sentir falta de ar e é obrigado a voltar à tona. Você tenta não pensar que pode estar aprisionado em um velho túnel submerso e fica aliviado quando emerge e encontra ar puro. Você está do outro lado da parede e pode ver o túnel saindo da água e continuando para o norte. Saindo da água, você verifica o conteúdo da mochila molhada. Teste sua Sorte. Se você tiver sorte, volte para 112. Se não tiver sorte, volte para 209."
cap379 = "Exaurido pelo longo duelo, você cai de joelhos. Ao olhar para o corpo imóvel de Throm, um ódio amargo ao Anão enche-lhe o coração. De alguma forma, você vingará Throm. Envolvido pela raiva, não repara que o Anão entra na arena, até que ele chega diante de você, uma besta carregada apontada para o seu peito. “Sei o que você está pensando”, ele diz calmamente, “mas não se esqueça que só eu sei o modo de sair daqui. Levante-se, está na hora de você ir embora.” O Anão indica que você deve andar à frente dele. De volta à câmara, ele vai até a parede norte e empurra uma das pedras que a compõem. Um pedaço da parede, semelhante a uma porta, gira, abrindo-se para um túnel iluminado por cristais. Com a besta ainda apontada para o seu peito, o Anão sorri, dizendo: “Boa sorte.” Se você quiser caminhar direto para o túnel, volte para 213. Se preferir desferir um soco no Anão, volte para 145."
cap380 = "A maça de ferro do Orca se choca contra o escudo e resvala sem causar dano. O túnel é estreito demais para que os dois o ataquem ao mesmo tempo, por isso você pode lutar com um de cada vez.znHABILIDADE	ENERGIA\nPrimeiro ORCA	5	5\nSegundo ORCA	6	4\nSe você vencer, volte para 257."
cap381 = "Você olha em volta no aposento e nada vê de interesse, exceto a alcova na parede do oeste e uma cadeira de pedra no meio do aposento, na qual se encontra sentado o esqueleto de um guerreiro armado, possivelmente um concorrente de anos atrás. Os dedos descamados da mão direita estão fechados em torno de um pedaço de pergaminho. Se você quiser pegar o pergaminho do esqueleto, volte para 331. Se preferir caminhar até a alcova, volte para 128."
cap382 = "O velho aponta para uma das estátuas, e você logo a reconhece. É o cavaleiro que iniciou a Prova dos Campeões, um olhar de agonia registrado na pedra para toda a eternidade. O velho sorri, dizendo: “Este homem pesa 50 kg mais a metade do peso dele. Quanto ele pesa?” O que você responderá?\n50 quilos?	Volte para 144\n75 quilos?	Volte para 227\n100 quilos?	Vá para 391"
cap383 = "Para sua grande surpresa, nada de extraordinário lhe acontece enquanto está sentado na cadeira. Nada há a fazer senão continuar para o norte pelo túnel. Volte para 188."
cap384 = "Para sua grande surpresa, nada de extraordinário lhe acontece enquanto está sentado na cadeira. Nada há a fazer senão continuar para o norte pelo túnel. Volte para 188."
cap385 = "Você derrama o conteúdo do frasco de vidro na boca e engole o líquido claro. Embora não sinta qualquer mudança imediata, você espera que a poção crie a ilusão de que você é um TROGLODITA igual aos outros diante de você. Respirando fundo, penetra decididamente na caverna. Os Trogloditas continuam com sua dança tribal, acreditando que você é um deles. Você passa por eles andando naturalmente e segue para o norte. Infelizmente, os efeitos da poção são de curta duração, e você ouve um berro atrás de si, quando um dos Trogloditas repara em você, que é forçado a correr, atravessando a caverna. Adiante, você vê um rio subterrâneo que corre de leste para oeste, cruzando a caverna, e uma ponte que liga uma margem à outra. Se você quiser correr pela ponte, volte para 318. Se preferir mergulhar no rio, volte para 47."
cap386 = "Você não chega a percorrer mais de três metros para o oeste antes de se chocar contra uma barreira invisível. Ela estala e solta faíscas, e você é repelido. Você colidiu com uma parede magnética. Você perde 1 ponto de ENERGIA. Não há outra alternativa senão voltar para a encruzilhada e seguir para o norte. Volte para 218."
cap387 = "Da sua frente vem o baque de passos pesados que se aproximam. Da penumbra surge um ser grande e primitivo, vestido com uma pele de animal e carregando uma clava de madeira. Ao vê-lo, ele grunhe e cospe no chão, em seguida ergue a clava e avança na sua direção, com um ar nada amigável. Você desembainha a espada e se prepara para enfrentar o HOMEM DA CAVERNA.\nHOMEM DA CAVERNA	HABILIDADE 7      ENERGIA 7\nSe você vencer, volte para 114."
cap388 = "O túnel logo chega a um beco sem saída. Um pedaço de papel, escurecido e enrugado de tão velho, está pregado na parede do fundo. Se você quiser pegá-lo para ver se contém alguma mensagem, volte para 23. Se preferir apressar-se a voltar pelo túnel para reunir-se ao Bárbaro, volte para 154."
cap389 = "Sem suas armas você está mais vulnerável, e a perda da espada faz com que se sinta praticamente nu. Você perde 4 pontos de HABILIDADE. Questionando se tomou a decisão correta, você segue pelo túnel para o norte. Volte para 181"
cap390 = "Você se agacha ao lado do pedestal, abaixo da linha de fogo das bestas. Estica a mão e puxa o crânio do pedestal, esperando que sua ação faça as bestas dispararem. Para sua grande surpresa, nada acontece. Some 1 ponto de SORTE. Ainda agachado, você arranca as jóias que formam os olhos do crânio. Você identifica as pedras amarelas - topázios - e as coloca na mochila. Olhando para a série de bestas, pergunta-se se ainda há uma armadilha à sua espera no aposento. Você:\nEngatinha para fora do aposento, levando o crânio?	Volte para 15\nRecoloca o crânio no pedestal antes de engatinhar\npara fora do aposento?	Volte para 204"
cap391 = "Ainda sorrindo, o velho olha para você e diz: “Muito bem, Estranho. Você respondeu corretamente. Desejo-lhe boa sorte durante o resto da Prova dos Campeões, e, com este objetivo, aumentarei seus poderes.” Ele então murmura mais umas poucas palavras ininteligíveis, e você sente um impulso poderoso percorrer-lhe o corpo. Acrescente 1 ponto a cada um dos seus índices de HABILIDADE, ENERGIA e SORTE. Você diz adeus ao velho e sai do aposento para continuar para o norte pela passagem. Volte para 100."
cap392 = "Você só tem tempo de ouvir o Gnomo dizer: “Três crânios”, antes que um raio branco de energia seja disparado da fechadura e atinja-lhe o peito, derrubando-o sem sentidos. Jogue um dado, some 1 ao número obtido e reduza esse total da sua ENERGIA. Se ainda estiver vivo, você recupera os sentidos e ouve o Gnomo ordenar que tente de novo. Você não acertou nenhuma das gemas, por isso não tentará essa combinação de novo.\nEsmeralda	Diamante	Safira	Volte para 16\nDiamante	Safira	Esmeralda	Fique em 392\nSafira	Esmeralda	Diamante	Volte para 177\nEsmeralda	Safira	Diamante	Volte para 287\nDiamante	Esmeralda	Safira	Volte para 132\nSafira	Diamante	Esmeralda	Volte para 249"
cap393 = "Você entra em um aposento frio, dividido por uma fenda profunda. Uma corda retesada estendida de lado a lado atravessa a fenda para o outro lado, onde um magnífico elmo alado repousa sobre um poste. Se você quiser caminhar pela corda bamba para chegar ao elmo, volte para 274. Se preferir retornar pelo túnel para continuar para o norte, volte para 291."
cap394 = "Você arrebenta o vidro com o cabo da espada, fazendo um buraco grande o bastante para que você passe. Imediatamente, os Insetos Gigantes saltam na sua direção. Sem perda de tempo, você entra no aposento, apanhando uma das tochas acesas para se defender. O fogo mantém a maioria dos Insetos a distância, mas, quando você consegue pegar a coroa e retornar ao corredor, certamente foi mordido por alguns deles. Jogue um dado e some 2 ao total. Este é o número de ferroadas que você recebeu, e terá que reduzir sua ENERGIA em 1 ponto para cada uma delas. Os Insetos Gigantes não vêm atrás de você, preferindo a luz brilhante do aposento em que estão. Você examina a coroa, e vê com desgosto que não é nada além de ferro pintado, e o “diamante” é vidro e não vale nada. Você a atira no chão com raiva e fica pensando aonde ir em seguida. Se quiser se dirigir para o oeste, volte para 59. Se preferir retornar ao cruzamento para continuar para o norte, volte para 14."
cap395 = "Ao ouvir o roído da sua bainha, um dos Trogloditas dá o alarme. Você se levanta e corre o mais rápido que pode pela caverna. Um dos arqueiros dispara uma flecha que lhe rasga o ombro com precisão mortal. Você perde 3 pontos de ENERGIA. Se ainda estiver vivo, volte para 259."
cap396 = "Você faz um laço com a corda, gira-o acima de si e o lança na cabeça do ídolo, sorrindo com alegria quando ele cai em torno do pescoço da estátua. Você então aperta o nó e começa a içar-se pela corda. Logo chega ao topo, sentando-se em cima do nariz do ídolo enquanto continua a segurar a corda. Você desembainha a espada e fica pensando de que olho arrancar a jóia primeiro. Se você quiser arrancar primeiro a do olho esquerdo, volte para 151. Se preferir arrancar a do olho direito, volte para 34."
cap397 = "O líquido é uma poção mágica que lhe permitirá detectar armadilhas ocultas. Some 2 pontos de SORTE. Se ainda não o fez, você pode abrir o livro vermelho – volte para 52. Do contrário, você terá que continuar para o norte com Throm - volte para 369."
cap398 = "Embora não haja qualquer armadilha evidente, você tem a forte sensação de que a arca contém um perigo oculto. A Poção de Detecção de Armadilha está funcionando bem. Você pára de um dos lados da arca e levanta a tampa com a espada, esticando o braço para mantê-la a distância. Quando a tampa se ergue, uma bola de ferro presa a um cordão é atirada para trás e quebra uma cápsula de vidro que está fixada no lado de dentro da tampa, instantaneamente liberando um gás. Felizmente, você tem tempo de pular para trás sem inalar os vapores venenosos. Quando o gás se dissipa, você caminha até a arca e olha dentro dela. Uma corrente com um pingente está jogada no fundo, mas alguém já tirou a jóia que havia nele. Você fica tão aborrecido que joga a corrente no chão e sai do aposento, furioso, para o túnel. Volte para 230."
cap399 = "O pão contém ervas curativas secretas dos elfos. Some 3 pontos de ENERGIA. Sentindo-se triste, embora forte, você guarda o espelho e o amuleto, saindo da caverna para seguir para o norte. Volte para 192."
vitoria = False
cap400 = "Logo que você aparece na saída do túnel, uma multidão grita e vibra. As pessoas abrem alas para que você siga na direção de um pequeno palanque, no qual, sentado embaixo de um pára- sol de bambu colorido, está o Barão Sukumvit. Ele parece apalermado, como se jamais esperasse que alguém conseguisse sair vivo do Calabouço da Morte. O segredo de Fang foi revelado. Quando o Barão se levanta da cadeira, você sobe os degraus do palanque, inclina-se diante dele e observa aqueles olhos frios fixos em você em completo espanto. Você sorri meio sem graça quando ele lhe oferece a mão estendida. Em meio ao barulho ensurdecedor da ovação do povo de Fang, o Barão Sukumvit abre o cofre que contém seu prêmio de 10.000 Peças de Ouro. Em seguida, ele coloca uma coroa de louros sobre a sua cabeça e o proclama Campeão do Calabouço da Morte."

cap = 1
capitulos = [0,cap1, cap2, cap3, cap4, cap5, cap6, cap7, cap8, cap9, cap10, cap11, cap12, cap13, cap14, cap15, cap16, cap17, cap18, cap19, cap20, cap21, cap22, cap23, cap24, cap25, cap26, cap27, cap28, cap29, cap30, cap31, cap32, 
cap33, cap34, cap35, cap36, cap37, cap38, cap39, cap40, cap41, cap42, cap43, cap44, cap45, cap46, cap47, cap48, cap49, cap50, cap51, cap52, cap53, cap54, cap55, cap56, cap57, cap58, cap59, cap60, cap61, cap62, cap63, cap64, cap65, cap66, cap67, cap68, cap69, cap70, cap71, cap72, cap73, cap74, cap75, cap76, cap77, cap78, cap79, cap80, cap81, cap82, cap83, cap84, cap85, cap86, cap87, cap88, cap89, cap90, cap91, cap92, cap93, cap94, cap95, cap96, cap97, cap98, cap99, cap100, cap101, cap102, cap103, cap104, cap105, cap106, cap107, cap108, cap109, cap110, cap111, cap112, cap113, cap114, cap115, cap116, cap117, cap118, cap119, cap120, cap121, cap122, cap123, cap124, cap125, cap126, cap127, cap128, cap129, cap130, cap131, cap132, cap133, cap134, cap135, cap136, cap137, cap138, cap139, cap140, cap141, cap142, cap143, cap144, cap145, cap146, cap147, cap148, cap149, cap150, cap151, cap152, cap153, cap154, cap155, cap156, cap157, cap158, cap159, cap160, cap161, cap162, cap163, cap164, cap165, cap166, cap167, cap168, cap169, cap170, cap171, cap172, cap173, cap174, cap175, cap176, cap177, cap178, cap179, cap180, cap181, cap182, cap183, cap184, cap185, cap186, cap187, cap188, cap189, cap190, cap191, cap192, cap193, cap194, cap195, cap196, cap197, cap198, cap199, cap200, cap201, cap202, cap203, cap204, cap205, cap206, cap207, cap208, cap209, cap210, cap211, cap212, cap213, cap214, cap215, cap216, cap217, cap218, cap219, cap220, cap221, cap222, cap223, cap224, cap225, cap226, cap227, cap228, cap229, cap230, cap231, cap232, cap233, cap234, cap235, cap236, cap237, cap238, cap239, cap240, cap241, cap242, cap243, cap244, cap245, cap246, cap247, cap248, cap249, cap250, cap251, cap252, cap253, cap254, cap255, cap256, cap257, cap258, cap259, cap260, cap261, cap262, cap263, cap264, cap265, cap266, cap267, cap268, cap269, cap270, cap271, cap272, cap273, cap274, cap275, cap276, cap277, cap278, cap279, cap280, cap281, cap282, cap283, cap284, cap285, cap286, cap287, cap288, cap289, cap290, cap291, cap292, cap293, cap294, cap295, cap296, cap297, cap298, cap299, cap300, cap301, cap302, cap303, cap304, cap305, cap306, cap307, cap308, cap309, cap310, cap311, cap312, cap313, cap314, cap315, cap316, cap317, cap318, cap319, cap320, cap321, cap322, cap323, cap324, cap325, cap326, cap327, cap328, cap329, cap330, cap331, cap332, cap333, cap334, cap335, cap336, cap337, cap338, cap339, cap340, cap341, cap342, cap343, cap344, cap345, cap346, cap347, cap348, cap349, cap350, cap351, cap352, cap353, cap354, cap355, cap356, cap357, cap358, cap359, cap360, cap361, cap362, cap363, cap364, cap365, cap366, cap367, cap368, cap369, cap370, cap371, cap372, cap373, cap374, cap375, cap376, cap377, cap378, cap379, cap380, cap381, cap382, cap383, cap384, cap385, cap386, cap387, cap388, cap389, cap390, cap391, cap392, cap393, cap394, cap395, cap396, cap397, cap398, cap399, cap400]

mochila = inventario.gerar_mochila()

inimigo_atual = ""

array_capitulos_que_morrem = [cap2, cap3, cap4, cap7, cap8, cap17, cap19, cap34, cap44, cap61, cap70, cap85, cap96, cap140, cap193, cap101, cap116, cap219, cap193, cap233, cap255, cap268, cap272, cap276, cap317, cap325, cap333, cap334, cap347, cap359, cap366, cap372]
morte = False

input("Aperte Enter para começar a jogar ")


print("Bem-vindo(a) ao jogo ao Calabouço da Morte")
print("Diga-me seu nome, herói: ")
nomepersonagem = input ("> ")

personagem_ficha = ficha.gerar_personagem()
print(f"Olá {nomepersonagem}, aqui está sua ficha")
print(f'Os seus status são: {personagem_ficha}')

input("\nPressione enter para continuar")

print("Você spawnou em Fang")
print("Vamos explorar esse mundo cheio de surpresas!")

print("Fang era uma cidade pequena e comum na província setentrional de Chiang Mai. Situada às margens do rio Kok, constituía-se num ponto de parada conveniente para os comerciantes e passageiros que se deslocavam pelo rio durante a maior parte do ano. Umas poucas barcaças, jangadas e, às vezes, um grande barco a vela podiam ser encontrados no atracadouro de Fang. Mas tudo isso foi há muito tempo, antes da criação da Prova dos Campeões. Agora, uma vez por ano, o rio fica apinhado de barcos, trazendo as pessoas que chegam de centenas de quilômetros ao redor, na esperança de testemunhara quebra de uma antiga tradição em Fang e ver alguém vitorioso na Prova dos Campeões.")

input("\nPressione enter para continuar")

print("No interior do labirinto escuro e sinuoso de Fang há horrores desconhecidos à sua espera. Concebido pela mente diabólica do Barão Sukumvit, o labirinto está infestado de armadilhas demoníacas e monstros sedentos de sangue, os quais submeterão suas habilidades a testes quase além do limite possível de resistência. Inúmeros aventureiros aceitaram o desafio da Prova dos Campeões e atravessaram a porta talhada em forma de boca do labirinto para nunca mais voltar. Aperte Enter caso você se atreva a entrar!")
input("\nPressione enter para continuar")



while vitoria == False and morte == False and personagem_ficha["energia"] > 0: 
        print(f'\nSeus status atuais: {personagem_ficha}\n')
        print(capitulos[cap])
        if capitulos[cap] == cap5:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("vá para rota 185")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 395")
                
        if capitulos[cap] == cap6:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 2
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        if capitulos[cap] == cap16:
            personagem_ficha["energia"] = personagem_ficha["energia"]  - dado.dados() - 1
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        if capitulos[cap] == cap17:
            soma = dado.dados() + dado.dados()
            continua= input("\nPressione enter para jogar os dados")
            print(f'O resultado dos dados foi de {soma}, agora escolha a rota baseado no resultado e sua habilidade')
        if capitulos[cap] == cap20:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] - 1
        if capitulos[cap] == cap21:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("vá para rota 97")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 116")
        if  capitulos[cap] == cap26:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] - 2
            print(f'agora sua Habilidade é de {personagem_ficha["habilidade"]}')
            soma = dado.dados() + dado.dados()
            continua= input("\nPressione enter para jogar os dados")
            print(f'O resultado dos dados foi de {soma}, agora escolha a rota baseado no resultado e sua habilidade')
            if  soma <= personagem_ficha["habilidade"]:
                print("vá para rota 55")
            if  soma > personagem_ficha["habilidade"]:
                print("vá para rota 202")
        if capitulos[cap] == cap28:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] + 1
            prox_capitulo = [20, 48]
        if  capitulos[cap] == cap33:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] - 3
        if capitulos[cap] == cap36:
            soma = dado.dados() + dado.dados()
            continua= input("\nPressione enter para jogar os dados")
            print(f'O resultado dos dados foi de {soma}, agora escolha a rota baseado no resultado e sua habilidade ou sua sorte')
            if  soma <= personagem_ficha["habilidade"] and soma > personagem_ficha["sorte"]:
                print("vá para rota 340")
            if  soma > personagem_ficha["habilidade"] or soma > personagem_ficha["sorte"]:
                print("vá para rota 7")
        if capitulos[cap] == cap38:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 3
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        if capitulos[cap] == cap39: #mosca
            inimigo_atual = "Mosca Gigante"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)
        if capitulos[cap] == cap40: #minotauro
            inimigo_atual = "Minotauro"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)
        if capitulos[cap] == cap42:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 5
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
            soma = dado.dados() + dado.dados()
            continua= input("\nPressione enter para jogar os dados")
            print(f'O resultado dos dados foi de {soma}, agora escolha a rota baseado no resultado e sua habilidade')
            if  soma <= personagem_ficha["habilidade"]:
                print("vá para rota 55")
            if  soma > personagem_ficha["habilidade"]:
                print("vá para rota 202")
        if capitulos[cap] == cap45:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 4
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] - 1
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 

        if capitulos[cap] == cap51: 
            inimigo_atual = "Segundo Hobgoblin"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)
            
        if capitulos[cap] == cap57:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 4
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 
        if capitulos[cap] == cap58:
            soma = dado.dados() + dado.dados()
            continua= input("\nPressione enter para jogar os dados")
            print(f'O resultado dos dados foi de {soma}, agora escolha a rota baseado no resultado e sua habilidade')
            if  soma <= personagem_ficha["habilidade"]:
                print("vá para rota 80")
            if  soma > personagem_ficha["habilidade"]:
                print("vá para rota 246")
        if capitulos[cap] == cap64:
            soma = dado.dados() + dado.dados()
            continua= input("\nPressione enter para jogar os dados")
            print(f'O resultado dos dados foi de {soma}, agora escolha a rota baseado no resultado e sua habilidade')
            if  soma <= personagem_ficha["habilidade"]:
                print("vá para rota 115")
            if  soma > personagem_ficha["habilidade"]:
                print("vá para rota 190")
        if capitulos[cap] == cap72:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] - 2
        if capitulos[cap] == cap84:
            soma = dado.dados() + dado.dados()
            continua= input("\nPressione enter para jogar os dados")
            if soma > 8:
                print('vá para 152')
            else:
                print('vá para 121')

        if capitulos[cap] == cap95:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] + 1

            

        if capitulos[cap] == cap102:
            print(f"Você gritou {nomepersonagem}")
        if capitulos[cap] == cap103:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 3
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 
        if capitulos[cap] == cap105:
            loot = "Taça"
            inv_atualizado = inventario.adicionar_item(mochila, loot)
            mochila = inv_atualizado
        if capitulos[cap] == cap106:
            loot = "Poção da Réplica"
            inv_atualizado = inventario.adicionar_item(mochila, loot)
            mochila = inv_atualizado
        if capitulos[cap] == cap115:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 3
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 
        if capitulos[cap] == cap123:
            loot = "Amuleto de Força"
            inv_atualizado = inventario.adicionar_item(mochila, loot)
            mochila = inv_atualizado
            personagem_ficha["energia"] = personagem_ficha["energia"] + 1
            personagem_ficha["habilade"] = personagem_ficha["habilidade"] + 1
        if capitulos[cap] == cap124:
            inimigo_atual = "Primeiro Goblin"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)
        if capitulos[cap] == cap125:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("vá para rota 69")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 139")
        if capitulos[cap] == cap130:
            inimigo_atual = "Primeiro Goblin"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)

            inimigo_atual = "Segundo Goblin"
            combate.batalha(personagem_ficha, inimigo_atual)        
        if capitulos[cap] == cap132:
            azar = dado.dados() + 1
            personagem_ficha["energia"] = personagem_ficha["energia"] - azar
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 
        if capitulos[cap] == cap133:
            resul = dado.dados() + dado.dados()
            if resul <= personagem_ficha["habilade"]:
                print("vá para 178")
            else:
                print("volte para 17")
        if  capitulos[cap] == cap139:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 2
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 
            else:
                inimigo_atual = "Erva"
                combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
                combate.batalha(personagem_ficha, inimigo_atual)
        if  capitulos[cap] == cap141:
            resul = dado.dados() + dado.dados()
            if resul <= personagem_ficha["habilade"]:
                print("volte para 72")
            else:
                print("volte para 96")
        if  capitulos[cap] == cap143:
            inimigo_atual = "Escorpião Gigante"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)
        if  capitulos[cap] == cap145:
            inimigo_atual = "Anão"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)         
        if  capitulos[cap] == cap147:
            personagem_ficha["energia"] += 3
        if capitulos[cap] == cap148:

            inimigo_atual = "Primeiro Cão de Guarda"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)

            inimigo_atual = "Segundo Cão de Guarda"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)            
        if capitulos[cap] == cap149:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("volte para 70")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para 353")
        if capitulos[cap] == cap150:
            loot = "Sino de Metal"
            inv_atualizado = inventario.adicionar_item(mochila, loot)
            mochila = inv_atualizado
            personagem_ficha["habilade"] = personagem_ficha["habilidade"] - 1
        if capitulos[cap] == cap151:
            personagem_ficha["habilade"] = personagem_ficha["habilidade"] - 2

            print("O terreno não te favorece, enfraquecendo seus ataques\n -2 Habilidade (Temporariamente)")

            inimigo_atual = "Primeiro Guardião Voador"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)

            inimigo_atual = "Segundo Guardião Voador"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)            

            personagem_ficha["habilade"] = personagem_ficha["habilidade"] + 2
        if capitulos[cap] == cap152:
            soma = dado.dados() + dado.dados()
            if soma <= personagem_ficha["habilidade"]:
                print("Volte para 55")
            else:
                print("Vá para 202")
        if capitulos[cap] == cap157:
            personagem_ficha["sorte"] = personagem_ficha["sorte"] + 1
        if capitulos[cap] == cap158:
            personagem_ficha["habilade"] = personagem_ficha["habilidade"] - 1
            personagem_ficha["energia"] = personagem_ficha["energia"] - 4
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        if capitulos[cap] == cap162: 
            personagem_ficha["sorte"] = personagem_ficha["sorte"] + 1
        if capitulos[cap] == cap166:
            personagem_ficha["habilade"] = personagem_ficha["habilidade"] - 3

            print("O terreno não te favorece, enfraquecendo seus ataques\n -3 Habilidade (Temporariamente)")

            inimigo_atual = "Primeiro Guardião Voador"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)

            inimigo_atual = "Segundo Guardião Voador"
            combate.batalha(personagem_ficha, inimigo_atual)            

            personagem_ficha["habilade"] = personagem_ficha["habilidade"] + 2
            
        if capitulos[cap] == cap167:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 4
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        if capitulos[cap] == cap171:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 4
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        if capitulos[cap] == cap172:
            print('')            
            inimigo_atual = "Besta Sangrenta"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)

        if capitulos[cap] == cap174:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("Volte para 39")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 350")
        if capitulos[cap] == cap175:
            personagem_ficha["sorte"] = personagem_ficha["sorte"] + 2
        if capitulos[cap] == cap177:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("Vá para 243")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("Volte para 103")
        if capitulos[cap] == cap179:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 2
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        if capitulos[cap] == cap180:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("Volte para 53")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("Volte para 272")
        if capitulos[cap] == cap181:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("Vá para 312")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("Volte para 45") 
        if capitulos[cap] == cap186:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("Vá para 260")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("Vá para 358")
        if capitulos[cap] == cap189:
            inimigo_atual = "Primeira Orca"
            combate.batalha(personagem_ficha, inimigo_atual)

            inimigo_atual = "Segunda Orca"
            combate.batalha(personagem_ficha, inimigo_atual)
        if capitulos[cap] == cap190:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 3
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        if capitulos[cap] == cap191:         
            soma = dado.dados() + dado.dados()
            if soma < 8:
                print("Volte para 152")
            else:
                print("Volte para 292")
        if capitulos[cap] == cap195:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 1
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        if capitulos[cap] == cap196:
            print()
            inimigo_atual = "Mantécora"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)
        if capitulos[cap] == cap199:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 2
            personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 
        if capitulos[cap] == cap202:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("Volte para 18")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("Volte para 42")
        if capitulos[cap] == cap203:
            print()
            inimigo_atual = "Diabo do Poço"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)
        if capitulos[cap] == cap204:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("Volte para 131")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("Volte para 199")
        if capitulos[cap] == cap207:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 3
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 
        
        if capitulos[cap] == cap215:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 2
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 

        if capitulos[cap] == cap223:
            personagem_ficha["sorte"] = personagem_ficha["sorte"] - 2
            soma = dado.dados() + dado.dados()
            continua= input("\nPressione enter para jogar os dados")
            personagem_ficha["energia"] = personagem_ficha["energia"] - soma
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 
        if capitulos[cap] == cap225:
            inimigo_atual = "Besta Sangrenta"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("vá para rota 97")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 21")
        if capitulos[cap] == cap226:
            personagem_ficha["energia"] = personagem_ficha["energia"] + 3
        if capitulos[cap] == cap228:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("vá para rota 150")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 33")

        if capitulos[cap] == cap235:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 2
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 
        
        if capitulos[cap] == cap236:
            inimigo_atual = "Imitador"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)
        if capitulos[cap] == cap238:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] + 1
            
        if capitulos[cap] == cap242:
            soma = dado.dados() + dado.dados()
            continua= input("\nPressione enter para jogar os dados")
            
            if soma <= personagem_ficha["habilidade"]:
                print('volte para 48')
            else:
                print('vá para 366')
        
        if capitulos[cap] == cap246:
            personagem_ficha["sorte"] = personagem_ficha["sorte"] - 2
            soma = dado.dados() + dado.dados()
            continua= input("\nPressione enter para jogar os dados")
            personagem_ficha["energia"] = personagem_ficha["energia"] - soma
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 
        
        if capitulos[cap] == cap247:
            inimigo_atual = "Mantécora"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)
            soma = dado.dados() + dado.dados()
            continua= input("\nPressione enter para jogar os dados")
            personagem_ficha["energia"] = personagem_ficha["energia"] - soma
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 
        if capitulos[cap] == cap249:
            personagem_ficha["energia"] = personagem_ficha["energia"] - dado.dados() - 1
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 
        if capitulos[cap] == cap256:
            loot = "Poção de Réplica"
            inv_atualizado = inventario.adicionar_item(mochila, loot)
            mochila = inv_atualizado
        if capitulos[cap] == cap257:
            loot = "Tubo oco de madeira"
            inv_atualizado = inventario.adicionar_item(mochila, loot)
            mochila = inv_atualizado
        if capitulos[cap] == cap269:
            personagem_ficha["energia"] = personagem_ficha["energia"] + 3

        if capitulos[cap] == cap270:
            loot = "Peça de Ouro"
            inv_atualizado = inventario.adicionar_item(mochila, loot)
            mochila = inv_atualizado
            
        if capitulos[cap] == cap271:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] - 1

        if capitulos[cap] == cap274:
            soma = dado.dados() + dado.dados()
            if soma <= personagem_ficha["habilidade"]:
                print('volte para 238')
            else:
                print('vá para 359')
        
        if capitulos[cap] == cap275:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("vá para rota 231")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 309")

        if capitulos[cap] == cap285:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] - 1
            personagem_ficha["energia"] = personagem_ficha["energia"] - 2
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 

        if capitulos[cap] == cap286:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] + 4
        
        if capitulos[cap] == cap287:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 1 - dado.dados()
            if personagem_ficha["energia"] <= 0:
                morte = True
                break 

        if capitulos[cap] == cap289:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("vá para rota 216")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 19")
            
        if capitulos[cap] == cap290:
            soma = dado.dados() + dado.dados()
            if soma == 8:
                print('vá para 152')
            else:
                print('vá para 121')

        if capitulos[cap] == cap294:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] - 2
            inimigo_atual = "Besta Sangrenta"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("vá para rota 97")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 21")

        if capitulos[cap] == cap295:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 5 

        if capitulos[cap] == cap297:
            personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            
        if capitulos[cap] == cap302:
            print('')            
            inimigo_atual = "Throm"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)

        if capitulos[cap] == cap304:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 6
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        
        if capitulos[cap] == cap306:
            mochila["itens_diversos"] = 0
            mochila["Poção de Vida"] = 0 
            mochila["Poção de Sorte"] = 0  
            mochila["espada"] = 0
            mochila["poção da réplica"] = 0
            mochila["itens_diversos"] = []
            mochila["Peça de Ouro"] = 0
            personagem_ficha["sorte"] = personagem_ficha["sorte"] - 2
        
        if capitulos[cap] == cap309:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 3
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("vá para rota 231")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 193")

        if capitulos[cap] == cap312:
            inimigo_atual = "Ninja"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)

        if capitulos[cap] == cap326:
            soma = dado.dados()
            if soma == 1 or soma == 2:
                print('vá para 91')
            if soma == 3 or soma == 4:
                print('vá para 189')
            if soma == 5 or soma == 6:
                print('vá para 380')
        
        if capitulos[cap] == cap330:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 1
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        
        if capitulos[cap] == cap331:
            inimigo_atual = "Guerreiro-Esqueleto"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)

        if capitulos[cap] == cap332:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("vá para rota 53")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 272")
        
        if capitulos[cap] == cap335:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("vá para rota 67")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 101")

        if capitulos[cap] == cap336:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] - 4

        if capitulos[cap] == cap337:
            personagem_ficha["energia"] = personagem_ficha["energia"] + 1
            personagem_ficha["sorte"] = personagem_ficha["sorte"] + 2
        
        if capitulos[cap] == cap339:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 1
            if personagem_ficha["energia"] <= 0:
                morte = True
                break

        if capitulos[cap] == cap343:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 1
            if personagem_ficha["energia"] <= 0:
                morte = True
                break

        if capitulos[cap] == cap348:
            soma = dado.dados() + dado.dados()
            if soma <=  personagem_ficha["habilidade"]:
                print('vá para 225')
            else:
                print("vá para 159")

        if capitulos[cap] == cap349:
            inimigo_atual = "Diabo do Poço"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)
            

        if capitulos[cap] == cap350:
            personagem_ficha["energia"] = personagem_ficha["energia"] - dado.dados()
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        
        if capitulos[cap] == cap353:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] - 1
            personagem_ficha["energia"] = personagem_ficha["energia"] - 4
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        
        if capitulos[cap] == cap354:
            personagem_ficha["sorte"] = personagem_ficha["sorte"] - 2
            soma = dado.dados() + dado.dados()
            if soma <=  personagem_ficha["habilidade"]:
                print('vá para 55')
            else:
                print("vá para 202")

        if capitulos[cap] == cap358:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 2
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
            
        if capitulos[cap] == cap361:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("volte para 118")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 295")
            
        if capitulos[cap] == cap363:
            personagem_ficha["energia"] = personagem_ficha["energia"] + 2
            
        if capitulos[cap] == cap367:
            print("Deseja Comprar? (sim/não)")
            r = input(">")
            if r == "sim":
                item = "Peça de Ouro"
                mochila = inventario.remover_item(mochila, item)
        if capitulos[cap] == cap368:
            print("Deseja Comprar? (sim/não)")
            r = input(">")
            if r == "sim":
                item = "Peça de Ouro"
                mochila = inventario.remover_item(mochila, item)
        if capitulos[cap] == cap369:
            inimigo_atual = "Troll da Caverna"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)

            inimigo_atual = "Troll da Caverna"
            combate.batalha(personagem_ficha, inimigo_atual)            

        if capitulos[cap] == cap370:
            soma = dado.dados() + dado.dados()
            if soma <= personagem_ficha["habilidade"]:
                print("Volte para 104")
            else:
                print("Volte para 342")
        if capitulos[cap] == cap371:
            soma = dado.dados() + dado.dados()
            if soma <= personagem_ficha["habilidade"]:
                print("Volte para 273")
            else:
                print("Volte para 113")
        if capitulos[cap] == cap374:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("volte para 118")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 295")
        if capitulos[cap] == cap377:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 5
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        if capitulos[cap] == cap378:
            testesorte = dado.dados() + dado.dados()
            if testesorte < personagem_ficha["sorte"]:
                print("volte para 112")
                personagem_ficha["sorte"] = personagem_ficha["sorte"] - 1
            else:
                print("vá para rota 209")
        if capitulos[cap] == cap380:
            inimigo_atual = "Primeira Orca"
            combate.batalha(personagem_ficha, inimigo_atual)

            inimigo_atual = "Segunda Orca"
            combate.batalha(personagem_ficha, inimigo_atual)

        if capitulos[cap] == cap384:
           personagem_ficha["energia"] = personagem_ficha["energia"] - 2
        if capitulos[cap] == cap386:
           personagem_ficha["energia"] = personagem_ficha["energia"] - 1

        if capitulos[cap] == cap387:
            inimigo_atual = "Homem da Caverna"
            combate.encontrou_inimigo(personagem_ficha, inimigo_atual)
            combate.batalha(personagem_ficha, inimigo_atual)            

        if capitulos[cap] == cap389:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] - 4
        if capitulos[cap] == cap390:
            personagem_ficha["sorte"] = personagem_ficha["sorte"] + 1
        if capitulos[cap] == cap391:
            personagem_ficha["habilidade"] = personagem_ficha["habilidade"] + 1
            personagem_ficha["energia"] = personagem_ficha["energia"] + 1
            personagem_ficha["sorte"] = personagem_ficha["sorte"] + 1

        if capitulos[cap] == cap392:
            unluck = dado.dados() + 1
            personagem_ficha["energia"] = personagem_ficha["energia"] - unluck
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        if capitulos[cap] == cap394:
            unluck = dado.dados() + 2
            personagem_ficha["energia"] = personagem_ficha["energia"] - unluck
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
        if capitulos[cap] == cap395:
            personagem_ficha["energia"] = personagem_ficha["energia"] - 3
            if personagem_ficha["energia"] <= 0:
                morte = True
                break
            
        if capitulos[cap] == cap397:
            personagem_ficha["sorte"] = personagem_ficha["sorte"] + 2

        if capitulos[cap] == cap399:
            personagem_ficha["energia"] = personagem_ficha["energia"] + 3
        
        if capitulos[cap] in array_capitulos_que_morrem:
            morte = True
        if cap == 400:
            vitoria = True

        while cap not in prox_capitulo:
            continua= input("\nPressione enter para continuar")
            print("\nQual foi a sua rota?")
            cap = int(input("> "))
            continua= input("\nPressione enter para continuar")

    
        
if vitoria == True:
    print(cap400)
    print(f'\nParabens {nomepersonagem}!\n')
    print('você conseguiu a experiência necessária e ganhou o jogo.')   
if morte == True:
    print(capitulos[cap])
    print(f'\nVocê está morto, {nomepersonagem}!\nFim de Jogo!')