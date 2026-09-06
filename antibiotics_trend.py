"""
antibiotics_trends.py

Pulls NHS England antibiotic prescribing trends from OpenPrescribing.net's
free, open API (no API key required) and produces:
  1. A CSV of the standardised "volume of antibiotic prescribing" measure
     by ICB (Integrated Care Board), month by month
  2. A national trend line chart (PNG)
  3. A chart comparing the highest- and lowest-prescribing ICBs (PNG)
"""

import csv
import sys
import time
import requests
import matplotlib.pyplot as plt
import pandas as pd


BASE = "https://openprescribing.net/api/1.0"
MEASURE_ID = "all_antibiotics"   
ORG_TYPE = "icb"        
REQUEST_DELAY = 0.2  

session = requests.Session()
session.headers.update({"User-Agent": "research-script (dissertation, non-commercial)"})

def api_get(path, params=None):
    url = f"{BASE}{path}"
    for attempt in range(3):
        resp = session.get(url, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 429:
            time.sleep(2 * (attempt + 1))
            continue
        resp.raise_for_status()
    resp.raise_for_status()

def fetch_measure_by_org(measure_id, org_type):
  """
  Returns one row per (org, month) with the measure's calculated value
  (items per 1,000 patients), numerator (items) and denominator (patients/1000).
  """
  print(f"Fetching '{measure_id}' by {org_type}...")
  data = api_get("/measure/", {"measure": measure_id, "org_type": org_type})
  rows = data.get("measures", [])
  if not rows:
      sys.exit(
          f"No data returned for measure='{measure_id}', org_type='{org_type}'.\n"
          f"Check the measure ID is correct at https://openprescribing.net/measure/"
      )
  out = []
  
  for entry in rows:
      org_id = entry.get("org_id")
      org_name = entry.get("org_name") or org_id
      for point in entry.get("data", []):
          out.append({
              "org_id": org_id,
              "org_name": org_name,
              "date": point.get("date"),
              "numerator": point.get("numerator"),
              "denominator": point.get("denominator"),
              "calc_value": point.get("calc_value"),
              "percentile": point.get("percentile"),
          })
  return out