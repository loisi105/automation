import pandas as pd
import numpy as np

def _parse_euro_number(x):
    if pd.isna(x):
        return np.nan
    # keep numeric types as-is
    if isinstance(x, (int, float, np.integer, np.floating)):
        return float(x)
    s = str(x).strip()
    if s == "":
        return np.nan
    # remove common thousands separators and convert comma decimal to dot
    s = s.replace(" ", "")      # remove spaces
    s = s.replace(".", "")      # remove dots used as thousands sep
    s = s.replace(",", ".")     # comma -> decimal point
    try:
        return float(s)
    except ValueError:
        return np.nan

def _get_last_row_values(_dataframe):
    last_row_raw = _dataframe.iloc[-1].apply(_parse_euro_number)
    return pd.to_numeric(last_row_raw, errors="coerce")

def _get_first_row_dates(_dataframe):
    return pd.to_datetime(_dataframe.iloc[0].tolist(), format="%d.%m.%Y", errors="coerce")

def _check_legal_limits(_data):
    for date, value in _data.items():
        if pd.isna(date) or pd.isna(value):
            print(f"Faulty data on {date}: {value}")
            continue

        if value >= 12:
            print(f"{date:%d.%m.%Y}: Worked time 12 hours or over with: {value}h")
        if date.weekday() >= 5 and value > 0:
            print(f"{date:%d.%m.%Y}: Worked time on a weekend: {value}h")

def _parse_xlsx(_file):
    # Read an Excel file
    data = pd.read_excel(f"./downloads/{_file}", header=None).iloc[:, 2:]

    first_row = _get_first_row_dates(data)
    last_row = _get_last_row_values(data)
    date_time_data = dict(zip(first_row, last_row))

    _check_legal_limits(date_time_data)

def parse_xlsx():
    for i in range(1, 12):
        _parse_xlsx(f"2025-{i:02d}-01_kimai_export.xlsx")
