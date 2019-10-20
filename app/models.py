"""Models stores all of the cheese application models.

Models: Cheese
"""

__author__ = "Harry Hum"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Harry Hum"
__email__ = "hum00051@algonquinlive.com"
__status__ = "Development"


class Cheese(object):

    def __init__(self, id="", name="", manufacturer_name="", manufacturer_prov_code="", manufacturer_type="",
                 website="", fat_content_percent="", moisture_percent="", particularities="", flavour="",
                 characteristics="", ripening="", organic="", category_type="", milk_type="", milk_treatment_type="",
                 rind_type="", last_update_date=""):
        """
        Constructor for Cheese.
        :param id:
        :param name:
        :param manufacturer_name:
        :param manufacturer_prov_code:
        :param manufacturer_type:
        :param website:
        :param fat_content_percent:
        :param moisture_percent:
        :param particularities:
        :param flavour:
        :param characteristics:
        :param ripening:
        :param organic:
        :param category_type:
        :param milk_type:
        :param milk_treatment_type:
        :param rind_type:
        :param last_update_date:
        """
        self.id = id
        self.name = name
        self.manufacturer_name = manufacturer_name
        self.manufacturer_prov_code = manufacturer_prov_code
        self.manufacturer_type = manufacturer_type
        self.website = website
        self.fat_content_percent = fat_content_percent
        self.moisture_percent = moisture_percent
        self.particularities = particularities
        self.flavour = flavour
        self.characteristics = characteristics
        self.ripening = ripening
        self.organic = organic
        self.category_type = category_type
        self.milk_type = milk_type
        self.milk_treatment_type = milk_treatment_type
        self.rind_type = rind_type
        self.last_update_date = last_update_date

    @classmethod
    def from_array(cls, array):
        """
        Creates a Cheese object from an array.
        :param array:
        :return:
        """
        return cls(array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9],
                   array[10], array[11], array[12], array[13], array[14], array[15], array[16], array[17])

    def to_array(self):
        return [self.id, self.name, self.manufacturer_name, self.manufacturer_prov_code,
                self.manufacturer_type, self.website, self.fat_content_percent, self.moisture_percent,
                self.particularities, self.flavour, self.characteristics, self.ripening, self.organic,
                self.category_type, self.milk_type, self.milk_treatment_type, self.rind_type,
                self.last_update_date]

    def __str__(self):
        """
        Returns the string interpretation of the Cheese object.
        :return:
        """
        return "CheeseId = {}, CheeseNameEn = {}, ManufacturerNameEn = {}, ManufacturerProvCode = {}, " \
               "ManufacturingTypeEn = {}, WebSiteEn = {}, FatContentPercent = {}, MoisturePercent = {}, " \
               "ParticularitiesEn = {}, FlavourEn = {}, CharacteristicsEn = {}, " \
               "RipeningEn = {}, Organic = {}, CategoryTypeEn = {}, MilkTypeEn = {},MilkTypeFr, " \
               "MilkTreatmentTypeEn = {}, RindTypeEn = {}, LastUpdateDate = {}" \
            .format(self.id, self.name, self.manufacturer_name, self.manufacturer_prov_code,
                    self.manufacturer_type, self.website, self.fat_content_percent, self.moisture_percent,
                    self.particularities, self.flavour, self.characteristics, self.ripening, self.organic,
                    self.category_type, self.milk_type, self.milk_treatment_type, self.rind_type,
                    self.last_update_date)
