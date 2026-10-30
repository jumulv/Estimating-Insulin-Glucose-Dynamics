import matplotlib.pyplot as plt
import scienceplots  # noqa: F401

plt.style.use("science")
plt.style.use("grid")
plt.style.use("bright")

# for thesis
# SMALL_SIZE = 10
# MEDIUM_SIZE = 12
# LARGE_SIZE = 14

# base_params = {
#     'figure.constrained_layout.use': True,
#     'font.size': MEDIUM_SIZE,
#     'axes.titlesize': LARGE_SIZE,
#     'axes.labelsize': MEDIUM_SIZE,
#     'xtick.labelsize': SMALL_SIZE,
#     'ytick.labelsize': SMALL_SIZE,
#     'legend.fontsize': SMALL_SIZE,
#     'figure.titlesize': LARGE_SIZE,
#     'lines.linewidth': 1.5,
#     'lines.markersize': 5,
#     'patch.linewidth': 0.5,
# }

# for presentation
SMALL_SIZE = 16
MEDIUM_SIZE = 18
LARGE_SIZE = 22

base_params = {
    "figure.constrained_layout.use": True,
    "font.size": MEDIUM_SIZE,
    "axes.titlesize": LARGE_SIZE,
    "axes.labelsize": MEDIUM_SIZE,
    "xtick.labelsize": SMALL_SIZE,
    "ytick.labelsize": SMALL_SIZE,
    "legend.fontsize": SMALL_SIZE,
    "figure.titlesize": LARGE_SIZE,
    "lines.linewidth": 2.5,
    "lines.markersize": 7,
    "patch.linewidth": 0.8,
}

plt.rcParams.update(base_params)
