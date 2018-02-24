from __future__ import absolute_import

import scrapy
from collections import defaultdict
from scrapy.loader.processors import Join, MapCompose, Identity
from w3lib.html import remove_tags
from .utils.processors import Text, Number, Price, Date, Url, Image


class PortiaItem(scrapy.Item):
    fields = defaultdict(
        lambda: scrapy.Field(
            input_processor=Identity(),
            output_processor=Identity()
        )
    )

    def __setitem__(self, key, value):
        self._values[key] = value

    def __repr__(self):
        data = str(self)
        if not data:
            return '%s' % self.__class__.__name__
        return '%s(%s)' % (self.__class__.__name__, data)

    def __str__(self):
        if not self._values:
            return ''
        string = super(PortiaItem, self).__repr__()
        return string


class InferenceForTheTwoParameterBathtubShapedDItem(PortiaItem):
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    keywords = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class RecentAdvancesInLipidSeparationsAndStructuItem(PortiaItem):
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class PhenotypicalChangeOfTumorAssociatedMacrophaItem(PortiaItem):
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    keywords = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class EmbryoProductionOfTwoSympatricSnappingShriItem(PortiaItem):
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    keywords = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class SpousesSubjectiveSocialStatusPredictsOlderItem(PortiaItem):
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    keywords = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class IntracerebroventricularInjectionsOfEndotoxinItem(PortiaItem):
    keywords = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class ReformingTheTaxonomyInDisordersOfConsciousItem(PortiaItem):
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class IncreasingMotorNeuronExcitabilityToTreatWeItem(PortiaItem):
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class TheDeliriumAndPopulationHealthInformaticsCItem(PortiaItem):
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class NonclassicalConvolutionsAndTheirUsesSpringItem(PortiaItem):
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    keywords = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class KlothoIsANonEnzymaticMolecularScaffoldFoItem(PortiaItem):
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class MiniaturizedNeuralSystemForChronicLocalIntItem(PortiaItem):
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class ProgressiveDeafnessdystoniaDueToSeracMutatiItem(PortiaItem):
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class IncreasedHepaticAbcaTransporterIsAssociatedItem(PortiaItem):
    keywords = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class ANewAlgorithmToVisualizeTheIndividualRelaItem(PortiaItem):
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class MembraneProteinInsertionThroughAMitochondriItem(PortiaItem):
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class ASelfAssembledNanoscaleRoboticArmControlleItem(PortiaItem):
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class CranialTumorSurgicalOutcomesAtAHighVolumeItem(PortiaItem):
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class EffectsOfAllopurinolOnEndothelialFunctionAItem(PortiaItem):
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class SuccessfulSupportOfBiventricularHeartFailurItem(PortiaItem):
    keywords = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class ImmunoproteomicIdentificationOfAntigenicCandItem(PortiaItem):
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    keywords = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class ExactInferenceForLaplaceDistributionUnderPItem(PortiaItem):
    keywords = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class TreatmentPatternsAndLowDensityLipoproteinCItem(PortiaItem):
    keywords = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class PrecursorsOfHumanCdCytotoxicTLymphocytesIItem(PortiaItem):
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class AnEmAlgorithmForTheDestructiveComPoissonItem(PortiaItem):
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    keywords = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()

class ResidentMemoryTCellsRunxAndHideScienceIItem(PortiaItem):
    journal = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    author = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    time = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    abstract = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    link=scrapy.Field()
