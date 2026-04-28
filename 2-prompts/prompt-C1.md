# Prompt — Cenário Piloto 1

Confiabilidade × Eficiência de Desempenho.
Derivado do Availability General Scenario, Bass, Clements e Kazman (2021), Cap. 4, Table 4.2.

O prompt foi submetido de forma idêntica ao Gemini 3.1 Pro e ao GPT-5.3 Instant, em conversas independentes e sem contexto de outras interações. A estrutura segue os seis elementos do Quality Attribute Scenario de Kazman. O vocabulário normativo da ISO/IEC 25010:2011 é exigido explicitamente para eliminar ambiguidade terminológica, conforme justificado em Cheng et al. (2026) e Wohlin et al. (2024), Cap. 9.6.

O prompt está redigido em inglês para evitar ambiguidade de tradução nos termos normativos e técnicos.

---

The following architectural scenario is structured according to the Quality Attribute Scenario model proposed by Bass, Clements, and Kazman (2021). Analyze it and perform the four tasks described at the end.

Source of Stimulus: an internal software component
Stimulus: a crash fault occurs in one processing node
Artifact: the data processing service
Environment: normal operation under load
Response: the system detects the fault and continues operating through redundancy
Response Measure: availability >= 99.9%; time to repair <= 5 seconds; system operates in degraded mode for <= 30 seconds

Tasks:

1. Identify and name the quality attributes in conflict in this scenario. Use exclusively the normative vocabulary of ISO/IEC 25010:2011, naming the characteristics and sub-characteristics involved.

2. Propose a justified architectural decision. The decision must be mappable to architectural tactics recognized by Bass, Clements, and Kazman (2021) and must demonstrate explicit alignment with the Response Measures of the scenario.

3. Present mitigation strategies for the negative impacts of the decision. For each strategy, identify the cost or trade-off it introduces.

4. Identify the residual risks that remain after the mitigations are applied.