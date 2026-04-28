# GenAI para Trade-off Analysis

**Qualidade das Recomendações e Impacto em Atributos ISO/IEC 25010**

Matheus Grande Giaretta, Rafael Carlim Brennsen, Rafael Schuck Segatto
PUCPR — Engenharia de Software, 2026

Este repositório contém os artefatos do quasi-experimento conduzido para avaliar a qualidade das análises de trade-off produzidas por Gemini 3.1 Pro e GPT-5.3 para pares de atributos conflitantes da ISO/IEC 25010:2011. O protocolo segue Wohlin et al. (2024). Todos os materiais estão disponíveis publicamente para que o estudo seja reproduzível por pesquisadores externos, conforme os princípios de Ciência Aberta adotados em Silveira Neto et al. (2025).

## Estrutura

```
1-protocolo/
    GQM.md                    objetivo, questões de pesquisa, hipóteses e testes estatísticos
    cenarios-piloto.md        dois cenários retirados dos General Scenarios de Kazman
    rubrica-v1.md             instrumento de avaliação com quatro dimensões e escala 0-3
    definicao-experimento.md  documento formal de definição do experimento

2-prompts/
    prompt-C1.md              prompt submetido ao Cenário Piloto 1
    prompt-C2.md              prompt submetido ao Cenário Piloto 2

3-respostas/
    gemini-C1.md              resposta do Gemini 3.1 Pro para o Cenário Piloto 1
    gemini-C2.md              resposta do Gemini 3.1 Pro para o Cenário Piloto 2
    gpt53-C1.md               resposta do GPT-5.3 Instant para o Cenário Piloto 1
    gpt53-C2.md               resposta do GPT-5.3 Instant para o Cenário Piloto 2

4-avaliacoes/
    formulario-branco.docx    formulário de avaliação para os três avaliadores
    matheus.md                notas do Avaliador 1
    brennsen.md               notas do Avaliador 2
    schuck.md                 notas do Avaliador 3

5-analise/
    kappa.py                  cálculo do Kappa de Cohen por dimensão e global
    testes-estatisticos.py    Wilcoxon, Mann-Whitney U e Kruskal-Wallis

6-documento/
    TCC_GenAI_TradeOff.docx   documento final
```

## Como reproduzir

Leia os arquivos em `1-protocolo/` antes de qualquer outra etapa — o GQM, os cenários e a rubrica definem os parâmetros de todo o experimento.

Para coletar dados, submeta os prompts em `2-prompts/` aos modelos Gemini 3.1 Pro e GPT-5.3 Instant. Abra uma conversa nova por cenário por modelo para evitar contaminação de contexto e registre as respostas integralmente em `3-respostas/`.

A avaliação é feita com o `formulario-branco.docx`. Cada avaliador preenche de forma independente, sem consultar os outros antes da consolidação.

Com as notas preenchidas no dicionário de `kappa.py`, execute o script para obter o Kappa por dimensão e global. Os testes de hipótese ficam em `testes-estatisticos.py`.

## Referências

BASS, L.; CLEMENTS, P.; KAZMAN, R. *Software architecture in practice*. 4. ed. Addison-Wesley, 2021.

ESPOSITO, M. et al. Generative AI for software architecture: applications, challenges, and future directions. *Journal of Systems and Software*, v. 231, 2025.

ISO/IEC 25010:2011. *System and software quality models*. Geneva: ISO, 2011.

SILVEIRA NETO, M. V. et al. Agile software architecture: perceptions on quality and architectural technical debt management. *SBCARS*, 2025.

WOHLIN, C. et al. *Experimentation in software engineering*. 2. ed. Springer, 2024.