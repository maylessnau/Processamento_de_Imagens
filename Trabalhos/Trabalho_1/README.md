# **README: Análise de Métricas de Modelos**

## **Como Utilizar**

### **Passo 1: Preparação do Ambiente**

Vamos precisar de três bibliotecas instaladas:

- **pandas**
- **matplotlib**
- **scikit-learn**

O script irá (ou tentará) verificar automaticamente se essas bibliotecas estão instaladas e, se necessário, as instalará (em modo --user).

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