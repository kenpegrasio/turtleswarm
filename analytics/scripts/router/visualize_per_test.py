import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "../../../data"
ANALYSIS = HERE / "../../analysis"

save_image = True
latency_file_paths = [
    DATA / "router/cartographers/latency/1.txt",
    DATA / "router/cartographers/latency/2.txt",
    DATA / "router/cartographers/latency/3.txt",
    DATA / "router/cartographers/latency/4.txt",
]
message_count_file_paths = [
    DATA / "router/cartographers/message_count/1.txt",
    DATA / "router/cartographers/message_count/2.txt",
    DATA / "router/cartographers/message_count/3.txt",
    DATA / "router/cartographers/message_count/4.txt",
]
number_of_data_per_experiment = 10

# Calculate maximum latency
maximum_latency = 0
for latency_file in latency_file_paths:
    with open(latency_file, "r") as f:
        latency_list = [float(line.strip()) for line in f if line.strip()]
        maximum_latency = max(maximum_latency, max(latency_list))

plt.figure()

for latency_file, message_count_file in zip(latency_file_paths, message_count_file_paths):
    with open(latency_file, "r") as f:
        latency_list = [float(line.strip()) for line in f if line.strip()]

    with open(message_count_file, "r") as f:
        message_count_list = [int(line.strip()) for line in f if line.strip()]

    averages = []
    index_offset = 0
    for message_count in message_count_list:
        cur_sum = 0
        for idx in range(index_offset, index_offset + message_count):
            cur_sum += latency_list[idx]
        index_offset += message_count
        # Replace lost latency with maximum latency
        cur_sum += (number_of_data_per_experiment - message_count) * maximum_latency
        averages.append(cur_sum / number_of_data_per_experiment)

    x = list(range(1, len(averages) + 1))

    plt.plot(x, averages, marker=".", label=f"{latency_file.stem} turtlebots")

plt.xticks([1, 2, 3, 4, 5])
plt.xlim(1, 5)
plt.xlabel("Experiment Index")
plt.ylabel("Average End to End Latency (ms)")
plt.title("[HUAWEI ROUTER] Average End to End Latency per Test")
plt.grid(True)
plt.legend()

if save_image:
    plt.savefig(ANALYSIS / "router/average_latency_per_test.png")

plt.show()
