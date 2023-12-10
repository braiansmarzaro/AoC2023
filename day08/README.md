# --- Dia 8: Deserto Assombrado ---
Você ainda está montado em um camelo cruzando a Ilha do Deserto quando avista uma tempestade de areia se aproximando rapidamente. Quando você se vira para avisar a Elfa, ela desaparece diante dos seus olhos! Para ser justo, ela acabara de terminar de avisar você sobre fantasmas alguns minutos atrás.

Uma das bolsas do camelo está rotulada como "mapas" - com certeza, está cheia de documentos (sua entrada de quebra-cabeça) sobre como navegar no deserto. Pelo menos, você tem quase certeza de que é isso que são; um dos documentos contém uma lista de instruções esquerda/direita, e o restante dos documentos parece descrever algum tipo de **rede** de nós rotulados.

Parece que você deve usar as instruções **esquerda/direita** para navegar **na rede**. Talvez, se você fizer com que o camelo siga as mesmas instruções, poderá escapar do deserto assombrado!

Depois de examinar os mapas por um tempo, dois nós se destacam: `AAA` e `ZZZ`. Você sente que `AAA` é onde você está agora, e você deve seguir as instruções **esquerda/direita** até chegar a `ZZZ`.

Este formato define cada **nó** da rede individualmente. Por exemplo:
```
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
```
Começando com `AAA`, você precisa **procurar o próximo elemento** com base na próxima instrução esquerda/direita em sua entrada. Neste exemplo, comece com `AAA` e vá para a **direita** (`R`), escolhendo o elemento à direita de `AAA`, **`CCC`**. Em seguida, L significa escolher o elemento **à esquerda** de `CCC`, `ZZZ`. Seguindo as instruções esquerda/direita, você chega a `ZZZ` em **2** etapas.

Claro, você pode não encontrar `ZZZ` imediatamente. Se ficar sem instruções esquerda/direita, repita toda a sequência de instruções conforme necessário: RL realmente significa `RLRLRLRLRLRLRLRL...` e assim por diante. Por exemplo, aqui está uma situação que leva `6` etapas para chegar a `ZZZ`:
```
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
```
Começando em `AAA`, siga as instruções esquerda/direita. **Quantas etapas são necessárias para chegar a ZZZ?**