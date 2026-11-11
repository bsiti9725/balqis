import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ===============================
# SIMULASI PUSAT MASSA
# ===============================

m1 = 2
m2 = 4

x1 = 2
x2 = 8

fig, ax = plt.subplots(figsize=(10, 5))

ax.set_xlim(0, 10)
ax.set_ylim(-2, 3)

ax.set_title("SIMULASI FISIKA: PUSAT MASSA")
ax.set_xlabel("Posisi (meter)")
ax.set_ylabel("Sumbu Y")

ax.grid(True)

# Benda pertama
benda1, = ax.plot([], [], 'bo', markersize=20, label="Benda 1")

# Benda kedua
benda2, = ax.plot([], [], 'ro', markersize=25, label="Benda 2")

# Pusat massa
pusat, = ax.plot([], [], 'go', markersize=15, label="Pusat Massa")

# Garis pusat massa
garis, = ax.plot([], [], 'g--')

# Informasi hasil
info = ax.text(
    0.5, 2.5, "",
    fontsize=12,
    bbox=dict(facecolor='yellow', alpha=0.5)
)

ax.legend()

def update(frame):

    # Gerakan benda
    posisi1 = x1 + 1.5 * np.sin(frame * 0.05)
    posisi2 = x2 + 1.5 * np.cos(frame * 0.05)

    # Perhitungan pusat massa
    xp = (m1 * posisi1 + m2 * posisi2) / (m1 + m2)

    # Update posisi benda
    benda1.set_data([posisi1], [0])
    benda2.set_data([posisi2], [0])

    pusat.set_data([xp], [0])

    garis.set_data([posisi1, xp, posisi2], [0, 0, 0])

    info.set_text(
        f"Massa 1 = {m1} kg\n"
        f"Massa 2 = {m2} kg\n"
        f"Pusat Massa = {xp:.2f} meter"
    )

    return benda1, benda2, pusat, garis, info

ani = FuncAnimation(
    fig,
    update,
    frames=500,
    interval=50,
    blit=False
)

plt.show()
