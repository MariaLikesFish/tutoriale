from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Springerspider(BasePortiaSpider):
    name = "springerSpider"
    allowed_domains = [u'link.springer.com']
    start_urls = [{u'url': u'https://link.springer.com/search?sortOrder=newestFirst&facet-content-type=Article&facet-journal-id=[...]', u'fragments': [{u'valid': True, u'type': u'fixed', u'value': u'https://link.springer.com/search?sortOrder=newestFirst&facet-content-type=Article&facet-journal-id='}, {u'valid': True, u'type': u'list', u'value': u'11428 125 204 40262 40265 392 429 10555 40263 382 11682 10495 10311 10350 40264 10570 10548 11892 11910 10664 12311 10563 10618 10585 223 277 11906 10238 338 40266 40256 11883 12012 10515 62 445 10546 12195 11511 11940 12094 10565 403 10531 10453 10534 455 10544 705 11916 10498 10633 10518 10616 40261 10459 10459 11571 10157 422 446 10543 10596 10014 10092 12149 12013 10286 10539 10539 10619 11686 381 10601 10614 10614 493 10666 236 365 12565 40314 11038 10595 14 10588 10588 366 12228 454 10440 13348 104 6 10631 11785 202 11445 11446 10511 10634 11533 37 180 10604 10625 10587 10255 11536 10120 10291 11419 11606 380 11605 190 12026 12263 10811 10762 264 15010 10707 702 417 10686 792 12161 11418 10029 10659 348 10732 10035 10493 10898 11483 10700 10689 10347 285 780 780 10884 12223 10921 13726 13187 10910 10909 11448 10878 145 10327 10709 10740 21 10701 10164 165 10152 10703 12041 10158 601 10791 10801 59 11537 106 11784 105 11476 481 10341 13258 767 11959 10697 11687 11487 108 10343 11290 10269 11214 11065 11065 12035 281 13311 11695 10346 40273 40273 10980 213 12017 10048 11036 12021 10240 572 11302 12028 11067 12032 467 11032 10107 779 766 10404 436 13127 10103 11011 11325 11948 11948 114 423 11012 211 11192 11192 11336 11336 10143 11004 11240 408 10266 40291 10265 10915 440 12471 12540 10994 10705 10072 12253 246 11005 11001 11557 11258 10236 11080 11056 247 11816 40295 10955 10953 208 29 11144 11075 606 795 11107 11085 12598 12217 383 10086 703 11081 193 12542 11135 11135 10950 11082 64 12650 10333 10201 11495 11228 11508 12600 30 115 9 11451 11021 11191 11191 11546 11047 11139 347 10579 209 605 11355 11117 10946 184 132 229 11178 11453 11504 11282 11177 194 10049 11172 11023 292 11494 11491 4 11006 11492 10987 32 11094 11450 117 12175 11710 112 11015 11041 16 16 11981 11062 11003 11839 11825 761 40279 10712 778 11904 11434 11920 11920 12284 11914 12020 11721 11926 40271 40271 268 11116 11116 497 11912 13758 12571 40272 11934 11886 13540 11899 11908 12471 214 240 10035 33 11295 13157 12282 11273 12145 12371 13386 13205 13199 10230 11749 11749 12080 40145 114 12053 12053 11230 13770 13770 10792 13533 13364 12351 12152 12152 11232 11600 12304 12304 40194 12633 12355 10 10388 11455 393 224 11454 10055 13536 11225 12225 41208 11223 11268 120'}], u'type': u'generated'}]
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'/article/'),
                deny=(u'fulltext')
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'.FulltextWrapper',
                [
                    Field(
                        u'journal',
                        '.ArticleHeader > .enumeration > p:nth-child(1) > a > .JournalTitle *::text',
                        []),
                    Field(
                        u'title',
                        '.ArticleHeader > .MainTitleSection > .ArticleTitle *::text',
                        []),
                    Field(
                        u'author',
                        '.ArticleHeader > .authors > .authors__list > .test-contributor-names > li:nth-child(1) > .authors__name *::text',
                        []),
                    Field(
                        u'time',
                        '.ArticleHeader > .main-context__container > div:nth-child(1) > .article-dates > .article-dates__entry *::text',
                        []),
                    Field(
                        u'abstract',
                        '.Abstract *::text',
                        []),
                    Field(
                        u'keywords',
                        '.KeywordGroup *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.FulltextWrapper',
                [
                    Field(
                        u'journal',
                        '.ArticleHeader > .enumeration > p:nth-child(1) > a > .JournalTitle *::text',
                        []),
                    Field(
                        u'title',
                        '.ArticleHeader > .MainTitleSection > .ArticleTitle *::text',
                        []),
                    Field(
                        u'author',
                        '.ArticleHeader > .authors > .authors__list > .test-contributor-names > li:nth-child(1) > .authors__name *::text',
                        []),
                    Field(
                        u'time',
                        '.ArticleHeader > .main-context__container > div:nth-child(1) > .article-dates > .article-dates__entry *::text',
                        []),
                    Field(
                        u'abstract',
                        '.Abstract *::text',
                        []),
                    Field(
                        u'keywords',
                        '.KeywordGroup *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.FulltextWrapper',
                [
                    Field(
                        u'journal',
                        '.ArticleHeader > .enumeration > p:nth-child(1) > a > .JournalTitle *::text',
                        []),
                    Field(
                        u'title',
                        '.ArticleHeader > .MainTitleSection > .ArticleTitle *::text',
                        []),
                    Field(
                        u'author',
                        '.ArticleHeader > .authors > .authors__list > .test-contributor-names > li:nth-child(1) > .authors__name *::text',
                        []),
                    Field(
                        u'time',
                        '.ArticleHeader > .main-context__container > div:nth-child(1) > .article-dates > .article-dates__entry *::text',
                        []),
                    Field(
                        u'abstract',
                        '.Abstract *::text',
                        []),
                    Field(
                        u'keywords',
                        '.KeywordGroup *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.FulltextWrapper',
                [
                    Field(
                        u'journal',
                        '.ArticleHeader > .enumeration > p:nth-child(1) > a > .JournalTitle *::text',
                        []),
                    Field(
                        u'title',
                        '.ArticleHeader > .MainTitleSection > .ArticleTitle *::text',
                        []),
                    Field(
                        u'author',
                        '.ArticleHeader > .authors > .authors__list > .test-contributor-names > li:nth-child(1) > .authors__name *::text',
                        []),
                    Field(
                        u'time',
                        '.ArticleHeader > .main-context__container > div:nth-child(1) > .article-dates > .article-dates__entry *::text',
                        []),
                    Field(
                        u'abstract',
                        '.Abstract *::text',
                        []),
                    Field(
                        u'keywords',
                        '.KeywordGroup *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.FulltextWrapper',
                [
                    Field(
                        u'journal',
                        '.ArticleHeader > .enumeration > p:nth-child(1) > a > .JournalTitle *::text',
                        []),
                    Field(
                        u'title',
                        '.ArticleHeader > .MainTitleSection > .ArticleTitle *::text',
                        []),
                    Field(
                        u'author',
                        '.ArticleHeader > .authors > .authors__list > .test-contributor-names > li:nth-child(1) > .authors__name *::text',
                        []),
                    Field(
                        u'time',
                        '.ArticleHeader > .main-context__container > div:nth-child(1) > .article-dates > .article-dates__entry *::text',
                        []),
                    Field(
                        u'abstract',
                        '.Abstract *::text',
                        []),
                    Field(
                        u'keywords',
                        '.KeywordGroup *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.FulltextWrapper',
                [
                    Field(
                        u'journal',
                        '.ArticleHeader > .enumeration > p:nth-child(1) > a > .JournalTitle *::text',
                        []),
                    Field(
                        u'title',
                        '.ArticleHeader > .MainTitleSection > .ArticleTitle *::text',
                        []),
                    Field(
                        u'author',
                        '.ArticleHeader > .authors > .authors__list > .test-contributor-names > li:nth-child(1) > .authors__name *::text',
                        []),
                    Field(
                        u'time',
                        '.ArticleHeader > .main-context__container > div:nth-child(1) > .article-dates > .article-dates__entry *::text',
                        []),
                    Field(
                        u'abstract',
                        '.Abstract *::text',
                        []),
                    Field(
                        u'keywords',
                        '.KeywordGroup *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.FulltextWrapper',
                [
                    Field(
                        u'journal',
                        '.ArticleHeader > .enumeration > p:nth-child(1) > a > .JournalTitle *::text',
                        []),
                    Field(
                        u'title',
                        '.ArticleHeader > .MainTitleSection > .ArticleTitle *::text',
                        []),
                    Field(
                        u'author',
                        '.ArticleHeader > .authors > .authors__list > .test-contributor-names > li:nth-child(1) > .authors__name *::text',
                        []),
                    Field(
                        u'time',
                        '.ArticleHeader > .main-context__container > div:nth-child(1) > .article-dates > .article-dates__entry *::text',
                        []),
                    Field(
                        u'abstract',
                        '.Abstract *::text',
                        []),
                    Field(
                        u'keywords',
                        '.KeywordGroup *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.FulltextWrapper',
                [
                    Field(
                        u'journal',
                        '.ArticleHeader > .enumeration > p:nth-child(1) > a > .JournalTitle *::text',
                        []),
                    Field(
                        u'title',
                        '.ArticleHeader > .MainTitleSection > .ArticleTitle *::text',
                        []),
                    Field(
                        u'author',
                        '.ArticleHeader > .authors > .authors__list > .test-contributor-names > li:nth-child(1) > .authors__name *::text',
                        []),
                    Field(
                        u'time',
                        '.ArticleHeader > .main-context__container > div:nth-child(1) > .article-dates > .article-dates__entry *::text',
                        []),
                    Field(
                        u'abstract',
                        '.Abstract *::text',
                        []),
                    Field(
                        u'keywords',
                        '.KeywordGroup *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.FulltextWrapper',
                [
                    Field(
                        u'journal',
                        '.ArticleHeader > .enumeration > p:nth-child(1) > a > .JournalTitle *::text',
                        []),
                    Field(
                        u'title',
                        '.ArticleHeader > .MainTitleSection > .ArticleTitle *::text',
                        []),
                    Field(
                        u'author',
                        '.ArticleHeader > .authors > .authors__list > .test-contributor-names > .u-mb-2 > .authors__name *::text',
                        []),
                    Field(
                        u'time',
                        '.ArticleHeader > .main-context__container > div:nth-child(1) > .article-dates > .article-dates__entry *::text',
                        []),
                    Field(
                        u'abstract',
                        '.Abstract *::text',
                        []),
                    Field(
                        u'keywords',
                        '.KeywordGroup *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.FulltextWrapper',
                [
                    Field(
                        u'journal',
                        '.ArticleHeader > .enumeration > p:nth-child(1) > a > .JournalTitle *::text',
                        []),
                    Field(
                        u'title',
                        '.ArticleHeader > .MainTitleSection > .ArticleTitle *::text',
                        []),
                    Field(
                        u'author',
                        '.ArticleHeader > .authors > .authors__list > .test-contributor-names > li:nth-child(1) > .authors__name *::text',
                        []),
                    Field(
                        u'time',
                        '.ArticleHeader > .main-context__container > div:nth-child(1) *::text',
                        []),
                    Field(
                        u'abstract',
                        '.Abstract *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.ArticleHeader',
                [
                    Field(
                        u'journal',
                        '.enumeration > p:nth-child(1) > a > .JournalTitle *::text',
                        []),
                    Field(
                        u'title',
                        '.MainTitleSection > .ArticleTitle *::text',
                        []),
                    Field(
                        u'author',
                        '.authors > .authors__list > .test-contributor-names > li:nth-child(1) > .authors__name *::text',
                        []),
                    Field(
                        u'time',
                        '.main-context__container > div:nth-child(1) > .article-dates > .article-dates__entry *::text',
                        [])])]]
