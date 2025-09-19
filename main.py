import numpy as np
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
import polars as pl
import polars.selectors as cs
from matplotlib.axes import Axes
from matplotlib.figure import Figure


def scatter_plot(x_data: pl.Series, y_data: pl.Series, x_label: str, y_label: str) -> tuple[Figure, Axes]:
    """
    Plots the scatter plot of the given data
    :param x_data: Series representing values for the x-axis
    :param y_data: Series representing values for the y-axis
    :param x_label: string values representing what's on the x-axis
    :param y_label: string values representing what's on the y-axis
    :return: Returns a tuple of composed of Figure and Axes objects from the matplotlib package
    """

    x = x_data.to_numpy()
    y = y_data.to_numpy()
    sorted_idx = np.argsort(x)          #Sort data for Spline
    x = x[sorted_idx]
    y = y[sorted_idx]

    xs = np.linspace(x_data.min(), x_data.max(), 1000)
    spl = UnivariateSpline(x,y)

    fig, ax = plt.subplots()
    fig.set_dpi(300)
    ax.scatter(
        x=x_data,
        y=y_data,
    )
    ax.plot(xs, spl(xs), linestyle=':')
    ax.grid(True)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    return fig, ax

#Read data
schema = {
    'Year': pl.Int64, 'W0': pl.String(), 'NL Beer consumption [x1000 hectoliter]': pl.Int64
}
data = pl.read_csv('./istherecorrelation.csv', separator=";", schema_overrides=schema)
data = data.with_columns(
    pl.col('W0')
    .str.replace(r",", '.')  #Replacing ',' with '.' so that parsing to float works
    .cast(pl.Float64)
)

#Plot data
last_col = data.select(cs.last())
fig, ax = scatter_plot(x_data=data['W0'], x_label='People with a WO-level education [x1000] ', y_data=last_col,
                       y_label='NL Beer consumption [x1000 hectoliter]')
ax.set_title(f'Consumption of beer in NL vs People with a WO-level education'
             f' ({data.select(pl.min("Year")).item()}-{data.select(pl.max("Year")).item()})',fontsize=8)
fig.set_dpi(300)
fig.savefig(f'{ax.get_title()}.png', dpi=300)