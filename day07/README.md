# --- Dia 7: Camel Cards ---
Sua viagem com todas as despesas pagas acaba sendo uma viagem de ida, de cinco minutos, em um **dirigível**. (Pelo menos é um dirigível **legal**!) Ele o deixa na beira de um vasto deserto e desce de volta para a Ilha Ilha.

"Você trouxe as peças?"

Você se vira para ver um Elfo completamente coberto de roupas brancas, usando óculos de proteção e montado em um grande **camelo**.

"Você trouxe as peças?" ela pergunta novamente, mais alto desta vez. Você não tem certeza de que peças ela está procurando; você está aqui para descobrir por que a areia parou.

"As peças! Para a areia, sim! Venha comigo; eu vou te mostrar." Ela acena para você subir no camelo.

Depois de andar um pouco pelas areias da Ilha do Deserto, você pode ver o que parecem ser rochas muito grandes cobrindo metade do horizonte. A Elfa explica que as rochas estão ao longo da parte da Ilha do Deserto que está diretamente acima da Ilha Ilha, dificultando até mesmo chegar lá. Normalmente, eles usam grandes máquinas para mover as rochas e filtrar a areia, mas as máquinas quebraram porque a Ilha do Deserto parou recentemente de receber as peças de que precisam para consertar as máquinas.

Você já assumiu que será seu trabalho descobrir por que as peças pararam quando ela pergunta se você pode ajudar. Você concorda automaticamente.

Como a jornada levará alguns dias, ela oferece para ensinar a você o jogo de **Cartas de Camelo**. Camel Cards é meio parecido com o pôquer, exceto que é projetado para ser mais fácil de jogar enquanto você está montado em um camelo.

No Camel Cards, você recebe uma lista de **mãos**, e seu objetivo é ordená-las com base na **força** de cada mão. Uma mão consiste em cinco cartas rotuladas como `A`, `K`, `Q`, `J`, `T`, `9`, `8`, `7`, `6`, `5`, `4`, `3` ou `2`. A força relativa de cada carta segue esta ordem, onde `A` é o mais alto e `2` é o mais baixo.

Cada mão é exatamente um **tipo**. Da mais forte para a mais fraca, elas são:

- **Cinco de um tipo**, onde todas as cinco cartas têm o mesmo rótulo: AAAAA
- **Quatro de um tipo**, onde quatro cartas têm o mesmo rótulo e uma carta tem um rótulo diferente: `AA8AA`
- **Casa cheia**, onde três cartas têm o mesmo rótulo, e as duas cartas restantes compartilham um rótulo diferente: `23332`
- **Três de um tipo**, onde três cartas têm o mesmo rótulo, e as duas cartas restantes são diferentes de qualquer outra carta na mão: `TTT98`
- **Dois pares**, onde duas cartas compartilham um rótulo, outras duas cartas compartilham um segundo rótulo, e a carta restante tem um terceiro rótulo: `23432`
- **Um par**, onde duas cartas compartilham um rótulo, e as outras três cartas têm um rótulo diferente do par e entre si: `A23A4`
Carta alta, onde os rótulos de todas as cartas são distintos: `23456`
As mãos são ordenadas principalmente com base no tipo; por exemplo, toda casa cheia é mais forte do que qualquer trinca.

Se duas mãos têm o mesmo tipo, uma segunda regra de ordenação entra em vigor. Comece comparando a **primeira carta de cada mão**. Se essas cartas forem diferentes, a mão com a primeira carta mais forte é considerada mais forte. Se a primeira carta em cada mão tiver o **mesmo rótulo**, no entanto, passe a considerar a **segunda carta de cada mão**. Se elas forem diferentes, a mão com a segunda carta mais alta vence; caso contrário, continue com a terceira carta de cada mão, depois a quarta e, por fim, a quinta.

Assim, `33332` e `2AAAA` são ambas mãos de **quatro de um tipo**, mas `33332` é mais forte porque sua primeira carta é mais forte. Da mesma forma, `77888` e `77788` são ambas uma **casa cheia**, mas `77888` é mais forte porque sua terceira carta é mais forte (e ambas as mãos têm a mesma primeira e segunda cartas).

Para jogar Camel Cards, você recebe uma lista de mãos e seus correspondentes **lances** (sua entrada de quebra-cabeça). Por exemplo:
```
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
```
Este exemplo mostra cinco mãos; cada mão é seguida pelo valor do lance. Cada mão ganha um valor igual ao seu lance multiplicado pela sua classificação, onde a mão mais fraca recebe a classificação 1, a segunda mão mais fraca recebe a classificação 2, e assim por diante até a mão mais forte. Como há cinco mãos neste exemplo, a mão mais forte terá a classificação 5 e seu lance será multiplicado por 5.

Então, o primeiro passo é colocar as mãos em ordem de força:

- `32T3K` é a única **uma dupla** e as outras mãos são de tipos mais fortes, então ela recebe a classificação **1**.
- `KK677` e `KTJJT` são ambos **dois pares**. Suas primeiras cartas têm o mesmo rótulo, mas a segunda carta de `KK677` é mais forte (K vs T), então `KTJJT` recebe a classificação **2** e `KK677` recebe a classificação **3**.
- `T55J5` e `QQQJA` são ambos **trinca**. `QQQJA` tem uma primeira carta mais forte, então ela recebe a classificação **5** e `T55J5` recebe a classificação **4**.

Agora, você pode determinar os ganhos totais deste conjunto de mãos, somando o resultado da multiplicação do lance de cada mão pela sua classificação (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4

 + 483 * 5). **Portanto, os ganhos totais neste exemplo são 6440.**

Descubra a classificação de cada mão em seu conjunto. **Quais são os ganhos totais?**
