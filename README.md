# 🧭 Optimizing Multi-Robot Collaboration using TurtleBot3

This guide walks you through setting up multiple TurtleBot3 robots for collaborative SLAM and navigation using ROS 2 Humble and Cartographer.

---

## 🧩 Prerequisites

Before proceeding, ensure that:

- You have completed **Chapter 3** of the official [TurtleBot3 Manual](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/) on **both**:
  - The **Raspberry Pi** onboard each TurtleBot3.
  - Your **Laptop/PC** used for control and visualization.

---

## 🚀 Namespace Setup

When running multiple TurtleBots, each robot must have a **unique namespace** to prevent topic and parameter conflicts.

---

### 🦾 Raspberry Pi Setup

Follow the instructions in the [**TurtleBot3 Manual – Chapter 10.11.4**](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#load-multiple-turtlebot3s), under the section:

> **Load Multiple TurtleBot3s → Multi Robot Launch (in reality)**

In this project, we assigned the namespace to each robot following this format:

```
tb3_<TURTLEBOT_NUMBER>
```

Each turtlebot3 are labeled by number from 1 to 4. These numbers will replace the `<TURTLEBOT_NUMBER>` format. For example, if the turtlebot3 is labeled by number 2, the namespace will be formatted as `tb3_2`

---

### 💻 Laptop Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/kenpegrasio/turtleswarm.git
   cd turtleswarm
   ```

2. **Copy the corresponding Cartographer package**

   Replace `<TURTLEBOT_NUMBER>` with the appropriate robot ID.

   ```bash
   cp -r tb3_<TURTLEBOT_NUMBER>_cartographer ~/turtlebot3_ws/src/turtlebot3
   ```

3. **Rebuild the workspace**
   ```bash
   cd ~/turtlebot3_ws
   colcon build --packages-select tb3_<TURTLEBOT_NUMBER>_cartographer
   source install/setup.bash
   ```

4. **Launch Cartographer**
   ```bash
   ros2 launch tb3_<TURTLEBOT_NUMBER>_cartographer cartographer.launch.py namespace:=tb3_<TURTLEBOT_NUMBER>
   ```

---

## 📝 Renaming the Namespace

If you wish to use a different namespace (e.g. `robot_alpha`), simply:

1. Replace all instances of `tb3_<TURTLEBOT_NUMBER>` for any value of `<TURTLEBOT_NUMBER>` in this repository with your new namespace in:
   - All related files in **Raspberry Pi Setup**
   - All related files in **Laptop Setup**.

2. Rebuild your workspace again:
   ```bash
   colcon build
   source install/setup.bash
   ```