# ESPN player eligibility importer

Imports MLB player eligibility from http://games.espn.go.com/flb/tools/eligibility.

## Data extraction

Scrape results include the following fields:

- ESPN player id
- Player name
- Team name
- Player's primary position
- All positions where player is eligible

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

