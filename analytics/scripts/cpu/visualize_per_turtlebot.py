import matplotlib.pyplot as plt

save_image = True
files = [
    "../../../data/cpu/0.txt",
    "../../../data/cpu/1.txt", 
    "../../../data/cpu/2.txt", 
    "../../../data/cpu/3.txt", 
    "../../../data/cpu/4.txt"
]
offsets = [(0, 6), (-8, 6), (-15, 4), (-20, -2), (-20, -8)]

averages = []

for file in files:
    with open(file, "r") as f:
        values = [float(line.strip()) for line in f if line.strip()]
        avg = sum(values) / len(values)
        averages.append(avg)

x = list(range(0, len(files)))

plt.figure()
plt.plot(x, averages, marker='o')
plt.xlabel("Number of Turtlebots")
plt.ylim(0, 100)
plt.ylabel("CPU Utilization (%)")
plt.title("Average CPU Utilization (%) based on Number of Turtlebots")
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
    plt.savefig("../../analysis/cpu/average_cpu_util_per_turtlebot.png")

plt.show()
