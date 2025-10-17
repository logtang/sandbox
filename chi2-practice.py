import numpy as np
from scipy.stats import chisquare

# Load all raw color IDs (1–6)
data = np.loadtxt('data/colorshirt.dat', dtype=int)

# Count frequency of each color
# np.bincount counts 0-indexed, so we add 1 dummy zero at front
counts = np.bincount(data)[1:]  # ignore the 0th bin
print("Observed counts:", counts)

# Expected: equal frequency for all six shirt colors
expected = np.full_like(counts, fill_value=np.mean(counts))

# Chi-squared test
chi2_stat, p_value = chisquare(f_obs=counts, f_exp=expected)
print(f"Chi-squared statistic: {chi2_stat:.3f}")
print(f"P-value: {p_value:.6f}")

# Contributions (optional)
colors = ['Black', 'White', 'Red', 'Yellow', 'Blue', 'Green']
contribs = (counts - expected)**2 / expected
for c, val in zip(colors, contribs):
    print(f"{c:>7}: {val:.3f}")
