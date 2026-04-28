"""
Kappa de Cohen — quasi-experimento GenAI para Trade-off Analysis
PUCPR, 2026

Preencha o dicionario 'notas' com os valores reais e execute:
    python kappa.py

Interpretacao segundo Landis e Koch (1977):
    < 0.20   Pobre
    0.21-0.40  Razoavel
    0.41-0.60  Moderada
    0.61-0.80  Substancial
    > 0.80   Quase perfeita
"""

# Formato por resposta:
# [M1_Av1, M1_Av2, M1_Av3,  M2_Av1, M2_Av2, M2_Av3,  M3_Av1, M3_Av2, M3_Av3,  M4_Av1, M4_Av2, M4_Av3]

notas = {
    'C1/Gemini':  [3, 3, 3,  3, 3, 2,  3, 2, 3,  3, 3, 3],
    'C1/GPT-5.3': [2, 2, 3,  3, 3, 3,  3, 2, 3,  2, 2, 2],
    'C2/Gemini':  [3, 3, 3,  3, 2, 3,  3, 3, 3,  2, 3, 3],
    'C2/GPT-5.3': [2, 3, 3,  3, 3, 3,  3, 3, 3,  2, 2, 2],
}

resps = list(notas.keys())
dims  = ['M1', 'M2', 'M3', 'M4']


def cohen_kappa(r1, r2):
    n  = len(r1)
    po = sum(a == b for a, b in zip(r1, r2)) / n
    pe = sum((r1.count(c) / n) * (r2.count(c) / n) for c in range(4))
    return (po - pe) / (1 - pe) if (1 - pe) != 0 else 1.0


def interpretar(k):
    if k < 0.20: return 'Pobre'
    if k < 0.40: return 'Razoavel'
    if k < 0.61: return 'Moderada'
    if k < 0.80: return 'Substancial'
    return 'Quase perfeita'


print('Kappa de Cohen por dimensao')
print('-' * 60)

kappas = []
for di, dim in enumerate(dims):
    av1 = [notas[r][di * 3 + 0] for r in resps]
    av2 = [notas[r][di * 3 + 1] for r in resps]
    av3 = [notas[r][di * 3 + 2] for r in resps]
    k12 = cohen_kappa(av1, av2)
    k13 = cohen_kappa(av1, av3)
    k23 = cohen_kappa(av2, av3)
    km  = (k12 + k13 + k23) / 3
    kappas.append(km)
    print(f'{dim}  Av1xAv2={k12:.3f}  Av1xAv3={k13:.3f}  Av2xAv3={k23:.3f}  media={km:.3f}  {interpretar(km)}')

kg = sum(kappas) / len(kappas)
print('-' * 60)
print(f'Global  {kg:.3f}  {interpretar(kg)}')

print()
print('Medias por resposta (pontuacao normalizada 0-3)')
print('-' * 60)
for r in resps:
    n = notas[r]
    av1 = sum([n[0], n[3], n[6], n[9]]) / 4
    av2 = sum([n[1], n[4], n[7], n[10]]) / 4
    av3 = sum([n[2], n[5], n[8], n[11]]) / 4
    print(f'{r:<15}  Av1={av1:.2f}  Av2={av2:.2f}  Av3={av3:.2f}  media={(av1+av2+av3)/3:.2f}')
