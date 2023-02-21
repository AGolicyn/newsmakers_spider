from scrapy.utils.project import get_project_settings
settings = get_project_settings()

LANGUAGE_MAPPER = {}
LANGUAGE_MAPPER.update({}.fromkeys(settings['RU_NEWSPAPERS_URLS'], 'RU'))
LANGUAGE_MAPPER.update({}.fromkeys(settings['US_NEWSPAPERS_URLS'], 'EN'))
LANGUAGE_MAPPER.update({}.fromkeys(settings['DE_NEWSPAPERS_URLS'], 'DE'))

GLOBAL_URLS = []
GLOBAL_URLS.extend(settings['RU_NEWSPAPERS_URLS'])
GLOBAL_URLS.extend(settings['US_NEWSPAPERS_URLS'])
GLOBAL_URLS.extend(settings['DE_NEWSPAPERS_URLS'])

COUNTRY_MAPPER = {}
COUNTRY_MAPPER.update({}.fromkeys(settings['RU_NEWSPAPERS_URLS'], 'Russia'))
COUNTRY_MAPPER.update({}.fromkeys(settings['US_NEWSPAPERS_URLS'], 'USA'))
COUNTRY_MAPPER.update({}.fromkeys(settings['DE_NEWSPAPERS_URLS'], 'Germany'))
