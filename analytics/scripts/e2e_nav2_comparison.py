import math
import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "../../data"
ANALYSIS = HERE / "../analysis"

save_image = True

ORDER = [
    "1_robot_launch",
    "1_nav2",
    "1_auto_nav",
    "2_robot_launch",
    "2_robot_launch_nav2",
    "2_robot_launch_auto_nav",
    "2_nav2",
    "2_nav2_auto_nav",
    "2_auto_nav",
]

TOTAL_MESSAGES = 50

fast_latencies, fast_drops = [], []
cyclone_latencies, cyclone_drops = [], []

for name in ORDER:
    for latencies, drops, dds in [
        (fast_latencies, fast_drops, "fast_dds"),
        (cyclone_latencies, cyclone_drops, "cyclone_dds"),
    ]:
        path = DATA / f"mobile/nav2/{dds}/{name}.txt"
        if not path.exists():
            latencies.append(math.nan)
            drops.append(math.nan)
            continue
        with open(path, "r") as f:
            values = [float(line.strip()) for line in f if line.strip()]
        latencies.append(sum(values) / len(values))
        drops.append(TOTAL_MESSAGES - len(values))

x = range(len(ORDER))
x_labels = [name.replace("_", "\n") for name in ORDER]

# ── Graph 1: Average End to End Latency ──────────────────────────────────────
fig1, ax = plt.subplots(figsize=(11, 5))

ax.plot(x, fast_latencies, marker="o", label="Fast DDS")
ax.plot(x, cyclone_latencies, marker="s", label="Cyclone DDS")

ax.set_xlabel("Test Scenario")
ax.set_ylabel("Average End to End Latency (ms)")
ax.set_title("[FAST DDS vs CYCLONE DDS] Average End to End Latency per Test Scenario")
ax.set_xticks(x)
ax.set_xticklabels(x_labels, fontsize=8)
ax.grid(True)
ax.legend()

plt.tight_layout()
if save_image:
    fig1.savefig(ANALYSIS / "e2e_nav2_comparison_latency.png")

# ── Graph 2: Messages Dropped ─────────────────────────────────────────────────
fig2, ax = plt.subplots(figsize=(11, 5))

ax.plot(x, fast_drops, marker="o", label="Fast DDS")
ax.plot(x, cyclone_drops, marker="s", label="Cyclone DDS")

ax.set_xlabel("Test Scenario")
ax.set_ylabel("Messages Dropped")
ax.set_title("[FAST DDS vs CYCLONE DDS] Messages Dropped per Test Scenario")
ax.set_xticks(x)
ax.set_xticklabels(x_labels, fontsize=8)
ax.set_ylim(0, TOTAL_MESSAGES)
ax.grid(True)
ax.legend()

plt.tight_layout()
if save_image:
    fig2.savefig(ANALYSIS / "e2e_nav2_comparison_drops.png")

plt.show()
