# Relatório de Análise de Tamanho de Imagem e Threshold

## Critérios de Avaliação

Vou me basear em três métricas para avaliar o melhor tamanho de imagem e threshold:

1. **F1-score:** Avalia o equilíbrio entre precisão e recall. Um bom modelo deve evitar extremos – alta precisão com recall baixo pode perder casos importantes, enquanto alto recall com precisão baixa gera muitos falsos positivos. O melhor threshold é aquele que maximiza essa métrica (valores mais próximos de 1).

2. **Curva Precision-Recall:** Quanto mais alta e estável, melhor o desempenho. Uma curva elevada indica que o modelo mantém boa precisão mesmo para altos valores de recall, enquanto uma curva instável sugere que a precisão cai rapidamente ao recuperar mais exemplos.

3. **Average Precision (AP):** Mede a área sob a curva PR; valores maiores indicam melhor desempenho geral.

O tamanho de imagem ideal tem a maior **AP** e uma curva **PR** mais estável. O melhor threshold é aquele com o maior **F1-score** dentro desse tamanho.

## Resultados da Análise

- **Imagem 800x800:** Apresentou os maiores valores de **F1-score**, indicando um melhor equilíbrio entre precisão e recall para um threshold fixo. A imagem 800x800 mantém valores altos de **F1-score** por mais tempo antes de começar a decrescer, demonstrando maior estabilidade em diferentes thresholds. Ela apresenta a melhor curva **Precision-Recall**, o que significa que o modelo tem melhor desempenho ao longo de um intervalo de thresholds.

- **Imagem 500x500:** Embora tenha a maior **AP** (0.1562), a imagem 500x500 apresenta uma curva **Precision-Recall** mais instável, o que pode indicar uma queda na precisão ao tentar recuperar mais exemplos. Ela perde para a imagem 800x800 em termos de estabilidade.

- **Imagem 608x608:** Decai rapidamente na curva **Precision-Recall**, tornando-se a opção menos favorável das três, com os menores **F1-scores**. Isso sugere que, embora ela tenha algum desempenho inicial razoável, não mantém a precisão em thresholds mais altos.

## Conclusão

Portanto, a imagem **800x800** é a melhor escolha, pois oferece o maior **F1-score** e uma curva **PR** mais estável, garantindo um desempenho mais consistente.

### Melhor Threshold para 800x800

O melhor **threshold** para a imagem de tamanho **800x800** é **0.75**, pois apresenta o maior **F1-score** (0.8860), indicando um ótimo equilíbrio entre precisão (0.8977) e recall (0.8745). Esse valor garante que quase 90% das previsões positivas estão corretas, ao mesmo tempo em que mantém uma boa taxa de detecção dos verdadeiros positivos. Acima desse threshold, a precisão continua aumentando, mas o recall cai significativamente, reduzindo o **F1-score**. Por outro lado, valores menores favorecem o recall, mas aumentam os falsos positivos.

### Conclusão Final

O melhor tamanho de imagem e threshold é **800x800** e **0.75**, respectivamente.
