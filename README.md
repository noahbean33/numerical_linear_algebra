# Linear Algebra: Theory and Implementation - Python Code

This repository contains Python implementations of linear algebra concepts from the course "Linear algebra: theory and implementation" by sincxpress.com.

## Repository Status

✅ **Refactored and Improved** (November 2024)
- All Jupyter notebooks removed
- Code refactored with best practices
- Comprehensive documentation added
- Bugs fixed and code quality improved

## Structure

The repository is organized by topic:

- **`eig/`** - Eigendecomposition (eigenvalues, eigenvectors, diagonalization)
- **`intro/`** - Introduction to linear algebra concepts
- **`introMatrices/`** - Basic matrix operations
- **`inverse/`** - Matrix inverse operations
- **`leastsquares/`** - Least squares regression
- **`matrixDet/`** - Matrix determinants
- **`matrixMults/`** - Matrix multiplication operations
- **`projorth/`** - Projections and orthogonalization
- **`quadformDefinite/`** - Quadratic forms
- **`rank/`** - Matrix rank
- **`spaces/`** - Vector spaces
- **`svd/`** - Singular Value Decomposition
- **`systems/`** - Systems of equations
- **`vectors/`** - Vector operations

## Running the Code

Each Python file is a standalone script that can be run directly:

```bash
# Example: Run eigenvalue demonstrations
python eig/LA_eig_eigenvalues.py

# Example: Run vector dot product demonstrations
python vectors/LA_vectors_dotProduct.py

# Example: Run SVD demonstrations
python svd/LA_svd_TheSVD.py
```

## Requirements

```bash
pip install numpy matplotlib scipy
```

Or create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install numpy matplotlib scipy
```

## Code Quality

All refactored scripts follow these best practices:

- ✅ **Proper functions** instead of script-style code
- ✅ **Comprehensive docstrings** (NumPy style)
- ✅ **Type hints** where appropriate
- ✅ **Main guards** (`if __name__ == '__main__':`)
- ✅ **Error handling** with try-except blocks
- ✅ **Clear visualizations** with labeled plots
- ✅ **Bug fixes** for common issues

## Refactoring Status

See `REFACTORING_SUMMARY.md` for detailed information about:
- Bugs that were fixed
- Best practices applied
- Refactored files (11 examples completed)
- Remaining files to refactor (29 files)
- Refactoring template and guidelines

## Example: Refactored Code

### Before (Original)
```python
# matrix
A = [ [1,5], [2,3] ]

# extract the eigenvalues
eigvals = np.linalg.eig(A)

print(eigvals[0])
```

### After (Refactored)
```python
"""Linear Algebra: Finding Eigenvalues

This module demonstrates eigenvalue extraction and visualization.
"""

import numpy as np
import matplotlib.pyplot as plt


def extract_eigenvalues(matrix):
    """Extract eigenvalues from a square matrix.
    
    Parameters
    ----------
    matrix : array_like
        A square matrix.
        
    Returns
    -------
    ndarray
        Array of eigenvalues.
    """
    eigenvalues, _ = np.linalg.eig(matrix)
    return eigenvalues


def main():
    """Main demonstration function."""
    A = np.array([[1, 5], 
                  [2, 3]])
    
    eigenvals = extract_eigenvalues(A)
    print(f"Eigenvalues: {eigenvals}")


if __name__ == '__main__':
    main()
```

## Contributing

When modifying code:
1. Follow the refactoring template in `REFACTORING_SUMMARY.md`
2. Add comprehensive docstrings
3. Test your changes
4. Ensure code follows PEP 8 style guidelines

## Course Information

- **Course**: Linear algebra: theory and implementation
- **Instructor**: sincxpress.com
- **Course URL**: https://www.udemy.com/course/linear-algebra-theory-and-implementation/

## License

Please refer to the course materials for licensing information.

## Contact

For questions about the refactoring work, refer to `REFACTORING_SUMMARY.md`.
