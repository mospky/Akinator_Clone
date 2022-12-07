import pandas as pd
import numpy as np
import math

###
def recommend(data):
  # 純度 = abs(回答がYesになる選択肢の数 - log2(データ数))
  purity = (data.iloc[:, 1:].sum() - np.full(data.shape[1]-1, math.log2(data.shape[0]))).abs()

  print(data.iloc[:, 1:])
  print("")

  print(data.iloc[:, 1:].sum())
  print("")

  print("----------------------")
  print("data.shape[1]-1   data.shape[0]/2")
  print(data.shape[1]-1) #列数-1 (タイトルは除外)
  print(data.shape[0]/2) #行数 / log2X
  

  print("----------------------")
  print("np.full(data.shape[1]-1, data.shape[0]/2)")
  print(np.full(data.shape[1]-1, data.shape[0]/2))

  print("----------------------")
  print("purity")
  print(purity)

  print("----------------------")
  print("purity.idxmin()")
  print(purity.idxmin())
  
  
  print("----------------------")
  selected_column = purity.idxmin()
  print(f'{selected_column}ですか？')
  choice = input()
  if choice == 'y':
    selected_data = data[data[selected_column]]
    print("----------------------")
    print(data[selected_column])
    print(selected_data)
  else:
    print("----------------------")
    selected_data = data[~data[selected_column]]

  print("----------------------")
  selected_data = selected_data.reset_index(drop=True)
  print(selected_data)

  if selected_data.shape[0] == 1:
    print(f'あなたにおすすめの動画は {selected_data.iloc[0, 0]} です')
  else:
    recommend(selected_data)

data = [{'title': 'VTuberのゲーム実況ライブ', 'ライブ配信': True,  'VTuber': True,  'ゲーム実況': True},
        {'title': 'VTuberの料理配信ライブ',   'ライブ配信': True,  'VTuber': True,  'ゲーム実況': False},
        {'title': 'VTuberによる解説動画',     'ライブ配信': False, 'VTuber': True,  'ゲーム実況': False},
        {'title': 'YouTuberによる料理動画',   'ライブ配信': False, 'VTuber': False, 'ゲーム実況': False}]

df = pd.DataFrame(data)
recommend(df)
# 見たいのはライブ配信ですか？
# y
# 見たいのはゲーム実況ですか？
# y
# あなたにおすすめの動画は VTuberのゲーム実況 です