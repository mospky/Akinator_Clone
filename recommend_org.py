import pandas as pd
import numpy as np

def recommend(data):
  # 純度 = abs(回答がYesになる選択肢の数 - 選択肢数/2)
  purity = (data.iloc[:, 1:].sum() - np.full(data.shape[1]-1, data.shape[0]/2)).abs()
  
  selected_column = purity.idxmin()
  print(f'見たいのは{selected_column}ですか？')
  choice = input()
  if choice == 'y':
    selected_data = data[data[selected_column]]
  else:
    selected_data = data[~data[selected_column]]
  selected_data = selected_data.reset_index(drop=True)
  if selected_data.shape[0] == 1:
    print(f'あなたにおすすめの動画は {selected_data.iloc[0, 0]} です')
  else:
    recommend(selected_data)

data = [{'タイトル': 'VTuberのゲーム実況', 'ライブ配信': True, 'VTuber': True, 'ゲーム実況': True},
        {'タイトル': 'VTuberの料理配信', 'ライブ配信': True, 'VTuber': True, 'ゲーム実況': False},
        {'タイトル': 'VTuberによる解説動画', 'ライブ配信': False, 'VTuber': True, 'ゲーム実況': False},
        {'タイトル': 'YouTuberによる料理配信', 'ライブ配信': False, 'VTuber': False, 'ゲーム実況': False}]
df = pd.DataFrame(data)
recommend(df)
# 見たいのはライブ配信ですか？
# y
# 見たいのはゲーム実況ですか？
# y
# あなたにおすすめの動画は VTuberのゲーム実況 です