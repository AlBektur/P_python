
from typing import Any


def dep_checker() -> bool:
    from importlib.metadata import distributions
    print("\nChecking dependencies:")

    data = {
        'pandas': "Data manipulation ready",
        'numpy': "Numerical computation ready",
        'requests': "Network access ready",
        'matplotlib': "Visualization ready",
    }
    with open('requirements.txt', 'r') as requirements:
        readed = requirements.read().split()
        content = set(readed)

    dependencies = [
        f"{dist.metadata['Name']}=={dist.version}" for dist in distributions()]
    deps = set(dependencies)

    res = content - deps

    if len(res) > 0:
        for lib in res:
            print(f"Missing: {lib}")
        print("\nPlease install the missing dependencies with the command:")
        print("For pip: pip install <package name>")
        return False
    for dist in distributions():
        temp = f"{dist.metadata['Name']}=={dist.version}"
        if temp in content:
            if dist.metadata['Name'] in data:
                print(f"[OK] {dist.metadata['Name']} ({dist.version})"
                      f"- {data[dist.metadata['Name']]}")

    return True


def get_data() -> Any:
    import requests
    from datetime import date, timedelta
    import numpy as np

    latitude = 41.3874
    longitude = 2.1686

    end_date = date.today() - timedelta(days=1)
    start_date = end_date - timedelta(days=999)

    url = "https://archive-api.open-meteo.com/v1/archive"

    from typing import Union, Sequence

    ParamValue = Union[
        str,
        int,
        float,
        bytes,
        Sequence[Union[str, int, float, bytes]],
        None,
    ]

    params: dict[str, ParamValue] = {
        'latitude': latitude,
        'longitude': longitude,
        'start_date': start_date.isoformat(),
        'end_date': end_date.isoformat(),
        'daily': "temperature_2m_mean",
        'timezone': "Europe/Madrid"
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    temperatures = np.array(
        data["daily"]["temperature_2m_mean"],
        dtype=float
    )

    return temperatures


def process_data(temperatures: Any) -> None:
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 5))

    x = np.arange(len(temperatures))

    plt.plot(
        x,
        temperatures,
        color="blue",
        linestyle="-",
        linewidth=1.5
    )

    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature evolution")
    plt.grid(True)

    print("Results saved to: matrix_analysis.png")
    plt.savefig("matrix_analysis.png", dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")

    if dep_checker():
        import numpy as np

        temperatures = get_data()

        print('\nAnalyzing Matrix data...')
        n, = (temperatures.shape)
        print(f"Processing {n} data points")
        process_data(temperatures)
