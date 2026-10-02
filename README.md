# Monte Carlo Estimation of π

A small computational experiment using Monte Carlo methods to estimate π and study how the statistical variation of the estimate changes with the number of samples.

## Overview

π can be estimated by generating random points in a square of side 1 and checking how many of them fall inside the quarter of a unit circle contained within the square.

The ratio of points inside the quarter circle to the total number of points approaches the ratio of their areas:

$$
\frac{N_{\mathrm{inside}}}{N} \approx \frac{\pi}{4}
$$

which gives

$$
\pi \approx 4\frac{N_{\mathrm{inside}}}{N}
$$

For this experiment, I used **100 independent trials** for each of the following sample sizes:

$$
N = 10^2,\ 10^3,\ 10^4,\ 10^5,\ 10^6
$$

For each sample size, the mean and standard deviation of the π estimates were calculated.

## Algorithm

For each value of $N$:

1. Generate $N$ random points $(x,y)$ in a square of side 1.
2. Check whether each point satisfies

$$
x^2 + y^2 \leq 1
$$

3. Use the fraction of points inside the quarter circle to estimate π:

$$
\pi_{\mathrm{est}} = 4\frac{N_{\mathrm{inside}}}{N}
$$

4. Repeat the calculation 100 times.
5. Calculate the mean and standard deviation of the 100 estimates.

I then looked at how the standard deviation changes with $N$.

The expected scaling is

$$
\sigma_\pi \propto N^{-1/2}
$$

Therefore, plotting the data on logarithmic axes should give approximately a straight line with a slope close to

$$
-\frac{1}{2}
$$

The scaling exponent was obtained using a linear fit between $\log(N)$ and $\log(\sigma_\pi)$.

## Mathematical Basis

The $N^{-1/2}$ scaling can be derived from binomial statistics.

For a randomly generated point, the probability of falling inside the quarter circle is

$$
p = \frac{\pi}{4}
$$

Therefore, the number of points inside the circle follows a binomial distribution:

$$
N_{\mathrm{inside}} \sim \mathrm{Binomial}(N,p)
$$

For a binomial distribution,

$$
\operatorname{Var}(N_{\mathrm{inside}}) = Np(1-p)
$$

Since

$$
\pi_{\mathrm{est}} = 4\frac{N_{\mathrm{inside}}}{N}
$$

the variance of the estimate is

$$
\operatorname{Var}(\pi_{\mathrm{est}})
=
\frac{16}{N^2}
\operatorname{Var}(N_{\mathrm{inside}})
$$

Substituting the binomial variance gives

$$
\operatorname{Var}(\pi_{\mathrm{est}})
=
\frac{16p(1-p)}{N}
$$

and therefore

$$
\sigma_\pi
=
4\sqrt{\frac{p(1-p)}{N}}
$$

Since $p$ is constant,

$$
\boxed{\sigma_\pi \propto N^{-1/2}}
$$

Thus, the statistical uncertainty is expected to decrease as the inverse square root of the number of samples.

## Results

The fitted scaling exponent was:

$$
\boxed{m = -0.5001}
$$

This is very close to the theoretically expected value:

$$
\boxed{m = -\frac{1}{2}}
$$

The result therefore agrees with the expected Monte Carlo scaling:

$$
\boxed{\sigma_\pi \propto \frac{1}{\sqrt{N}}}
$$

This demonstrates that increasing the number of random samples reduces the statistical variation of the Monte Carlo estimate according to the expected $1/\sqrt{N}$ law.

## Figures

### Monte Carlo estimation of π

![Monte Carlo estimation of π](results/monte_carlo_estimation_of_pi.png)

### Standard deviation scaling

![Standard deviation scaling](results/variation_in_pi.png)

### Absolute error

![Absolute error](results/error_in_pi_estimates.png)

## Requirements

Python 3

NumPy

Matplotlib

Install the required packages with:

```bash
pip install -r requirements.txt

