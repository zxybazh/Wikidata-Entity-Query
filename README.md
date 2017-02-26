# Wikidata-Entity-Query

A query interface for convenient related entity query on `wikidata`.

As `freebase` has been deprecated from Google, you might need to immigrate entity query system to `wikidata`. This interface provides related entity query through `wikidata` api.

This api has been developed for further use in research thus efficiency has not been fully utilized. I would update upon request.

Issues are welcomed : P

##Example
The example runs the given program and input `Fudan University` as entity name.
```
$ Please input the entity name
Fudan University
[{'eid': u'Q8686',
  'entity': u'Shanghai',
  'pid': u'P159',
  'property': u'headquarters location'},
 {'eid': u'Q8475113',
  'entity': u'Category:Fudan University',
  'pid': u'P910',
  'property': u"topic's main category"},
 {'eid': u'Q2634906',
  'entity': u'C9 League',
  'pid': u'P749',
  'property': u'parent company'},
 {'eid': u'Q148',
  'entity': u"People's Republic of China",
  'pid': u'P17',
  'property': u'country'},
 {'eid': u'Q2634906',
  'entity': u'C9 League',
  'pid': u'P463',
  'property': u'member of'},
 {'eid': u'Q3918',
  'entity': u'university',
  'pid': u'P31',
  'property': u'instance of'}]

```

##Getting Started
The program needs `python 2.7` environment.
To simply run and see what it can do, simple run `python api.py` and input `Fudan University`.

##Output Specification
The api returns a list containing several dicts composed of `property id`, `property name`, `entity id`, `entity name` represented in wikidata.

##Helpful Links
[Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page)
[Freebase-Wikidata-mappings](https://developers.google.com/freebase/#freebase-wikidata-mappings)
