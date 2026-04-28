"""
Script de Análise Estatística - GenAI para Trade-off Analysis
Autores: Matheus Grande Giaretta, Rafael Carlim Brennsen, Rafael Schuck Segatto
Ano: 2026
Repositório: https://github.com/Giarettamat/TCC-GenAI-TRADEOFF-ANALYSIS

Descrição:
Este script executa os testes estatísticos não-paramétricos (Mann-Whitney U, 
Wilcoxon e Kruskal-Wallis) para avaliar as hipóteses do quasi-experimento 
comparando Gemini 3.1 Pro e GPT-5.3 Instant na análise de trade-offs arquiteturais.
"""

import pandas as pd
import numpy as np
from scipy import stats

def interpretar_hipotese(p_valor, alfa=0.05):
    """Retorna a interpretação padrão baseada no p-valor."""
    if p_valor < alfa:
        return "Rejeita H0 (Diferença estatisticamente significativa)"
    else:
        return "Falha em rejeitar H0 (Sem diferença estatisticamente significativa)"

def executar_testes():
    print("="*70)
    print(" ANÁLISE ESTATÍSTICA - GENAI PARA TRADE-OFF ANALYSIS")
    print(" Nível de Significância Adotado (alfa) = 0.05")
    print("="*70)

    # -------------------------------------------------------------------------
    # 1. CARREGAMENTO DOS DADOS
    # Para o uso real, substitua o bloco abaixo por: 
    # df = pd.read_csv('../4-avaliacoes/notas_consolidadas.csv')
    # -------------------------------------------------------------------------
    
    # Dados simulados representando as 8 análises (8 cenários) 
    # Nota normalizada (0 a 3) após cálculo das 4 dimensões (M1, M2, M3, M4)
    dados_simulados = {
        'Cenario': ['C1_Avail', 'C2_Modif', 'C3_Perf', 'C4_Sec', 'C5_Rel', 'C6_Maint', 'C7_Usab', 'C8_Port'],
        'Nota_Gemini': [2.25, 2.50, 1.75, 2.75, 2.50, 2.00, 2.25, 2.50],
        'Nota_GPT53':  [1.75, 2.00, 1.50, 2.25, 1.75, 2.00, 1.50, 2.00]
    }
    df = pd.DataFrame(dados_simulados)
    
    notas_gemini = df['Nota_Gemini']
    notas_gpt = df['Nota_GPT53']

    # Exibindo Estatística Descritiva Básica
    print("\n[ESTATÍSTICA DESCRITIVA BÁSICA]")
    print(f"Gemini 3.1 Pro -> Média: {notas_gemini.mean():.2f} | Mediana: {notas_gemini.median():.2f} | Desvio Padrão: {notas_gemini.std():.2f}")
    print(f"GPT-5.3 Instant -> Média: {notas_gpt.mean():.2f} | Mediana: {notas_gpt.median():.2f} | Desvio Padrão: {notas_gpt.std():.2f}")
    print("-" * 70)

    # -------------------------------------------------------------------------
    # 2. TESTE DE MANN-WHITNEY U (Hipótese H01 / H11)
    # Conforme definido no documento de TCC para comparar os modelos.
    # Avalia se a distribuição das notas de um modelo é estocasticamente 
    # maior que a do outro (amostras independentes).
    # -------------------------------------------------------------------------
    print("\n[TESTE 1] MANN-WHITNEY U (Comparação entre Modelos)")
    print("H01: Não há diferença significativa na qualidade (Gemini = GPT-5.3)")
    print("H11: Há diferença significativa na qualidade entre os modelos")
    
    u_stat, p_val_u = stats.mannwhitneyu(notas_gemini, notas_gpt, alternative='two-sided')
    
    print(f"Estatística U: {u_stat:.4f}")
    print(f"P-valor      : {p_val_u:.4f}")
    print(f"Resultado    : {interpretar_hipotese(p_val_u)}")
    print("-" * 70)

    # -------------------------------------------------------------------------
    # 3. TESTE DE WILCOXON SIGNED-RANK (Alternativa pareada para H01 / H11)
    # Como o design é "within-subjects" (mesmos cenários testados nos 2 modelos),
    # o Wilcoxon é altamente recomendado para pareamento direto.
    # -------------------------------------------------------------------------
    print("\n[TESTE 2] WILCOXON SIGNED-RANK (Comparação Pareada por Cenário)")
    print("Justificativa: Maior poder estatístico para designs within-subjects.")
    
    try:
        w_stat, p_val_w = stats.wilcoxon(notas_gemini, notas_gpt, zero_method='zsplit')
        print(f"Estatística W: {w_stat:.4f}")
        print(f"P-valor      : {p_val_w:.4f}")
        print(f"Resultado    : {interpretar_hipotese(p_val_w)}")
    except ValueError as e:
        print("Aviso: Dados insuficientes ou perfeitamente idênticos para Wilcoxon.")
    print("-" * 70)

    # -------------------------------------------------------------------------
    # 4. TESTE DE KRUSKAL-WALLIS (Hipótese H02 / H12)
    # Avalia se a variação dos pares de atributos (Cenários) afeta a qualidade.
    # -------------------------------------------------------------------------
    print("\n[TESTE 3] KRUSKAL-WALLIS (Variação por Cenário)")
    print("H02: A qualidade não varia significativamente conforme o cenário avaliado.")
    print("H12: A qualidade varia significativamente conforme o cenário avaliado.")
    
    # Para o Kruskal-Wallis, precisamos agrupar todas as notas (Gemini e GPT juntas) 
    # de acordo com o cenário específico.
    # Criando listas de notas agrupadas por cenário:
    notas_por_cenario = []
    for index, row in df.iterrows():
        # Adiciona uma lista contendo as notas dos dois modelos para aquele cenário
        notas_por_cenario.append([row['Nota_Gemini'], row['Nota_GPT53']])
    
    # Desempacotando os argumentos para a função kruskal (*args)
    kw_stat, p_val_kw = stats.kruskal(*notas_por_cenario)
    
    print(f"Estatística H: {kw_stat:.4f}")
    print(f"P-valor      : {p_val_kw:.4f}")
    print(f"Resultado    : {interpretar_hipotese(p_val_kw)}")
    print("="*70)

if __name__ == "__main__":
    # Verifica se os pacotes necessários estão instalados antes de rodar
    try:
        executar_testes()
    except Exception as e:
        print(f"Erro durante a execução dos testes: {e}")
        print("Certifique-se de ter instalado as dependências: pip install pandas scipy numpy")