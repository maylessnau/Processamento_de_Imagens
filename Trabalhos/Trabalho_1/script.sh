#!/bin/bash

# configura o LC_NUMERIC para forçar o uso de ponto como separador decimal
# pra não zoar o csv com a separação por vírgula
export LC_NUMERIC="C"

# cria um diretório para armazenar os arquivos extraídos
mkdir -p Modelos

# descompactando os arquivos dentro do diretório que criamos
tar -xf Modelos.tar -C Modelos

# cria arquivos de saída
echo "Tamanho,Threshold,TP,FP,FN,Precisão,Recall,F1-Score" > metricas_512.csv
echo "Tamanho,Threshold,TP,FP,FN,Precisão,Recall,F1-Score" > metricas_608.csv
echo "Tamanho,Threshold,TP,FP,FN,Precisão,Recall,F1-Score" > metricas_800.csv

# monta arquivo com todas as métricas
for arquivo in Modelos/*.txt; do

    # extrai o tamanho da imagem do nome do arquivo (512, 608, 800)
    tamanho=$(basename "$arquivo" | grep -o '^[0-9]\+')

    if [ "$tamanho" -eq 512 ]; then
        arquivo_saida="metricas_512.csv"
    elif [ "$tamanho" -eq 608 ]; then
        arquivo_saida="metricas_608.csv"
    elif [ "$tamanho" -eq 800 ]; then
        arquivo_saida="metricas_800.csv"
    fi

    # extrai dados das linhas relevantes e calcular métricas
    awk -v tam="$tamanho" '
    BEGIN {
        # Inicializando variáveis
        threshold = 0;
        TP = 0;
        FP = 0;
        FN = 0;
    }
    {
        # Busca conf_thresh na linha, se achar então extrai os valores
        if ($0 ~ /conf_thresh/) {
            # Extrai cada valor separadamente
            for (i = 1; i <= NF; i++) {
                if ($i == "conf_thresh") { threshold = $(i+2) + 0.0 }
                if ($i == "TP") { TP = $(i+2) + 0 }
                if ($i == "FP") { FP = $(i+2) + 0 }
                if ($i == "FN") { FN = $(i+2) + 0 }
            }

            # Cálculo das métricas verificando se não tem divisão por 0
            precision = (TP + FP == 0) ? 0 : TP / (TP + FP);
            recall = (TP + FN == 0) ? 0 : TP / (TP + FN);
            f1_score = (precision + recall == 0) ? 0 : (2 * precision * recall) / (precision + recall);

            # Salva resultados no CSV
            printf "%s,%.2f,%d,%d,%d,%.4f,%.4f,%.4f\n", tam, threshold, TP, FP, FN, precision, recall, f1_score;
        }
    }' "$arquivo" >> "$arquivo_saida"

done

mkdir -p Graficos

# criar ambiente virtual (se não existir)
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# ativar ambiente virtual
source venv/bin/activate

# garantir que todas as bibliotecas necessárias estão instaladas
pip install --upgrade pip > /dev/null 2>&1
pip install pandas matplotlib scikit-learn > /dev/null 2>&1

# rodar o Python no ambiente virtual
for arquivo in *.csv
do
    python3 plot_e_AP.py "$arquivo"
done

# mostrar os gráficos
for arquivo in Graficos/*.png; do
    xdg-open "$arquivo" &
done

# desativar o ambiente virtual
deactivate

# exclui arquivos gerados
rm -f *.csv

# exclui o diretório criado
rm -r Modelos