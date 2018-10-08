import pandas as pd
import math
import random

html=[]
words_colors=[]

color_choices=['#8000FF',
               '#3498DB',
               '#FF5733',
               '#223AE6',
               '#2ECC71',
               '#5F6A6A',
               '#6C22E6',
               '#CE22E6',
               '#ACB02E',
               '#B18904',
               '#848484',
               '#04B404',
               '#5882FA',
               '#FF0080',
               '#0489B1',
               '#FA5858',
               '#DBA901',
               '#00b4ff',
               '#008080',
               '#003366',
               '#725394'
               ]

#randomize color choices
#random.shuffle(color_choices)
    

def get_color_code(score):   
    
    step=0.05
    start=0
    idx=0
    
    while start<1:
        if score<=start:
            return color_choices[idx]
        idx+=1
        start=start+step
        
    return color_choices[0]
    
    
    
def get_font_size(score):
    # font size start and increment
    scale=0.6
    scale_step=0.3
    
    #score increment
    score_step=0.05
    start=0
    idx=0
    
    
    while start<1:
        if score<=start:
            return scale
        start=start+score_step
        scale+=scale_step

def get_embed_code(df:pd.DataFrame):
    random.shuffle(color_choices)
    html=[]
    words_colors=[]

    html=["<div align='center' style='width:100%'><div align='center' style='text-align:justify; overflow-x: scroll; width:70% !important; padding:10px; '; text-align: center; word-wrap: break-word;>"]
    for idx,row in df.iterrows():
        word=row.words.replace(" ","-")
        scale=get_font_size(row.score)
        color_code=get_color_code(row.score)
        words_colors.append(" <span style='line-height:1.1em;color:{0};font-size:{1}em;font-family:georgia'>{2}&nbsp;</span>".format(color_code,scale,word))
    
    random.shuffle(words_colors)

    html.extend(words_colors)
    html.append("</div></div>")
    return ''.join(html)
