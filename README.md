## Linear algebra exercise - matrix multiplication
Implement matrix multiplication as discussed in the lecture. 
We saw that multiplication of matrix 
$ \mathbf{A} \in \mathbb{R}^{m,n } $
with m rows and n columns and matrix
$\mathbf{B} \in \mathbb{R}^{n,p }$
with n rows and o columns resulted in a third matrix
$\mathbf{C} \in \mathbb{R}^{m,p}$
with m rows and o columns.

The product of
$\mathbf{A}$ 
and
$\mathbf{B}$ is given by:
$$ c_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj} $$
with
$ i = 1, \dots , m $
and
$ j = 1, \dots, p $

please finish the `my_multiply` function in the `matrix_multiply.py` module.
Keep in mind that python starts counting at 0.

Use:
```shell
nox -s test
```
the check your solution.
