--- Dia 6: Espere Por Isso ---
A balsa rapidamente leva você através da Ilha da Ilha. Depois de perguntar por aí, você descobre que normalmente há de fato uma grande pilha de areia em algum lugar aqui, mas você não vê nada além de muita água e da pequena ilha onde a balsa atracou.

Enquanto tenta descobrir o que fazer a seguir, você nota um cartaz em uma parede perto da doca da balsa. "Corridas de barco! Abertas ao público! O prêmio principal é uma viagem com todas as despesas pagas para a **Ilha do Deserto**!" Deve ser de onde vem a areia! E o melhor de tudo, as corridas de barco estão começando em apenas alguns minutos.

Você consegue se inscrever como competidor nas corridas de barco bem a tempo. O organizador explica que não é realmente uma corrida tradicional - em vez disso, você terá um tempo fixo durante o qual seu barco deve viajar o máximo que puder, e você vence se seu barco for o mais longe possível.

Ao se inscrever, você recebe uma folha de papel (sua entrada de quebra-cabeça) que lista o **tempo** permitido para cada corrida e também a melhor **distância** já registrada naquela corrida. Para garantir que você ganhe o grande prêmio, você precisa garantir que você vá mais longe em cada corrida do que o atual detentor do recorde.

O organizador o leva para a área onde as corridas de barco são realizadas. Os barcos são muito menores do que você esperava - na verdade, são **barcos de brinquedo**, cada um com um grande botão em cima. Manter pressionado o botão **carrega o barco**, e soltar o botão **permite que o barco se mova**. Os barcos se movem mais rápido se o botão for mantido por mais tempo, mas o tempo gasto segurando o botão conta contra o tempo total da corrida. Você só pode manter o botão no início da corrida, e os barcos não se movem até que o botão seja liberado.

Por exemplo:
``` yaml
Tempo:      7  15   30
Distância:  9  40  200
```
Este documento descreve três corridas:

- A primeira corrida dura 7 milissegundos. A distância recorde nesta corrida é de 9 milímetros.
- A segunda corrida dura 15 milissegundos. A distância recorde nesta corrida é de 40 milímetros.
- A terceira corrida dura 30 milissegundos. A distância recorde nesta corrida é de 200 milímetros.

Seu barco de brinquedo tem uma velocidade inicial de **zero milímetros por milissegundo**. Para cada milissegundo inteiro que você passa no início da corrida mantendo pressionado o botão, a velocidade do barco aumenta em **um milímetro por milissegundo**.

Portanto, como a primeira corrida dura 7 milissegundos, você só tem algumas opções:

- Não segure o botão (ou seja, mantenha-o pressionado por **`0` milissegundos**) no início da corrida. O barco não se moverá; ele terá percorrido 0 milímetros até o final da corrida.
- Segure o botão por 1 milissegundo no início da corrida. Em seguida, o barco se moverá a uma velocidade de 1 milímetro por milissegundo por 6 milissegundos, alcançando uma distância total percorrida de 6 **milímetros**.
- Segure o botão por 2 **milissegundos**, dando ao barco uma velocidade de 2 **milímetros** por milissegundo. Em seguida, ele terá 5 **milissegundos** para se mover, alcançando uma distância total de 10 **milímetros**.
- Segure o botão por 3 **milissegundos**. Após seus restantes 4 **milissegundos** de tempo de viagem, o barco terá percorrido 12 **milímetros**.
- Segure o botão por 4 **milissegundos**. Após seus restantes 3 **milissegundos** de tempo de viagem, o barco terá percorrido 12 **milímetros**.
- Segure o botão por 5 **milissegundos**, fazendo com que o barco percorra um total de 10 **milímetros**.
- Segure o botão por 6 **milissegundos**, fazendo com que o barco percorra um total de 6 **milímetros**.
- Segure o botão por 7 **milissegundos**. Esse é o tempo total da corrida. Você nunca solta o botão. O barco não pode se mover até que você solte o botão. Por favor, certifique-se de soltar o botão para que o barco possa se mover. **`0` milímetros**.

Como o recorde atual para esta corrida é de 9 milímetros, há na verdade 4 maneiras diferentes de vencer: você pode segurar o botão por 2, 3, 4 ou 5 milissegundos no início da corrida.

Na segunda corrida, você pode segurar o botão por pelo menos 4 milissegundos e no máximo `11` milissegundos e vencer o recorde, um total de **`8`** maneiras diferentes de vencer.

Na terceira corrida, você pode segurar o botão por pelo menos `11` milissegundos e no máximo `19` milissegundos e ainda vencer o recorde, um total de **`9`** maneiras de vencer.

Para ver quanto de margem de erro você tem, determine o número de maneiras que você **pode vencer o recorde** em cada corrida; neste exemplo, se você multiplicar esses valores juntos, você obtém **288** (`4 * 8 * 9`).

Determine o número de maneiras que você poderia vencer o recorde em cada corrida. **O que você obtém ao multiplicar esses números?**

# Parte 2
