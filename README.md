# Aerial Flight Intent Dataset

## Descrição

Este dataset contém vídeos classificados de aviões, drones e helicópteros, com o objetivo de identificar diferentes intenções de voo. A classificação manual dos vídeos resultou em um total de 818 segmentos de vídeo, distribuídos entre os três tipos de agentes aéreos. Este dataset é uma base valiosa para o desenvolvimento e treinamento de algoritmos de aprendizado de máquina voltados para a classificação das intenções de voo.

## Estrutura do Dataset

O dataset está organizado em diferentes classes, onde cada classe corresponde a um tipo específico de movimento ou estado dos agentes aéreos (aviões, drones e helicópteros). Cada classe tem sua própria pasta, que contém os vídeos associados a essa classe. Os arquivos de vídeo e seus respectivos arquivos CSV são nomeados seguindo um padrão específico para facilitar a identificação e a organização.

### Organização dos Diretórios

- **avioes/**: Contém vídeos de aviões.
  - **Subindo/**: Contém vídeos e arquivos CSV de aviões subindo.
  - **Descendo/**: Contém vídeos e arquivos CSV de aviões descendo.
  - **Outras classes**: Pastas adicionais para cada classe de movimento ou estado.
- **drones/**: Contém vídeos de drones.
  - **Voando/**: Contém vídeos e arquivos CSV de drones voando.
  - **Outras classes**: Pastas adicionais para cada classe de movimento ou estado.
- **helicopteros/**: Contém vídeos de helicópteros.
  - **Pairando/**: Contém vídeos e arquivos CSV de helicópteros pairando.
  - **Outras classes**: Pastas adicionais para cada classe de movimento ou estado.

### Padrões de Nomeação

Os arquivos de vídeo e seus respectivos arquivos CSV seguem o padrão:

agenteAereo.classe.numeracao.extensao


- `<tipo>`: Tipo de agente aéreo (drone, aviao, helicop)
- `<classe>`: Classe do vídeo
- `<numeracao>`: Número sequencial
- `<extensao>`: Extensão do arquivo (.mp4 para vídeos, .csv para metadados)

### Metadados

Os vídeos foram anotados para incluir os seguintes metadados essenciais:

- Nome do Arquivo
- Tamanho do Arquivo
- Data de Modificação
- Duração
- Classe

Os metadados são armazenados no arquivo `metadata.csv` no diretório base do dataset.

### Arquivos CSV de Detecção de Objetos

Cada vídeo passou por uma rede de detecção de objetos que gerou arquivos CSV contendo:

- Video Name
- Frame ID
- Object ID
- Class ID
- Class Name
- Confidence
- BoundingBox_X
- BoundingBox_Y
- BoundingBox_Width
- BoundingBox_Height

## Especificações Técnicas

- **Número total de vídeos:** 818
- **Taxa de quadros (FPS):** 30
- **Resolução média:** 1920x1080 pixels
- **Duração de cada segmento:** 10 segundos

### Quantidade de Segmentos por Tipo de Agente Aéreo

| Tipo de Agente Aéreo | Quantidade Total de Segmentos |
|----------------------|-------------------------------|
| Drones               | 272                           |
| Aviões               | 417                           |
| Helicópteros         | 129                           |

### Quantidade de Segmentos por Classe

| Classe             | Drones | Aviões | Helicópteros | Total |
|--------------------|--------|--------|--------------|-------|
| Subindo            | 24     | -      | -            | 24    |
| Descendo           | 22     | -      | -            | 22    |
| Voando - Frente    | 13     | 31     | 5            | 49    |
| Voando - Trás      | 27     | 6      | 42           | 75    |
| Voando - Direita   | 17     | 3      | 7            | 27    |
| Voando - Esquerda  | 26     | 3      | 4            | 33    |
| Parado             | 18     | 51     | 8            | 77    |
| Pairando           | 56     | -      | 6            | 62    |
| Mudança de Trajetória | 68  | -      | -            | 68    |
| Taxiando           | -      | 292    | 14           | 306   |
| Pousando           | -      | 54     | 14           | 68    |
| Decolando          | -      | 28     | 29           | 57    |

## Como Utilizar

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/ingridportilho23/AerialFlightIntent.git
    ```

2. **Acesse o diretório do dataset:**

    ```bash
    cd AerialFlightIntent
    ```

3. **Utilize os vídeos e os arquivos CSV para treinar e avaliar seus algoritmos de aprendizado de máquina.**

## Referência

Se utilizar este dataset em sua pesquisa, por favor cite este repositório:

@dataset{aerial_flight_intent_2024,
author = {Ingrid Portilho and Sanderson de Oliveira Macedo},
title = {Aerial Flight Intent Dataset},
year = {2024},
url = {https://github.com/ingridportilho23/AerialFlightIntent}
}


## Licença

Este dataset é disponibilizado sob a licença [MIT](LICENSE).



