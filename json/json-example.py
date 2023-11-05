import json
from types import SimpleNamespace
import requests

r = requests.get('https://api.github.com/users/Talits')
result = json.loads(r.text, object_hook=lambda d: SimpleNamespace(**d))

print(result.name)
print(result.company)
print(result.blog)