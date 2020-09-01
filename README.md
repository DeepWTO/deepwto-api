# DeepWTO API
[![Python Version Supported](https://img.shields.io/badge/python-3.6|7|8-blue.svg)](https://www.python.org/downloads/release/python-360/)

Pip installable deepwto-api that can read, write and graph-query the [deepwto database](https://github.com/DeepWTO/deepwto-stream). 

Please email [ceo@cmmnd.org](mailto:ceo@cmmnd.org) to get an API Key and its endpoint URL of the database.


## Installation
```
pip install deepwto==0.1.1
```

## API
***Get factual description with dispute settlement (ds) number***

```python
# Email syyun@snu.ac.kr to get API Key and Endpoint URL
import deepwto

api_key = "this-is-api-key"
endpoint_url ="this-is-endpoint-url"

client = deepwto.DataBase(api_key=api_key, endpoint_url=endpoint_url)

client.available_ds
>>> [2, 18, 22, 31, 34, 46, 56, 58, 60, 62, 67, 68, 69, 75, 76, 87, 90, 98, 103, 108, 121, 122, 135, 136, 139, 141, 146, 152, 155, 161, 162, 165, 166, 174, 175, 177, 184, 202, 207, 212, 217, 219, 221, 231, 234, 238, 244, 245, 246, 248, 257, 264, 265, 266, 267, 268, 269, 276, 282, 283, 286, 290, 294, 295, 296, 301, 302, 308, 312, 315, 316, 320, 321, 322, 332, 336, 339, 343, 344, 345, 350, 353, 360, 363, 366, 371, 379, 381, 384, 392, 394, 396, 397, 399, 400, 406, 412, 414, 415, 422, 425, 427, 429, 430, 431, 435, 436, 437, 440, 442, 447, 449, 453, 454, 456, 457, 461, 464, 468, 471, 472, 473, 475, 476, 477, 479, 480, 482, 483, 484, 485, 486, 488, 490, 492, 493, 495, 499, 504, 505, 513, 518, 523]

client.available_ds_num
>>> 143

client.get_factual(ds=2)
>>> 'II.       FACTUAL ASPECTS\n          A.       The Clean Air Act\n2.1       The Clean Air Act ("CAA"), originally enacted in 1963, aims at preventing and\ncontrolling air pollution in the United States. ...
```
***Get article content of GATT with article name***
```python
client.available_article
>>> ['Article I', 'Article I:1', 'Article II', 'Article II:1', 'Article II:1(a)', 'Article II:1(b)', 'Article II:2', 'Article II:3', 'Article III', 'Article III:1', 'Article III:2', 'Article III:4', 'Article III:5', 'Article III:7', 'Article IV', 'Article IX', 'Article IX:2', 'Article V', 'Article V:1', 'Article V:2', 'Article V:3', 'Article V:3(a)', 'Article V:4', 'Article V:5', 'Article V:6', 'Article V:7', 'Article VI', 'Article VI:1', 'Article VI:2', 'Article VI:2(a)', 'Article VI:2(b)', 'Article VI:3', 'Article VI:5(a)', 'Article VI:6', 'Article VII', 'Article VII:1', 'Article VII:2', 'Article VII:5', 'Article VIII', 'Article VIII:1', 'Article VIII:3', 'Article VIII:4', 'Article X', 'Article X:1', 'Article X:2', 'Article X:3', 'Article X:3(a)', 'Article XI', 'Article XI:1', 'Article XIII', 'Article XIII:1', 'Article XIII:2', 'Article XIII:3(b)', 'Article XIX', 'Article XIX:1', 'Article XIX:2', 'Article XIX:3', 'Article XV', 'Article XVI', 'Article XVI:1', 'Article XVI:4', 'Article XVII', 'Article XVII:1', 'Article XVII:1(c)', 'Article XVIII', 'Article XVIII:10', 'Article XVIII:11', 'Article XX', 'Article XXI', 'Article XXII', 'Article XXII:1', 'Article XXIII', 'Article XXIII:1', 'Article XXIII:1(a)', 'Article XXIII:1(b)', 'Article XXIV', 'Article XXIV:12', 'Article XXIV:5(b)', 'Article XXIV:6', 'Article XXVIII']

client.available_article_num
>>> 80

client.get_article(article="Article I")
>>> 'Article I\nGeneral Most-Favoured-Nation Treatment \n1. With respect to customs duties and charges of any kind imposed on or in connection with importation or exportation or imposed on the international transfer of payments for imports or exports, and with respect to the method of levying such duties and charges, and with respect to all rules and formalities in connection with importation and exportation, and with respect to all matters referred to in paragraphs 2 and 4 of Article III,* any advantage, favour, privilege or immunity granted by any contracting party to any product originating in or destined for any other country shall be accorded immediately and unconditionally to the like product originating in or destined for the territories of all other contracting parties.\n2. The provisions of paragraph 1 of this Article shall not require the elimination of any preferences in respect of import duties or charges which do not exceed the levels provided for in paragraph 4 of this Article and which fall within the following descriptions:\n(a) Preferences in force exclusively between two or more of the territories listed in Annex A, subject to the conditions set forth therein;\n(b) Preferences in force exclusively between two or more territories which on July 1, 1939, were connected by common sovereignty or relations of protection or suzerainty and which are listed in Annexes B, C and D, subject to the conditions set forth therein;\n(c) Preferences in force exclusively between the United States of America and the Republic of Cuba;\n(d) Preferences in force exclusively between neighbouring countries listed in Annexes E and F.\n3. The provisions of paragraph 1 shall not apply to preferences between the countries formerly a part of the Ottoman Empire and detached from it on July 24, l923, provided such preferences are approved under paragraph 5† of Article XXV, which shall be applied in this respect in the light of paragraph 1 of Article XXIX.\n4. The margin of preference* on any product in respect of which a preference is permitted under paragraph 2 of this Article but is not specifically set forth as a maximum margin of preference in the appropriate Schedule annexed to this Agreement shall not exceed:\n(a) in respect of duties or charges on any product described in such Schedule, the difference between the most-favoured-nation and preferential rates provided for therein; if no preferential rate is provided for, the preferential rate shall for the purposes of this paragraph be taken to be that in force on April 10, l947, and, if no most-favoured-nation rate is provided for, the margin shall not exceed the difference between the most-favoured-nation and preferential rates existing on April 10, 1947;\n(b) in respect of duties or charges on any product not described in the appropriate Schedule, the difference between the most- favoured-nation and preferential rates existing on April 10, 1947.\nIn the case of the contracting parties named in Annex G, the date of April\n10, 1947, referred to in sub-paragraph (a) and (b) of this paragraph shall be replaced by the respective dates set forth in that Annex.'
```

***Get cited label***

```python
client.get_label(article='Article I', ds=2)
>>> True
client.get_label(article='Article I', ds=18)
>>> False
```
 
## Publish to PyPi
    # make sure change version in setup.py
    python setup.py sdist bdist_wheel
    # if initial publish
    python -m twine upload dist/*
    # elif not initial publish
    python -m twine upload --skip-existing dist/*
