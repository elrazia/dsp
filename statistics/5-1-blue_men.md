[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```python
# imports
import scipy.stats as sp

# parameters of distribution
mu = 178
sigma = 7.7
```

```python
# generate distribution, find difference between cumulative densities of two heights (inches to centimeters by multiplying by 2.54)
distribution = sp.norm(loc=mu, scale=sigma)
distribution.cdf(70*2.54)-distribution.cdf(73*2.54)
```
> -0.34274683763147457

34.3% of males in the U.S. population qualify to join the Blue Man Group.
