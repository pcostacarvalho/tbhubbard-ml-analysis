"""Regression helpers used by the modeling notebooks (e.g. 03, 05)."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_regression(model, X_train, y_train, X_test=None, y_test=None):
    """
    RMSE, R², and MAE on train and optional test data.

    Assumes ``model.predict(X)`` is on the same scale as ``y_train`` / ``y_test``
    (e.g. statsmodels OLS with no separate inverse transform).

    Parameters
    ----------
    model : object
        Fitted model with a ``predict`` method.
    X_train : array-like
        Training design matrix (include intercept column if the model was fit with one).
    y_train : array-like
        Training targets.
    X_test, y_test : array-like, optional
        If both are given, test metrics are computed.

    Returns
    -------
    dict
        ``rmse_train``, ``r2_train``, ``mae_train``, and when test data are provided
        ``rmse_test``, ``r2_test``, ``mae_test``.
    """
    metrics: dict[str, float] = {}

    y_train = pd.Series(y_train).reset_index(drop=True)
    y_pred_train = pd.Series(model.predict(X_train), dtype=float).reset_index(drop=True)
    metrics["rmse_train"] = float(np.sqrt(mean_squared_error(y_train, y_pred_train)))
    metrics["r2_train"] = float(r2_score(y_train, y_pred_train))
    metrics["mae_train"] = float(mean_absolute_error(y_train, y_pred_train))

    print(f"Training RMSE: {metrics['rmse_train']:.4f}")
    print(f"Training R²: {metrics['r2_train']:.4f}")
    print(f"Training MAE: {metrics['mae_train']:.4f}")

    if X_test is not None and y_test is not None:
        y_test = pd.Series(y_test).reset_index(drop=True)
        y_pred_test = pd.Series(model.predict(X_test), dtype=float).reset_index(drop=True)
        metrics["rmse_test"] = float(np.sqrt(mean_squared_error(y_test, y_pred_test)))
        metrics["r2_test"] = float(r2_score(y_test, y_pred_test))
        metrics["mae_test"] = float(mean_absolute_error(y_test, y_pred_test))

        print(f"Test RMSE: {metrics['rmse_test']:.4f}")
        print(f"Test R²: {metrics['r2_test']:.4f}")
        print(f"Test MAE: {metrics['mae_test']:.4f}")

    return metrics


def breusch_pagan(model):
    """
    Breusch–Pagan test for heteroscedasticity (auxiliary regression of squared residuals on fitted values).

    Parameters
    ----------
    model : statsmodels.regression.linear_model.RegressionResults
        Fitted OLS-style results with ``fittedvalues`` and ``resid``.

    Returns
    -------
    lm_stat : float
        Lagrange multiplier statistic (n × R² from the auxiliary regression).
    p_value : float
        Asymptotic p-value, χ² with 1 degree of freedom.
    """
    yhat = model.fittedvalues
    resid = model.resid
    resid2 = resid**2
    aux = sm.OLS(resid2, sm.add_constant(yhat)).fit()
    n = int(aux.nobs)
    lm_stat = n * float(aux.rsquared)
    p_value = float(1.0 - stats.chi2.cdf(lm_stat, df=1))

    print(f"LM Statistic: {lm_stat:.4f}")
    print(f"p-value: {p_value:.6e}")

    return lm_stat, p_value
