import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

nsample = 100
np.random.seed(7654321)

fig = plt.figure()
ax = fig.add_subplot(111)
#x = stats.loggamma.rvs(c=2.5, size=500)
#x = stats.t.rvs(3, size=nsample)
#res = stats.probplot(x, dist=stats.loggamma, sparams=(2.5,), plot=ax)
#x = stats.t.rvs(5, size=nsample)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
res = stats.probplot(x, plot=plt)

ax.set_title("Probplot for Normal dist 0, 1")

plt.show()
