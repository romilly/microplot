from explorer import ExplorerPlotter
from plots import LinePlot
from data_log import read_csv_data


data = read_csv_data('rechargeable.csv', skip=2)

plot = LinePlot(data,'discharging')
plotter = ExplorerPlotter()
plot.plot(plotter)
