

```python
import hypothesis
import first
import numpy as np
```

The `DiffMeansPermute` object has a `pool` property and length properties for the two original groups.<br>

The resampling method we'll implement draws values from the pool with replacement into two groups with sizes corresponding to the original groups.


```python
class DiffMeansResample(hypothesis.DiffMeansPermute):

    def RunModel(self):
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.m, replace=True)

        return group1, group2
```

First we'll get the data, then apply our two models, Resample and Permute.


```python
live, firsts, others = first.MakeFrames()
```


```python
data_prglngth = firsts['prglngth'].values, others['prglngth'].values
```


```python
resample = DiffMeansResample(data_prglngth)
permute = hypothesis.DiffMeansPermute(data_prglngth)

print 'Original test statistic:', resample.actual
print 'Resample p-value:', resample.PValue(iters=10000)
print 'Resample test statistic:', resample.MaxTestStat()
print 'Permute p-value:', permute.PValue(iters=10000)
print 'Permute test statistic', permute.MaxTestStat()
```

    Original test statistic: 0.0780372667775
    Resample p-value: 0.1676
    Resample test statistic: 0.240934208256
    Permute p-value: 0.1657
    Permute test statistic 0.224261284278



```python
data_wgt = firsts['totalwgt_lb'].dropna().values, others['totalwgt_lb'].dropna().values
```


```python
resample = DiffMeansResample(data_wgt)
permute = hypothesis.DiffMeansPermute(data_wgt)

print 'Original test statistic:', resample.actual
print 'Resample p-value:', '%.15f' % resample.PValue(iters=10000)
print 'Resample test statistic:', resample.MaxTestStat()
print 'Permute p-value:', '%.15f' % permute.PValue(iters=10000)
print 'Permute test statistic', permute.MaxTestStat()
```

    Original test statistic: 0.124761184535
    Resample p-value: 0.000100000000000
    Resample test statistic: 0.126943748537
    Permute p-value: 0.000000000000000
    Permute test statistic 0.11642529364


For both pregnancy length and total weight, the original test statistic is the same for resample and permute.  This makes sense because the test statistic is calculated using the same values for the data.<br>

The p-values differ slightly although both fall in a similar range.  The test statistic for the data with resample is higher than the test statistic using permute.<br>

The difference between the resample and permute functions is the use of replacement.  <br>

The test statistic is the difference between the means of the groups, having replacement enables the two groups to have the largest possible difference.  As a result the max test statistic should be slightly higher for resample.  The experiment shows that the test statistics are close to each other.<br>

P-value is the fraction of test statistics that exceed the original test statistic.  The p-values appear to be very close as well.  Both tests would lead to the same conclusions.


```python

```
