# SPIDER_MODULES = ['spider.spiders']

NEWSPIDER_MODULE = 'spider.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 5

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/'
              'apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br' !!!! Ruins everything
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'spider.pipelines.DuplicatesPipeLine': 200,
    'spider.pipelines.TextPipeLine': 300,
    'spider.pipelines.PublisherPipeLine': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 20
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# SPLASH_URL = 'http://192.168.0.102:8050'
SPLASH_URL = 'http://splash:8050'

DNS_TIMEOUT = 15

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

# FEEDS = {"my_items.json": {
#     "format": "jsonlines",
#     "encoding": "utf-8",
# },
# }

RU_NEWSPAPERS_URLS = [
    'https://aif.ru/',
    'https://lenta.ru/',
    'https://www.mk.ru/',
    'https://rg.ru/',
    'https://www.kommersant.ru/',
    'https://www.vedomosti.ru/',
    'https://www.kp.ru/',
    'https://tass.ru/',
]
US_NEWSPAPERS_URLS = [
    'https://www.nytimes.com/',
    'https://edition.cnn.com/',
    'https://www.nbcnews.com/',
    'https://www.usatoday.com/',
    'https://www.foxnews.com/',
    'https://abcnews.go.com/',
    'https://www.latimes.com/',
    'https://nypost.com/',
    'https://www.tampabay.com/',

]
DE_NEWSPAPERS_URLS = [
    'https://www.focus.de/',
    'https://www.spiegel.de/',
    'https://www.faz.net/aktuell/',
    'https://www.sueddeutsche.de/',
    'https://taz.de/',
    'https://www.deutschland.de/de',
    'https://www.tagesschau.de/',
    'https://www.mdr.de/nachrichten/index.html',
    'https://www.tagesspiegel.de/',
    'https://www.deutschlandfunk.de/',
    'https://www.nachrichtenleicht.de/',
    'https://www.stern.de/',
    'https://www.rnd.de/',
    'https://www.handelsblatt.com/',
    'https://www.berliner-zeitung.de/',
    'https://www.fnp.de/',
    'https://www.rtl.de/',
    'https://www.nd-aktuell.de/',
    'https://www.rbb24.de/',
    'https://www.msn.com/de-de',
]

UK_NEWSPAPERS_URLS = [
    'https://www.thesun.co.uk/',
    'https://www.theguardian.com/international',
    'https://news.sky.com/',
    'https://www.independent.co.uk/',
    'https://www.thetimes.co.uk/',
    'https://www.express.co.uk/',
    'https://www.mirror.co.uk/'
    'https://metro.co.uk/',
    'https://www.ft.com/',
    'https://www.standard.co.uk/',
]

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.2; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0", ]
LOG_LEVEL = 'INFO'
# LOG_LEVEL = 'DEBUG'
RETRY_ENABLED = False

# Socket settings
SUBSCRIBERS_EXPECTED = 1
