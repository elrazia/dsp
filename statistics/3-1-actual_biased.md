[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python
# imports
import thinkplot as tp
import thinkstats2 as ts
import chap01soln
import matplotlib.pyplot as plt
%matplotlib inline

# dataframe
res = chap01soln.ReadFemResp()

# biased pmf function
def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
```

```python
# actual and biased pmfs
pmf = ts.Pmf(res['numkdhh'],label='actual')
bpmf = BiasPmf(pmf,label='biased')

# plot
tp.Pmfs([pmf,bpmf])
tp.Show(xlabel='Number of Children',ylabel='PMF')
```

```python
pmf.Mean()
```
> 1.0242051550438309

```python
bpmf.Mean()
```
> 2.4036791006642821
