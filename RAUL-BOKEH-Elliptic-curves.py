# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:15:59 2016

@author: rrferrero
"""
import numpy as np

from bokeh.layouts import row, widgetbox
from bokeh.models import CustomJS, Slider
from bokeh.plotting import figure, output_file, show, ColumnDataSource

a = 1
b = 1
max_xy = 5
x = np.linspace(-10, 10, 500)
y = np.sqrt(x**3 + a*x + b)

source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(y_range=(-max_xy, max_xy), plot_width=400, plot_height=400)

plot.line('x', 'y', source=source, line_width=2, line_alpha=0.6)

callback = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    var _A = Aaa.value;
    var _B = Bbb.value;
    x = data['x']
    y = data['y']
    for (i = 0; i < x.length; i++) {
        y[i] = Math.pow( (Math.pow(x[i],3) + _A*x[i] + _B), 0.5);
    }
    source.trigger('change');
""")

A_slider = Slider(start=-5, end=5, value=-1, step=.1,
                    title="Var (A)", callback=callback)
callback.args["Aaa"] = A_slider

B_slider = Slider(start=-5, end=5, value=1, step=.1,
                     title="Var (B)", callback=callback)
callback.args["Bbb"] = B_slider




layout = row(
    plot,
    widgetbox(A_slider, B_slider),
)

output_file("slider.html", title="slider.py example")

show(layout)