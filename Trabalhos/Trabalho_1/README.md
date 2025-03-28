# **README: Análise de Métricas de Modelos**

Resultados da análise poderão ser encontrados no arquivo "Relatorio.md". Pode abrir com editor de texto mesmo ou acessar meu github (só pra ficar mais apresentável): https://github.com/maylessnau/Processamento_de_Imagens/tree/03b0d97daa44dded977c2bc76b686ed35592efd1/Trabalhos/Trabalho_1 

## **Como Utilizar**

### **Passo 1: Preparação do Ambiente**

Para rodar o script, você precisará de um ambiente Python com as seguintes bibliotecas instaladas:

- **pandas**
- **matplotlib**
- **scikit-learn**

Caso não queira ou não consiga instalar, poderá criar um ambiente virtual.

### **Criar o Ambiente Virtual (opcional, mas recomendado)**

Caso ainda não tenha um ambiente virtual, você pode criar um para isolar as dependências do projeto. Para isso, siga as instruções abaixo:

1. Criação do ambiente virtual:

No terminal, navegue até o diretório do projeto e execute:

```bash
python3 -m venv venv
```

2. Ativação do ambiente virtual:

Se você estiver usando Linux, execute:

```bash
source venv/bin/activate
```
3. Instalar as Bibliotecas

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```bash
pip install pandas matplotlib scikit-learn
```

### **Passo 2: Estrutura de Arquivos**

O script espera que você tenha um arquivo comprimido `Modelos.tar` que contenha arquivos de texto com as métricas dos modelos no mesmo diretório.

1. **Modelos.tar**: Arquivo comprimido contendo os arquivos de métricas (ex: `512.txt`, `608.txt`, `800.txt`).
2. O script criará um diretório chamado **Modelos** para descompactar os arquivos, mas não se preocupa que no fim de tudo ele exclui.

### **Passo 3: Tornando o Script Executável**

Para executar o script, você precisa primeiro garantir que ele seja executável. No terminal, navegue até o diretório onde o script está localizado e execute o seguinte comando:

```bash
chmod +x script.sh
```

Isso dará permissão de execução ao script.

### **Passo 4: Execução do Script**

Após garantir que o script é executável, basta rodá-lo com o seguinte comando:

```bash
./seu_script.sh
```

**Importante**: Sempre execute o script dentro do ambiente virtual que você criou, caso tenha sido necessário. Para garantir que o script use as bibliotecas instaladas no venv, verifique se a venv está ativada antes de rodar o script.

## **O que Acontece ao Executar**

### **Extração e Cálculo das Métricas:**

O script descompacta os arquivos Modelos.tar e calcula métricas como precisão, recall e F1-score para cada conjunto de tamanho de imagem (512, 608, 800). As métricas são salvas em três arquivos CSV: metricas_512.csv, metricas_608.csv e metricas_800.csv.

### **Instalação das Dependências:**

O script garante que todas as dependências Python (pandas, matplotlib, scikit-learn) sejam instaladas.

### **Execução do Código Python para Gráficos e Cálculo do AP:**

O script executa o arquivo plot_e_AP.py que gera png's com os gráficos de Precision-Recall para cada conjunto de métricas e calcula o valor de Average Precision (AP). Nesse momento você poderá ver no terminal todas as métricas calculadas.

### **Exibição dos Gráficos:**

Os gráficos gerados serão exibidos automaticamente na sua máquina.

### **Limpeza:**

O script apaga os arquivos CSV gerados e o diretório Modelos após a execução, mantendo seu ambiente limpo.