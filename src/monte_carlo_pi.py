import numpy as np
from matplotlib import pyplot as plt

plt.ion()
pi_values = []
std_values = []
tries = 0
q = 2

while tries < 5:

    n = 10**q
    q += 1

    trials = 0
    current_values = []

    while trials < 100:
        x = np.random.uniform(0, 1, n)
        y = np.random.uniform(0, 1, n)

        inside = x**2 + y**2 <= 1

        # You can uncomment this part to visualize each Monte Carlo trial
        
        # x_inside = x[inside]
        # y_inside = y[inside]
        # x_outside = x[~inside]
        # y_outside = y[~inside]

        # plt.scatter(x_inside,y_inside)
        # plt.scatter(x_outside,y_outside)
        # plt.axis('equal')
        # plt.title(f"Try {tries + 1} | N = {n}")
        # plt.pause(0.5)
        # plt.clf()

        n_inside = np.sum(inside)
        n_total = len(x)
        pi_estimate = 4 * (n_inside / n_total)

        current_values.append(float(pi_estimate))

        trials += 1

    mean_pi = np.mean(current_values)
    std = np.std(current_values)

    print(f"For n = {n}, estimated pi is {mean_pi:.8f}")

    pi_values.append(mean_pi)
    std_values.append(std)

    tries += 1

print(f"\nActual pi: {np.pi:.8f}")

plt.ioff()

estimates = [10**q for q in range(2, 7)]
error_list = [np.abs(np.pi - value) for value in pi_values]

plt.figure()
plt.plot(estimates, pi_values, marker="o", label="Monte Carlo estimate")
plt.xscale('log')
plt.axhline(np.pi, color="red", linestyle="--", label="Actual pi")
plt.xlabel("Number of points per trial")
plt.ylabel("Estimated value of pi")
plt.title("Monte Carlo Estimation of Pi")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

plt.figure()
plt.plot(estimates, std_values, marker="o")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Number of points per trial")
plt.ylabel("Standard deviation")
plt.title("Variation in Pi Estimates")
plt.grid(True, which="both", alpha=0.3)
plt.show()

plt.figure()
plt.plot(estimates, error_list, marker="o")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Number of points per trial")
plt.ylabel("Absolute error")
plt.title("Error in Pi Estimates")
plt.grid(True, which="both", alpha=0.3)
plt.show()

X = np.log(estimates)
Y = np.log(std_values)
m, c = np.polyfit(X, Y, deg=1)

print(f"\nLog-log slope: {m:.4f}")
print(f"Log-log intercept: {c:.4f}")
