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

    def __init__(self, id, name, manufacturer_name, manufacturer_prov_code, manufacturer_type, website,
                 fat_content_percent, moisture_percent, particularities, flavour, characteristics, ripening, organic,
                 category_type, milk_type, milk_treatment_type, rind_type, last_update_date):
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
        self.__id = id
        self.__name = name
        self.__manufacturer_name = manufacturer_name
        self.__manufacturer_prov_code = manufacturer_prov_code
        self.__manufacturer_type = manufacturer_type
        self.__website = website
        self.__fat_content_percent = fat_content_percent
        self.__moisture_percent = moisture_percent
        self.__particularities = particularities
        self.__flavour = flavour
        self.__characteristics = characteristics
        self.__ripening = ripening
        self.__organic = organic
        self.__category_type = category_type
        self.__milk_type = milk_type
        self.__milk_treatment_type = milk_treatment_type
        self.__rind_type = rind_type
        self.__last_update_date = last_update_date

    @classmethod
    def from_array(cls, array):
        """
        Creates a Cheese object from an array.
        :param array:
        :return:
        """
        return cls(array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9],
                   array[10], array[11], array[12], array[13], array[14], array[15], array[16], array[17])

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
            .format(self.__id, self.__name, self.__manufacturer_name, self.__manufacturer_prov_code,
                    self.__manufacturer_type, self.__website, self.__fat_content_percent, self.__moisture_percent,
                    self.__particularities, self.__flavour, self.__characteristics, self.__ripening, self.__organic,
                    self.__category_type, self.__milk_type, self.__milk_treatment_type, self.__rind_type,
                    self.__last_update_date)
