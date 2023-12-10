# Dia 9: Manutenção do Oásis

[https://adventofcode.com/2023/day/9](https://adventofcode.com/2023/day/9)

## Descrição

### Parte Um

Você cavalga o camelo através da tempestade de areia e para onde os mapas do fantasma disseram para parar. <span title="O som de uma tempestade de areia se dissipando lentamente.">A tempestade de areia subsequentemente diminui, de alguma forma revelando você de pé em um <em>oásis</em>!</span>

O camelo vai pegar água e você estica o pescoço. Enquanto olha para cima, você descobre o que deve ser mais uma ilha flutuante gigante, esta feita de metal! Deve ser de lá que vêm as _peças para consertar as máquinas de areia_.

Há até um [asa-delta](https://en.wikipedia.org/wiki/Hang_gliding) parcialmente enterrado na areia aqui; uma vez que o sol se levante e aqueça a areia, você pode ser capaz de usar a asa-delta e o ar quente para chegar até a ilha de metal!

Enquanto espera o sol nascer, você admira o oásis escondido aqui no meio da Ilha do Deserto. Deve ter um ecossistema delicado; você pode muito bem fazer algumas leituras ecológicas enquanto espera. Talvez você possa relatar quaisquer instabilidades ambientais que encontrar para que o oásis possa estar por aqui para o próximo viajante desgastado pela tempestade de areia.

Você pega o seu prático _Sensor de Instabilidade do Oásis e da Areia_ e analisa seus arredores. O OASIS produz um relatório de muitos valores e como eles estão mudando ao longo do tempo (sua entrada de quebra-cabeça). Cada linha no relatório contém a _história_ de um único valor. Por exemplo:

    0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45
    

Para proteger melhor o oásis, seu relatório ambiental deve incluir uma _previsão do próximo valor_ em cada história. Para fazer isso, comece fazendo uma nova sequência a partir da _diferença em cada passo_ de sua história. Se essa sequência _não_ for toda de zeros, repita este processo, usando a sequência que você acabou de gerar como a sequência de entrada. Uma vez que todos os valores em sua última sequência são zeros, você pode extrapolar qual deve ser o próximo valor da história original.

No conjunto de dados acima, a primeira história é `0 3 6 9 12 15`. Como os valores aumentam `3` a cada passo, a primeira sequência de diferenças que você gera será `3 3 3 3 3`. Observe que esta sequência tem um valor a menos do que a sequência de entrada porque em cada passo ela considera dois números da entrada. Como esses valores não são _todos zero_, repita o processo: os valores diferem `0` em cada passo, então a próxima sequência é `0 0 0 0`. Isso significa que você tem informações suficientes para extrapolar a história! Visualmente, essas sequências podem ser organizadas assim:

    0   3   6   9  12  15
      3   3   3   3   3
        0   0   0   0
    

Para extrapolar, comece adicionando um novo zero ao final da sua lista de zeros; como os zeros representam diferenças entre os dois valores acima deles, isso também significa que agora há um espaço reservado em cada sequência acima deles:

    0   3   6   9  12  15   B
      3   3   3   3   3   A
        0   0   0   0   0
    

Você pode então começar a preencher os espaços reservados de baixo para cima. `A` precisa ser o resultado de aumentar `3` (o valor à sua esquerda) por `0` (o valor abaixo dela); isso significa que `A` deve ser _`3`_:

    0   3   6   9  12  15   B
      3   3   3   3   3   3
        0   0   0   0   0
    

Finalmente, você pode preencher `B`, que precisa ser o resultado de aumentar `15` (o valor à sua esquerda) por `3` (o valor abaixo dela), ou _`18`_:

    0   3   6   9  12  15  18
     

 3   3   3   3   3   3
        0   0   0   0   0
    

Portanto, o próximo valor da primeira história é _`18`_.

Encontrar diferenças todos-zero para a segunda história requer uma sequência adicional:

    1   3   6  10  15  21
      2   3   4   5   6
        1   1   1   1
          0   0   0
    

Então, seguindo o mesmo processo que antes, descubra o próximo valor em cada sequência de baixo para cima:

    1   3   6  10  15  21  28
      2   3   4   5   6   7
        1   1   1   1   1
          0   0   0   0
    

Portanto, o próximo valor da segunda história é _`28`_.

A terceira história requer ainda mais sequências, mas seu próximo valor pode ser encontrado da mesma forma:

    10  13  16  21  30  45  68
       3   3   5   9  15  23
         0   2   4   6   8
           2   2   2   2
             0   0   0
    

Portanto, o próximo valor da terceira história é _`68`_.

Se você encontrar o próximo valor para cada história neste exemplo e somá-los, obterá _`114`_.

Analise seu relatório OASIS e extrapole o próximo valor para cada história. _Qual é a soma desses valores extrapolados?_