import pandas as pd
import numpy as np
from recommand.clients.models import wallpaper
data = pd.read_csv(r'C:\\Users\\Nowav\Desktop\\Recommand\\recommand\wrec\\filelist\\filelist_raw.csv')

imagNAME= data.iloc[:,0]
imagNAME=np.array( imagNAME)
print(imagNAME)

imagSRC = data.iloc[:,1]
imagSRC = np.array(imagSRC)
print(imagSRC)

imagTAGS = data.iloc[:,1:]
imagTAGS = np.array(imagTAGS)
print(imagTAGS)


wallpaper(imagNAME = ,)
wallpaper.save（）