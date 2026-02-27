"""Linear Algebra: Least Squares Example 1

This module demonstrates least squares regression with different design matrices,
showing how to fit various models (constant, linear, quadratic) to data.

Course: Linear algebra: theory and implementation
Section: Least-squares
Topic: Least-squares example 1
"""

import numpy as np
import matplotlib.pyplot as plt


def fit_least_squares(X, y):
    """Fit a least squares model using the normal equations.
    
    Parameters
    ----------
    X : ndarray
        Design matrix of shape (n_samples, n_features).
    y : ndarray
        Target values of shape (n_samples, 1) or (n_samples,).
        
    Returns
    -------
    ndarray
        Coefficient vector that minimizes ||Xb - y||^2.
        
    Notes
    -----
    Uses the normal equation: b = (X^T X)^(-1) X^T y
    This is solved using np.linalg.solve for numerical stability.
    """
    return np.linalg.solve(X.T @ X, X.T @ y)


def plot_fit(data, y_predicted, x_axis, model_name):
    """Plot data and model predictions.
    
    Parameters
    ----------
    data : ndarray
        Actual data points.
    y_predicted : ndarray
        Model predictions.
    x_axis : ndarray
        X-axis values for plotting.
    model_name : str
        Name of the model for the title.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x_axis, data, 'bs-', linewidth=2, markersize=8, label='Data')
    plt.plot(x_axis, y_predicted, 'ro--', linewidth=2, markersize=8, 
             label='Model prediction', alpha=0.7)
    plt.xlabel('Sample index', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.title(f'Least Squares Fit: {model_name}', fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.show()


def fit_constant_model(data):
    """Fit a constant model (just the mean).
    
    Parameters
    ----------
    data : ndarray
        Input data.
        
    Returns
    -------
    tuple
        (coefficient, predictions)
    """
    print("\n" + "=" * 60)
    print("Model 1: Constant Model (Mean)")
    print("=" * 60)
    
    N = len(data)
    
    # Design matrix: column of ones
    X = np.ones((N, 1))
    
    # Fit the model
    b = fit_least_squares(X, data)
    
    # Compare with numpy mean
    mean_val = np.mean(data)
    
    print(f"Least squares coefficient: {b[0, 0]:.4f}")
    print(f"NumPy mean:                {mean_val:.4f}")
    print(f"Difference:                {abs(b[0, 0] - mean_val):.2e}")
    
    # Compute predictions
    y_hat = X @ b
    
    return b, y_hat


def fit_slope_model(data):
    """Fit a model with only a slope term (no intercept).
    
    Parameters
    ----------
    data : ndarray
        Input data.
        
    Returns
    -------
    tuple
        (coefficient, predictions)
    """
    print("\n" + "=" * 60)
    print("Model 2: Slope Only (No Intercept)")
    print("=" * 60)
    
    N = len(data)
    
    # Design matrix: just indices
    X = np.arange(N).reshape(-1, 1)
    
    # Fit the model
    b = fit_least_squares(X, data)
    
    print(f"Slope coefficient: {b[0, 0]:.4f}")
    
    # Compute predictions
    y_hat = X @ b
    
    return b, y_hat


def fit_linear_model(data):
    """Fit a linear model with intercept and slope.
    
    Parameters
    ----------
    data : ndarray
        Input data.
        
    Returns
    -------
    tuple
        (coefficients, predictions)
    """
    print("\n" + "=" * 60)
    print("Model 3: Linear Model (Intercept + Slope)")
    print("=" * 60)
    
    N = len(data)
    
    # Design matrix: intercept and slope terms
    X = np.concatenate([np.ones((N, 1)), np.arange(N).reshape(-1, 1)], axis=1)
    
    # Fit the model
    b = fit_least_squares(X, data)
    
    print(f"Intercept: {b[0, 0]:.4f}")
    print(f"Slope:     {b[1, 0]:.4f}")
    print(f"Model: y = {b[0, 0]:.4f} + {b[1, 0]:.4f}*x")
    
    # Compute predictions
    y_hat = X @ b
    
    return b, y_hat


def fit_quadratic_model(data):
    """Fit a quadratic model with intercept and squared term.
    
    Parameters
    ----------
    data : ndarray
        Input data.
        
    Returns
    -------
    tuple
        (coefficients, predictions)
    """
    print("\n" + "=" * 60)
    print("Model 4: Quadratic Model (Intercept + x^2)")
    print("=" * 60)
    
    N = len(data)
    
    # Design matrix: intercept and squared terms
    X = np.concatenate([np.ones((N, 1)), (np.arange(N) ** 2).reshape(-1, 1)], axis=1)
    
    # Fit the model
    b = fit_least_squares(X, data)
    
    print(f"Intercept:        {b[0, 0]:.4f}")
    print(f"Quadratic coeff:  {b[1, 0]:.4f}")
    print(f"Model: y = {b[0, 0]:.4f} + {b[1, 0]:.4f}*x^2")
    
    # Compute predictions
    y_hat = X @ b
    
    return b, y_hat


def main():
    """Main function demonstrating various least squares models."""
    print("=" * 60)
    print("Least Squares Regression Examples")
    print("=" * 60)
    
    # Sample data
    data = np.array([[-4, 0, -3, 1, 2, 8, 5, 8]]).T
    N = len(data)
    x_axis = np.arange(1, N + 1)
    
    print(f"\nData: {data.T[0]}")
    print(f"Number of samples: {N}")
    
    # Model 1: Constant (mean)
    _, y_hat1 = fit_constant_model(data)
    plot_fit(data, y_hat1, x_axis, "Constant (Mean)")
    
    # Model 2: Slope only
    _, y_hat2 = fit_slope_model(data)
    plot_fit(data, y_hat2, x_axis, "Slope Only")
    
    # Model 3: Linear (intercept + slope)
    _, y_hat3 = fit_linear_model(data)
    plot_fit(data, y_hat3, x_axis, "Linear")
    
    # Model 4: Quadratic (intercept + x^2)
    _, y_hat4 = fit_quadratic_model(data)
    plot_fit(data, y_hat4, x_axis, "Quadratic")
    
    print("\n" + "=" * 60)
    print("All models fitted successfully!")
    print("=" * 60)


if __name__ == '__main__':
    main()
