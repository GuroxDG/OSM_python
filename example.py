#%%
# Which object does the way with the id 5887599 represent?
from OSMPythonTools.api import Api

api = Api()
way = api.query('way/5887599')

# %%

print(way.tag('building'))

print(way.tag('architect'))

print(way.tag('website'))


# %%

# What is the English name of the church called "Stephansdom", what address does it have, and which of which denomination is the church?
from OSMPythonTools.overpass import Overpass
overpass = Overpass()
result = overpass.query('way["name"="Stephansdom"]; out body;')

# %%

stephansdom = result.elements()[0]

print(stephansdom.tag('name:en'))
print('%s %s, %s %s' % (stephansdom.tag('addr:street'), stephansdom.tag('addr:housenumber'), stephansdom.tag('addr:postcode'), stephansdom.tag('addr:city')))
print(stephansdom.tag('building'))
print(stephansdom.tag('denomination'))

# %%
from OSMPythonTools.overpass import Overpass
overpass = Overpass()
result = overpass.query('way["name"="Santuario de Las Lajas"]; out body;')

stephansdom = result.elements()[0]

print(stephansdom.tag('name'))
print('%s %s, %s %s' % (stephansdom.tag('addr:street'), stephansdom.tag('addr:housenumber'), stephansdom.tag('addr:postcode'), stephansdom.tag('addr:city')))
print(stephansdom.tag('building'))
print(stephansdom.tag('denomination'))
# %%
