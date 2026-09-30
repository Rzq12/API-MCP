import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from ..config import settings

def call(path, params=None):
    url = f"{settings.bkn_api_base_url.rstrip('/')}{path}"
    if params:
        url += f"?{urlencode(params)}"
    try:
        with urlopen(Request(url, headers={"Accept": "application/json"}), timeout=60) as response:
            return json.loads(response.read().decode())
    except HTTPError as error:
        raise RuntimeError(f"BKN API error {error.code}: {error.read().decode(errors='replace')}") from error
    except URLError as error:
        raise RuntimeError(f"Tidak dapat terhubung ke BKN API: {error.reason}") from error

def pagination(page, size):
    if page < 0 or size < 1:
        raise ValueError("page harus >= 0 dan size harus >= 1")
    return {"page": page, "size": size}