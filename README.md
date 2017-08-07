Thread Genius API Python Client
====================


Overview
---------------------
This Python client provides a simple wrapper around our vision <a href="http://docs.threadgenius.co">API</a>.



Installation
---------------------
The API client is available on Pip. You can simply install it with a `pip install`
```
pip install thread-genius
```

Getting Started
---------------------
The following example will setup the client and search a private catalog with an image query.
```python
from threadgenius import ThreadGenius
from threadgenius.types import ImageUrlInput

tg = ThreadGenius(api_key='key_123')
image = ImageUrlInput(url='http://cdn.example.com/image.jpeg')
tg.search_by_image(catalog_gid='catalog_123', image=image, n_results=10)
```

Documentations
---------------------
Read more code examples and references at http://docs.threadgenius.co
