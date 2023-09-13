import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dfDatiDemo= pd.read_csv('popolazioneITACSV.csv',sep=';')
nMaschi=np.array(dfDatiDemo['Totale Maschi'])
nFemmine=np.array(dfDatiDemo['Totale Femmine'])
x_pos=np.array(dfDatiDemo['Eta'])

plt.figure()
fig,ax = plt.subplots()
plt.barh(x_pos,nMaschi*-1,color='#87CEEB',label='maschi')
plt.barh(x_pos,nFemmine,color='#FF69B4',label='femmine')
plt.legend(loc="upper left")
plt.title('popolazione italiana maschile e femminile distribuita per età')
plt.ylabel('età')
plt.xlabel('popolazione aggiornata al 01/01/2023')
ticks =ax.get_xticks()
ax.xaxis.set_major_formatter(lambda y, pos: f'{abs(y):g}')
plt.show()


