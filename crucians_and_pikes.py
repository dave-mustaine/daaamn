import matplotlib.pyplot as plt

D = 0.8
BCRUCIANS = 0.01  # for crucians
BPIKES = 0.012  # for pikes
K = 0.2
CRUCIANS = 1_000  # number of crucians
PIKES = 1_000  # number of pikes
LIMIT = 10_000
time = 0
time_step = 1

population_crucians = [[0], [100]]
population_pikes = [[0], [5]]

for i in range(100):
    kl = K * (LIMIT - CRUCIANS) / LIMIT
    crucians = round((1 + kl - BCRUCIANS * population_pikes[1][i]) * population_crucians[1][i])
    pikes = round((1 - D + BPIKES * population_crucians[1][i]) * population_pikes[1][i])
    population_crucians[1].append(round((1 + kl - BCRUCIANS * population_pikes[1][i]) * population_crucians[1][i]))
    population_pikes[1].append(round((1 - D + BPIKES * population_crucians[1][i]) * population_pikes[1][i]))

    time += time_step
    population_crucians[0].append(time)
    population_pikes[0].append(time)

plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 2)
plt.plot(population_pikes[0], population_pikes[1], color='green')
plt.plot(population_crucians[0], population_crucians[1], color='red')

plt.title('Pikes')

plt.show()
