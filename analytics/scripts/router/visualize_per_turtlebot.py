import matplotlib.pyplot as plt

save_image = True
files = [
    "../../../data/router/latency/1.txt", 
    "../../../data/router/latency/2.txt", 
    "../../../data/router/latency/3.txt", 
    "../../../data/router/latency/4.txt"
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
plt.ylabel("Average Network Latency (ms)")
plt.title("[ROUTER] Average Network Latency based on Number of Turtlebots")
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
    plt.savefig("../../analysis/router/average_latency_per_turtlebot.png")

plt.show()
