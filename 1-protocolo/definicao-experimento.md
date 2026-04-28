# Definição do Experimento

Protocolo de Basili et al. (1986) e Wohlin et al. (2024), conforme adotado em Silveira Neto (2021).

## Motivação

Ferramentas de GenAI estão sendo adotadas por arquitetos de software sem evidência empírica sobre a qualidade das análises de trade-off que produzem. Esposito et al. (2025) identificaram que 93% dos estudos sobre GenAI em arquitetura de software não validam formalmente os outputs dos modelos e que trade-off analysis é uma lacuna explícita na literatura. Este experimento ataca essa lacuna.

## Objeto de estudo

Os outputs produzidos por Gemini 3.1 Pro e GPT-5.3 para cenários arquiteturais estruturados segundo Bass, Clements e Kazman (2021).

## Propósito

Avaliar e comparar a qualidade das análises de trade-off produzidas pelos dois modelos para pares de atributos conflitantes da ISO/IEC 25010:2011.

## Perspectiva

Pesquisadores em Engenharia de Software.

## Domínio

**Sujeitos:** Gemini 3.1 Pro e GPT-5.3. A escolha baseia-se em Esposito et al. (2025): GPT domina 62% dos estudos sobre GenAI em arquitetura de software; Gemini representa 2%. Comparar os dois modelos preenche uma lacuna específica identificada nos estudos de base.

**Objetos:** cenários arquiteturais derivados dos General Scenarios de Bass, Clements e Kazman (2021), Cap. 4 e Cap. 8.

## Escopo

Multi-test within object study: dois sujeitos avaliados sobre o mesmo conjunto de objetos, conforme Wohlin et al. (2024), Tabela 8.1. Caracterizado como quasi-experimento pela ausência de randomização dos sujeitos — os modelos foram selecionados intencionalmente, não sorteados.

## Variáveis

| Tipo | Variável | Descrição |
|------|----------|-----------|
| Independente | Modelo de LLM | Gemini 3.1 Pro ou GPT-5.3 Instant |
| Independente | Cenário arquitetural | Par de atributos ISO/IEC 25010 em conflito |
| Dependente | Qualidade da análise | Pontuação normalizada pela rubrica v1: soma de M1+M2+M3+M4 dividida por 4 |

## Hipóteses

H₀₁: μ(Gemini) = μ(GPT-5.3) — sem diferença significativa na qualidade média entre os modelos (p ≥ 0,05).
H₁₁: μ(Gemini) ≠ μ(GPT-5.3) — diferença estatisticamente significativa (p < 0,05).
H₀₂: a qualidade não varia significativamente conforme o par de atributos avaliado (p ≥ 0,05).
H₁₂: a qualidade varia significativamente conforme o par de atributos avaliado (p < 0,05).

Nível de significância: α = 0,05.

## Testes estatísticos

Mann-Whitney U para H₀₁/H₁₁ e Kruskal-Wallis para H₀₂/H₁₂. Justificativa: dados ordinais com amostras pequenas — Wohlin et al. (2024), Cap. 11.3.

## Instrumentação

Template de prompt fixo com os seis elementos do Quality Attribute Scenario de Kazman, submetido de forma idêntica aos dois modelos. Rubrica v1 com quatro dimensões e escala 0–3, aplicada independentemente por três avaliadores. Concordância medida pelo Kappa de Cohen, seguindo Esposito et al. (2025).

## Referências

BASILI, V. R.; SELBY, R. W.; HUTCHENS, D. H. Experimentation in software engineering. *IEEE Transactions on Software Engineering*, v. SE-12, n. 7, 1986.

BASS, L.; CLEMENTS, P.; KAZMAN, R. *Software architecture in practice*. 4. ed. Addison-Wesley, 2021.

ESPOSITO, M. et al. Generative AI for software architecture. *Journal of Systems and Software*, v. 231, 2025.

ISO/IEC 25010:2011. *System and software quality models*. Geneva: ISO, 2011.

SILVEIRA NETO, M. V. *Monitoramento e gestão da dívida técnica de code smell*. Dissertação de Mestrado, PUCPR, 2021.

WOHLIN, C. et al. *Experimentation in software engineering*. 2. ed. Springer, 2024.