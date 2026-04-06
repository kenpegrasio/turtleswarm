import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "../../data"
ANALYSIS = HERE / "../analysis"

save_image = True
files = [
    DATA / "memory/0.txt",
    DATA / "memory/1.txt",
    DATA / "memory/2.txt",
    DATA / "memory/3.txt",
    DATA / "memory/4.txt",
]
offsets = [(0, 6), (-8, 6), (-15, 4), (-16, -2), (-20, -3)]

averages = []

for file in files:
    with open(file, "r") as f:
        values = []
        for line in f:
            if not line.strip():
                continue
            if not line.startswith('RAM used (GB):'):
                continue
            values.append(float(line.split()[-1]))
        avg = sum(values) / len(values)
        averages.append(avg)

x = list(range(0, len(files)))

plt.figure()
plt.plot(x, averages, marker='o')
plt.xlabel("Number of Turtlebots")
plt.ylabel("Memory Usage (GB)")
plt.title("Average Memory Usage based on Number of Turtlebots")
plt.xticks(x)
plt.grid(True)

for xi, yi, offset in zip(x, averages, offsets):
    plt.annotate(
        f"{yi:.2f}",
        (xi, yi),
        textcoords="offset points",
        xytext=(offset[0], offset[1]),
        ha="center"
    )

if save_image:
    plt.savefig(ANALYSIS / "memory_usage_per_turtlebot.png")

plt.show()
