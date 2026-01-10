import matplotlib.pyplot as plt

save_image = True
files = [
    "../../../data/mobile/1.txt", 
    "../../../data/mobile/2.txt", 
    "../../../data/mobile/3.txt", 
    "../../../data/mobile/4.txt"
]
number_of_data_per_experiment = 10


plt.figure()

for file in files:
    with open(file, "r") as f:
        values = [float(line.strip()) for line in f if line.strip()]

    chunk_averages = [
        sum(values[i:i + number_of_data_per_experiment]) / number_of_data_per_experiment
        for i in range(0, len(values), number_of_data_per_experiment)
    ]

    x = list(range(1, len(chunk_averages) + 1))

    plt.plot(x, chunk_averages, marker=".", label=f"{file.split('/')[-1].split('.')[0]} turtlebots")

plt.xticks([1, 2, 3, 4, 5])
plt.xlim(1, 5)
plt.xlabel("Experiment Index")
plt.ylabel("Average Network Latency (ms)")
plt.title("[MOBILE] Average Network Latency per Test")
plt.grid(True)
plt.legend()

if save_image:
    plt.savefig('../../analysis/mobile/average_latency_per_test.png')

plt.show()
