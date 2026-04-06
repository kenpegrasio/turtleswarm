import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "../../data"
ANALYSIS = HERE / "../analysis"

save_image = True
files = [
    DATA / "mobile/cartographers/1.txt",
    DATA / "mobile/cartographers/2.txt",
    DATA / "mobile/cartographers/3.txt",
    DATA / "mobile/cartographers/4.txt",
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

    plt.plot(x, chunk_averages, marker=".", label=f"{file.stem} turtlebots")

plt.xticks([1, 2, 3, 4, 5])
plt.xlim(1, 5)
plt.xlabel("Experiment Index")
plt.ylabel("Average End to End Latency (ms)")
plt.title("[MOBILE] Average End to End Latency per Test")
plt.grid(True)
plt.legend()

if save_image:
    plt.savefig(ANALYSIS / "e2e_cartographers_mobile_per_test.png")

plt.show()
