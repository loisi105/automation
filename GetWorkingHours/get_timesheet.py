from datetime import date
import requests
import os
from pathlib import Path
from dotenv import load_dotenv

def _create_out_folder(_foldername):
    OUTDIR = Path(_foldername)
    OUTDIR.mkdir(exist_ok=True)

def _call_api(_session: requests.Session, _url: str | bytes, _params, _headers, _cookies, _stream: bool) -> requests.Response:
    return _session.get(_url, params=_params, headers=_headers, cookies=_cookies, stream=_stream)

def _write_response_to_file(_response: requests.Response, filepath_: str):
    with open(filepath_, "wb") as f:
                for chunk in _response.iter_content(chunk_size=8192):
                    if chunk:  # filter out keep-alive chunks
                        f.write(chunk)

def _set_constants(_url, _cookie: list[str, str, str], _year: int):
    """ 
    Set constant headers, cookies, and dates for API calls 

    Args:
        _url (str): The URL for the API endpoint
        _cookie (list[str, str, str]): List with the values for PHPSESSID, K2P and REMEMBERME
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.5",
        "referee": _url,
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }
    cookies = {
        "PHPSESSID": _cookie[0],
        "K2P": _cookie[1],
        "REMEMBERME": _cookie[2]
    }
    dates = [f"{_year}-01-01", f"{_year}-02-01", f"{_year}-03-01", f"{_year}-04-01", 
            f"{_year}-05-01", f"{_year}-06-01", f"{_year}-07-01", f"{_year}-08-01", 
            f"{_year}-09-01", f"{_year}-10-01", f"{_year}-11-01", f"{_year}-12-01"]
    return headers, cookies, dates

def get_xlsx_from_remote_api(_year: int = date.today().year):
    save_folder = "./downloads"
    _create_out_folder(save_folder)

    session = requests.Session()
    load_dotenv() 

    url= os.getenv("REMOTE_API_URL")
    headers, cookies, dates = _set_constants(url, os.getenv("API_COOKIE").split(","), _year)
    
    for date in dates:
        response = _call_api(
            session, 
            url,
            {
                "date": date,
                "sumtype": "duration",
            },
            headers, 
            cookies, 
            True)

        if response.status_code == 200:
            filename = f"{date}_kimai_export.xlsx"
            _write_response_to_file(response, os.path.join(save_folder, filename))

            print(f"File downloaded successfully as: {filename}")
        else:
            print(f"Failed to download data: HTTP {response.status_code}")
            print(response.text[:500])  # Print a snippet if it's an error page

    session.close()
