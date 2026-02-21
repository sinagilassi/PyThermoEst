# import libs
import os
import numpy as np
from rich import print
from pythermodb_settings.models import Temperature, Pressure
from pyThermoEst.docs.antoine import (
    estimate_coefficients,
    AntoineFitResult,
    calc_vapor_pressure
)
import matplotlib.pyplot as plt
# local
from antoine_utils import plot_antoine_fit

# NOTE: experimental data file path
# ! Temperature unit: K
temperature_unit = "K"
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
pressure_unit = "Pa"
pressures = [
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
Ts = [Temperature(value=T, unit=temperature_unit) for T in temperatures]
# >> pressure
Ps = [Pressure(value=P, unit=pressure_unit) for P in pressures]


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
    # A
    A = result.model_dump().get("A")
    # B
    B = result.model_dump().get("B")
    # C
    C = result.model_dump().get("C")
    # base
    base = result.model_dump().get("base", "log10")

    print("\n[bold blue]Calculating vapor pressures using the Antoine equation...[/bold blue]")
    print(f"A = {A}, B = {B}, C = {C}, base = {base}\n")

    # check
    if A is None or B is None or C is None:
        print("[bold red]Invalid Antoine coefficients.[/bold red]")
        raise ValueError("Invalid Antoine coefficients.")

    calc_res = []
    for item in Ts:
        res_ = calc_vapor_pressure(
            temperature=item,
            A=A,
            B=B,
            C=C,
            base=base,
        )

        if res_ is not None:
            calc_res.append(res_.model_dump().get("value"))

    print(calc_res)

    # plot
    plt.figure()
    plt.scatter(temperatures, pressures, label="Experimental")
    plt.plot(temperatures, calc_res, label="Antoine fit")
    # plt.yscale("log")
    plt.xlabel('T (K)')
    plt.ylabel('Psat (Pa)')
    plt.title("Antoine Fit: Psat(T)")
    plt.legend()
    plt.show()

# NOTE: plot using utility function
if result is not None:
    plot_antoine_fit(
        T_data=np.array(temperatures),
        P_data=np.array(pressures),
        fit_report=result.model_dump(),
        T_unit="K",
        p_data_unit="Pa",
        n_curve=200,
        show_residuals=True,
    )
