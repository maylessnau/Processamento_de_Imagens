# Classificador de Pneumotórax com Comparadores do OpenCV

Este projeto implementa um classificador simples para imagens médicas da base **SIIM Small**, utilizando 4 métodos de comparação disponíveis no OpenCV. O objetivo é avaliar a capacidade dos métodos em distinguir entre imagens com e sem Pneumotórax.

## 📦 Arquivos incluídos

- `trabalho_introducao.ipynb` – Notebook com todo o código fonte do projeto.
- `resultados.txt` – Resultados das métricas (sensibilidade, especificidade) e matrizes de confusão para cada método.

## ⚙️ Instruções de Execução

1. **Abra o arquivo `trabalho_introducao.ipynb` no Google Colab** clicando em `Arquivo` e em seguida em `Fazer upload de notebook`. 
2. Faça o download da base de imagens SIIM Small executando a célula com o comando abaixo:
   ```bash
   !wget -c https://s3.amazonaws.com/fast-ai-imagelocal/siim_small.tgz
   !tar -xvzf siim_small.tgz
   ```
4. Execute todas as células, **uma por vez**, na ordem em que estão conforme o notebook.
5. Ao final, os resultados serão exibidos diretamente no notebook.

## 🧪 Métodos Avaliados

Os seguintes métodos de comparação do OpenCV foram utilizados:

- `CV_COMP_CORREL` – Correlação
- `CV_COMP_CHISQR` – Qui-quadrado
- `CV_COMP_INTERSECT` – Interseção
- `CV_COMP_BHATTACHARYYA` – Distância de Bhattacharyya

## 📊 Avaliação

Para cada imagem, o classificador realiza a comparação com as outras 29, simulando uma abordagem Leave-One-Out. Com isso, são calculadas:

- **Matriz de confusão**
- **Sensibilidade** (True Positive Rate)
- **Especificidade** (True Negative Rate)

A classe **Pneumothorax** é considerada a **classe positiva**.
