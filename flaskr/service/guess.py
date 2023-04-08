from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.controllers.db import get_db

from typing import Tuple

import pandas as pd
import numpy as np
import math

def get_question_test(data, choice):
  global selected_data
  global selected_column

  # 

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


def get_question(data, choice):
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

