#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import json
import codecs
import pokemon

current_dir = os.getcwd()
data_dir = "/home/sylveurdance/Téléchargements/Pokedex_Offine/"

 #Parse a pokemon file and extract information to place it in pokemon class
def parsePokemon(num_fiche_poke):
	poke = pokemon.Pokemon()
	f_pokemon = open(data_dir+num_fiche_poke,"r")
	lines = f_pokemon.readlines()
	for index, line in enumerate(lines):
		line = line.decode('iso-8859-1').encode('utf8')
		if 'Fiche Pokédex de ' in line:
			poke.name = line.split('Fiche Pokédex de ')[1].split(' /')[0]
			#print poke.name
		if 'Numéro National' in line:
			poke.numero = lines[index+14].decode('iso-8859-1').encode('utf8').strip('	,/\n,\r')
			#print poke.numero
		if 'gen4_types' in line:
			if not poke.type1 and not poke.type2:
				poke.type1 = line.split('alt="')[1].split('"')[0]
				poke.type2 = lines[index+2].decode('iso-8859-1').encode('utf8').split('alt="')[1].split('"')[0]
				poke.genre = lines[index+6].decode('iso-8859-1').encode('utf8').strip('	,/\n,\r')
				#print poke.type1
				#print poke.type2
				#print poke.genre
		if 'Capacités spéciales' in line:
			poke.capacite1 = lines[index+4].decode('iso-8859-1').encode('utf8').split('<b>')[1].split(' :</b>')[0].strip('/\n')
			if '</td>' not in lines[index+6].decode('iso-8859-1').encode('utf8'):
				poke.capacite2 = lines[index+6].decode('iso-8859-1').encode('utf8').split('<b>')[1].split(' :</b>')[0].strip('/\n')
			#print poke.capacite1
			#print poke.capacite2
		if '<td class="fiche_poke_stats"><b>' in line:
			if not poke.pv:
				poke.pv = line.split('<td class="fiche_poke_stats"><b>')[1].split('</b></td>')[0]
				poke.attaque = lines[index+9].decode('iso-8859-1').encode('utf8').split('<td class="fiche_poke_stats"><b>')[1].split('</b></td>')[0]
				poke.defense = lines[index+18].decode('iso-8859-1').encode('utf8').split('<td class="fiche_poke_stats"><b>')[1].split('</b></td>')[0]
				poke.att_spe = lines[index+27].decode('iso-8859-1').encode('utf8').split('<td class="fiche_poke_stats"><b>')[1].split('</b></td>')[0]
				poke.def_spe = lines[index+36].decode('iso-8859-1').encode('utf8').split('<td class="fiche_poke_stats"><b>')[1].split('</b></td>')[0]
				poke.vitesse = lines[index+45].decode('iso-8859-1').encode('utf8').split('<td class="fiche_poke_stats"><b>')[1].split('</b></td>')[0]
				#print poke.pv
				#print poke.attaque
				#print poke.defense
				#print poke.att_spe
				#print poke.def_spe
				#print poke.vitesse
		if 'href="../fiches-attaques/' in line:
			id_attaque = line.split('href="../fiches-attaques/attaque')[1].split('.html')[0]
			if id_attaque not in poke.attaques:
				poke.attaques.append(id_attaque)
	#poke.attaques.sort()
	#print poke.attaques
	#print poke
	f_pokemon.close()
	return poke

def parseAttaques(id_attaque):
	attaque = pokemon.Attaque()
	attaque.numero = id_attaque
	f_attaque = open(data_dir+"fiches-attaques/attaque"+str(id_attaque)+".html","r")
	lines = f_attaque.readlines()
	for index, line in enumerate(lines):
		line = line.decode('iso-8859-1').encode('utf8')
		if '<h1>' in line:
			attaque.name = line.split('<h1>Attaque ')[1].split(' (')[0]
		if '<i>' in line:
			attaque.effect = line.split('<i>')[1].split('</i>')[0]
		if 'Type :' in line:
			attaque.a_type = line.split('images/gen4_types/')[1].split('.png')[0]
		if 'Puissance :' in line:
			attaque.puissance = line.split('</b> ')[1].split('<br />')[0]
		if 'Précision :' in line:
			attaque.precision = line.split('</b> ')[1].split('<br />')[0]
		if 'Points de pouvoir :' in line:
			attaque.pp = line.split('</b> ')[1].split('<br />')[0]
		if 'Classe :' in line:
			attaque.classe = line.split('</b> ')[1].split('<br />')[0]
	#print attaque
	return attaque

#parsePokemon("fiches-pokemon/fiche42.html")

#Open pokedex file et call every pokemon file
f_pokedex = open(data_dir+"liste_des_pokemon.html","r")
pokedex = []
for line in f_pokedex.readlines():
	if 'fiches-pokemon' in line:
		pokedex.append(parsePokemon(line.split('"')[1]))

#print pokedex[0]
#print pokedex[1]
f_pokedex.close()

#Parse attaques
list_of_attaques = []
for id_attaque in range(1,354):
	list_of_attaques.append(parseAttaques(id_attaque))

# Put into JSON files
with codecs.open("./data/pokedex.json", "w", encoding='utf8') as poke_fichier:
	json.dump(pokedex, poke_fichier, indent=4, ensure_ascii=False, encoding='utf8', default=pokemon.serialiseur_json)

with codecs.open("./data/attaques.json", "w", encoding='utf8') as att_fichier:
	json.dump(list_of_attaques, att_fichier, indent=4, ensure_ascii=False, encoding='utf8', default=pokemon.serialiseur_json)
