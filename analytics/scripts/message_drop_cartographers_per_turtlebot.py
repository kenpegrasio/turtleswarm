import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "../../data"
ANALYSIS = HERE / "../analysis"

save_image = True

TOTAL_MESSAGES_PER_RUN = 10
TOTAL_MESSAGES = 50

# HUAWEI ROUTER — read message counts and compute total drops per turtlebot

router_msg_files = [
    DATA / "router/cartographers/message_count/1.txt",
    DATA / "router/cartographers/message_count/2.txt",
    DATA / "router/cartographers/message_count/3.txt",
    DATA / "router/cartographers/message_count/4.txt",
]

router_total_drops = []
for file in router_msg_files:
    with open(file, "r") as f:
        received = [int(line.strip()) for line in f if line.strip()]
    drops = [TOTAL_MESSAGES_PER_RUN - r for r in received]
    router_total_drops.append(sum(drops))

# MOBILE HOTSPOT — no message drops recorded

mobile_total_drops = [0] * len(router_msg_files)

# Plot

x = list(range(1, len(router_msg_files) + 1))

plt.figure(figsize=(10, 5))

plt.plot(x, router_total_drops, marker="o", label="Huawei Router")
plt.plot(x, mobile_total_drops, marker="o", label="Mobile Hotspot")

plt.xlabel("Number of Turtlebots")
plt.ylabel("Total Messages Dropped (out of 50)")
plt.title("[MOBILE HOTSPOT VS HUAWEI ROUTER] Total Message Drops per Turtlebot")
plt.xticks(x)
plt.ylim(0, TOTAL_MESSAGES)
plt.grid(True)
plt.legend()

for xi, yi in zip(x, router_total_drops):
    plt.annotate(
        str(yi),
        (xi, yi),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center",
    )

for xi, yi in zip(x, mobile_total_drops):
    plt.annotate(
        str(yi),
        (xi, yi),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center",
    )

if save_image:
    plt.savefig(ANALYSIS / "message_drop_cartographers_per_turtlebot.png")

plt.show()
