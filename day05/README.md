--- Dia 5: Se Você Der Um Fertilizante a Uma Semente ---
Você pega o barco e encontra o jardineiro exatamente onde disseram que ele estaria: administrando uma "horta" gigante que parece mais para você como uma fazenda.

"Uma fonte de água? A **Ilha da Ilha** **é** a fonte de água!" Você aponta que a Ilha da Neve não está recebendo água.

"Oh, tivemos que parar a água porque **acabamos de areia** para filtrar! Não podemos fazer neve com água suja. Não se preocupe, tenho certeza de que teremos mais areia em breve; só desligamos a água há alguns dias... semanas... ah não." Seu rosto afunda em uma expressão de realização horrorizada.

"Estive tão ocupado garantindo que todos aqui tenham comida que esqueci completamente de verificar por que paramos de receber mais areia! Há uma balsa saindo em breve naquela direção - é muito mais rápida que seu barco. Você poderia dar uma olhada, por favor?"

Você mal tem tempo para concordar com este pedido quando ele traz outro. "Enquanto você espera pela balsa, talvez você possa nos ajudar com nosso **problema de produção de alimentos**. O último Almanaque da Ilha da Ilha acabou de chegar e estamos tendo dificuldades para entender."

O almanaque (sua entrada de quebra-cabeça) lista todas as sementes que precisam ser plantadas. Ele também lista qual tipo de solo usar com cada tipo de semente, qual tipo de fertilizante usar com cada tipo de solo, qual tipo de água usar com cada tipo de fertilizante e assim por diante. Cada tipo de semente, solo, fertilizante, etc., é identificado com um número, mas os números são reutilizados por cada categoria - ou seja, solo `123` e fertilizante `123` não são necessariamente relacionados entre si.

Por exemplo:
```
sementes: 79 14 55 13

mapa de semente-para-solo:
50 98 2
52 50 48

mapa de solo-para-fertilizante:
0 15 37
37 52 2
39 0 15

mapa de fertilizante-para-água:
49 53 8
0 11 42
42 0 7
57 7 4

mapa de água-para-luz:
88 18 7
18 25 70

mapa de luz-para-temperatura:
45 77 23
81 45 19
68 64 13

mapa de temperatura-para-umidade:
0 69 1
1 0 69

mapa de umidade-para-localização:
60 56 37
56 93 4
```
O almanaque começa listando quais sementes precisam ser plantadas: sementes `79`, `14`, `55` e `13`.

O restante do almanaque contém uma lista de **mapas** que descrevem como converter números de uma **categoria de origem** para números em uma **categoria de destino**. Ou seja, a seção que começa com mapa de semente-para-solo: descreve como converter um **número de semente** (a origem) em um **número de solo** (o destino). Isso permite que o jardineiro e sua equipe saibam qual solo usar com quais sementes, qual água usar com qual fertilizante, e assim por diante.

Em vez de listar cada número de origem e seu número correspondente de destino um por um, os mapas descrevem **intervalos inteiros** de números que podem ser convertidos. Cada linha dentro de um mapa contém três números: o **início do intervalo de destino**, o **início do intervalo de origem** e o **comprimento do intervalo**.

Considere novamente o exemplo `mapa de semente-para-solo`:

```
50 98 2
52 50 48
```
A primeira linha tem um **início do intervalo de destino** de 50, um **início do intervalo de origem** de `98` e um **comprimento do intervalo** de 2. Isso significa que o intervalo de origem começa em `98` e contém dois valores: `98` e `99`. O intervalo de destino é do mesmo comprimento, mas começa em `50`, então seus dois valores são `50` e 51. Com essa informação, você sabe que o número de semente `98` corresponde ao número de solo `50` e que o número de semente 99 corresponde ao número de solo `51`.

A segunda linha significa que o intervalo de origem começa em `50` e contém 48 valores: `50`, `51`, ..., `96`, `97`. Isso corresponde a um intervalo de destino que começa em `52` e também contém `48` valores: `52`, `53`, ..., `98`, `99`. Portanto, o número de semente `53` corresponde ao número de solo `55`.

Quaisquer números de origem que **não estão mapeados** correspondem ao mesmo número de destino. Portanto, o número de semente `10` corresponde ao número de solo `10`.

Assim, a lista completa de números de semente e seus números de solo correspondentes se parece com isso:
```
semente  solo
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
```
Com esse mapa, você pode procurar o número de solo necessário para cada número de semente inicial:

- O número de semente `79` corresponde ao número de solo `81`.
- O número de semente `14` corresponde ao número de solo `14`.
- O número de semente `55` corresponde ao número de solo `57`.
- O número de semente `13` corresponde ao número de solo `13`.
O jardineiro e sua equipe querem começar o mais rápido possível, então eles gostariam de saber a localização mais próxima que precisa de uma semente. Usando esses mapas, encontre o número de localização mais baixo que corresponde a

 qualquer uma das sementes iniciais. Para fazer isso, você precisará converter cada número de semente por meio de outras categorias até encontrar seu número de localização correspondente. Neste exemplo, os tipos correspondentes são:

- Semente `79`, solo `81`, fertilizante `81`, água `81`, luz `74`, temperatura `78`, umidade `78`, **localização** `82`.
- Semente `14`, solo `14`, fertilizante `53`, água `49`, luz `42`, temperatura `42`, umidade `43`, **localização** `43`.
- Semente `55`, solo `57`, fertilizante `57`, água `53`, luz `46`, temperatura `82`, umidade `82`, **localização** `86`.
- Semente `13`, solo `13`, fertilizante `52`, água `41`, luz `34`, temperatura `34`, umidade `35`, **localização** `35`.
Portanto, o número de localização mais baixo neste exemplo é `35`.

**Qual é o número de localização mais baixo que corresponde a qualquer uma das sementes iniciais?**