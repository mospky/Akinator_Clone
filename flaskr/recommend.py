from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.db import get_db

from typing import Tuple

import pandas as pd
import numpy as np
import math

###
d = {"name": "0"}
data = [{'title': 'VTuberのゲーム実況ライブ',  'ライブ配信': True,  'VTuber': True,  'ゲーム実況': True, '雑談': False,'歌ってみた':False},
        {'title': 'VTuberの雑談ライブ',       'ライブ配信': True,  'VTuber': True,  'ゲーム実況': False,'雑談': True, '歌ってみた':False},
        {'title': 'VTuberの歌ってみた動画',    'ライブ配信': False, 'VTuber': True,  'ゲーム実況': False,'雑談': False, '歌ってみた':True},
        {'title': 'VTuberのゲーム実況動画',    'ライブ配信': False, 'VTuber': True,  'ゲーム実況': False,'雑談': False, '歌ってみた':False},
        {'title': 'YouTuberのゲーム実況ライブ', 'ライブ配信': True, 'VTuber': False, 'ゲーム実況': True, '雑談': False, '歌ってみた':False},
        {'title': 'YouTuberの雑談ライブ',      'ライブ配信': True, 'VTuber': False, 'ゲーム実況': False,  '雑談': True, '歌ってみた':False},
        {'title': 'YouTuberの歌ってみた動画',   'ライブ配信': False, 'VTuber': False, 'ゲーム実況': False, '雑談': False, '歌ってみた':True},
        {'title': 'YouTuberのゲーム実況動画',   'ライブ配信': False, 'VTuber': False, 'ゲーム実況': True,'雑談': False, '歌ってみた':False},
        {'title': 'YouTuberのゲーム実況と雑談動画',  'ライブ配信': False, 'VTuber': False, 'ゲーム実況': True,'雑談': True, '歌ってみた':False}]

selected_data = []
selected_column = ""

bp = Blueprint('recommend', __name__)

@bp.route('/')
def index():
    global selected_data

    df = pd.DataFrame(data)

    selected_data, d['name'] = recommend(df, 0)

    return render_template('recommend/index.html', que=d)


@bp.route('/<string:choice>/update', methods=('GET', 'POST'))
def update(choice):
  global selected_data
  
  selected_data, d['name'] = recommend(selected_data, choice)

  return render_template('recommend/index.html', que=d)

###
def recommend(data, choice):
  global selected_data
  global selected_column

  if choice == 0 :
    purity = (data.iloc[:, 1:].sum() - np.full(data.shape[1]-1, math.log2(data.shape[0]))).abs()
    selected_column = purity.idxmin()

    que = f'{selected_column}ですか？'
    selected_data = data

    return selected_data, que
    
  elif choice == 'y':
    selected_data = data[data[selected_column]]

  else :
    selected_data = data[~data[selected_column]]

  selected_data = selected_data.reset_index(drop=True)

  # 純度 = abs(回答がYesになる選択肢の数 - log2(データ数))
  purity = (selected_data.iloc[:, 1:].sum() - np.full(selected_data.shape[1]-1, math.log2(selected_data.shape[0]))).abs()
  selected_column = purity.idxmin()

  que = f'{selected_column}ですか？'

  if selected_data.shape[0] == 1:
    que = f'あなたにおすすめの動画は {selected_data.iloc[0, 0]} です'
    return selected_data, que
    
  else:
    return selected_data, que

