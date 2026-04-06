import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "../../../data"
ANALYSIS = HERE / "../../analysis"

save_image = True
files = [
    DATA / "router/cartographers/latency/1.txt",
    DATA / "router/cartographers/latency/2.txt",
    DATA / "router/cartographers/latency/3.txt",
    DATA / "router/cartographers/latency/4.txt",
]
offsets = [(0, 6), (-8, 6), (-15, 4), (-24, -2)]
number_of_data_per_turtlebot = 50

# Calculate maximum latency
maximum_latency = 0
for file in files:
    with open(file, "r") as f:
        latency_list = [float(line.strip()) for line in f if line.strip()]
        maximum_latency = max(maximum_latency, max(latency_list))

averages = []

for file in files:
    with open(file, "r") as f:
        values = [float(line.strip()) for line in f if line.strip()]
        # Replace lost latency with maximum latency
        total_sum = sum(values) + (number_of_data_per_turtlebot - len(values)) * maximum_latency
        avg = total_sum / number_of_data_per_turtlebot
        averages.append(avg)

x = list(range(1, len(files) + 1))

plt.figure()
plt.plot(x, averages, marker='o')
plt.xlabel("Number of Turtlebots")
plt.ylabel("Average End to End Latency (ms)")
plt.title("[HUAWEI ROUTER] Average End to End Latency based on Number of Turtlebots")
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
    plt.savefig(ANALYSIS / "router/average_latency_per_turtlebot.png")

plt.show()
