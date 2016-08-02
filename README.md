# aclla
Database of grain data.


## bsparser
This parser is able to retrieve data from BeerSmith's XML files to use with Aclla.  BeerSmith 2 seems to use a dialect derived from BeerXML "standard" [1].

### Grain
The `Grain` class can handle BeerSmith's grain files --usually `Grain.bsmx`.  Just pass the path to that file and the tags you wish to get.  Common tag names are: `_MOD_`, `F_G_NAME`, `F_G_ORIGIN`, `F_G_SUPPLIER`, `F_G_TYPE`, `F_G_IN_RECIPE`, `F_G_INVENTORY`, `F_G_AMOUNT`, `F_G_COLOR`, `F_G_YIELD`, `F_G_LATE_EXTRACT`, `F_G_PERCENT`, `F_G_NOT_FERMENTABLE`, `F_ORDER`, `F_G_COARSE_FINE_DIFF`, `F_G_MOISTURE`, `F_G_DIASTATIC_POWER`, `F_G_PROTEIN`, `F_G_IBU_GAL_PER_LB`, `F_G_ADD_AFTER_BOIL`, `F_G_RECOMMEND_MASH`, `F_G_MAX_IN_BATCH`, `F_G_NOTES`, `F_G_BOIL_TIME`, `F_G_PRICE`, and `F_G_CONVERT_GRAIN`.

### Example
```python
>>> from aclla.bsparser import Grain
>>> g = Grain('/home/forkd/Downloads/Grain.bsmx')
>>> g.parse(['F_G_NAME', 'F_G_YIELD', 'F_G_COLOR', 'F_G_ORIGIN', 'F_G_NOTES'])
```


# References
[ 1] BeerSmith.  Importing and Exporting Files.  Available at:
     <http://www.beersmith.com/help2/index.html?importing_and_exporting_
     files.htm>.
