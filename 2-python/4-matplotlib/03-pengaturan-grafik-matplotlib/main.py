# 27 / 10 / 2023
# Day - 36
# Pengaturan Grafik Matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 20, 0.5)
y = x**2

fig = plt.figure(figsize=(4, 4), dpi=100)
axes = fig.add_axes([0, 0, 1, 1])
print(axes.plot(x, y))

fig1, axes1 = plt.subplots(2, 1, figsize=(4,8), dpi=200)
print(axes1[0].plot(x,y))
print(axes1[0].set_title("Grafik 1"))

print(axes1[1].plot(x,y))
print(axes1[1].set_title("Grafik 2"))

print(plt.tight_layout())
print(plt.show())

# melakukan save plot grafik yang sudah dibuat
print(fig1.savefig("gambarku.png"))
print(fig1.savefig("gambarku2.png", dpi=300))

# menambahkan Legenda / Legend
# yaitu keterangan didalam sebuah grafik
fig3 = plt.figure(facecolor="yellow", dpi=200)
axes2 = fig3.add_axes([0,0,1,1])
print(axes2.plot(x, y, label="Pangkat 2"))
print(axes2.plot(x, x**3, label="Pangkat 3"))
print(axes2.plot(x, x**4, label="Pangkat 4"))

# menambahkan Legend
print(axes2.legend(loc=(0.5, 0.5)))

# menambahkan Grid
print(axes2.grid(True))
print(plt.show())

# penggunaan linewidth, linestyle & marker
# linewidth / lw = ketebalan dari sebuah garis
# linestyle / ls = tipe garis {'-', '--', '-.', ':', '', (offset, on-off-seq), ...} 
# marker = perpotongan sumbu x dan sumbu y
fig4 = plt.figure()
axes3 = fig4.add_axes([0,0,1,1])

print(axes3.plot(x, y, label="Pangkat 2", lw=1, ls=":", marker="o", markersize=5, mfc="yellow", mew=1, mec="red"))
print(axes3.plot(x, x**3, label="Pangkat 3", lw=2, ls="--", marker="*", markersize=5, mfc="blue", mew=1))
print(axes3.plot(x, x**4, label="Pangkat 4", lw=3.5, ls="-.", marker="+", markersize=5, mfc="yellow", mew=1, mec="red"))

print(axes3.legend(loc=0))
print(axes3.grid(True))

# membatasi batas extend batas y
# print(axes3.set_xlim(left, right, emit=True, auto=False))
print(axes3.set_xlim([0, 12.5]))
print(axes3.set_ylim([0, 2500]))

print(plt.show())
