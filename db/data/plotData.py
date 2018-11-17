import pandas as pd
import numpy as np
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.palettes import inferno
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource
from bokeh.io import export_png


def plot(position):

    output_file(position + ".html")

    df = pd.read_csv(position+'pointsAgainst.csv')
    # print(df.head())

    teams = df['Abbr']
    pointsAllowed = df['AvgPtsAllowed']

    source = ColumnDataSource(data=dict(teams=teams, pointsAllowed=pointsAllowed))

    p = figure(x_range=teams, title="Fantasy Points Allowed by NFL Defenses vs " + position, toolbar_location=None, tools="", plot_width=1500)
    p.vbar(x='teams', top='pointsAllowed', width=0.9, source=source, fill_color=factor_cmap('teams', palette=inferno(32)[::-1], factors=teams))

    # p.legend.orientation = "horizontal"
    # p.legend.location = "top_center"
    # p.legend.label_text_font_size = '8pt'

    show(p)
    # export_png(p, filename=position+".png")
