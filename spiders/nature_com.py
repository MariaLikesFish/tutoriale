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

#http://www.nature.com/[...]/current-issue
class Nature(BasePortiaSpider):
    name = "www.nature.com"
    allowed_domains = [u'www.nature.com']
    start_urls = [{u'url': u'https://www.nature.com/[...]/',
                   u'fragments': [{u'valid': True,
                                   u'type': u'fixed',
                                   u'value': u'http://www.nature.com/'},
                                  {u'valid': True,
                                   u'type': u'list',
                                   u'value': u'aps ajg ajgsup bdjopen bdjteam bcj bmt boneres bdj bjc cgt cddis cdd cddiscovery celldisc cr cmi cti ctg commsbio commschem commsphys emi ejcn ejhg ebd emm eye gt gene gim hdy hortres hgv hr icb ijir ijo ijosup ijos ismej jes jhg jhh jp ja laban labinvest leu leusup lsa micronano modpathol mp mi nature natastron natbiomedeng nbt natcatal ncb nchembio nchem nclimate ncomms ndigest natecolevol natelectron nenergy ng ngeo nathumbehav ni natmachintell nmat nm natmetab nmeth nmicrobiol milestones nnano neuro nphoton nphys nplants nprot nrc nrcardio natrevchem nrclinonc nrdp nrd nrendo nrgastro nrg nri natrevmats nrmicro nrm nrneph nrneurol nrn natrevphys nrrheum nrurol nsmb natsustain npp am npj npjamd npjbiofilms npjbcancer npjcleanwater npjclimatsci npjcompumats npjdigitalmed npjflexelectron npjgenmed npjmatdeg npjmgrav npjmolphen npjparkd npjpollcon npjprecisiononcology npjpcrm npjqi npjquantmats npjregenmed npjschz npjscifood npjscilearn npjsba npjvaccines nutd onc oncsis palcomms pr pj npjpcrm pcan tpj scientificamerican scientificamericanmind scientificdata srep sigtrans sc scsandc tp nature ncomms nmat nchem srep nature ncomms nprot srep'},
                                  {u'valid': True,
                                   u'type': u'fixed',
                                   u'value': u'/current-issue'}],
                   u'type': u'generated'}]
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'/articles/'),
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
                u'.full-width-print',
                [
                    Field(
                        u'title',
                        'header > .grid > .small-space-below *::text',
                        []),
                    Field(
                        u'author',
                        'header > .grid > .grid > li > a > span *::text',
                        []),
                    Field(
                        u'journal',
                        'header > .grid > .flex-box > div:nth-child(1) > .flex-box-item > li:nth-child(1) > i *::text',
                        []),
                    Field(
                        u'time',
                        'header > .grid > .flex-box > .last > .flex-box-item > dl > dd:nth-child(6) > time::attr(datetime)',
                        []),
                    Field(
                        u'abstract',
                        '#abstract-content > p *::text',
                        [])])]]
