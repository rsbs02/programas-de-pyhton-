import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(20,20))
ax.set_facecolor('xkcd:silver')
#fig.patch.set_facecolor('black')
#ax.set_facecolor('tab:skyblue')
#ax ayuda a graficar las dos lineas en un mismo espacio .
ax.plot(TABLA_CONTEOS['Mes'], TABLA_CONTEOS['Negocios'], marker = 'o',linestyle='-', color='b')
ax.plot(TABLA_CONTEOS['Mes'], TABLA_CONTEOS['Buro'], marker = 'o', linestyle='--', color='r')

#Se crea para poder etiquetar los puntos 
x , y= TABLA_CONTEOS['Mes'] ,TABLA_CONTEOS['Buro'] 
etiquetas = TABLA_CONTEOS['Porcentaje']
for i, txt in enumerate(etiquetas):
    plt.annotate('{}%'.format(str(txt)), xy=(x[i],y[i]), xytext=(-20, 20),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle = 'fancy', connectionstyle='Arc3, rad=0.2'))

ax.set_xlabel('MESES',fontsize=18)
ax.set_ylabel("RFC's",fontsize=18)
ax.set_title('CONTEOS A NIVEL RFC',fontsize=25)

#Ayuda a obtener que los valores del eje x giren de forma vertical.
plt.xticks(rotation=90)
plt.grid()
plt.show()
plt.show()