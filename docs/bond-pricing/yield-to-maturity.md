# Yield to Maturity (YTM)

## Definition
It is expected annual rate of return earned on a bond (check "Bonds: How They Work and How to Invest" by Jason Fernando on www.investopedia.com), assuming the debt security is held until maturity. 

Given the following three assumptions hold, the issuer expecting to earn from bond:

1. The return assumes the bond investor held onto the debt instrument until the maturity date.
2. All the interest payments (coupons) and principal repayment (at the maturity date) were made on schedule.
3. The coupon payments were reinvested at the same rate as the yield-to-maturity.
 

## 1. Equation (YTM approximation)
$$YTM = \frac{C + \frac{FV - PV}{n}}{\frac{FV + PV}{2}}$$

Where:
- C : Represents annual coupon of the bond. Bonds make interest payment that do not change through redemption time, which maturity of the bond comes to end. These payments called as coupons.
- FV : Face Value (sometimes referred to as the principal value). This is the money that the issuer returns to the holder at the maturity date.
- PV : Present Value. Current market price of the bond. This varying among higher or lower than the bond's FV based on the market conditions.
- n : Total number of coupon periods until maturity (e.g. years × payments per year)

## 2. Equation (Coupon-Bearing Bonds)
$$M = FVe^{-y(T-t)}+ \sum_{i = 1}^{N}Ce^{-y(t_i - t)}$$

- M : Current Market price of the bond
- FV : Face value
- C : Coupon and is paid at the time $t_{i}$
- T : Redemption date (Maturity date)
- t : Current time
- N : Number of remaining coupon payment times $t_{i}$ until T
- y : Yield to maturity expressed under continuous compounding.

This equation gives more accurate results than the approximation formula, provided the yield is quoted under continuous compounding (or equivalently the spot/zero‐rates use continuous compounding). In many real‐world bond markets, however, yields are calculated with discrete compounding (e.g. semi‐annual or annual), so one must check market convention before applying the continuous formula.

## Status 
*Learning in Progress* - Adding implementation and examples soon

## References

- Steve Bell, *Quantiative Finance for Dummies*, Wiley, pp. 75-76.
- Jason Fernando, *Yield to Maturity: What It Is and How It Works*, Investopedia.
- *Yield to Maturity (YTM) - Comprehensive Overview of Yield of Maturity and How to Calculate It*, wallstreetprep.com. May. 14, 2025.
- Adam Hayes, *Bond Yield: What It Is, Why It Matters, and How It's Calculated*, Investopedia