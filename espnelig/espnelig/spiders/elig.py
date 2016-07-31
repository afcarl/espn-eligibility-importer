# -*- coding: utf-8 -*-
import re

import scrapy

from ..items import EligibilityItem


team_re = re.compile(r'\*?\, ([A-z]+)\s')

POSITIONS = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'DH', 'SP', 'RP']

class EligSpider(scrapy.Spider):
    name = 'elig'
    allowed_domains = ['games.espn.go.com']
    start_urls = (
        'http://games.espn.go.com/flb/tools/eligibility',
    )

    def parse(self, response):
        table = response.css('table.playerTableTable')
        for row in table.css('tr.pncPlayerRow'):
            player = row.css('td.playertablePlayerName')

            # extract espn id
            player_id = row.xpath(
                './td[@class="playertablePlayerName"]/a/@playerid'
            ).extract_first()
            player_id = int(player_id)

            # pull player name
            player_name = player.css('::text').extract_first()

            # extract raw player team and positions
            team_raw = player.xpath(
                './a/following-sibling::text()[1]'
            ).extract_first()
            team = team_re.match(team_raw).group(1)

            # extract positions from eligibility chart
            primary_position = None
            eligible_positions = []
            all_positions = {}

            for i in range(len(POSITIONS)):
                position = POSITIONS[i]

                # extract position marker from point in table
                elig_marker = row.css(
                    'td:nth-child({idx}) span::text'.format(idx=i+3)
                ).extract_first().strip()

                if elig_marker in ('X', 'PP'):
                    eligible_positions.append(position)

                    if elig_marker == 'PP':
                        primary_position = position
                elif elig_marker == '--':
                    elig_marker = False
                else:
                    # try this as "games until eligible" int
                    try:
                        elig_marker = int(elig_marker)
                    except ValueError:
                        pass

                all_positions[position] = elig_marker

            elig = EligibilityItem()
            elig['name'] = player_name
            elig['pid'] = player_id
            elig['team'] = team
            elig['primary_position'] = primary_position
            elig['eligible_positions'] = eligible_positions
            elig['all_positions'] = all_positions
            yield elig

        # continue to next page if exists
        nxpath = '//div[@class="paginationNav"]//a[contains(., "NEXT")]/@href'
        nxp_url = response.xpath(nxpath).extract_first()
        if nxp_url:
            yield scrapy.Request(nxp_url)

