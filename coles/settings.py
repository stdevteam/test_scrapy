# -*- coding: utf-8 -*-

# Scrapy settings for coles project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'coles'

SPIDER_MODULES = ['coles.spiders']
NEWSPIDER_MODULE = 'coles.spiders'

ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline':1
}

IMAGES_STORE = 'images'

REQUIRED_IMAGES = [
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/2/5/3/2534298.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/3/2/2/3228468.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/2/5/3/2534276.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/7/6/9/7695272.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/8/5/5/8554130.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/2/0/8/208216.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/5/0/8/5089012.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/2/8/7/287041.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/3/8/1/381323.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/2/8/6/286923.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/5/1/3/5138490.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/3/2/2/3222494.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/9/3/6/9368743.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/7/1/7/7172208.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/7/2/0/7203039.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/5/6/1/5615272.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/7/1/8/7181107.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/2/8/6/286843.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/3/1/8/318495.jpg",
    "https://shop.coles.com.au/wcsstore/Coles-CAS/images/5/4/3/5435340.jpg",
]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'coles (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'coles.middlewares.ColesSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'coles.middlewares.ColesDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'coles.pipelines.ColesPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
