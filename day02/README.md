--- Dia 2: Enigma dos Cubos ---
Você é lançado alto na atmosfera! O ápice de sua trajetória mal atinge a superfície de uma grande ilha flutuante no céu. Você pousa suavemente em uma pilha fofa de folhas. Está bastante frio, mas você não vê muita neve. Um Elfo corre para cumprimentá-lo.

O Elfo explica que você chegou na **Ilha da Neve** e pede desculpas pela falta de neve. Ele ficará feliz em explicar a situação, mas é um pouco longe, então você tem algum tempo. Eles não recebem muitos visitantes aqui em cima; você gostaria de jogar um jogo enquanto espera?

Enquanto você caminha, o Elfo mostra a você uma pequena bolsa e alguns cubos que são vermelhos, verdes ou azuis. Cada vez que você joga este jogo, ele esconderá um número secreto de cubos de cada cor na bolsa, e seu objetivo é descobrir informações sobre o número de cubos.

Para obter informações, uma vez que uma bolsa foi carregada com cubos, o Elfo mergulhará na bolsa, pegará um punhado de cubos aleatórios, mostrará a você e depois os colocará de volta na bolsa. Ele fará isso algumas vezes por jogo.

Você joga vários jogos e registra as informações de cada jogo (sua entrada de quebra-cabeça). Cada jogo é listado com seu número de ID (como o 11 em `Jogo 11: ...`) seguido por uma lista separada por ponto e vírgula de subconjuntos de cubos que foram revelados da bolsa (como `3 azuis, 5 vermelhos, 4 azuis`).

Por exemplo, o registro de alguns jogos pode parecer assim:

```
Jogo 1: 3 azuis, 4 vermelhos; 1 vermelho, 2 verdes, 6 azuis; 2 verdes
Jogo 2: 1 azul, 2 verdes; 3 verdes, 4 azuis, 1 vermelho; 1 verde, 1 azul
Jogo 3: 8 verdes, 6 azuis, 20 vermelhos; 5 azuis, 4 vermelhos, 13 verdes; 5 verdes, 1 vermelho
Jogo 4: 1 verde, 3 vermelhos, 6 azuis; 3 verdes, 6 vermelhos; 3 verdes, 15 azuis, 14 vermelhos
Jogo 5: 6 vermelhos, 1 azul, 3 verdes; 2 azuis, 1 vermelho, 2 verdes
```

No jogo 1, três conjuntos de cubos são revelados da bolsa (e depois colocados de volta novamente). O primeiro conjunto é composto por 3 cubos azuis e 4 cubos vermelhos; o segundo conjunto é composto por 1 cubo vermelho, 2 cubos verdes e 6 cubos azuis; o terceiro conjunto contém apenas 2 cubos verdes.

O Elfo gostaria de saber primeiro quais jogos teriam sido **possíveis** se a bolsa contivesse **apenas 12 cubos vermelhos, 13 cubos verdes e 14 cubos azuis**?

No exemplo acima, os jogos 1, 2 e 5 teriam sido **possíveis** se a bolsa tivesse sido carregada com essa configuração. No entanto, o jogo 3 teria sido **impossível** porque em um momento o Elfo mostrou a você 20 cubos vermelhos de uma vez; da mesma forma, o jogo 4 também teria sido **impossível** porque o Elfo mostrou a você 15 cubos azuis de uma vez. Se somar os IDs dos jogos que teriam sido possíveis, você obtém **`8`**.

Determine quais jogos teriam sido possíveis se a bolsa tivesse sido carregada com apenas 12 cubos vermelhos, 13 cubos verdes e 14 cubos azuis. **Qual é a soma dos IDs desses jogos?**

--- Parte Dois ---
O Elfo diz que pararam de produzir neve porque não estão recebendo água! Ele não tem certeza do motivo pelo qual a água parou; no entanto, ele pode te mostrar como chegar à fonte de água para verificar por si mesmo. É só ali na frente!

Enquanto você continua a caminhada, o Elfo faz uma segunda pergunta: em cada jogo que você jogou, **qual é o menor número de cubos de cada cor** que poderia ter estado na bolsa para tornar o jogo possível?

Considere novamente os exemplos de jogos anteriores:
```
Jogo 1: 3 azuis, 4 vermelhos; 1 vermelho, 2 verdes, 6 azuis; 2 verdes
Jogo 2: 1 azul, 2 verdes; 3 verdes, 4 azuis, 1 vermelho; 1 verde, 1 azul
Jogo 3: 8 verdes, 6 azuis, 20 vermelhos; 5 azuis, 4 vermelhos, 13 verdes; 5 verdes, 1 vermelho
Jogo 4: 1 verde, 3 vermelhos, 6 azuis; 3 verdes, 6 vermelhos; 3 verdes, 15 azuis, 14 vermelhos
Jogo 5: 6 vermelhos, 1 azul, 3 verdes; 2 azuis, 1 vermelho, 2 verdes
```
- No jogo 1, o jogo poderia ter sido jogado com no mínimo 4 cubos vermelhos, 2 verdes e 6 cubos azuis. Se qualquer cor tivesse pelo menos um cubo a menos, o jogo teria sido impossível.
- O Jogo 2 poderia ter sido jogado com no mínimo 1 cubo vermelho, 3 verdes e 4 azuis.
- O Jogo 3 deve ter sido jogado com pelo menos 20 cubos vermelhos, 13 verdes e 6 azuis.
- O Jogo 4 exigiu no mínimo 14 cubos vermelhos, 3 verdes e 15 cubos azuis.
- O Jogo 5 precisava de pelo menos 6 cubos vermelhos, 3 verdes e 2 azuis na bolsa.
O poder de um conjunto de cubos é igual ao número de cubos vermelhos, verdes e azuis multiplicados juntos. O poder do conjunto mínimo de cubos no jogo 1 é 48. Nos jogos 2 a 5, foi `12`, `1560`, `630` e `36`, respectivamente. Somando esses cinco poderes, obtemos a soma **`2286`**.

Para cada jogo, encontre o conjunto mínimo de cubos que deve ter estado presente. **Qual é a soma dos poderes desses conjuntos?**