import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "../../../../../data"
ANALYSIS = HERE / "../../../../analysis"

save_image = True

ORDER = [
    "1_robot_launch",
    "1_nav2",
    "1_auto_nav",
    "2_robot_launch",
    "2_robot_launch_nav2",
    "2_robot_launch_auto_nav",
    "2_nav2",
]

TOTAL_MESSAGES = 50

latencies = []
drops = []

for name in ORDER:
    path = DATA / f"mobile/nav2/fast_dds/{name}.txt"
    with open(path, "r") as f:
        values = [float(line.strip()) for line in f if line.strip()]
    latencies.append(sum(values) / len(values))
    drops.append(TOTAL_MESSAGES - len(values))

x = range(len(ORDER))
x_labels = [name.replace("_", "\n") for name in ORDER]

fig, ax1 = plt.subplots(figsize=(11, 5))

color_latency = "tab:blue"
color_drops = "tab:red"

ax1.set_xlabel("Test Scenario")
ax1.set_ylabel("Average End to End Latency (ms)", color=color_latency)
ax1.plot(x, latencies, marker="o", color=color_latency, label="Avg Latency (ms)")
ax1.tick_params(axis="y", labelcolor=color_latency)
ax1.set_xticks(x)
ax1.set_xticklabels(x_labels, fontsize=8)

ax2 = ax1.twinx()
ax2.set_ylabel("Messages Dropped", color=color_drops)
ax2.plot(x, drops, marker="s", linestyle="--", color=color_drops, label="Messages Dropped")
ax2.tick_params(axis="y", labelcolor=color_drops)
ax2.set_ylim(0, TOTAL_MESSAGES)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

plt.title("[FAST DDS] Average End to End Latency and Messages Dropped per Test Scenario")
plt.tight_layout()

if save_image:
    plt.savefig(ANALYSIS / "end_to_end/nav2/fast_dds/fast_dds_per_test.png")

plt.show()
