from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.controllers.db import get_db
from flaskr.service.guess import get_question
from flaskr.service.guess import get_question_test

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

    # 1 : DB取得
    db = get_db()
    title = db.execute(
        'SELECT * FROM TITLE'
    ).fetchall()

    # 2 : DataFrameに変換
    df_title = pd.DataFrame(title)
    df = pd.DataFrame(data)

    # 3 : 質問取得
    # selected_data, d['name'] = get_question_test(df_title, 0)
    selected_data, d['name'] = get_question(df, 0)

    # 4 : View
    return render_template('recommend/index.html', que=d)


@bp.route('/<string:choice>/update', methods=('GET', 'POST'))
def update(choice):
  global selected_data
  
  selected_data, d['name'] = get_question(selected_data, choice)

  return render_template('recommend/index.html', que=d)
