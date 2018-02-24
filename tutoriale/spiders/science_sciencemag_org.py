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


class ScienceSciencemagOrg(BasePortiaSpider):
    name = "science.sciencemag.org"
    allowed_domains = [
        u'stke.sciencemag.org',
        u'science.sciencemag.org',
        u'immunology.sciencemag.org',
        u'advances.sciencemag.org',
        u'stm.sciencemag.org',
        u'robotics.sciencemag.org']
    start_urls = [u'http://science.sciencemag.org/',
                  u'http://advances.sciencemag.org/',
                  u'http://stm.sciencemag.org/',
                  u'http://stke.sciencemag.org/',
                  u'http://immunology.sciencemag.org/',
                  u'http://robotics.sciencemag.org/']
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'abstract'),
                deny=()
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
                u'.container--content',
                [
                    Field(
                        u'title',
                        '.primary > .pane-highwire-article-citation > .pane-content > .highwire-article-citation > .highwire-cite > .article__header > .article__headline > .highwire-cite-title *::text',
                        []),
                    Field(
                        u'author',
                        '#page-top > div:nth-child(6) > .region > div > .row > .container > .primary > .pane-highwire-article-citation > .pane-content > .highwire-article-citation > .highwire-cite > .article__header > .article__expandable-area > .article > .highwire-markup > div > .contributors > .contributor-list > li > .name *::text',
                        []),
                    Field(
                        u'abstract',
                        '.primary > .pane-highwire-panel-tabs-container > .pane-content > .panels-ajax-tab-container > .panels-ajax-tab-wrap-jnl_sci_tab_art > .panel-display > .panel-panel > div > .panel-pane > .pane-content > .highwire-markup > div > .article > .abstract > p *::text',
                        []),
                    Field(
                        u'journal',
                        'article > div > h3 > a > span *::text',
                        []),
                    Field(
                        u'time',
                        'article > div > p.minor *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.container--content',
                [
                    Field(
                        u'title',
                        '.primary > .pane-highwire-article-citation > .pane-content > .highwire-article-citation > .highwire-cite > .article__header > .article__headline > .highwire-cite-title *::text',
                        []),
                    Field(
                        u'author',
                        '.primary > .pane-highwire-article-citation > .pane-content > .highwire-article-citation > .highwire-cite > .article__header > .article__expandable-area > .article > .highwire-markup > div > .contributors > .contributor-list > li > .name *::text',
                        []),
                    Field(
                        u'abstract',
                        '.primary > .pane-highwire-panel-tabs-container > .pane-content > .panels-ajax-tab-container > .panels-ajax-tab-wrap-jnl_sci_tab_art > .panel-display > .panel-panel > div > .panel-pane > .pane-content > .highwire-markup > div > .article > .abstract *::text',
                        []),
                    Field(
                        u'journal',
                        '.highwire-cite-linked-title:nth-child(1) > .highwire-cite-title *::text',
                        []),
                    Field(
                        u'time',
                        'article > div > p.minor *::text',
                        [])])]]
