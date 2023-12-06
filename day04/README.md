--- Dia 4: Raspadinhas ---
A gôndola te leva para cima. Estranhamente, no entanto, o chão não parece estar subindo com você; você não está subindo uma montanha. À medida que o círculo da Ilha da Neve diminui abaixo de você, um novo bloco de terra surge subitamente acima de você! A gôndola te leva até a superfície da nova ilha e se inclina para a estação.

Ao sair da gôndola, a primeira coisa que você percebe é que o ar aqui é muito mais **quente** do que estava na Ilha da Neve. Também está bastante **úmido**. Será que esta é a fonte de água?

A próxima coisa que você nota é um Elfo sentado no chão do outro lado da estação em um monte de cartões quadrados coloridos.

"Oh! Olá!" O Elfo corre animado até você. "Como posso ser útil?" Você pergunta sobre fontes de água.

"Não tenho certeza; eu só opero o teleférico. Isso parece algo que teríamos, no entanto - esta é a **Ilha Ilha**, afinal de contas! Acho que o **jardineiro** saberá. Ele está em uma ilha diferente, no entanto - ah, do tipo pequeno cercado por água, não o tipo flutuante. Realmente precisamos criar um esquema de nomenclatura melhor. Diz o que: se você puder me ajudar com algo rápido, vou deixar você **pegar emprestado meu barco** e você pode visitar o jardineiro. Recebi todos esses [cartões raspáveis](https://en.wikipedia.org/wiki/Scratchcard) como presente, mas não consigo entender o que ganhei."

O Elfo te leva até o monte de cartões coloridos. Lá, você descobre dezenas de cartões raspáveis, todos com sua cobertura opaca já raspada. Pegando um, parece que cada cartão tem duas listas de números separadas por uma barra vertical (|): uma lista de **números vencedores** e, em seguida, uma lista de **números que você tem**. Você organiza as informações em uma tabela (sua entrada de quebra-cabeça).

Até onde o Elfo conseguiu entender, você tem que descobrir quais dos **números que você tem** aparecem na lista de **números vencedores**. O primeiro acerto torna o cartão valendo **um ponto** e cada acerto após o primeiro duplica o valor daquele cartão.

Por exemplo:
```
Cartão 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Cartão 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Cartão 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Cartão 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Cartão 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Cartão 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```

No exemplo acima, o cartão 1 tem cinco números vencedores (`41`, `48`, `83`, `86` e `17`) e oito números que você tem (`83`, `86`, `6`, `31`, `17`, `9`, `48` e `53`). Dos números que você tem, quatro deles (`48`, `83`, `17` e `86`) são números vencedores! Isso significa que o cartão 1 vale **`8`** pontos (1 pelo primeiro acerto, depois duplicado três vezes para cada um dos três acertos após o primeiro).

O Cartão 2 tem dois números vencedores (`32` e `61`), então vale 2 pontos.
O Cartão 3 tem dois números vencedores (`1` e `21`), então vale 2 pontos.
O Cartão 4 tem um número vencedor (`84`), então vale 1 ponto.
O Cartão 5 não tem números vencedores, então não vale pontos.
O Cartão 6 não tem números vencedores, então não vale pontos.
Assim, neste exemplo, o monte de cartões raspáveis do Elfo vale 13 pontos.

Sente-se no grande monte de cartões coloridos. **Quantos pontos eles valem no total?**

# Parte 2
# --- Parte Dois ---
Assim que você está prestes a relatar suas descobertas para o Elfo, um de vocês percebe que as regras na verdade foram impressas na parte de trás de cada carta o tempo todo.

Não há tal coisa como "pontos". Em vez disso, os cartões de raspadinha só fazem você **ganhar mais cartões de raspadinha** iguais ao número de números vencedores que você tem.

Especificamente, você ganha **cópias** dos cartões de raspadinha abaixo do cartão vencedor igual ao número de correspondências. Portanto, se o cartão 10 tiver 5 números correspondentes, você ganharia uma cópia de cada um dos cartões 11, 12, 13, 14 e 15.

As cópias dos cartões de raspadinha são pontuadas como cartões de raspadinha normais e têm o **mesmo número de cartão** que o cartão que eles copiaram. Então, se você ganhar uma cópia do cartão 10 e ele tiver 5 números correspondentes, ele ganharia então uma cópia dos mesmos cartões que o cartão original 10 ganhou: cartões 11, 12, 13, 14 e 15. Esse processo se repete até que nenhuma das cópias faça você ganhar mais cartões. (Os cartões nunca farão você copiar um cartão além do final da mesa.)

Desta vez, o exemplo acima ocorre de maneira diferente:
```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```
- O Cartão 1 tem quatro números correspondentes, então você ganha uma cópia de cada um dos quatro próximos cartões: cartões 2, 3, 4 e 5.
- Seu cartão original 2 tem dois números correspondentes, então você ganha uma cópia de cada um dos cartões 3 e 4.
- Sua cópia do cartão 2 também ganha uma cópia de cada um dos cartões 3 e 4.
- Suas quatro instâncias do cartão 3 (um original e três cópias) têm dois números correspondentes, então você ganha **quatro** cópias de cada um dos cartões 4 e 5.
- Suas oito instâncias do cartão 4 (um original e sete cópias) têm um número correspondente, então você ganha **oito** cópias do cartão 5.
- Suas quatorze instâncias do cartão 5 (um original e treze cópias) não têm números correspondentes e não ganham mais cartões.
- Sua única instância do cartão 6 (um original) não tem números correspondentes e não ganha mais cartões.
Depois que todos os originais e cópias foram processados, você acaba com `1` instância do cartão 1, `2` instâncias do cartão 2, `4` instâncias do cartão 3, `8` instâncias do cartão 4, `14` instâncias do cartão 5 e `1` instância do cartão 6. No total, esse exemplo de pilha de cartões de raspadinha faz com que você tenha, em última análise, 30 cartões de raspadinha!

Processe todos os cartões de raspadinha originais e copiados até não ganhar mais cartões de raspadinha. **Incluindo o conjunto original de cartões de raspadinha, quantos cartões de raspadinha você acaba tendo?**