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
#http://www.journals.elsevier.com/[...]/recent-articles

class JournalsElsevier(BasePortiaSpider):
    name = "www.journals.elsevier.com"
    allowed_domains = [
        u'www.journals.elsevier.com',
        u'www.mayoclinicproceedings.org',
        u'www.sciencedirect.com']
    start_urls = [{u'url': u'https://www.sciencedirect.com/journal/[...]/articles-in-press', u'fragments': [{u'valid': True, u'type': u'fixed', u'value': u'http://www.journals.elsevier.com/'}, {u'valid': True, u'type': u'list', u'value': u'biological-psychiatry drug-resistance-updates autoimmunity-reviews current-opinion-in-immunology current-opinion-in-chemical-biology ageing-research-reviews clinical-gastroenterology-and-hepatology cytokine-and-growth-factor-reviews current-opinion-in-microbiology current-opinion-in-neurobiology brain-stimulation brain-behavior-and-immunity 09608524bioresource-technology current-opinion-in-pharmacology environmental-pollution#description catalysis-today clinical-nutrition clinical-colorectal-cancer best-practice-and-research-clinical-endocrinology-and-metabolism environmental-modelling-and-software cortex antiviral-research cement-and-concrete-composites atherosclerosis bone diabetes-and-metabolism building-and-environment clinical-immunology ecological-indicators#description clinical-neurophysiology environmental-research computers-and-education computers-and-education cognitive-psychology cognitive-psychology the-annals-of-thoracic-surgery dna-repair bba-biomembranes appetite astroparticle-physics clinical-oncology bioorganic-chemistry decision-support-systems advances-in-water-resources biological-psychology biological-psychology digestive-and-liver-disease ad-hoc-networks acta-astronautica brain-research-bulletin computers-and-chemical-engineering behavioural-brain-research contraception clinical-breast-cancer the-breast biomedicine-and-pharmacotherapy best-practice-and-research-clinical-obstetrics-and-gynaecology brain-research computers-in-industry epilepsy-and-behavior annual-reviews-in-control applied-geochemistry engineering-geology#description clinical-genitourinary-cancer computers-and-geosciences computer-networks clinical-lymphoma-myeloma-and-leukemia clinical-radiology annals-of-physics annales-de-linstitut-henri-poincare-c-analyse-non-lineaire brain-and-language brain-and-language brain-and-cognition brain-and-cognition design-studies epilepsy-research archives-of-cardiovascular-diseases basic-and-applied-ecology computational-materials-science#description anaerobe clinics-in-dermatology applied-mathematics-letters archives-of-civil-and-mechanical-engineering early-human-development economics-and-human-biology economics-and-human-biology contemporary-clinical-trials brachytherapy burns comptes-rendus-physique ecological-informatics cretaceous-research complementary-therapies-in-medicine electronic-commerce-research-and-applications electronic-commerce-research-and-applications computer-speech-and-language blood-cells-molecules-and-diseases comptes-rendus-chimie comparative-immunology-microbiology-and-infectious-diseases clinical-biomechanics applied-ergonomics applied-ergonomics digital-investigation chemical-physics archives-of-oral-biology behavioural-processes behavioural-processes deep-sea-research-part-ii-topical-studies-in-oceanography data-and-knowledge-engineering atomic-data-and-nuclear-data-tables computer-standards-and-interfaces calphad applied-ocean-research arthropod-structure-and-development comptes-rendus-geoscience displays brain-and-development brazilian-journal-of-infectious-diseases cryogenics chaos-solitons-and-fractals clinical-neurology-and-neurosurgery comptes-rendus-palevol advances-in-medical-sciences computer-aided-geometric-design annals-of-nuclear-energy current-problems-in-cancer british-journal-of-oral-and-maxillofacial-surgery asian-journal-of-surgery cognitive-systems-research cognitive-systems-research actas-urologicas-espanolas computers-and-graphics applied-radiation-and-isotopes auris-nasus-larynx dynamics-of-atmospheres-and-oceans comptes-rendus-biologies atencion-primaria biocybernetics-and-biomedical-engineering comptes-rendus-mecanique clinical-imaging discrete-applied-mathematics biomedicine-and-pharmacotherapy annales-dendocrinologie chemical-engineering-journal bulletin-des-sciences-mathematiques annals-of-pure-and-applied-logic discrete-mathematics discrete-optimization comptes-rendus-mathematique endeavour animal-feed-science-and-technology filtrationseparation frontiers-in-neuroendocrinology journal-of-autoimmunity gondwana-research 00219517journal-of-catalysis journal-of-hazardous-materials international-journal-of-plasticity information-fusion gynecologic-oncology fuel#description journal-of-adolescent-health journal-of-adolescent-health 17505836international-journal-of-greenhouse-gas-control journal-of-dermatological-science journal-of-molecular-liquids journal-of-affective-disorders journal-of-affective-disorders evolution-and-human-behavior evolution-and-human-behavior hormones-and-behavior experimental-gerontology experimental-eye-research information-and-management information-and-management fungal-ecology icarus journal-of-memory-and-language journal-of-memory-and-language journal-of-food-and-drug-analysis hearing-research geotextiles-and-geomembranes immunology-letters experimental-hematology 03064379information-systems journal-of-manufacturing-systems journal-of-biomedical-informatics immunobiology journal-of-neuroimmunology information-and-software-technology image-and-vision-computing journal-of-archaeological-science journal-of-archaeological-science international-journal-of-psychophysiology international-journal-of-psychophysiology geothermics journal-of-neuroradiology journal-of-magnetic-resonance journal-of-engineering-and-technology-management journal-of-engineering-and-technology-management journal-of-pharmacological-sciences information-processing-and-management#description information-processing-and-management#description journal-of-invertebrate-pathology#description journal-of-health-economics journal-of-health-economics human-immunology general-hospital-psychiatry general-hospital-psychiatry journal-of-molecular-catalysis-b-enzymatic journal-of-insect-physiology fungal-biology finite-elements-in-analysis-and-design health-policy health-policy journal-of-fluorine-chemistry#description jornal-de-pediatria journal-of-aerosol-science forensic-science-international journal-of-differential-equations food-and-bioproducts-processing journal-of-great-lakes-research human-movement-science human-movement-science journal-of-cultural-heritage journal-of-geodynamics gaceta-sanitaria gaceta-sanitaria journal-of-clinical-anesthesia heart-and-lung-the-journal-of-acute-and-critical-care journal-for-nature-conservation journal-of-econometrics journal-of-econometrics journal-of-molecular-spectroscopy journal-of-pediatric-and-adolescent-gynecology journal-of-clinical-neuroscience journal-of-electrocardiology international-journal-of-sediment-research geobios journal-of-african-earth-sciences journal-of-neurolinguistics journal-of-neurolinguistics journal-of-mathematical-psychology journal-of-mathematical-psychology insurance-mathematics-and-economics insurance-mathematics-and-economics hellenic-journal-of-cardiology journal-of-atmospheric-and-solar-terrestrial-physics fusion-engineering-and-design#description journal-of-complexity journal-of-functional-analysis journal-of-comparative-pathology the-journal-of-emergency-medicine fire-safety-journal journal-of-asia-pacific-entomology journal-of-approximation-theory gastroenterologia-y-hepatologia journal-of-applied-logic journal-of-geometry-and-physics finite-fields-and-their-applications irbm journal-of-number-theory#description journal-of-engineering-and-technology-management expositiones-mathematicae journal-of-algebra journal-of-mathematical-economics journal-of-mathematical-economics journal-of-exercise-science-and-fitness geofisica-internacional indagationes-mathematicae historia-mathematica historia-mathematica hong-kong-journal-of-occupational-therapy journal-of-the-anatomical-society-of-india progress-in-materials-science materials-science-and-engineering-r-reports nano-today physics-of-life-reviews progress-in-neurobiology progress-in-retinal-and-eye-research pharmacology-and-therapeutics progress-in-quantum-electronics seminars-in-immunology seminars-in-cancer-biology sleep-medicine-reviews progress-in-surface-science metabolic-engineering mayo-clinic-proceedings progress-in-nuclear-magnetic-resonance-spectroscopy 10538119neuroimage pain resuscitation neurobiology-of-aging neurobiology-of-disease neuropharmacology quaternary-science-reviews oral-oncology psychoneuroendocrinology osteoarthritis-and-cartilage pattern-recognition landscape-and-urban-planning landscape-and-urban-planning knowledge-based-systems#description parkinsonism-and-related-disorders the-ocular-surface radiotherapy-and-oncology lung-cancer journal-of-psychiatric-research journal-of-psychiatric-research nitric-oxide-biology-and-chemistry progress-in-solid-state-chemistry schizophrenia-research schizophrenia-research progress-in-aerospace-sciences journal-of-proteomics new-astronomy-reviews precambrian-research methods molecular-genetics-and-metabolism mitochondrion nutrition-metabolism-and-cardiovascular-diseases marine-geology neurobiology-of-learning-and-memory neurobiology-of-learning-and-memory preventive-medicine nutrition progress-in-crystal-growth-and-characterization-of-materials sleep-medicine ocean-modelling seminars-in-fetal-and-neonatal-medicine neuroscience#description maturitas respiratory-medicine journal-of-the-energy-institute neuropsychologia neuropsychologia seminars-in-perinatology journal-of-plant-physiology ore-geology-reviews molecular-and-cellular-neuroscience the-journal-of-supercritical-fluids neuromuscular-disorders progress-in-organic-coatings journal-of-psychosomatic-research journal-of-psychosomatic-research pancreatology journal-of-physiology-paris journal-of-process-control obesity-research-and-clinical-practice journal-of-sound-and-vibration mechanism-and-machine-theory psychiatry-research psychiatry-research leukemia-research sensors-and-actuators-a-physical process-biochemistry mechatronics journal-of-volcanology-and-geothermal-research neuropeptides pediatric-infectious-disease polymer-testing quaternary-geochronology seizure-european-journal-of-epilepsy patient-education-and-counseling patient-education-and-counseling nuclear-medicine-and-biology journal-of-structural-geology sedimentary-geology microvascular-research solid-state-ionics medecine-et-maladies-infectieuses physiology-and-behavior physiology-and-behavior reproductive-toxicology physical-mesomechanics pediatric-clinics-of-north-america precision-engineering nursing-outlook nursing-outlook magnetic-resonance-imaging paediatric-respiratory-reviews quaternary-international quaternary-research neuroscience-letters neurologia materials-chemistry-and-physics neuroscience-research marine-structures pediatric-neurology pedobiologia science-and-justice physica-medica robotics-and-autonomous-systems midwifery midwifery rangeland-ecology-and-management nuclear-physics-a ocean-engineering planetary-and-space-science marine-micropaleontology psychiatry-research-neuroimaging optical-switching-and-networking orthopedic-clinics-of-north-america medical-engineering-and-physics microelectronic-engineering pathologie-biologie speech-communication optical-fiber-technology mechanics-research-communications performance-evaluation journal-of-systems-architecture revista-portuguesa-de-pneumologia pathology-research-and-practice public-health public-health physica-d-nonlinear-phenomena reproductive-biology orthopaedics-and-traumatology-surgery-and-research radiation-measurements physics-and-chemistry-of-the-earth microelectronics-reliability parallel-computing revista-iberoamericana-de-micologia neuroimaging-clinics-of-north-america pediatrics-and-neonatology pain-management-nursing pain-management-nursing legal-medicine journal-of-symbolic-computation microelectronics-journal nuclear-data-sheets medicina-clinica soils-and-foundations journal-of-web-semantics medical-hypotheses science-of-computer-programming revue-neurologique microprocessors-and-microsystems new-carbon-materials mycoscience linear-algebra-and-its-applications medical-dosimetry new-astronomy revista-da-associacao-medica-brasileira nephrologie-and-therapeutique neurologia-i-neurochirurgia-polska neurochirurgie journal-of-microbiological-methods polymer operations-research-letterseditorial-board journal-of-pure-and-applied-algebra reports-on-mathematical-physics revista-mexicana-de-biodiversidad nursing-clinics-of-north-america nursing-clinics-of-north-america journal-of-the-korean-statistical-society neuroscience science-and-sports revista-argentina-de-microbiologia mathematical-social-sciences mathematical-social-sciences pratiques-psychologiques pratiques-psychologiques nutrition-clinique-et-metabolisme studies-in-mycology surface-science-reports nano-energy jacc-cardiovascular-imaging the-lancet-hiv jacc-heart-failure trends-in-analytical-chemistry the-lancet-haematology physics-of-the-dark-universe current-opinion-in-virology trends-in-cardiovascular-medicine arabian-journal-of-chemistry surgery-for-obesity-and-related-diseases neuroimage-clinical developmental-cognitive-neuroscience journal-of-co2-utilization ecosystem-services ecosystem-services algal-research nonlinear-analysis-hybrid-systems current-opinion-in-environmental-sustainability swarm-and-evolutionary-computation vascular-pharmacology current-opinion-in-insect-science stem-cell-research current-opinion-in-chemical-engineering surgical-oncology technovation technovation vaccine fungal-biology-reviews ticks-and-tick-borne-diseases journal-of-functional-foods structural-safety journal-of-saudi-chemical-society thin-walled-structures social-science-and-medicine social-science-and-medicine energy-for-sustainable-development journal-of-natural-gas-science-and-engineering journal-of-fluency-disorders journal-of-fluency-disorders tectonophysics saudi-journal-of-biological-sciences health-and-place health-and-place journal-of-sport-and-health-science journal-of-sport-and-health-science journal-of-evidence-based-dental-practice journal-of-visceral-surgery multiple-sclerosis-and-related-disorders pervasive-and-mobile-computing ultrasonics journal-of-manufacturing-processes urology aeolian-research epidemics physical-mesomechanics international-journal-of-surgery urban-forestry-and-urban-greening urban-forestry-and-urban-greening 00396028surface-science-including-surface-science-letters progress-in-natural-science-materials-international astronomy-and-computing seminars-in-pediatric-neurology thin-solid-films the-veterinary-journal contact-lens-and-anterior-eye transplant-immunology sustainable-cities-and-society journal-of-computational-science vibrational-spectroscopy utilities-policy utilities-policy atmospheric-pollution-research international-journal-of-disaster-risk-reduction wave-motion computational-and-theoretical-chemistry anaesthesia-critical-care-and-pain-medicine vacuum telecommunications-policy telecommunications-policy journal-of-bone-oncology journal-of-infection-and-public-health complementary-therapies-in-clinical-practice journal-of-hydro-environment-research#description journal-of-communication-disorders journal-of-communication-disorders european-geriatric-medicine journal-of-herbal-medicine transfusion-and-apheresis-science journal-of-global-antimicrobial-resistance legal-medicine medicina-intensiva spatial-statistics palaeoworld socio-economic-planning-sciences socio-economic-planning-sciences journal-of-forensic-and-legal-medicine polar-science international-journal-of-paleopathology journal-of-asia-pacific-entomology journal-of-integrative-agriculture revista-brasileira-de-reumatologia results-in-physics taiwanese-journal-of-obstetrics-and-gynecology high-energy-density-physics european-journal-of-integrative-medicine biologically-inspired-cognitive-architectures transfusion-clinique-et-biologique theoretical-computer-science wilderness-and-environmental-medicine statistical-methodology statistics-and-probability-letters topology-and-its-applications revista-internacional-de-andrologia'}, {u'valid': True, u'type': u'fixed', u'value': u'/recent-articles'}], u'type': u'generated'}]
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'abstract$', u'article\\/pii'),
                deny=(u'twitter', u'facebook', u'googleplus', u'linkedin')
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
                u'.cl-m-3-3',
                [
                    Field(
                        u'journal',
                        '.Publication > .publication-volume > .publication-title > .size-xl > .publication-title-link *::text',
                        []),
                    Field(
                        u'time',
                        '.Publication > .publication-volume > div > .size-m *::text',
                        []),
                    Field(
                        u'title',
                        '.Head > .title-text *::text',
                        []),
                    Field(
                        u'author',
                        '.Banner > .wrapper > .AuthorGroups > .author-group > a > span *::text',
                        []),
                    Field(
                        u'abstract',
                        '.Abstracts > .author *::text',
                        []),
                    Field(
                        u'keywords',
                        '.Keywords > div:nth-child(2) *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.cl-m-3-3',
                [
                    Field(
                        u'journal',
                        '.Publication > .publication-volume > .publication-title > .size-xl > .publication-title-link *::text',
                        []),
                    Field(
                        u'time',
                        '.Publication > .publication-volume > div:nth-child(2) > .size-m *::text',
                        []),
                    Field(
                        u'title',
                        '.Head > .title-text *::text',
                        []),
                    Field(
                        u'author',
                        '.Banner > .wrapper > .AuthorGroups > .author-group > a > span *::text',
                        []),
                    Field(
                        u'abstract',
                        '.Abstracts > .author *::text',
                        []),
                    Field(
                        u'keywords',
                        '.Keywords > .keywords-section *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.cl-m-3-3',
                [
                    Field(
                        u'journal',
                        '.Publication > .publication-volume > .publication-title > .size-xl > .publication-title-link *::text',
                        []),
                    Field(
                        u'time',
                        '.Publication > .publication-volume > div > .size-m *::text',
                        []),
                    Field(
                        u'title',
                        '.Head > .title-text *::text',
                        []),
                    Field(
                        u'author',
                        '.Banner > .wrapper > .AuthorGroups > .author-group > a > span *::text',
                        []),
                    Field(
                        u'abstract',
                        '.Abstracts > .author > div > p *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'main',
                [
                    Field(
                        u'journal',
                        '.pageHeader > .wrapped > .widget-body > .page-header > div > .layout-two-columns > .wrapped > .widget-body > .pb-columns > div:nth-child(1) > .pb-autoheight > .widget > .wrapped > .widget-body > .logo-container > a:nth-child(2) > img::attr(alt)',
                        []),
                    Field(
                        u'time',
                        '.pageBody > .wrapped > .widget-body > .page-body > div > .layout-two-columns > .wrapped > .widget-body > .pb-columns > .width_11_16 > .pb-autoheight > .articleNavigation > .wrapped > .widget-body > .articleNav > .artBib > a *::text',
                        []),
                    Field(
                        u'title',
                        '.pageBody > .wrapped > .widget-body > .page-body > div > .layout-two-columns > .wrapped > .widget-body > .pb-columns > .width_11_16 > .pb-autoheight > .articleContent > .wrapped > .widget-body > .article > .artInfoWrapper > .articleInfo > h1 *::text',
                        []),
                    Field(
                        u'author',
                        '.pageBody > .wrapped > .widget-body > .page-body > div > .layout-two-columns > .wrapped > .widget-body > .pb-columns > .width_11_16 > .pb-autoheight > .articleContent > .wrapped > .widget-body > .article > .artInfoWrapper > .articleInfo > .authorGroup > div:nth-child(1) > .openAuthorLayer *::text',
                        []),
                    Field(
                        u'abstract',
                        '.pageBody > .wrapped > .widget-body > .page-body > div > .layout-two-columns > .wrapped > .widget-body > .pb-columns > .width_11_16 > .pb-autoheight > .articleContent > .wrapped > .widget-body > .article > .tabs > .tab-content > .abstract *::text',
                        [])])]]
