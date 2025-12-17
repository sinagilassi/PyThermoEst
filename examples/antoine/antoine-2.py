# import libs
import os
import numpy as np
from rich import print
from pythermodb_settings.models import Temperature, Pressure
from pyThermoEst.docs.antoine import (
    estimate_coefficients,
    AntoineFitResult,
)
# local
from antoine_utils import plot_antoine_fit

# NOTE: experimental data file path
# ! Temperature unit: K
temperatures = [
    298,
    308,
    318,
    328,
    338,
    348,
    358,
    368,
    378,
    388,
    398,
    408,
]
# ! Pressure unit: Pa
Pressures = [
    3392.900018,
    5738.327528,
    9332.604721,
    14657.31121,
    22310.8695,
    33018.32269,
    47638.5333,
    67168.53995,
    92744.96477,
    125642.5053,
    167269.663,
    219161.9542,
]

# >> temperature
Ts = [Temperature(value=T, unit="K") for T in temperatures]
# >> pressure
Ps = [Pressure(value=P, unit="Pa") for P in Pressures]


# NOTE: estimate Antoine coefficients
result: AntoineFitResult | None = estimate_coefficients(
    temperatures=Ts,
    pressures=Ps,
)
if result is None:
    print("[bold red]Failed to estimate Antoine coefficients.[/bold red]")
else:
    print("[bold green]Estimated Antoine coefficients:[/bold green]")
    print(result)


# NOTE: plot Antoine fit
if result is not None:
    plot_antoine_fit(
        T_data=np.array(temperatures),
        P_data=np.array(Pressures),
        fit_report=result.model_dump(),
        T_unit="K",
        p_unit="Pa",
        n_curve=200,
        show_residuals=True,
    )
