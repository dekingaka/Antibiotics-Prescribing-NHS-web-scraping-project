# Antibiotic Prescribing Trends (NHS England)

Pulls NHS England antibiotic prescribing data from **OpenPrescribing.net**'s free, 
open API and produces a CSV + trend charts of antibiotic prescribing by 
ICB (Integrated Care Board) over time.

## No API key needed
OpenPrescribing's API is genuinely open — no
registration, no key, no header to configure. `pip install`, run, done.

## Data source & measure
We use OpenPrescribing's own pre-built, clinically validated **"volume of
antibiotic prescribing"** measure (`all_antibiotics`) rather than defining
"what counts as an antibiotic" ourselves — it's the same standardised
metric NHS antimicrobial stewardship leads use: prescription items for all
oral antibacterial drugs (BNF section 5.1, excluding
antituberculosis/antileprotic drugs) per 1,000 patients, already
population-adjusted.

Other antibiotic-stewardship measures you can swap in by changing
`MEASURE_ID` in the script (see the full list at
https://openprescribing.net/measure/):

- `co-amoxiclav_cephalosporins` — WHO "Watch" category antibiotics
  (broader-spectrum, higher resistance risk)
- `three_day_uti` — three-day courses for uncomplicated UTIs
- `trimethoprim_nitrofurantoin` — trimethoprim vs nitrofurantoin choice

## Project structure

```
antibiotic_prescribing_project/
├── .vscode/
│   ├── launch.json      # F5 debug config
│   └── settings.json    # points VS Code at the .venv interpreter
├── .gitignore
├── requirements.txt
├── antibiotic_trends.py # the script
└── README.md
```

## Data licence & attribution

OpenPrescribing data is open and free to use. If you use it in your
dissertation, cite it as:

> OpenPrescribing.net, Bennett Institute for Applied Data Science,
> University of Oxford, 2026.
