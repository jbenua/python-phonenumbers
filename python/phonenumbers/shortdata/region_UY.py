"""Auto-generated file, do not edit by hand. UY metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_UY = PhoneMetadata(id='UY', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[19]\\d{2,3}', possible_number_pattern='\\d{3,4}', possible_length=(3, 4)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    emergency=PhoneNumberDesc(national_number_pattern='128|911', possible_number_pattern='\\d{3,4}', example_number='911', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='1(?:0[4-9]|1[2368]|2[0-3568]|787)|911', possible_number_pattern='\\d{3,4}', example_number='104', possible_length=(3, 4)),
    standard_rate=PhoneNumberDesc(national_number_pattern='1787', possible_number_pattern='\\d{4}', example_number='1787', possible_length=(4,)),
    carrier_specific=PhoneNumberDesc(),
    short_data=True)
