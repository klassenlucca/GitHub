import pandas as pd
import os
import time

user_windows = os.getlogin()

# Caminho do executável ou atalho
eng_tool = r"C:\Program Files (x86)\AB Volvo\EngineeringTool_2.0\EngineeringTool.DesktopClient.Shell.exe"
os.startfile(eng_tool)

# Aguarda 20 segundos
time.sleep(20)