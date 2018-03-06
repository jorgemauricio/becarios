import pandas as pd

data = pd.read_csv('../data/examen_final.csv')

for i in range (1,6):
	df = data[data['Dia']==i]
	df.to_csv('resultados/d{}.csv'.format(i))
for i in range (1,6):
	df = data[data['Dia']==i]	
	df = df[df['Lat'] > 21.0]
	df = df[df['Lat'] < 24.0]
	df = df[df['Long'] > -104.0]
	df = df[df['Long'] < -100.0]
	df.to_csv('resultados/d{}_filtrado.csv'.format(i))
Rain,Tmax,Tmin,Dia=[],[],[],[]
new = pd.DataFrame()
for i in range (1,6):
	df = data[data['Dia']==i]
	Rain.append(df['Rain'].mean())
	Tmax.append(df['Tmax'].mean())
	Tmin.append(df['Tmin'].mean())
	Dia.append(i)
new['Dia'] = Dia
new['Rain'] = Rain
new['Tmax'] = Tmax
new['Tmin'] = Tmin
new.to_csv('resultados/Medias.csv')
Rain,Tmax,Tmin,Dia=[],[],[],[]
new = pd.DataFrame()
for i in range (1,6):
	df = data[data['Dia']==i]
	Rain.append(df['Rain'].mean())
	Tmax.append(df['Tmax'].mean())
	Tmin.append(df['Tmin'].mean())
	Dia.append(i)
new['Dia'] = Dia
new['Rain'] = Rain
new['Tmax'] = Tmax
new['Tmin'] = Tmin
new.to_csv('resultados/Medias_filtrado.csv')