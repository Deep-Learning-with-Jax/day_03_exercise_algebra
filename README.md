## Linear Algebra Exercise
Welcome to the exercise repository for day 3 of our course.
To help you, we have prepared unit-tests.
Use:
```shell
nox -s test
```
While coding, use `nox -s lint`, and `nox -s typing` to check your code.
Autoformatting help is available via `nox -s format`.
Feel free to read more about nox at https://nox.thea.codes/en/stable/ .


### Part 1: Proof of concept
Use `b = pandas.read_csv('./data/noisy_signal.tab')` to load a noisy signal.
The first part will be concerned with modeling this signal using polynomials.

#### Regression
Linear regression is usually a good first step. Start by implementing the function
`set_up_point_matrix` from the `src/regularization.py` module. 
The function should produce polynomial-coordinate matrices $\mathbf{A}_m$ of the form:

$$
\mathbf{A}_m = 
\begin{pmatrix}
          1       & x_1^1    & x_1^2  & \dots & x_1^m  \\\\ 
          1       & x_2^1    & x_2^2  & \dots & x_2^m  \\\\
          1       & x_3^1    & x_3^2  & \dots & x_3^m  \\\\
          \vdots  & \vdots   & \vdots  & \ddots & \vdots \\\\ 
          1       & x_n^1    & x_n^2  & \dots & x_n^m  \\\\
   \end{pmatrix}
$$

With m=2,

$$\mathbf{A}_m^{\dagger}\mathbf{b} = \mathbf{x}$$

will produce the coefficients for a straight line. Evaluate your first-degree polynomial via ax+b.
Plot the result using `matplotlib.pyplot`'s `plot` function.


#### Fitting a Polynomial to a function
The straight line above is insufficient to model the data. Using your 
implementation of `set_up_point_matrix` set n=300 and fit the polynomial
by computing

$$\mathbf{A}^{\dagger}\mathbf{b} = \mathbf{x}_{\text{fit}}.$$

Having estimated the coefficients

$$\mathbf{A} \mathbf{x}_{\text{fit}}$$

computes the function values. Plot the original points and the function values using matplotlib.
What do you see?



#### Regularization
Unfortunately, the fit is not ideal. The polynomial tracks the noise.
The singular value decomposition (SVD) can help!
Recall that the SVD turns a matrix

$$\mathbf{A} \in \mathbb{R}^{m,n}$$

into the form:

$$
      \mathbf{A}
      = \mathbf{U} \Sigma \mathbf{V}^T 
      = \mathbf{U}
      \begin{pmatrix}
      \sigma_1 & & \\\\
      & \ddots &  \\\\
      & & \sigma_m \\\\ \hline 
      & 0 & \\\\
      \end{pmatrix} \mathbf{V}^T
$$

In the SVD-Form computing, the inverse is simple. Swap U and V  and replace every of the m singular values with it's inverse

$$1/\sigma_i .$$

A solution to the overfitting problem is to filter the singular values.
Compute a diagonal for a filter matrix by evaluating:

$$f_i = \sigma_i^2 / (\sigma_i^2 + \epsilon)$$

The idea is to compute a loop over i for all of the m singular values.
Roughly speaking multiplication by f underscore i will filter a singular value when

$$\sigma_i &lt; \epsilon .$$

Apply the regularization by computing:


$$
    \mathbf{x}_r= \mathbf{V} \mathbf{F} \begin{pmatrix}
      \sigma_1^{-1} & & & \\\\
      &  \ddots & \\\\
      &  & \sigma_m^{-1} \\\\ \hline
      & 0 &
    \end{pmatrix}
    \mathbf{U}^T \mathbf{b}
$$


with

$$\mathbf{A} \in \mathbb{R}^{m,n}, \mathbf{U} \in \mathbb{R}^{m,m}, \mathbf{V} \in \mathbb{R}^{n,n}, \mathbf{F} \in \mathbb{R}^{m,m}, \Sigma^{\dagger} \in \mathbb{R}^{n,m} \text{ and } \mathbf{b} \in \mathbb{R}^{n,1}.$$
  
Setting m=300 turns A into a square matrix. In this case, the zero block in the sigma-matrix disappears.
Plot the result for epsilon equal to 0.1, 1e-6, and 1e-12.


### Part 2: Real data analysis
Now we are ready to deal with real data! Feel free to use your favorite time series data or work with the Rhine level data we provide.
The file `./data/pegel.tab` contains the Rhine water levels measured in Bonn over the last 100 years. 
Data source https://pegel.bonn.de .

#### Regression
The `src/pegel_bonn.py` file already contains code to pre-load the data for you.
Make the Rhine level measurements your new vector $\mathbf{b}$.
Generate a matrix A by setting m=2 and compute 

$$\mathbf{A}^{\dagger}\mathbf{b}.$$

Plot the result. Compute the zero. When do the regression line and the x-axis intersect?

#### Fitting a higher order Polynomial

Re-using the code you wrote for the proof of concept task, fit a polynomial of degree 20 to the data.
Plot the result.


#### Regularization
Something happened around the year 2000. To investigate further, focus on the data from 2000 onward and
filter the singular values.
Matrix A is not square in this case. Consequently, a zero block must appear in your singular value matrix. 
Plot filtered eigen-polynomials using epsilon equal to 0.1, 1e-3, 1e-9.
