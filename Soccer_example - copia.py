
# coding: utf-8

# In[2]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# In[4]:


from Animation.game_animation import make_plot
from bokeh.io import show, output_notebook
import pandas as pd
from functools import partial

output_notebook()

df = pd.read_csv('sample_data/soccer_sample.csv')
image_url = 'static/images/soccer.png'

x_range=(-52.5,52.5)
y_range=(-34, 34)

id_def = 2
id_att = 1

make_anim_plot = partial(make_plot, df=df,image_url=image_url, id_def=id_def, id_att = id_att,
                           x_range=x_range, y_range=y_range, slider_steps=1,
                           headers = ["x", "y", "team_id", "player_id","time"], 
                           anim_speed=60,show_dist_speed=True)

show(make_anim_plot)

