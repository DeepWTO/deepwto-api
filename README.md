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
cleint.get_factual(ds=2)
```

## Publish to PyPi
    # make sure change version in setup.py
    python setup.py sdist bdist_wheel
    # if initial publish
    python -m twine upload dist/*
    # elif not initial publish
    python -m twine upload --skip-existing dist/*
