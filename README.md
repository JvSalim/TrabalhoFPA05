# Projeto FloodFill: Colorindo Regiões de um Terreno com Obstáculos

## Descrição do Projeto

Este projeto implementa o algoritmo Flood Fill para identificar e preencher automaticamente regiões conectadas em um grid bidimensional. O sistema é projetado para simular o mapeamento inteligente de terrenos para robôs autônomos, onde cada célula do grid pode ser um espaço livre (navegável) ou um obstáculo. O objetivo principal é "colorir" todas as áreas livres conectadas, facilitando a visualização e o planejamento de rotas para os robôs.

## Introdução ao Problema

O problema abordado neste projeto envolve a identificação e o preenchimento de regiões conectadas em um grid 2D. Em cenários de mapeamento de terreno, é crucial distinguir áreas navegáveis de obstáculos e, dentro das áreas navegáveis, identificar regiões contíguas. O algoritmo Flood Fill é uma solução clássica para esse tipo de problema, permitindo a propagação de uma "cor" (ou valor) por todas as células conectadas a um ponto inicial, respeitando as barreiras.

Neste contexto, o grid é composto por células que podem ter os seguintes valores:

*   `0`: Terreno navegável (espaço livre, a ser preenchido).
*   `1`: Obstáculo (não navegável, impede a propagação do preenchimento).
*   `2, 3, 4, ...`: Cores já preenchidas em outras regiões.

O algoritmo começa a partir de uma célula inicial (`x`, `y`) e se propaga para todas as células adjacentes (ortogonalmente: acima, abaixo, à esquerda e à direita) que possuem o valor `0`. À medida que as células são visitadas, seu valor é alterado para uma nova cor, indicando que aquela região foi preenchida. O processo continua até que todas as células navegáveis conectadas à célula inicial sejam preenchidas. Após o preenchimento de uma região, o programa busca automaticamente a próxima célula navegável (`0`) não preenchida e inicia um novo processo de Flood Fill com uma cor diferente, garantindo que todo o terreno seja mapeado e colorido.

## Como Configurar e Executar o Projeto

Para configurar e executar este projeto, siga os passos abaixo:

1.  **Pré-requisitos:**
    *   Python 3.x instalado em seu sistema.

2.  **Download do Código:**
    *   Baixe o arquivo `main.py` para o seu diretório de trabalho.

3.  **Execução:**
    *   Abra um terminal ou prompt de comando.
    *   Navegue até o diretório onde você salvou o arquivo `main.py`.
    *   Execute o script Python usando o seguinte comando:

        ```bash
        python3 main.py
        ```

    *   O programa irá imprimir no console os grids iniciais e os grids preenchidos para os exemplos fornecidos.

## Explicação do Algoritmo Flood Fill Implementado

A implementação do algoritmo Flood Fill neste projeto utiliza uma abordagem recursiva para percorrer o grid. A função principal `flood_fill(grid, x, y, new_color, original_color)` é responsável por preencher uma única região conectada. Ela funciona da seguinte forma:

1.  **Condições de Parada:**
    *   Verifica se as coordenadas (`x`, `y`) estão fora dos limites do grid.
    *   Verifica se a célula atual já foi preenchida com uma cor diferente da `original_color` (ou seja, já faz parte de outra região preenchida ou é um obstáculo).
    *   Verifica se a célula atual é um obstáculo (`1`).
    Se qualquer uma dessas condições for verdadeira, a função retorna, impedindo a propagação do preenchimento.

2.  **Preenchimento:**
    *   Se as condições de parada não forem atendidas, a célula atual (`grid[x][y]`) é preenchida com a `new_color`.

3.  **Chamadas Recursivas:**
    *   A função então faz chamadas recursivas para as quatro células adjacentes (acima, abaixo, à esquerda e à direita) da célula atual. Isso garante que o preenchimento se propague por toda a região conectada.

A função `find_and_fill_all_regions(grid, start_color=2)` é responsável por iterar sobre todo o grid e garantir que todas as regiões navegáveis sejam preenchidas. Ela faz isso da seguinte maneira:

1.  Percorre cada célula do grid.
2.  Se encontra uma célula com valor `0` (terreno navegável não preenchido), ela chama a função `flood_fill` para iniciar o preenchimento dessa região com a `current_color`.
3.  Após o preenchimento de uma região, a `current_color` é incrementada para garantir que a próxima região encontrada seja preenchida com uma cor diferente.

Este processo continua até que todas as células navegáveis (`0`) do grid tenham sido identificadas e preenchidas.

## Exemplos de Entrada e Saída

Para ilustrar o funcionamento do projeto, apresentamos dois exemplos claros de entrada e saída, utilizando grids de diferentes tamanhos e configurações.

### Exemplo 1

**Grid Inicial:**
```
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
```

**Coordenadas Iniciais:** (0, 0)

**Grid Preenchido:**
```
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```

### Exemplo 2

**Grid Inicial:**
```
0 1 0 0 1
0 1 0 0 1
0 1 1 1 1
0 0 0 1 0
```

**Coordenadas Iniciais:** (0, 2)

**Grid Preenchido:**
```
2 1 3 3 1
2 1 3 3 1
2 1 1 1 1
2 2 2 1 4
```

**Legenda de Cores:**
*   `0` – Branco (Terreno navegável)
*   `1` – Preto (Obstáculo)
*   `2` – Vermelho
*   `3` – Laranja
*   `4` – Amarelo



