"""
antibiotic_trends.py

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
matplotlib.use("Agg")  # write PNGs without needing a display
import matplotlib.pyplot as plt
import pandas as pd