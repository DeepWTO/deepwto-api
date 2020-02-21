# DeepWTO API
Pip installable deepwto-api that can read, write and graph-query the [deepwto db](https://github.com/DeepWTO/deepwto-stream). 

## Installation
```
pip install deepwto=0.0.6
```

## API

```python
# Email syyun@snu.ac.kr to get API Key and Endpoint URL
client = deepwto.DataBase(api_key=api_key, endpoint_url=endpoint_url)

client.available_ds
>>> [2, 18, 22, 31, 34, 46, 56, 58, 60, 62, 67, 68, 69, 75, 76, 87, 90, 98, 103, 108, 121, 122, 135, 136, 139, 141, 146, 152, 155, 161, 162, 165, 166, 174, 175, 177, 184, 202, 207, 212, 217, 219, 221, 231, 234, 238, 244, 245, 246, 248, 257, 264, 265, 266, 267, 268, 269, 276, 282, 283, 286, 290, 294, 295, 296, 301, 302, 308, 312, 315, 316, 320, 321, 322, 332, 336, 339, 343, 344, 345, 350, 353, 360, 363, 366, 371, 379, 381, 384, 392, 394, 396, 397, 399, 400, 406, 412, 414, 415, 422, 425, 427, 429, 430, 431, 435, 436, 437, 440, 442, 447, 449, 453, 454, 456, 457, 461, 464, 468, 471, 472, 473, 475, 476, 477, 479, 480, 482, 483, 484, 485, 486, 488, 490, 492, 493, 495, 499, 504, 505, 513, 518, 523]

cleint.get_factual(ds=2)
>>> 'II.       FACTUAL ASPECTS\n          A.       The Clean Air Act\n2.1       The Clean Air Act ("CAA"), originally enacted in 1963, aims at preventing and\ncontrolling air pollution in the United States. ...
```

## Publish to PyPi
    # make sure change version in setup.py
    python setup.py sdist bdist_wheel
    # if initial publish
    python -m twine upload dist/*
    # elif not initial publish
    python -m twine upload --skip-existing dist/*
