# ESPN player eligibility importer

Imports MLB player eligibility from http://games.espn.go.com/flb/tools/eligibility.

## Data extraction

Scrape results include the following fields:

- ESPN player id (`int`)
- Player name (`string`)
- Team name (`string`)
- Player's primary position (`string`)
- All eligible positions (`list`)
- All positions where player is eligible (`object`)

Which looks something like...

```json
[
  {
    "all_positions": {
      "1B": 5,
      "SS": 1,
      "LF": "X",
      "C": false,
      "DH": 1,
      "2B": false,
      "RP": false,
      "CF": 1,
      "SP": false,
      "3B": "PP",
      "RF": "X"
    },
    "team": "ChC",
    "name": "Kris Bryant",
    "primary_position": "3B",
    "eligible_positions": [
      "3B",
      "LF",
      "RF"
    ],
    "pid": 5675
  },
]
```

## Installation

Clone this repo into a virtual environment, then install project requirements:

```shell
git clone git@github.com:mattdennewitz/espn-eligibility-importer.git
cd espn-eligibility-importer
pip install -r requirements.txt 
```

## Running the crawler

Hop into the `espnelig` directory and run the scraper,
capturing output as JSON:

```shell
cd espnelig
scrapy crawl elig -o eligibility.json
```

## One more thing

Please do not abuse or overwhelm ESPN's servers. This app is in no way
affiliated with ESPN or MLB. Use responsibily.

