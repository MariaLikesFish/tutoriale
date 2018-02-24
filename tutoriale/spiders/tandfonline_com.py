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


class Tandfonline(BasePortiaSpider):
    name = "www.tandfonline.com"
    allowed_domains = [u'www.tandfonline.com']
    start_urls = [{u'url': u'http://www.tandfonline.com/action/showAxaArticles?journalCode=[...]', u'fragments': [{u'valid': True, u'type': u'fixed', u'value': u'http://www.tandfonline.com/action/showAxaArticles?journalCode='}, {u'valid': True, u'type': u'list', u'value': u'tadp20 kaup20 bpts20 uajb20 uajb20 kepi20 laps20 kccy20 iort20 kcbt20 tcph20 ionc20 rbri20 ncny20 camh20 camh20 iaut20 icbi20 hbsm20 vbmd20 vbmd20 iblo20 icac20 itam20 kchl20 icnv20 ldrt20 ibij20 ibij20 uast20 teis20 hdvn20 hdvn20 tdia paph20 lpde20 tcwr20 ntcn20 ntcn20 gcic20 ucbs20 tcjp20 ierc20 vaeh20 lecr20 lecr20 gaan20 ucmg20 ucmg20 gcec20 iebm20 iahb20 iahb20 iode20 taje20 tcyt20 pcgn20 pcgn20 tdmp20 ioto20 bbrm20 tcoi20 ibjn20 ibih20 uasr20 tato20 gthm20 gapa20 tadr20 cbst20 cbps20 ccos20 tajf20 tfor20 ucsu20 teco20 nbrr20 yacb20 naqi20 uemg20 ther20 tacb20 lagb20 tacs20 saga20 tasc20 tasc20 iedd20 iett20 hhci20 ieop20 iedc20 ieru20 iebt20 ierv20 ieds20 tjoo20 iiri20 ierm20 iern20 ierz20 idrt20 iemd20 ietp20 iemt20 tgda20 tigr20 ierd20 iery20 ijic20 ijic20 tjom20 tjom20 khvi20 cijw20 iimt20 lfri20 ceth20 ceth20 ijdt20 tsdw20 ijmf20 iimm20 terg20 terg20 tags20 yhct20 gits20 iiht20 ijas20 tfab20 igye20 teee20 yjoc20 bher20 uegm20 iivs20 ueht20 ugmb20 iipi20 ljge20 uasp20 uasp20 ielu20 cfai20 imif20 uopt20 uear20 titr20 vjmb20 vjmb20 uism20 tjhr20 uoeh20 nnmr20 ijcl20 sgra20 ghpr20 ueqe20 lbps20 yirs20 yjbr20 tjeo20 rjbe20 tjfe20 uhvc20 kfly20 tizo20 taca20 tijr20 uahh20 list20 tips20 tjen20 tnah20 lmsb20 tjas tiee20 cjas20 ipdp20 gmas20 gmas20 lfbt20 gfer20 uexm20 gnst20 teop20 ufio20 ginf20 vgnt20 vgnt20 tmam20 taar20 yisr20 yisr20 ijan20 ijan20 hchn20 hchn20 imup20 thpl20 gfel20 yhis20 lmsc20 lspr20 krnb20 tjsp20 ipec20 hmbr20 hmbr20 rjsp20 igas20 lsei20 hnuc20 tppc20 pnrh20 unht20 psns20 yrer20 ipgm20 tmph20 gnpl20 tped20 gspm20 yscm20 uawm20 gpol20 tpal20 tnzv20 tphm20 cphm20 cphm20 uths20 iclb20 tjot20 trmp20 sact20 sact20 cngs20 cngs20 gsrp20 ulrm20 gmos20 bssc20 smar20 umgt20 gpch20 iocc20 iocc20 lsst2 lsfm20 icdv20 tqrt20 gpht20 lmst20 goms20 glma20 umgd20 tnzb20 nncs20 rquf20 rquf20 gopt20 tphl20 ismr20 bose20 tost20 tnzz20 gnte20 upst20 tjss20 yprc20 njhn20 lpla20 tmma20 grad20 nmcm20 tqma20 GMPS20 GMPS20 toin20 koni20 koni20 kvir20 kcam20 kogg20 iern20 hsem20 hsem20 ierj20 ierh20 nurw20 wsub20 wsub20 brfs21 ttrb20 ttrb20 tbps20 ierx20 rsse20 rsse20 iups20 iaac20 iaac20 kncl20 kncl20 ierr20 kisl20 khvi20 nvsd20 gags20 tsab20 ttra21 ttra21 PCNS20 plcp21 plcp21 ypch20 tgcl20 tgnh20 ypgh20 kbie20 utrb20 tgei20 tjpi20 gcry20 itxm20 uawm20 ghbi20 tech rwin20 trsl20 isju20 tsos20 cses20 cses20 pcnp20 pcnp20 lqen20 ipsm20 tjbd20 igen20 ulrm20 gsch20 isum20 isum20 gmpr20 ytsr20 isio20 ipdr20 tcyt20 iasl20 iasl20 umcf20 gaan20 tveq20 hapc20 tran20 tran20 uesb20 infd20 uedi20 uedi20 ihuf20 tqrt20 htlm20 TCPS20 TCPS20 wjnf20 tbob20 tfls20 ysre20 wjsa21 iphs20 iclp20 iclp20 uhvc21 imhn20 imhn20 rspb20 gsta20 iptp20 itxr20 tham20 hapn20 hapn20 iusp20 yacb20 gcov20 wcli20 wcli20 ysic20 lsaa20 ieod20 uemj20 uemj20 tzme20 tnze20 wagr20 ther20 ttqm20 usbr20 tjov20 lstm20 ttzo20 nens20 lsqa20 test20 test20'}], u'type': u'generated'}]
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'/doi/full/', u'showAxaArticles'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[]]
