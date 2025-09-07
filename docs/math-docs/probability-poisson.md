# Poisson Distribution

**Probability Mass Function**
$$
P(X=k) = e^{-\lambda}\frac{\lambda^k}{k!}, \; k=0,1,2,\dots
$$

**Mean / Var**
$$
\mathbb{E}[X] = \lambda,\quad \mathrm{Var}(X)=\lambda 
$$

**Use-cases**
Count of rare, independent events per unit time/space (arrivals, default, trades, jumps in commodity prices)

**Poisson as Binomial Limit**
If \(X_n \sim \mathrm{Pois}(\lambda)\) as \(n\to\infty\)
Key Limits:
- \(M_X(t) = \exp\{\lambda(e^t-1)\}\)

**Notebook**: `notebooks/math-notebook/poisson_from_binomial.ipynb`
**Module**: `src/math-src/poisson.py`