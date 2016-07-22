# -*- coding: utf-8 -*-
import scrapy


from ..items import EligibilityItem


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

            # player name
            player_name = player.css('::text').extract_first()
            player_id = row.xpath('./td[@class="playertablePlayerName"]/a/@playerid').extract_first()

            # extract raw player team and positions
            team_raw = player.xpath('./a/following-sibling::text()[1]').extract_first()

            # positions extracted from table
            positions = [False] * 11
            for i in range(3, 14):
                elig_at_pos = row.css('td:nth-child({idx}) span::text'.format(idx=i)).extract_first()
                elig_at_pos = elig_at_pos.strip()
                if elig_at_pos == '--':
                    continue
                positions[i-3] = elig_at_pos

            elig = EligibilityItem()
            elig['name'] = player_name
            elig['pid'] = player_id
            elig['team'] = team_raw
            elig['positions'] = dict(list(zip(POSITIONS, positions)))
            yield elig

        # look for next page
        nxpath = '//div[@class="paginationNav"]//a[contains(., "NEXT")]/@href'
        nxp_url = response.xpath(nxpath).extract_first()
        if nxp_url:
            yield scrapy.Request(nxp_url)

