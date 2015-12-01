

```python
import first
import thinkstats2
```

The problem asks to compute Cohen's d to quantify the difference between the the weight of first babies versus other babies.<br>
In order to do calculate Cohen's d, we first need to calculate 3 values:<br>

* The mean for the first babies group.
* The mean for the other babies group.
* The pooled standard deviation using both groups.

First the data is aggregated using the MakeFrames function.


```python
live,firsts,others = first.MakeFrames()
```

Next we calculate the values.


```python
weight_mean_firsts = firsts.totalwgt_lb.mean()
weight_mean_others = others.totalwgt_lb.mean()

weight_var_firsts = firsts.totalwgt_lb.var()
weight_var_others = others.totalwgt_lb.var()

n_firsts = len(firsts.totalwgt_lb)
n_others = len(others.totalwgt_lb)

pooled_var = (n_firsts * weight_var_firsts + n_others * weight_var_others) / (n_firsts + n_others)

weight_cohens_d = (weight_mean_firsts - weight_mean_others) / (pooled_var**.5)

print 'Mean Firsts:', weight_mean_firsts
print 'Mean Others:', weight_mean_others
print "Cohen's d for weight:", weight_cohens_d
```

    Mean Firsts: 7.20109443044
    Mean Others: 7.32585561497
    Cohen's d for weight: -0.0886729270726


The Cohen's d for pregnancy length between first babies and not first babies was .029 standard deviations.<br>
The Cohen's d for weight between first babies and not first babies was -.089.<br>
This implies that the effect of being a first baby has a greater impact on birth weight than it does pregnancy length.<br>
The sign of Cohen's d also leads to the conclusion that being a first baby reduces birthweight while it increases the pregnancy length.<br>
The effect size seems small relative to the example in the book of 1.7 for height.
