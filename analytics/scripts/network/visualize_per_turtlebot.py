import matplotlib.pyplot as plt

save_image = True

# SIMBA ROUTER

router_files = [
    "../../../data/router/latency/1.txt", 
    "../../../data/router/latency/2.txt", 
    "../../../data/router/latency/3.txt", 
    "../../../data/router/latency/4.txt"
]
number_of_data_per_turtlebot = 50

# Find maximum latency across all router files
maximum_latency = 0
for file in router_files:
    with open(file, "r") as f:
        latency_list = [float(line.strip()) for line in f if line.strip()]
        maximum_latency = max(maximum_latency, max(latency_list))

router_averages = []
for file in router_files:
    with open(file, "r") as f:
        values = [float(line.strip()) for line in f if line.strip()]
        total_sum = sum(values) + (number_of_data_per_turtlebot - len(values)) * maximum_latency
        avg = total_sum / number_of_data_per_turtlebot
        router_averages.append(avg)

# MOBILE

mobile_files = [
    "../../../data/mobile/1.txt", 
    "../../../data/mobile/2.txt", 
    "../../../data/mobile/3.txt", 
    "../../../data/mobile/4.txt"
]

mobile_averages = []
for file in mobile_files:
    with open(file, "r") as f:
        values = [float(line.strip()) for line in f if line.strip()]
        avg = sum(values) / len(values)
        mobile_averages.append(avg)

# Plot

x = list(range(1, len(router_files) + 1))
router_offsets = [(0, 6), (-12, 6), (-15, 4), (-24, -2)]
mobile_offsets = [(0, 9), (0, 9), (2, 6), (-4, 2)]

plt.figure()

plt.plot(x, router_averages, marker="o", label="SIMBA Router")
plt.plot(x, mobile_averages, marker="o", label="Mobile")

plt.xlabel("Number of Turtlebots")
plt.ylabel("Average Network Latency (ms)")
plt.title("[MOBILE VS SIMBA ROUTER] Average Network Latency per Turtlebot")
plt.xticks(x)
plt.grid(True)
plt.legend()

for xi, yi, offset in zip(x, router_averages, router_offsets):
    plt.annotate(
        f"{yi:.2f}",
        (xi, yi),
        textcoords="offset points",
        xytext=offset,
        ha="center"
    )

for xi, yi, offset in zip(x, mobile_averages, mobile_offsets):
    plt.annotate(
        f"{yi:.2f}",
        (xi, yi),
        textcoords="offset points",
        xytext=(offset[0], offset[1] - 20),
        ha="center"
    )

if save_image:
    plt.savefig("../../analysis/network/average_latency_per_turtlebot.png")

plt.show()
