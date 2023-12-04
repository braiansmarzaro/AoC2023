--- Dia 3: Relações de Engrenagem ---
Você e o Elfo eventualmente chegam a uma estação de **teleférico**; ele diz que o teleférico o levará até a **fonte de água**, mas este é o máximo que ele pode te acompanhar. Vocês entram.

Não demora muito para encontrar as gôndolas, mas parece haver um problema: elas não estão se movendo.

"Aaaah!"

Você se vira para ver um Elfo ligeiramente oleoso com uma chave inglesa e uma expressão de surpresa. "Desculpe, eu não estava esperando ninguém! O teleférico não está funcionando agora; ainda vai demorar um pouco antes que eu possa consertá-lo." Você se oferece para ajudar.

O engenheiro explica que uma parte do motor parece estar faltando, mas ninguém consegue descobrir qual. Se você conseguir **somar todos os números das peças** no esquema do motor, deve ser fácil descobrir qual parte está faltando.

O esquema do motor (sua entrada de quebra-cabeça) consiste em uma representação visual do motor. Há muitos números e símbolos que você não entende muito bem, mas aparentemente **qualquer número adjacente a um símbolo**, até mesmo diagonalmente, é um "número de peça" e deve ser incluído na sua soma. (Pontos (`.`) não contam como símbolos.)

Aqui está um exemplo de esquema do motor:
```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```
Neste esquema, dois números não são números de peças porque não estão adjacentes a um símbolo: `114` (canto superior direito) e `58` (meio direito). Todos os outros números estão adjacentes a um símbolo e, portanto, são números de peças; a soma deles é 4361.

Claro, o esquema real do motor é muito maior. **Qual é a soma de todos os números das peças no esquema do motor?**

# --- Parte Dois ---
O engenheiro encontra a peça que faltava e a instala no motor! À medida que o motor ganha vida, você pula na gôndola mais próxima, finalmente pronto para subir até a fonte de água.

No entanto, você não parece estar indo muito rápido. Talvez ainda haja algo errado? Felizmente, a gôndola tem um telefone rotulado como "ajuda", então você pega o telefone e a engenheira atende.

Antes que você possa explicar a situação, ela sugere que você olhe pela janela. Lá está o engenheiro, segurando um telefone em uma mão e acenando com a outra. Você está se movendo tão lentamente que nem saiu da estação. Você sai da gôndola.

A peça que faltava não foi o único problema - uma das engrenagens no motor está errada. Uma **engrenagem** é qualquer símbolo `*` que é adjacente exatamente a dois números de peça. Sua **relação de engrenagem** é o resultado da multiplicação desses dois números.

Desta vez, você precisa encontrar a relação de engrenagem de cada engrenagem e somar todas elas para que a engenheira possa descobrir qual engrenagem precisa ser substituída.

Considere novamente o mesmo esquema do motor:
```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```
Neste esquema, há **duas** engrenagens. A primeira está no canto superior esquerdo; ela tem números de peça `467` e `35`, então sua relação de engrenagem é `16345`. A segunda engrenagem está no canto inferior direito; sua relação de engrenagem é `451490`. (O `*` adjacente a 617 não é uma engrenagem porque está apenas adjacente a um número de peça.) Somando todas as relações de engrenagem, obtemos **`467835`**.

**Qual é a soma de todas as relações de engrenagem no esquema do seu motor?**