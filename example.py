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

# How many trees are in the OSM data of Vienna? And how many trees have there been in 2013?

# This time, we have to first resolve the name "Vienna" to an area id:

from OSMPythonTools.nominatim import Nominatim
nominatim = Nominatim()
nominatim.u
areaId = nominatim.query('Vienna, Austria').areaId()
# %%

from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
overpass = Overpass()
query = overpassQueryBuilder(area=areaId, elementType='node', selector='"natural"="tree"', out='count')
result = overpass.query(query)
result.countElements()
# %%
result = overpass.query(query, date='2013-01-01T00:00:00Z', timeout=60)
result.countElements()


# %%

#How did the number of trees in Berlin, Paris, and Vienna change over time?
#Before we can answer the question, we have to import some modules:

from collections import OrderedDict
from OSMPythonTools.data import Data, dictRangeYears, ALL
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass

dimensions = OrderedDict([
    ('year', dictRangeYears(2013, 2017.5, 1)),
    ('city', OrderedDict({
        'berlin': 'Berlin, Germany',
        'paris': 'Paris, France',
        'vienna': 'Vienna, Austria',
    })),
])

overpass = Overpass()
def fetch(year, city):
    areaId = nominatim.query(city).areaId()
    query = overpassQueryBuilder(area=areaId, elementType='node', selector='"natural"="tree"', out='count')
    return overpass.query(query, date=year, timeout=60).countElements()
data = Data(fetch, dimensions)

data.plot(city=ALL, filename='example4.png')

data.select(city=ALL).getCSV()
# %%
