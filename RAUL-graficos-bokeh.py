# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
from bokeh.charts import Area, show, output_file, output_notebook

# create some example data
data = dict(
    python=[2, 3, 7, 5, 26, 221, 44, 233, 254, 265, 266, 267, 120, 111],
    pypy=[12, 33, 47, 15, 126, 121, 144, 233, 254, 225, 226, 267, 110, 130],
    jython=[22, 43, 10, 25, 26, 101, 114, 203, 194, 215, 201, 227, 139, 160],
)

area = Area(data, title="Area Chart", legend="top_left",
            xlabel='time', ylabel='memory')
# output to static HTML file
# output_file('Grafico Output File 1.html')

# output to this screen in Jupyter
# output_notebook()

# show the results
show(area)