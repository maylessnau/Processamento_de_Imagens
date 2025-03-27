import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import auc

def plot_precision_recall(csv_file):

    # mostra a tabela com os valores

    # carregar os dados, pulando a primeira linha (cabeçalho)
    df = pd.read_csv(csv_file, names=["Tamanho", "Threshold", "TP", "FP", "FN", "Precisão", "Recall", "F1-Score"])
    
    # converter as colunas 'Precisão' e 'Recall' para numérico, caso necessário
    df['Precisão'] = pd.to_numeric(df['Precisão'], errors='coerce')
    df['Recall'] = pd.to_numeric(df['Recall'], errors='coerce')

    # exclui linhas inválidas se houver
    df = df.dropna()

    # mostra a tabela com os valores
    print(df.to_string()) 
    
    # extrai as colunas necessárias
    tamanho = df["Tamanho"].iloc[0]
    thresholds = df["Threshold"]
    precision = df["Precisão"]
    recall = df["Recall"]
    
    # calcular AUC da curva Precision-Recall
    auc_pr = auc(recall, precision)
    
    # criando o gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(thresholds, precision, marker='o', label='Precisão', linestyle='-')
    plt.plot(thresholds, recall, marker='s', label='Recall', linestyle='--')
    plt.xlabel("Threshold")
    plt.ylabel("Valor")
    plt.title(f"Precision-Recall - {tamanho} (AUC = {auc_pr:.4f})")
    plt.legend()
    plt.grid()
    
    output_file = f"precision_recall_{tamanho}.png"
    plt.savefig(output_file)

    return tamanho, auc_pr

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <arquivo_csv>")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    tamanho, auc_value = plot_precision_recall(csv_file)
    tamanho_formatado = f"{tamanho}x{tamanho}"
    print(f"AUC da Precision-Recall {tamanho_formatado}: {auc_value:.4f}")