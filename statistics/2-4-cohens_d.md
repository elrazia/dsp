[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```python
# imports
import numpy as np
import pandas as pd
import nsfg
import thinkstats2 as ts

# dataframe and variables
preg_df = nsfg.ReadFemPreg()
oldest = preg_df[preg_df['pregordr']==1]
younguns = preg_df[preg_df['pregordr']!=1]
```

```python
# total weight effect size
ts.CohenEffectSize(oldest.totalwgt_lb, younguns.totalwgt_lb)
```
> -0.06911825348820934

```python
# pregnancy length effect size
ts.CohenEffectSize(oldest.prglngth, younguns.prglngth)
```
> -0.03131178583370273

The data suggest that first babies tend to be ever so slightly lighter than babies born later in the order. Though the effect size for total weight is twice that of the effect size for pregnancy length, neither of these values are notable because the interpretation for Cohen's D suggests a value of 0.2 as a "small effect" and these values are a fraction of that benchmark.
