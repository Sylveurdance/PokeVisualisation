#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import json
import codecs
import pokemon
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

pokedex = []

# Load data from Json
with codecs.open("./data/pokedex.json", "r", encoding="utf-8") as f_pokedex:
	pokedex = json.load(f_pokedex, object_hook=pokemon.deserialiseur_json)

# Transform a part of data in matrix
X = []
for poke in pokedex:
	poke_tuple = []
	poke_tuple.append(int(poke.pv.encode('utf8')))
	poke_tuple.append(int(poke.attaque.encode('utf8')))
	poke_tuple.append(int(poke.att_spe.encode('utf8')))
	poke_tuple.append(int(poke.defense.encode('utf8')))
	poke_tuple.append(int(poke.def_spe.encode('utf8')))
	poke_tuple.append(int(poke.vitesse.encode('utf8')))
	poke_tuple.append(pokemon.getTypeCategory(int(poke.type1.encode('utf8')),int(poke.type2.encode('utf8'))))
	X.append(poke_tuple)

X = np.asarray(X)

# Apply Kmeans
nb_clusters = 3
y_pred = KMeans(n_clusters=nb_clusters).fit_predict(X)

#Look at Pokemon
poke_class = []
for index, p in enumerate(pokedex):
	poke_tuple = []
	poke_tuple.append(p.name.encode('utf8'))
	poke_tuple.append(int(y_pred[index]))
	poke_class.append(poke_tuple)

poke_class = np.asarray(poke_class)
poke_class =  poke_class[np.lexsort((poke_class[:,0],poke_class[:,1]))] #sort table
poke_class = poke_class.tolist() #transform to list to put in JSON files

# Put into JSON files
with codecs.open("./data/pokedexKMeans"+str(nb_clusters)+".json", "w", encoding='utf8') as poke_fichier:
	json.dump(poke_class, poke_fichier, indent=4, ensure_ascii=False, encoding='utf8')

# Plot results
plt.subplot(221)
plt.scatter(X[:, 5], X[:, 1], c=y_pred)
plt.xlabel('Vitesse')
plt.ylabel('Attaque')
plt.title("KMeans with "+str(nb_clusters)+" classes (Att / Vit)")

plt.subplot(222)
plt.scatter(X[:, 5], X[:, 2], c=y_pred)
plt.xlabel('Vitesse')
plt.ylabel('Attaque Spe')
plt.title("KMeans with "+str(nb_clusters)+" classes (AttSpe / Vit)")

plt.subplot(223)
plt.scatter(X[:, 3], X[:, 0], c=y_pred)
plt.xlabel('Pv')
plt.ylabel('Defense')
plt.title("KMeans with "+str(nb_clusters)+" classes (Def / Pv)")

plt.subplot(224)
plt.scatter(X[:, 4], X[:, 0], c=y_pred)
plt.xlabel('Pv')
plt.ylabel('Defense Spe')
plt.title("KMeans with "+str(nb_clusters)+" classes (DefSpe / PV)")

plt.show()

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 3], X[:, 4], X[:, 0], c=y_pred)
ax.set_xlabel('Defense')
ax.set_ylabel('DefSpe')
ax.set_zlabel('Pv')
plt.title("KMeans with "+str(nb_clusters)+" classes (Def / DefSpe / PV)")
plt.show()
