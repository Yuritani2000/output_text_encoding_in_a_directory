import chardet
import glob
import sys
import pandas as pd
import numpy as np
import os

if __name__ == "__main__":
  
  args = sys.argv
  
  # コマンドライン引数で渡されたファイルのファイル一覧を取得
  files_in_a_directory = glob.glob("{}/*".format(args[1]))
  
  save_dir_path = '.'
  
  if len(args) > 2:
    save_dir_path = args[2]
    
  save_path = "{}/endocings_in_directory_{}.csv".format(save_dir_path, os.path.basename(args[1]))
  
  results = np.full((len(files_in_a_directory), 2), np.array(['','']), dtype=object)
  
  i = 0
  for file_path in files_in_a_directory:
    with open(file_path, 'rb') as f:
      c = f.read()
      
      result = chardet.detect(c)
      
      print(result['encoding'])
      
      results[i][0] = os.path.basename(file_path)
      results[i][1] = result['encoding']
      
      i += 1
      
  pd_results = pd.DataFrame(results, columns=["file_name", "encoding"])
  
      
  print("ファイル保存先: {}".format(save_path))
  pd_results.to_csv(save_path)
      
  print(results)