# Poisson Distribution

**Probability Mass Function**
$$P(X=k) = e^{-\lambda} \cdot \frac{\lambda^k}{k!}, \quad k=0,1,2,\ldots$$

**Mean / Var**
$$E[X] = \lambda, \quad \text{Var}(X)=\lambda$$

**Use-cases**
Count of rare, independent events per unit time/space (arrivals, default, trades, jumps in commodity prices)

**Poisson as Binomial Limit**
If $X_n \sim \text{Pois}(\lambda)$ as $n\to\infty$.
Key Limits:
- $M_X(t) = \exp\(\lambda(e^t-1))$

**Notebook**: `notebooks/math-notebook/poisson_from_binomial.ipynb`
**Module**: `src/math-src/poisson.py`