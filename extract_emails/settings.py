BOT_NAME = 'extract_emails'
SPIDER_MODULES = ['extract_emails.spiders']
NEWSPIDER_MODULE = 'extract_emails.spiders'

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 512


DOWNLOADER_MIDDLEWARES = {'scrapy_crawlera.CrawleraMiddleware': 610}
ITEM_PIPELINES = {
   'extract_emails.pipelines.ExtractEmailsPipeline': 300,
}

HTTPCACHE_ENABLED = False
HTTPERROR_ALLOW_ALL = True

CRAWLERA_ENABLED = True
CRAWLERA_APIKEY = '6fb5e1784f5846af94c3f7c9cfaef420'
CONCURRENT_REQUESTS_PER_DOMAIN = 32


RETRY_ENABLED = False
SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.DownloaderAwarePriorityQueue'
REACTOR_THREADPOOL_MAXSIZE = 300
LOG_LEVEL = 'INFO'

DOWNLOAD_MAXSIZE = 10000000
REDIRECT_ENABLED = False
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429]
DOWNLOAD_FAIL_ON_DATALOSS = False



















# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'extract_emails (+http://www.yourdomain.com)'

# Obey robots.txt rules

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# this one is added new

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 1
# CONCURRENT_REQUESTS_PER_IP = 16 doest support by priority queue



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
#    'extract_emails.middlewares.ExtractEmailsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
#     'scrapy_crawlera.CrawleraMiddleware': 610
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False




# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings



#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# LOG_ENABLED = False

# DOWNLOAD_DELAY = .5
# AUTOTHROTTLE_ENABLED = True
# CRAWLERA_PRESERVE_DELAY = True




# RETRY_TIMES = 2

# DUPEFILTER_DEBUG = True
# DOWNLOAD_TIMEOUT = 10
# COOKIES_ENABLED = False


# REDIRECT_MAX_TIMES = 10
# AJAXCRAWL_ENABLED = True
# DEPTH_PRIORITY = 1
# SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

# Limit ITEMS to Debug
# CLOSESPIDER_ITEMCOUNT = 60
