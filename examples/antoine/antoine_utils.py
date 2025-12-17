# import libs
from typing import Any, Dict
import numpy as np
import matplotlib.pyplot as plt


def plot_antoine_fit(
    T_data,
    P_data,
    fit_report,
    *,
    T_unit="K",
    p_data_unit="Pa",     # unit of your experimental P_data
    p_display_unit="Pa",  # how you want to show the y-axis
    n_curve=200,
    show_residuals=True,
):
    import numpy as np
    import matplotlib.pyplot as plt

    T = np.asarray(T_data, dtype=float).ravel()
    P = np.asarray(P_data, dtype=float).ravel()

    # Temperature handling
    if T_unit.lower() in ("c", "degc", "celsius", "°c"):
        T_k = T + 273.15
        x = T
        xlabel = "T (°C)"
        Tgrid_k = np.linspace(np.min(T_k), np.max(T_k), n_curve)
        Tgrid = Tgrid_k - 273.15
    else:
        T_k = T
        x = T
        xlabel = "T (K)"
        Tgrid_k = np.linspace(np.min(T_k), np.max(T_k), n_curve)
        Tgrid = Tgrid_k

    # Convert experimental P_data -> Pa (internal)
    p_data_unit = p_data_unit.lower()
    if p_data_unit == "pa":
        P_pa = P
    elif p_data_unit == "bar":
        P_pa = P * 1e5
    else:
        raise ValueError("p_data_unit must be 'Pa' or 'bar'.")

    # Evaluate fit (always yields Pa internally)
    A, B, C = fit_report["A"], fit_report["B"], fit_report["C"]
    base = str(fit_report.get("base", "log10")).lower()

    y_hat_grid = A - B / (Tgrid_k + C)
    if base == "log10":
        P_fit_pa = 10.0 ** y_hat_grid
        y = np.log10(P_pa)
        y_hat = A - B / (T_k + C)
    else:
        P_fit_pa = np.exp(y_hat_grid)
        y = np.log(P_pa)
        y_hat = A - B / (T_k + C)

    # Convert both experimental and fit to display unit
    p_display_unit = p_display_unit.lower()
    if p_display_unit == "pa":
        P_plot = P_pa
        P_fit_plot = P_fit_pa
        ylabel = "Psat (Pa)"
    elif p_display_unit == "bar":
        P_plot = P_pa / 1e5
        P_fit_plot = P_fit_pa / 1e5
        ylabel = "Psat (bar)"
    else:
        raise ValueError("p_display_unit must be 'Pa' or 'bar'.")

    # Plot
    plt.figure()
    plt.scatter(x, P_plot, label="Experimental")
    plt.plot(Tgrid, P_fit_plot, label="Antoine fit")
    plt.yscale("log")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title("Antoine Fit: Psat(T)")
    plt.legend()
    plt.show()

    if show_residuals:
        r = y_hat - y
        plt.figure()
        plt.scatter(x, r)
        plt.axhline(0.0)
        plt.xlabel(xlabel)
        plt.ylabel("Residual in log(P)")
        plt.title("Antoine Fit Residuals (log-space)")
        plt.show()
