# Rubrica de Avaliação v1

Instrumento utilizado no estudo piloto. Versão v1, aprovada em abril de 2026.

A rubrica tem quatro dimensões com escala ordinal de 0 a 3. A pontuação de cada resposta é a soma das quatro dimensões (máximo 12 pontos), normalizada dividindo por 4 para obter escala 0–3. Essa escala justifica o uso de testes não-paramétricos na análise estatística, conforme Wohlin et al. (2024), Cap. 11.3.

## M1 — Identificação do conflito

Fonte: Bass, Clements e Kazman (2021), Cap. 4; ISO/IEC 25010:2011.

| Nota | Critério |
|------|---------|
| 0 | Não identificou os atributos em conflito ou nomeou atributos inexistentes na norma |
| 1 | Identificou parcialmente ou descreveu o conflito sem referenciar a ISO/IEC 25010 |
| 2 | Nomeou os dois atributos com terminologia correta e descreveu o conflito com clareza |
| 3 | Nomeou características e subcaracterísticas corretas, descreveu o conflito e identificou a tática causadora |

## M2 — Adequação da decisão arquitetural

Fonte: Bass, Clements e Kazman (2021), Cap. 4 — Architectural Tactics; Wohlin et al. (2024), Cap. 9.6.

| Nota | Critério |
|------|---------|
| 0 | Decisão inadequada, contraditória ou ausente |
| 1 | Decisão plausível mas sem referência a táticas arquiteturais reconhecidas |
| 2 | Decisão mapeável a tática de Kazman, mas sem alinhamento explícito com as Response Measures |
| 3 | Decisão mapeável a tática específica de Kazman com alinhamento explícito e justificado a cada Response Measure |

## M3 — Mitigação e riscos residuais

Fonte: Kazman et al. (2000) — ATAM, trade-off points e sensitivity points; Bass, Clements e Kazman (2021), Cap. 4.

| Nota | Critério |
|------|---------|
| 0 | Sem estratégias de mitigação |
| 1 | Mitigações genéricas não mapeáveis a táticas arquiteturais |
| 2 | Duas ou mais mitigações mapeáveis a táticas, com risco residual identificado |
| 3 | Três ou mais mitigações mapeáveis a táticas, com custo ou trade-off explícito de cada uma |

## M4 — Cobertura ISO/IEC 25010

Fonte: ISO/IEC 25010:2011; Esposito et al. (2025).

| Nota | Critério |
|------|---------|
| 0 | Sem terminologia da norma ou com atributos inexistentes na ISO/IEC 25010 |
| 1 | Terminologia da norma apenas nos títulos das seções, sem uso consistente no corpo |
| 2 | Nomes corretos das características no corpo da resposta, sem nomear as subcaracterísticas |
| 3 | Características e subcaracterísticas corretas e consistentes ao longo de toda a resposta, sem atributos inexistentes |

## Protocolo de aplicação

Cada avaliador preenche o formulário de forma independente, sem consultar os outros antes da consolidação. A justificativa por célula deve referenciar elementos concretos da resposta avaliada. Após o preenchimento individual, o Kappa de Cohen é calculado por dimensão e global.

## Resultado do piloto

Kappa global de 0,264, razoável segundo Landis e Koch (1977). As principais divergências ocorreram em M1 e M2. Em M1, a penalização por atributos não induzidos pelo cenário não estava clara o suficiente. Em M2, o critério de alinhamento explícito às Response Measures foi interpretado de formas distintas pelos três avaliadores. Esses pontos serão revisados na rubrica v2, usada na coleta definitiva.