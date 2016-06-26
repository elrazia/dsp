[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```python
# imports
import random
import thinkstats2 as ts
import thinkplot as tp
%matplotlib inline
```

```python
# generate random numbers, create pmf and cdf
nums = [random.random() for i in range(1000)]
pmf = ts.Pmf(nums, label="probability mass")
cdf = ts.Cdf(nums, label="cumulative density")
```

```python
# pmf plot
tp.Pmf(pmf)
tp.Show(xlabel="number", ylabel="mass",axis=[0, 1, 0.000, 0.002])

# cdf plot
tp.Cdf(cdf)
tp.Show(xlabel="number", ylabel="cumulative density", axis=[0, 1, 0, 1])
```

The distribution is indeed approximately uniform. Both the pmf and the cdf are able to show this, though the cdf produces a better visualization. The CDF's line is diagonal and mostly straight, indicating that the cumulative densities are increasing at the same rate (uniformity).
