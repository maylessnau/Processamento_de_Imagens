import sys #argv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, average_precision_score

# calcula com base na formula
def calcular_ap(precision, recall):
    
    # ordena recall e precision em ordem crescente de recall
    indices_ordenados = recall.argsort()
    recall_ordenado = recall.iloc[indices_ordenados]
    precision_ordenado = precision.iloc[indices_ordenados]

    # inicializa ap_score pra acumular a soma
    ap_score = 0.0

    for i in range(1, len(recall_ordenado)):
        # calcula a diferença de recall
        dif_recall = recall_ordenado.iloc[i] - recall_ordenado.iloc[i-1]
        # acumula na ap_score o produto de delta_recall e precisão no ponto i
        ap_score += dif_recall * precision_ordenado.iloc[i]

    # arredondando casas decimais       
    ap_score_arredondado = round(ap_score, 4)
    return ap_score_arredondado

def plot_precision_recall(csv_file):
    # carregar os dados, pulando a primeira linha (cabeçalho)
    df = pd.read_csv(csv_file, names=["Tamanho", "Threshold", "TP", "FP", "FN", "Precisão", "Recall", "F1-Score"])

    # converter as colunas 'Precisão' e 'Recall' para numérico, caso necessário
    df['Precisão'] = pd.to_numeric(df['Precisão'], errors='coerce')
    df['Recall'] = pd.to_numeric(df['Recall'], errors='coerce')

    # exclui linhas inválidas se houver
    df = df.dropna()

    # extrair as colunas necessárias
    tamanho = df["Tamanho"].iloc[0]
    precision = df["Precisão"]
    recall = df["Recall"]

    # plota a curva Precision-Recall
    plt.figure()
    plt.plot(recall, precision, marker='.', label='Curva P-R')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title(f'Precision-Recall {tamanho}x{tamanho}')
    plt.legend()
    plt.grid()

    # salva arquivo com o gráfico
    output_file = f"precision_recall_{tamanho}.png"
    plt.savefig(output_file)

    # imprime os dados do arquivo .csv 
    print("\n" + "-" * 40 + f" Dados {tamanho}x{tamanho} " + "-" * 40)
    print(df.to_string(index=False, header=True))

    # calcula ap_score
    ap_score = calcular_ap (precision, recall)
    
    return tamanho, ap_score

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <arquivo_csv>")
        sys.exit(1)
    csv_file = sys.argv[1]
    tamanho, ap_score = plot_precision_recall(csv_file)
    tamanho_formatado = f"{tamanho}x{tamanho}"
    print(f"Average Precision (AP) {tamanho_formatado}: {ap_score}")