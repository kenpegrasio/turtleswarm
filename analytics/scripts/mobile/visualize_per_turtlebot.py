import matplotlib.pyplot as plt

save_image = True
files = [
    "../../../data/mobile/1.txt", 
    "../../../data/mobile/2.txt", 
    "../../../data/mobile/3.txt", 
    "../../../data/mobile/4.txt"
]
offsets = [(0, 6), (-8, 6), (-15, 4), (-24, -2)]

averages = []

for file in files:
    with open(file, "r") as f:
        values = [float(line.strip()) for line in f if line.strip()]
        avg = sum(values) / len(values)
        averages.append(avg)

x = list(range(1, len(files) + 1))

plt.figure()
plt.plot(x, averages, marker='o')
plt.xlabel("Number of Turtlebots")
plt.ylabel("Average Network Latency (ms)")
plt.title("[MOBILE] Average Network Latency based on Number of Turtlebots")
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
    plt.savefig("../../analysis/mobile/average_latency_per_turtlebot.png")

plt.show()
