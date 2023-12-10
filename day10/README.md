# Dia 10: Labirinto de Tubos

[https://adventofcode.com/2023/day/10](https://adventofcode.com/2023/day/10)

## Descrição

### Parte Um

Você usa a asa-delta para voar com o ar quente da Ilha do Deserto até a ilha flutuante de metal. Esta ilha é surpreendentemente fria e definitivamente não há termais para planar, então você deixa sua asa-delta para trás.

Você vagueia por um tempo, mas não encontra nenhuma pessoa ou animal. No entanto, ocasionalmente, você encontra placas sinalizadoras rotuladas "[Hot Springs](https://en.wikipedia.org/wiki/Hot_spring)" apontando em uma direção aparentemente consistente; talvez você possa encontrar alguém nas fontes termais e perguntar a eles onde as peças da máquina do deserto são feitas.

A paisagem aqui é alienígena; até as flores e árvores são feitas de metal. Ao parar para admirar uma grama de metal, você percebe algo metálico se afastar em sua visão periférica e pular em um grande tubo! Não parecia nenhum animal que você já viu; se você quiser dar uma olhada melhor, precisará ficar à frente dele.

Ao escanear a área, você descobre que todo o campo em que está pisando está <span title="Fabricado pela Hamilton and Hilbert Pipe Company">densamente cheio de tubos</span>; foi difícil perceber no início porque são da mesma cor prateada metálica que o "chão". Você faz um esboço rápido de todos os tubos de superfície que consegue ver (sua entrada do quebra-cabeça).

Os tubos são dispostos em uma grade bidimensional de _tiles_:

*   `|` é um _tubo vertical_ conectando norte e sul.
*   `-` é um _tubo horizontal_ conectando leste e oeste.
*   `L` é uma _curva de 90 graus_ conectando norte e leste.
*   `J` é uma _curva de 90 graus_ conectando norte e oeste.
*   `7` é uma _curva de 90 graus_ conectando sul e oeste.
*   `F` é uma _curva de 90 graus_ conectando sul e leste.
*   `.` é o _chão_; não há tubo neste tile.
*   `S` é a _posição inicial_ do animal; há um tubo neste tile, mas seu esboço não mostra qual é a forma do tubo.

Com base na acústica do movimento do animal, você tem certeza de que o tubo que contém o animal é _um grande circuito contínuo_.

Por exemplo, aqui está um circuito quadrado de tubos:

    .....
    .F-7.
    .|.|.
    .L-J.
    .....
    

Se o animal tivesse entrado neste circuito no canto noroeste, o esboço seria assim:

    .....
    .S-7.
    .|.|.
    .L-J.
    .....
    

No diagrama acima, o tile `S` ainda é uma curva de `F` de 90 graus: você pode perceber isso pela forma como os tubos adjacentes se conectam a ele.

Infelizmente, também há muitos tubos que _não estão conectados ao circuito_! Este esboço mostra o mesmo circuito acima:

    -L|F7
    7S-7|
    L|7||
    -L-J|
    L|-JF
    

No diagrama acima, você ainda pode descobrir quais tubos formam o circuito principal: são aqueles conectados a `S`, tubos que esses tubos se conectam, tubos _esses_ tubos se conectam e assim por diante. Todo tubo no circuito principal se conecta a seus dois vizinhos (incluindo `S`, que terá exatamente dois tubos conectados a ele, e que se presume se conectar de volta a esses dois tubos).

Aqui está um esboço que contém um circuito principal um pouco mais complexo:

    ..F7.
    .FJ|.
    SJ.L7
    |F--J
    LJ...
    

Aqui está o mesmo esboço de exemplo com os tiles de tubo extra, não pertencentes ao circuito principal

, também mostrados:

    7-F7-
    .FJ|7
    SJLL7
    |F--J
    LJ.LJ
    

Se você quiser _ficar à frente do animal_, deve encontrar o tile no circuito que está _mais longe da posição inicial_. Como o animal está no tubo, não faz sentido medir isso pela distância direta. Em vez disso, você precisa encontrar o tile que levaria o maior número de passos _ao longo do circuito_ para chegar da posição inicial ao ponto mais distante da posição inicial - independentemente de qual caminho o animal seguiu ao redor do circuito.

No primeiro exemplo com o circuito quadrado:

    .....
    .S-7.
    .|.|.
    .L-J.
    .....
    

Você pode contar a distância que cada tile no circuito tem da posição inicial assim:

    .....
    .012.
    .1.3.
    .234.
    .....
    

Neste exemplo, o ponto mais distante do início está a _`4`_ passos de distância.

Aqui está o circuito mais complexo novamente:

    ..F7.
    .FJ|.
    SJ.L7
    |F--J
    LJ...
    

Aqui estão as distâncias para cada tile neste circuito:

    ..45.
    .236.
    01.78
    14567
    23...
    

Encontre o único circuito gigante começando em `S`. _Quantos passos ao longo do circuito são necessários para ir da posição inicial ao ponto mais distante da posição inicial?_