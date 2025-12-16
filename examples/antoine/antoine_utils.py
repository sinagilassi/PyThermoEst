# import libs
from typing import Any, Dict
import numpy as np
import matplotlib.pyplot as plt


def plot_antoine_fit(
    T_data: np.ndarray,
    P_data: np.ndarray,
    fit_report: Dict[str, Any],
    *,
    T_unit: str = "K",
    p_unit: str = "Pa",
    n_curve: int = 200,
    show_residuals: bool = True,
) -> None:
    """
    Plot experimental vs Antoine fit (Psat vs T) and optional residual plot in log(P).
    Pressure axis is log-scale (recommended for vapor pressure).
    """
    T = np.asarray(T_data, dtype=float).ravel()
    P = np.asarray(P_data, dtype=float).ravel()

    # x-axis
    if T_unit.lower() in ("c", "degc", "celsius", "°c"):
        T_k = T + 273.15
        T_plot = T
        xlabel = "T (°C)"
        Tgrid_plot = np.linspace(np.min(T), np.max(T), n_curve)
        Tgrid_k = Tgrid_plot + 273.15
    else:
        T_k = T
        T_plot = T
        xlabel = "T (K)"
        Tgrid_k = np.linspace(np.min(T_k), np.max(T_k), n_curve)
        Tgrid_plot = Tgrid_k

    # y-axis
    if p_unit.lower() == "bar":
        P_pa = P * 1e5
        P_plot = P
        ylabel = "Psat (bar)"
    else:
        P_pa = P
        P_plot = P
        ylabel = "Psat (Pa)"

    A, B, C = float(fit_report["A"]), float(
        fit_report["B"]), float(fit_report["C"])
    base = str(fit_report.get("base", "log10")).lower()

    y_hat_grid = A - B / (Tgrid_k + C)
    if base == "log10":
        P_hat_grid_pa = 10.0 ** y_hat_grid
        y = np.log10(P_pa)
    else:
        P_hat_grid_pa = np.exp(y_hat_grid)
        y = np.log(P_pa)

    if p_unit.lower() == "bar":
        P_hat_grid = P_hat_grid_pa / 1e5
    else:
        P_hat_grid = P_hat_grid_pa

    plt.figure()
    plt.scatter(T_plot, P_plot, label="Experimental")
    plt.plot(Tgrid_plot, P_hat_grid, label="Antoine fit")
    plt.yscale("log")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title("Antoine Fit: Psat(T)")
    plt.legend()
    plt.show()

    if not show_residuals:
        return

    y_hat = A - B / (T_k + C)
    r = y_hat - y

    plt.figure()
    plt.scatter(T_plot, r)
    plt.axhline(0.0)
    plt.xlabel(xlabel)
    plt.ylabel("Residual in log(P)")
    plt.title("Antoine Fit Residuals (log-space)")
    plt.show()
