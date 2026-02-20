# import libs
import os
from rich import print
from pyThermoEst.docs.antoine import (
    estimate_coefficients_from_experimental_data,
    AntoineFitResult,
)

# NOTE: experimental data file path
DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "data-2.csv")
print(f"[bold green]DATA_FILE_PATH:[/bold green] {DATA_FILE_PATH}")

# NOTE: estimate Antoine coefficients from experimental data
result: AntoineFitResult | None = estimate_coefficients_from_experimental_data(
    experimental_data=DATA_FILE_PATH,
    temperature_unit="K",  # ! specify temperature unit in experimental data
    pressure_unit="Pa",  # ! specify pressure unit in experimental data
)
if result is None:
    print("[bold red]Failed to estimate Antoine coefficients from experimental data.[/bold red]")
else:
    print("[bold green]Estimated Antoine coefficients from experimental data:[/bold green]")
    print(result)
