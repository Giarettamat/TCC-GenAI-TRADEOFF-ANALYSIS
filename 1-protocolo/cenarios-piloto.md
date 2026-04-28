# Cenários Piloto

Os dois cenários foram retirados dos General Scenarios de Bass, Clements e Kazman (2021). General Scenarios são abstratos e independentes de domínio ou sistema específico — essa característica elimina o viés de seleção do pesquisador em relação ao contexto de aplicação. Cenários concretos criados pelos próprios autores do livro, ou derivados de estudos empíricos externos, não foram utilizados para preservar essa independência.

Os dois cenários cobrem pares de atributos de natureza distinta: o Cenário 1 envolve um conflito operacional em tempo de execução, o Cenário 2 envolve um conflito estrutural em tempo de projeto. Essa diferença maximiza a cobertura do piloto com apenas dois cenários e permite verificar se a rubrica se comporta de forma consistente em situações arquiteturais diferentes.

## Cenário Piloto 1

Confiabilidade × Eficiência de Desempenho.
Derivado do Availability General Scenario, Cap. 4, Table 4.2.

| Elemento | Valor |
|----------|-------|
| Source of Stimulus | An internal software component |
| Stimulus | A crash fault occurs in one processing node |
| Artifact | The data processing service |
| Environment | Normal operation under load |
| Response | The system detects the fault and continues operating through redundancy |
| Response Measure | Availability >= 99.9%; time to repair <= 5 seconds; system operates in degraded mode for <= 30 seconds |

Par de atributos ISO/IEC 25010:2011: Confiabilidade (Disponibilidade, Tolerância a Falhas, Recuperabilidade) × Eficiência de Desempenho (Comportamento Temporal, Utilização de Recursos).

## Cenário Piloto 2

Manutenibilidade × Eficiência de Desempenho.
Derivado do Modifiability General Scenario, Cap. 8, Table 8.1.

| Elemento | Valor |
|----------|-------|
| Source of Stimulus | A developer |
| Stimulus | A directive to modify an existing component to improve processing capacity |
| Artifact | A software component responsible for data processing |
| Environment | Design time |
| Response | The modification is made, tested, and deployed without introducing defects in other components |
| Response Measure | Modification completed in <= 3 hours; number of affected components <= 2; no new defects introduced |

Par de atributos ISO/IEC 25010:2011: Manutenibilidade (Modificabilidade, Testabilidade, Analisabilidade) × Eficiência de Desempenho (Comportamento Temporal, Utilização de Recursos).

O termo "Modifiability" de Kazman corresponde à subcaracterística "Modificabilidade" da característica "Manutenibilidade" da ISO/IEC 25010:2011. O Kazman trata Modifiability como o atributo central de qualidade arquitetural; a ISO o subsume como subcaracterística de Maintainability. A equivalência é reconhecida na literatura de arquitetura de software.