import json, urllib # Needed libs
from pprint import pprint # Not necessary

def entity2id(q):
	# Get wikidata id from wikidata api
	ans = []
	url = "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&search="+"+".join(q.split(" "))+"&language=en"
	response = json.loads(urllib.urlopen(url).read())
	ans += response["search"]
	if (ans == [] and " " in q):
		# Reverse Trick : Pan Changjiang
		url = "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&search="+"+".join(q.split(" ")[::-1])+"&language=en"
		response = json.loads(urllib.urlopen(url).read())
		ans += response["search"]
	if (ans == [] and len(q.split(" ")) > 2):
		# Abbreviation Trick
		url = "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&search="+"+".join([q.split(" ")[0], q.split(" ")[-1]])+"&language=en"
		response = json.loads(urllib.urlopen(url).read())
		ans += response["search"]
	if len(ans) > 0:
		# Returns the first one, most likely one
		return ans[0]["id"]
	else:
		# Some outliers : Salvador Domingo Felipe Jacinto Dali i Domenech - Q5577
		return "Not Applicable"

def getp(p):
	# Get property name given property id
	# Initialization required
	return property_dict[p]

def getc(c):
	# Get entity name given entity id
	url = "https://www.wikidata.org/w/api.php?action=wbgetentities&props=labels&ids="+c+"&languages=en&format=json"
	response = json.loads(urllib.urlopen(url).read())
	return response["entities"][c]["labels"]["en"]["value"]

def Related(name):
	# Get related property-entity (property id, property name, entity id, entity name) given entity name
	# Return a list of dicts, each dict contains (pid, property, eid, entity)
	# Fail to fetch eid would result in empty list
	query = entity2id(name)
	if query == "Not Applicable": return []
	ans = []
	url = "https://www.wikidata.org/w/api.php?action=wbgetentities&ids="+query+"&format=json&languages=en"
	response = json.loads(urllib.urlopen(url).read())
	for p in response["entities"][query]["claims"]:
		for c in response["entities"][query]["claims"][p]:
			# Enumerate property & entity (multi-property, multi-entity)
			try:
				# Some properties are not related to entities, thus try & except
				cid = c["mainsnak"]["datavalue"]["value"]["id"]
				ans.append({
					"pid": p,
					"property": getp(p),
					"eid": cid,
					"entity": getc(cid)
					})
				#ans.append("\\property\\"+p+"\t"+getp(p)+"\t\\entity\\"+cid+"\t"+getc(cid))
				# Print in a pid-pname-eid-ename fashion
			except:
				continue
	return ans

def init():
	# WARNING: RUN BEFORE USE GETP
	# Needed for property name fetching
	global property_dict
	property_dict = {}
	url = "https://quarry.wmflabs.org/run/45013/output/1/json"
	# Fetch json from given lib
	res = json.loads(urllib.urlopen(url).read())
	for w in res["rows"]:
		property_dict[w[0]] = w[1]


init()
# For test only
entity = raw_input("Please input the entity name\n")
pprint(Related(entity))