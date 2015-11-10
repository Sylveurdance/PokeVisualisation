#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Pokemon:

	def __init__(self, numero=0,name="",type1="",type2="",genre="",capacite1="",capacite2="",pv=0,attaque=0,defense=0,att_spe=0,def_spe=0,vitesse=0,attaques=[]):
		self.numero = numero
		self.name = name
		self.type1 = type1
		self.type2 = type2
		self.genre = genre
		self.capacite1 = capacite1
		self.capacite2 = capacite2
		self.pv = pv
		self.attaque = attaque
		self.defense = defense
		self.att_spe = att_spe
		self.def_spe = def_spe
		self.vitesse = vitesse
		self.attaques = attaques

	def __str__(self):
		return "numero : "+self.numero+"\nname : "+self.name
		+"\ntype1 : "+self.type1+"\ntype2 : "+self.type2
		+"\ngenre : "+self.genre+"\ncapacite1 : "+self.capacite1
		+"\ncapacite2 : "+self.capacite2+"\npv : "+self.pv
		+"\nattaque : "+self.attaque+"\ndefense : "+self.defense
		+"\natt_spe : "+self.att_spe+"\ndef_spe : "+self.def_spe
		+"\nvitesse : "+self.vitesse+"\nattaques : "+str(self.attaques)

	def serialize_pokemon(self):
		return {"__class__": "Pokemon",
			"numero": self.numero,
			"name": self.name,
			"type1": self.type1,
			"type2": self.type2,
			"genre": self.genre,
			"capacite1": self.capacite1,
			"capacite2": self.capacite2,
			"pv": self.pv,
			"attaque": self.attaque,
			"defense": self.defense,
			"att_spe": self.att_spe,
			"def_spe": self.def_spe,
			"vitesse": self.vitesse,
			"attaques": self.attaques}

	def deserialize_pokemon(self, poke_obj):
		self.numero = poke_obj["numero"]
		self.name = poke_obj["name"]
		self.type1 = poke_obj["type1"]
		self.type2 = poke_obj["type2"]
		self.genre = poke_obj["genre"]
		self.capacite1 = poke_obj["capacite1"]
		self.capacite2 = poke_obj["capacite2"]
		self.pv = poke_obj["pv"]
		self.attaque = poke_obj["attaque"]
		self.defense = poke_obj["defense"]
		self.att_spe = poke_obj["att_spe"]
		self.def_spe = poke_obj["def_spe"]
		self.vitesse = poke_obj["vitesse"]
		self.attaques = poke_obj["attaques"]
		return self

class Attaque:

	def __init__(self, numero=0, name="", a_type="", puissance="", precision="", pp=0, classe="", effect=""):
		self.numero = numero
		self.name = name
		self.a_type = a_type
		self.puissance = puissance
		self.precision = precision
		self.pp = pp
		self.classe = classe
		self.effect = effect

	def __str__(self):
		return "numero : "+str(self.numero)+"\nname : "+self.name
		+"\na_type : "+self.a_type+"\npuissance : "+self.puissance
		+"\nprecision : "+self.precision+"\npp : "+str(self.pp)
		+"\nclasse : "+self.classe+"\neffect : "+self.effect

	def serialize_attaque(self):
		return {"__class__": "Attaque",
			"numero": self.numero,
			"name": self.name,
			"a_type": self.a_type,
			"puissance": self.puissance,
			"precision": self.precision,
			"pp": self.pp,
			"classe": self.classe,
			"effect": self.effect}

	def deserialize_attaque(self, attaque_dict):
		self.numero = attaque_dict["numero"]
		self.name = attaque_dict["name"]
		self.a_type = attaque_dict["a_type"]
		self.puissance = attaque_dict["puissance"]
		self.precision = attaque_dict["precision"]
		self.pp = attaque_dict["pp"]
		self.classe = attaque_dict["classe"]
		self.effect = attaque_dict["effect"]
		return self

# Serialise an object in a dictionary so that it can be putted in a json file properly
def serialiseur_json(obj):

	# If it's a Pokemon object
	if isinstance(obj, Pokemon):
		return obj.serialize_pokemon()

	# If it's an Attaque object
	if isinstance(obj, Attaque):
		return obj.serialize_attaque()

	# Otherwise
	raise TypeError(repr(obj) + " is not serialisable !")

# Deserialise a dictionary object to get a real object
def deserialiseur_json(obj_dict):
	if "__class__" in obj_dict:
		if obj_dict["__class__"] == "Pokemon":
			obj = Pokemon()
			obj.deserialize_pokemon(obj_dict)
			return obj

		if obj_dict["__class__"] == "Attaque":
			obj = Attaque()
			obj.deserialize_attaque(obj_dict)
			return obj
	return objet
