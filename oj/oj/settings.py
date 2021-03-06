# -*- coding: utf-8 -*-

# Scrapy settings for oj project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'oj'

SPIDER_MODULES = ['oj.spiders']
NEWSPIDER_MODULE = 'oj.spiders'

# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# REDIS_URL = 'redis://127.0.0.1:6379'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
SCHEDULER_PERSIST = True


# Obey robots.txt rules
ROBOTSTXT_OBEY = False
HTTPPROXY_ENABLED = True
LOG_ENABLED = True
LOG_ENCODING = "utf-8"
DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 3600
CONCURRENT_REQUESTS = 1
RETRY_ENABLED = False
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

#TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Cookie":"connect.sid=s%3A8uXBE5ddfuL2jqVeV7XUuSsA86dhx_on.FvkDenfGbWB6xnIOQKLJrXZ654fiD3YpHqxIae3KQss",
    "Host":"loj.ac",
    "Referer":"https://loj.ac/problem",
    "Upgrade-Insecure-Requests":"1",
    # "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2765.26 Safari/537.36"
}


#SPIDER_MIDDLEWARES = {
#    'oj.middlewares.OjSpiderMiddleware': 543,
#}


DOWNLOADER_MIDDLEWARES = {
    'oj.middlewares.RandomUserAgentMiddleware': 543,
    # 'oj.middlewares.RandomProxyMiddleware': 345
}


#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# ITEM_PIPELINES = {
#    'oj.pipelines.OjPipeline': 300,
# }


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
