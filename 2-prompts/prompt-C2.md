# Prompt — Cenário Piloto 2

Manutenibilidade × Eficiência de Desempenho.
Derivado do Modifiability General Scenario, Bass, Clements e Kazman (2021), Cap. 8, Table 8.1.

O prompt foi submetido de forma idêntica ao Gemini 3.1 Pro e ao GPT-5.3 Instant, em conversas independentes e sem contexto de outras interações. A estrutura segue os seis elementos do Quality Attribute Scenario de Kazman. O vocabulário normativo da ISO/IEC 25010:2011 é exigido explicitamente, conforme Cheng et al. (2026) e Wohlin et al. (2024), Cap. 9.6.

O prompt está redigido em inglês. "Modifiability" de Kazman corresponde à subcaracterística "Modificabilidade" de Manutenibilidade na ISO/IEC 25010:2011.

---

The following architectural scenario is structured according to the Quality Attribute Scenario model proposed by Bass, Clements, and Kazman (2021). Analyze it and perform the four tasks described at the end.

Source of Stimulus: a developer
Stimulus: a directive to modify an existing component to improve processing capacity
Artifact: a software component responsible for data processing
Environment: design time
Response: the modification is made, tested, and deployed without introducing defects in other components
Response Measure: modification completed in <= 3 hours; number of affected components <= 2; no new defects introduced

Tasks:

1. Identify and name the quality attributes in conflict in this scenario. Use exclusively the normative vocabulary of ISO/IEC 25010:2011, naming the characteristics and sub-characteristics involved.

2. Propose a justified architectural decision. The decision must be mappable to architectural tactics recognized by Bass, Clements, and Kazman (2021) and must demonstrate explicit alignment with the Response Measures of the scenario.

3. Present mitigation strategies for the negative impacts of the decision. For each strategy, identify the cost or trade-off it introduces.

4. Identify the residual risks that remain after the mitigations are applied.