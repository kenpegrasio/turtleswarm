import psutil

print(psutil.cpu_percent(interval=1))

ram = psutil.virtual_memory()
print("RAM usage (%):", ram.percent)
print("RAM used (GB):", round(ram.used / 1e9, 2))