# Análise de Dados com Python [T2]

## Mini-Projeto Avaliativo - Módulo 1 - Semana 07

### Aluno: Eric Felipe Barros Marques
### Turma: Análise de Dados com Python [T2]

### 1. CONTEXTUALIZAÇÃO

Você está desenvolvendo uma Análise Exploratória de Dados (AED) aplicada ao varejo para aprender como transformar dados brutos em informações úteis.

A base “Varejo” contém registros reais de compras (datas, clientes, produtos, categorias e valores). Aprender a verificar qualidade, limpar e sumarizar esses dados é uma habilidade prática essencial para quem trabalha com BI e Visualização de Dados.<br>
Neste mini-projeto você vai praticar tarefas comuns no trabalho: identificar problemas nos dados (valores nulos, tipos incorretos, duplicados), tratar esses problemas com ferramentas como pandas e gerar estatísticas  simples e funções de agrupamento, para responder perguntas operacionais (quem compra mais, quais categorias vendem mais, como variam as vendas ao longo do tempo).

O objetivo educacional é que, ao final, você saiba preparar uma base para análises mais avançadas ou para alimentar um dashboard: entender os dados, limpá-los, extrair estatísticas descritivas e comunicar os principais insights de forma objetiva.

 
### 2. DESAFIO

Entregar um script em Python que realize uma **Análise Exploratória** da base Varejo seguindo etapas claras, documentadas e reproduzíveis.

#### Etapas obrigatórias

- Carregar a base Varejo.csv com pandas e mostrar: número de registros, colunas e tipos de dados
- Verificar e reportar ao menos dois problemas básicos: valores nulos por coluna, duplicatas, possíveis inconsistências( ex.: datas inválidas ou categorias vazias)
- Fazer as três etapas de limpeza mínima necessária: remover ou imputar nulos (explicar a escolha), eliminar duplicatas relevantes e ajustar tipos de dados (ex.: converter coluna DATA para datetime)
- Gerar estatísticas descritivas básicas para a coluna de número de filhos do cliente (média, mediana, desvio padrão, moda, máximo, mínimo, contagem, quartis)
- Explorar padrões de agrupamento **com pelo menos dois agrupamentos** (por exemplo: gênero com mais vendas, compras), usando groupby() ou pivot_table().
- Produzir um pequeno bloco de conclusões **(3–6 tópicos)** com os principais insights obtidos e possíveis problemas remanescentes na base.

#### Requisitos técnicos mínimos

- O script deve ser executável em VsCode ou Google Colab (arquivo .py).

- Usar pandas; outras bibliotecas são opcionais (NumPy, Matplotlib, Seaborn).

