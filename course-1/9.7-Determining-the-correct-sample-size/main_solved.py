import scipy.stats as stats

alpha = 0.05  # For a 95% confidence interval, alpha is 5%
sigma = 0.2  # The standard deviation of the customers
E = 0.05     # The expected effect size (MoE)

# Calculate the required Z-score
z = stats.norm.ppf(1 - alpha / 2)

# Define a function to calculate the sample size
def samp_size(z, E, sigma):
    out = ((z * sigma) / E) ** 2
    return out

n = samp_size(z, E, sigma)

print("Required Sample Size:", n)
