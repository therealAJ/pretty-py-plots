
# ## Global GDP by Country in 2015

import plotly.plotly as py
import plotly.graph_objs as go 
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True) 

df = pd.read_csv('2014_World_GDP')

data = dict(type = 'choropleth',
            locations = df['CODE'],
            z=df['GDP (BILLIONS)'],
            text=df['COUNTRY'],
            colorbar = {'title':'GDP in Billions USD'})

layout = dict(title='Global GDP in 2015',
              geo = dict(projection= {'type':'natural earth'}))
choromap = go.Figure(data=[data],layout=layout)


# #### For API licensed version

#py.image.save_as(choromap, filename='map.png')
#py.image.ishow(choromap)

iplot(choromap)

