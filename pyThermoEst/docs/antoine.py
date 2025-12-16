# import libs
import logging
from typing import List, Dict, Tuple, Optional
import numpy as np
from pythermodb_settings.models import Temperature, Pressure
from pathlib import Path
# local
from ..core import Antoine

# NOTE: set up logger
logger = logging.getLogger(__name__)


def estimate_coefficients(
    temperatures: List[Temperature],
    pressures: List[Pressure],
    *,
    base: str = "log10",
    fit_in_log_space: bool = True,
    weights: Optional[np.ndarray] = None,
    x0: Optional[Tuple[float, float, float]] = None,
    bounds: Optional[
        Tuple[
            Tuple[float, float, float],
            Tuple[float, float, float]
        ]
    ] = None,
    max_nfev: int = 5000,
    validate: bool = True,
    min_margin_kelvin: float = 1.0,
    # robust options
    loss: str = "linear",
    f_scale: Optional[float] = None,
):
    """
    Estimate Antoine coefficients from experimental data to fit the Antoine equation as follows:

        log10(P) = A - B / (T + C)   (if base is "log10")
        ln(P)   = A - B / (T + C)    (if base is "ln")

    Parameters
    ----------
    temperatures : List[Temperature]
        List of Temperature models containing temperature values and units.
    pressures : List[Pressure]
        List of Pressure models containing pressure values and units.
    base : str, optional
        Logarithm base used in the Antoine equation ('log10' or 'ln'), by default "log10".
    fit_in_log_space : bool, optional
        Whether to perform fitting in logarithmic space, by default True.
    weights : Optional[np.ndarray], optional
        Optional weights for each data point, by default None.
    x0 : Optional[Tuple[float, float, float]], optional
        Initial guess for coefficients (A, B, C), by default None.
    bounds : Optional[Tuple[Tuple[float, float, float], Tuple[float, float, float]]], optional
        Bounds for coefficients (A, B, C), by default None.
    max_nfev : int, optional
        Maximum number of function evaluations for the optimizer, by default 5000.
    validate : bool, optional
        Whether to perform validation checks on the fitted coefficients, by default True.
    min_margin_kelvin : float, optional
        Minimum margin in Kelvin to ensure valid temperature range, by default 1.0.
    loss : str, optional
        Loss function for robust fitting, by default "linear".
    f_scale : Optional[float], optional
        Scale parameter for robust fitting, by default None.

    Returns
    -------
    dict
        Dictionary containing fitted coefficients and metrics.
    """
    pass


def estimate_coefficients_from_experimental_data(
    experimental_data: str | Path,
    *,
    base: str = "log10",
    fit_in_log_space: bool = True,
    weights: Optional[np.ndarray] = None,
    x0: Optional[Tuple[float, float, float]] = None,
    bounds: Optional[
        Tuple[
            Tuple[float, float, float],
            Tuple[float, float, float]
        ]
    ] = None,
    max_nfev: int = 5000,
    validate: bool = True,
    min_margin_kelvin: float = 1.0,
    # robust options
    loss: str = "linear",
    f_scale: Optional[float] = None,
):
    """
    Estimate Antoine coefficients from experimental data to fit the Antoine equation as follows:

        log10(P) = A - B / (T + C)   (if base is "log10")
        ln(P)   = A - B / (T + C)    (if base is "ln")

    Parameters
    ----------
    experimental_data : str | Path
        Path to experimental data file (CSV, JSON, etc.) containing temperature and pressure data.
    base : str, optional
        Logarithm base used in the Antoine equation ('log10' or 'ln'), by default "log10".
    fit_in_log_space : bool, optional
        Whether to perform fitting in logarithmic space, by default True.
    weights : Optional[np.ndarray], optional
        Optional weights for each data point, by default None.
    x0 : Optional[Tuple[float, float, float]], optional
        Initial guess for coefficients (A, B, C), by default None.
    bounds : Optional[Tuple[Tuple[float, float, float], Tuple[float, float, float]]], optional
        Bounds for coefficients (A, B, C), by default None.
    max_nfev : int, optional
        Maximum number of function evaluations for the optimizer, by default 5000.
    validate : bool, optional
        Whether to perform validation checks on the fitted coefficients, by default True.
    min_margin_kelvin : float, optional
        Minimum margin in Kelvin to ensure valid temperature range, by default 1.0.
    loss : str, optional
        Loss function for robust fitting, by default "linear".
    f_scale : Optional[float], optional
        Scale parameter for robust fitting, by default None.

    Returns
    -------
    dict
        Dictionary containing fitted coefficients and metrics.
    """
    pass
