# GQM — Goal Question Metric

Versão v1, aprovada em abril de 2026.
Referência metodológica: Wohlin et al. (2024), Cap. 8; Basili et al. (1986).

## Objetivo

Analisar as análises de trade-off produzidas por Gemini 3.1 Pro e GPT-5.3 Instant com o propósito de avaliar e comparar a qualidade dos outputs gerados, com respeito à precisão terminológica da ISO/IEC 25010:2011, à adequação arquitetural segundo as táticas de Bass, Clements e Kazman (2021) e à cobertura de mitigações, do ponto de vista de pesquisadores em Engenharia de Software, no contexto de cenários arquiteturais genéricos estruturados segundo Bass, Clements e Kazman (2021).

## Questões de pesquisa

| QP | Questão | Métrica |
|----|---------|---------|
| QP1 | Os modelos identificam corretamente os atributos ISO/IEC 25010 em conflito no cenário? | Nota M1 da rubrica v1 (0–3) |
| QP2 | As decisões arquiteturais propostas são coerentes com as táticas de Bass, Clements e Kazman? | Nota M2 da rubrica v1 (0–3) |
| QP3 | As estratégias de mitigação são mapeáveis a táticas arquiteturais reconhecidas? | Nota M3 da rubrica v1 (0–3) |
| QP4 | Há diferença estatisticamente significativa na qualidade entre os dois modelos? | Teste Mann-Whitney U sobre pontuações normalizadas |

## Hipóteses

As hipóteses foram formuladas antes da coleta de dados, conforme exigido por Wohlin et al. (2024), Cap. 9.2. Nenhum limiar numérico de qualidade foi definido a priori para evitar viés do pesquisador.

**H₀₁:** não há diferença estatisticamente significativa na qualidade das análises produzidas por Gemini 3.1 Pro e GPT-5.3 Instant para os mesmos cenários arquiteturais (p ≥ 0,05).

**H₁₁:** há diferença estatisticamente significativa entre os dois modelos (p < 0,05).

**H₀₂:** a qualidade das análises não varia significativamente conforme o par de atributos conflitantes avaliado (p ≥ 0,05).

**H₁₂:** a qualidade varia significativamente conforme o par de atributos conflitantes avaliado (p < 0,05).

## Testes estatísticos

| Hipótese | Teste | Justificativa |
|----------|-------|---------------|
| H₀₁ / H₁₁ | Mann-Whitney U | Dados ordinais, amostras independentes pequenas — Wohlin et al. (2024), Cap. 11.3 |
| H₀₂ / H₁₂ | Kruskal-Wallis | Comparação de múltiplos grupos independentes — Wohlin et al. (2024), Cap. 11.3 |

Nível de significância: α = 0,05. A escolha de testes não-paramétricos decorre da natureza ordinal dos dados e do tamanho reduzido das amostras.