Base de dados sugerida - Kaggle: <br>
[https://www.kaggle.com/datasets/namespaiva/base-varejo/data](https://www.kaggle.com/datasets/namespaiva/base-varejo/data)


### 3. RESULTADOS ESPERADOS (ENTREGA)

Para que sua avaliação seja concluída com sucesso, você deve entregar:
1. **Código-Fonte (Python)**: Um arquivo .py ou link do **Google Colab** contendo a lógica desenvolvida. O código deve estar comentado, explicando o que cada bloco de lógica realiza.
1. **Repositório no GitHub**: O projeto deve ser enviado para um repositório público no GitHub. Espera-se que: 
    - O repositório tenha um arquivo **README.md** básico explicando o projeto.
    - O histórico de commits demonstre o progresso do trabalho (não envie tudo em um único commit final!).

1. Arquivo **README_NomeDoAluno_Turma.md**, com instruções simples (ex.: "Abra no VsCode ou Colab e rode todas as células" ou "python Miniprojeto_…py").
1. Os arquivos com a solução do mini-projeto deverão ser inseridos no **Repositório GitHub da turma em modo público** dentro de uma pasta com o próprio nome do aluno (seguindo o padrão **Miniprojeto_NomeDoAluno_Turma**).
1. O **link do Repositório GitHub** deverá ser submetido na tarefa **Módulo 1 - Mini-Projeto Avaliativo**, presente na semana 07 do AVA até o dia **01/06/2026 às 12h**.



### 4. REQUISITOS DAS TAREFAS

Neste item devem ser listadas tarefas em formato de Sprint para que os estudantes possam realizar durante o período de execução do Mini-projeto Avaliativo. Seguindo as orientações e critérios disponibilizados neste arquivo.

- **Sprint 1 (Importação dos dados)**: Realização da importação dos dados na plataforma Kaggle para a IDE VsCode ou Colab, onde  o script  será executado.

- **Sprint 2 (Transformação de Strings, Integer e Float e Datetime)**: Desenvolvimento das funções de limpeza de texto, inteiros e decimais usando métodos e expressões regulares.

- **Sprint 3 (Limpeza de Nulos e Duplicatas)**: Aplicação das condicionais e funções  para identificação e substituição de valores vazios e  de str para valores de data tipo datetime, na tabela de varejo. 

- **Sprint 4 (Estatística Descritiva)**: Aplicação das funções estatísticas para coletar parâmetros da coluna de Número de filhos do cliente.

- **Sprint 5 (Relatório e Documentação)**: Construção dos contadores do relatório final exibido no terminal, finalização do README.md com a reflexão teórica e submissão do link no AVA.

- **Sprint 6 (Versionamento)**: Envio dos arquivos (script + <u>README.md</u> + df_limpo), via Git para o repositório da turma no GitHub



### 5. CRITÉRIOS DE AVALIAÇÃO

A tabela abaixo apresenta os critérios que serão avaliados durante a correção do projeto. O mesmo possui variação de nota de 0 (zero) a 10 (dez) como nota mínima e máxima, e possui peso de **25% sobre a avaliação do módulo**.

Serão desconsiderados e atribuída a nota 0 (zero) os projetos que apresentarem plágio de soluções encontradas na internet ou de outros colegas. Lembre-se: Você está livre para utilizar outras soluções como base, mas não é permitida a cópia.

----

### Documentação do Projeto (2,50)
<table>
  <thead>
    <tr>
        <th>Nº</th>
        <th>Critério de Avaliação</th>
        <th>0</th>
        <th>1,25</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>1</td>
        <td>Versionamento</td>
        <td>Não entregou o repositório no GitHub contendo os arquivos organizados e um README.md explicativo com a reflexão teórica obrigatória sobre ETL e qualidade de dados.</td>
        <td>Entregou o repositório no GitHub contendo os arquivos organizados e um README.md explicativo com a reflexão teórica obrigatória sobre ETL e qualidade de dados.</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Documentação</td>
        <td>Não desenvolveu Arquivo README.md contendo de 3-6 tópicos com insights obtidos da análise dos dados.</td>
        <td>Desenvolveu Arquivo README.md contendo de 3-6 tópicos com insights obtidos da análise dos dados.</td>
    </tr>
  </tbody>
</table>

### Desenvolvimento do Projeto (7,50)

<table>
  <thead>
    <tr>
        <th>Nº</th>
        <th>Critério de Avaliação</th>
        <th>0</th>
        <th>0,75</th>
        <th>1,50</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>3</td>
        <td>Manipulação de Arquivos CSV</td>
        <td>Não realizou a leitura e extração dos arquivos de dados de forma parcialmente estruturada (csv.DictReader).</td>
        <td>Realizou a leitura e extração dos arquivos de dados de forma parcialmente estruturada (csv.DictReader).</td>
        <td>Realizou a leitura e extração dos arquivos de dados de forma estruturada e nativa (csv.DictReader).</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Tratamento de Nulos e Condicionais</td>
        <td>Não implementou a lógica (if/else) para preencher categorias vazias com "Sem Categoria" e não tratou os nulos das dimensões físicas, justificando a escolha.</td>
        <td>Implementou parcialmente a lógica (if/else) para preencher categorias vazias com "Sem Categoria" e tratou parcialmente os nulos das dimensões físicas, justificando a escolha.</td>
        <td>Implementou a lógica (if/else) para preencher categorias vazias com "Sem Categoria" e tratou corretamente os nulos das dimensões físicas, justificando a escolha.</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Regras de Negócio e Datas</td>
        <td>Não validou a regra do identificador de número de compra separando os registros, e converteu parcialmente a string de data da compra utilizando o módulo datetime.</td>
        <td>Validou parcialmente a regra do identificador de número de compra separando os registros, e converteu parcialmente a string de data da compra utilizando o módulo datetime.</td>
        <td>Validou a regra do identificador de número de compra, e converteu com sucesso a string de data da compra utilizando o módulo datetime.</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Padrões de Agrupamento</td>
        <td>Não explorou padrões de agrupamento com pelo menos duas combinações.</td>
        <td>Explorou parcialmente padrões de agrupamento com uma combinação.</td>
        <td>Explorou padrões de agrupamento com pelo menos duas combinações.</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Geração de Estatísticas Básicas</td>
        <td>Não gerou as estatísticas básicas de acordo com a coluna Número de filhos dos clientes, não contemplando os parâmetros elencados</td>
        <td>Gerou parcialmente as estatísticas básicas de acordo com a coluna Número de filhos dos clientes, contemplando parte dos parâmetros elencados</td>
        <td>Gerou as estatísticas básicas de acordo com a coluna Número de filhos dos clientes, contemplando todos os parâmetros elencados</td>
    </tr>
  </tbody>
</table>



### 6. Execussão do projeto
#### Importação da base de dados

Para a importação da base de dados, pode-se efetuar de duas formas:

1. Download dos arquivos via API onde deve-se proceder da seguinte maneira:
    - Para que seja possível utilizar a API do Kaggle, é necessário que você já possua uma conta no site.
    - Após ter uma conta válida, com acesso à API, deve-se inderir as informações no arquivo `.env` que deve ficar localizado na raiz do projeto.
    - Caso seja utilizada a API da Kaggle para o download do arquivo base, antes de executar o script do projeto, no terminal deve-se executar o comando `kaggle auth login`. Será soolicitado que você se autentique na plataforma Kaggle 

1. Dowlnoad manual do arquivo base.
    - Adicionar o arquivo .csv ao diretório `data/raw`, que é o local onde o script irá procurar o arquivo para leitura e posterior tratamentos

#### Executção do projeto
Primeiramente deve-se instalar as dependências utilizando o comando `pip install requirements.txt`
Para executar o script que dará início ao tratamento dos dados, na raiz do projeto, deve-se executar no terminal o comando `python -m main` 

### Tecnologias utilizadas
- Python
- Pandas

### Limpeza de Dados
Para a limpeza dos dados foram efetuados os seguintes procedimentos:

- Remoção de colunas totalmente vazias (Unnamed: 10 - 13);
- Identificação e remoção de registros duplicados;
- Limpeza de linhas onde as colunas PR_CAT e PR_NOME possuíam valor #N/D
- Conversão das informações da coluna `data` de string para date.
- Padronização dos textos das colunas PR_CAT e PR_NOME pata str.title


## Análise Exploratória doas dados da base `Base Varejo`

O foco desta análise é identificar possíveis anomalias nos dados, efetuar tratamento  e limpeza destes dados inconsistentes.

A base de dados refere-se a uma relação de compras efetuadas por clientes.

### Análises Exploratórias:
#### Filhos `CL_FHL`
A coluna CL_FHL representa a coluna onde informa a quantidade de filhos onde cada comprador informo possuir.

Tendo os seguintres números:
- Média de 1,15 filhos por compra/cliente
- Quantidade mínima de 0 e mácima de 4 filhos

#### Compras
Analisado o quesito de por gênero `CL_GENERO`, onde a referida coluna representa a informação de gênero(M/F) informados por compra, onde obteve-se os seguintes resultados:
- Feminino: 380735
- Masculino: 349484

Com relação às compras de gêneros X estado civil, obtivemos os seguintes resultados:

<table>
  <thead>
    <tr>
        <th>Nº</th>
        <th>Gênero</th>
        <th>Estado Civil</th>
        <th>Quantidade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>1</td>
        <td>Feminino</td>
        <td>Casado ou União Estável</td>
        <td>79298</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Feminino</td>
        <td>Divorciado</td>
        <td>87869</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Feminino.</td>
        <td>Separado</td>
        <td>100255</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Feminino</td>
        <td>Solteiro</td>
        <td>99579</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Feminino</td>
        <td>Viúvo</td>
        <td>13734</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Masculino</td>
        <td>Casado ou União Estável</td>
        <td>91946</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Masculino</td>
        <td>Divorciado</td>
        <td>83611</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Masculino</td>
        <td>Separado</td>
        <td>87983</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Masculino</td>
        <td>Solteiro</td>
        <td>78851</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Masculino</td>
        <td>Viúvo</td>
        <td>7093</td>
    </tr>
  </tbody>
</table>

A média de itens por copora foi de `39,54`

#### Top 5 itens mais comprados por estado civil.

<table>
  <thead>
    <tr>
      <th>Nº</th>
      <th>Estado Civil</th>
      <th>Produto</th>
      <th>Quantidade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Casado ou União Estável</td>
      <td>Presunto Cozido</td>
      <td>2938</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Casado ou União Estável</td>
      <td>Preservativo</td>
      <td>1605</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Casado ou União Estável</td>
      <td>Cebola</td>
      <td>1589</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Casado ou União Estável</td>
      <td>Sardinha</td>
      <td>1582</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Casado ou União Estável</td>
      <td>Papel Higiênico</td>
      <td>1566</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Divorciado</td>
      <td>Presunto Cozido</td>
      <td>2956</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Divorciado</td>
      <td>Cebola</td>
      <td>1579</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Divorciado</td>
      <td>Removedor</td>
      <td>1568</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Divorciado</td>
      <td>Papel Higiênico</td>
      <td>1567</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Divorciado</td>
      <td>Desengordurante</td>
      <td>1559</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Separado</td>
      <td>Presunto Cozido</td>
      <td>3369</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Separado</td>
      <td>Modelador</td>
      <td>1727</td>
    </tr>
    <tr>
      <td>13</td>
      <td>Separado</td>
      <td>Chupeta</td>
      <td>1717</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Separado</td>
      <td>Leite</td>
      <td>1712</td>
    </tr>
    <tr>
      <td>15</td>
      <td>Separado</td>
      <td>Tira Mancha</td>
      <td>1710</td>
    </tr>
    <tr>
      <td>16</td>
      <td>Solteiro</td>
      <td>Presunto Cozido</td>
      <td>3104</td>
    </tr>
    <tr>
      <td>17</td>
      <td>Solteiro</td>
      <td>Detergente</td>
      <td>1657</td>
    </tr>
    <tr>
      <td>18</td>
      <td>Solteiro</td>
      <td>Papinha Infantil</td>
      <td>1654</td>
    </tr>
    <tr>
      <td>19</td>
      <td>Solteiro</td>
      <td>Banana</td>
      <td>1642</td>
    </tr>
    <tr>
      <td>20</td>
      <td>Solteiro</td>
      <td>Mamão</td>
      <td>1636</td>
    </tr>
    <tr>
      <td>21</td>
      <td>Viúvo</td>
      <td>Presunto Cozido</td>
      <td>352</td>
    </tr>
    <tr>
      <td>22</td>
      <td>Viúvo</td>
      <td>Lustra Móveis</td>
      <td>208</td>
    </tr>
    <tr>
      <td>23</td>
      <td>Viúvo</td>
      <td>Manga</td>
      <td>208</td>
    </tr>
    <tr>
      <td>24</td>
      <td>Viúvo</td>
      <td>Rodo</td>
      <td>205</td>
    </tr>
    <tr>
      <td>25</td>
      <td>Viúvo</td>
      <td>Shampoo</td>
      <td>205</td>
    </tr>
  </tbody>
</table>

#### Média de itens por classe social.

<table>
  <thead>
    <tr>
      <th>Nº</th>
      <th>Classe Econômica</th>
      <th>Média de Itens por Compra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>A</td>
      <td>39.82</td>
    </tr>
    <tr>
      <td>2</td>
      <td>C</td>
      <td>39.79</td>
    </tr>
    <tr>
      <td>3</td>
      <td>B</td>
      <td>39.39</td>
    </tr>
  </tbody>
</table>