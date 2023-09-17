# Scrapy settings for intro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "intro"

SPIDER_MODULES = ["intro.spiders"]
NEWSPIDER_MODULE = "intro.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "intro (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
COOKIES = {"_mibhv":"anon-1675965111153-7173809033_4481","atrc":"d48dd289-bb78-444f-9b12-800c86f55b44","ak_bmsc": "5A3B280AB8AA089E93FFC2D4AE16E982~000000000000000000000000000000~YAAQFLQRYEPZiJeKAQAA/eVoohVKGuYg2BqBT1Jt0IXbFqE/46aZ6zvlaUxErYzG8XLRqSeOjG4mUdoYQJ2JzRqGLz8pxbKqLBKDwGLtTkTCH132iuiKmyc8ZFypk3y+ID6uceruv4DMPA6Ou/YbrRIXuIGdisNEDPhVa27KMQ6X28tnjcPxk/00sp5KRdvOuNujkZCwAxCUSTGOvM1l3MAhIZp9Rwob7NdDlrdHXiZsmRwyRMY5U4Xegt/ypPS0kVEW8F6uIzFobzSuPsDPUxR99C0JSNHoyOGk6AjxqJy4H8EAq8y44g90r6DtQEty/2RFdGVyt4lUk8KBPY1n1+UGVV/IiRRdKwfHnt70iYx2p1ZzzhKG1icb9nqaVqbJmh01aww7HRODB6zxGe0ZnC3SqB1bkkegnTN6WtBKGJWX7B+yHvzuoQpr+bF6NkQRdZSKnEHhllRWjBFw6FjC90q8RBurA3AVztZV7cMei/qNie15veO2IM38qQTu8cnAX6v99BMy0NfHo1FGSBSYiQDejTzl6V2zNhhDkDcYmm+Oe8fJD7lmvs8xS31RrRoJjO3QcEMB9MA5NY5h6uHH7WiP5A0Mqda4/LYu8l5t2n0WJxUYn6OUpn14KHR/LMpaRkpW+g==", "s_ecid" :"MCMID%7C42942869526993913931696225266067582139", "_abck":"CEFBB6D5E1F5364CC66436630B125846~0~YAAQEkw5F1qTa5uKAQAA11aoogrIv1k+6ZmibbeZcBl3HeSWCLZBY0ahYLtF0Hvj3wRyqgAR/1Y31i17l14ll7AQQ1Vuz6i2204F/FfP9G93IUHGloy3ihXJn3cqefjAJHet9UyVORpszvXVgrsxCUmh6FNiezz0A/FYdh8c1fdDR9EOVYpgYmad5LMSoVV/vaTVwtWZ2V5aX4CWJWv0SGTt9yv0wKNt2hnvfr4P34vacamEhIidzLH15mPasAo4PgpojzsCbLc5iI1y9f3w1ZXsnXanQQkCEJcMDhTrx7np4VKH1IMkInEPaaHFssBjGz0p4IUYZMIXzvDUsGyySL19iF0pp32h1svQH73PhcLTAi1YrUkbT1vm87MMlAKENl+py4ywbgWWxrHRBUUx3k/J5T+GZxs=~-1~-1~1694949606", "s_cc" : "true", "_uetsid" : "5a28ea1053cf11eea69bf3220c676045", "_ga" : "GA1.2.987200008.1694613475", "da_lid": "CE140C499A73EA163BE7BB99F06361C7E3|0|0|0", "bm_mi":"CC9466367A908AF930C2CB0075CD6B87~YAAQFLQRYOrXiJeKAQAAz+BoohURjj0gQoOwCgvVW4MK5x6ukyJsykmdYXzhHT6p3YgDovfWBPPqftOUZO+NDD9e96x9c6iQKhTkBw0+jdFN4Ljw+nY2uWcrmblxT5kTCIrgPVYRYOnQ3UaqNiAS9KGM/kWFmiMvw1XvWLstAUUdQslA0wKehRYbVcZ0046EmUZsa21C/X8sE2Qf9h1Q0FgRy4j3xjocNm0T0M2Ujs4e/ZR/kDrcSPH9br7PRS7GOXuoGdB5/snNqoqeDAAuPUfQfVz1L8FJmUSrpEYvrUkS9OV0b1C2h/0QJFo75/Yje5QX4rjf20DqsPhe4HQZY1+ReL3LPGQdM7cbnVvw/g==~1","AMCV_E4860C0F53CE56C40A490D45%40AdobeOrg":"1585540135%7CMCIDTS%7C19618%7CMCMID%7C42942869526993913931696225266067582139%7CMCAAMLH-1695546698%7C3%7CMCAAMB-1695546698%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1694949098s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0","_fbp":"fb.1.1694613492922.1700352203", "_gid":"GA1.2.816839715.1694786050", "bm_sv" : "EDF4CE50FA3185711E56B52D223E36A7~YAAQEkw5F/sJa5uKAQAA2zN+ohVu7oC1vCEMlBiH/mx2ztVzmDIIYZlUbaYFd1lq2CWjD9tzLzPKxmUsdTgJv5iZIwq7Tp5g8eIV6lYDQLCDVjDba2m2qjw8fHsZeYPU7LSe2F8XAWYh8P/EpKYSjSnzz+OACju9OkCygxjWj3LYjlcpbrYLn/IssgNfoQ/QAKeqUyrjbeQZ7IqxYeBLJg9BX9rEUy1XHgKIZ+wUHj4mzAGZ63I6V4C/BkzJacjv~1","_mibhv":"anon-1675965111153-7173809033_4481","_ait":"0a4f5c31-0792-686e-6911-9581210c8e2b", "consumer":"default","DCO":"wdc","AMCVS_E4860C0F53CE56C40A490D45%40AdobeOrg":"1","_4c_mc_":"bf1be925-b755-4544-bb5d-3c3fa91ca90f","atrc":"d48dd289-bb78-444f-9b12-800c86f55b44","ak_bmsc":"5A3B280AB8AA089E93FFC2D4AE16E982~000000000000000000000000000000~YAAQFLQRYEPZiJeKAQAA/eVoohVKGuYg2BqBT1Jt0IXbFqE/46aZ6zvlaUxErYzG8XLRqSeOjG4mUdoYQJ2JzRqGLz8pxbKqLBKDwGLtTkTCH132iuiKmyc8ZFypk3y+ID6uceruv4DMPA6Ou/YbrRIXuIGdisNEDPhVa27KMQ6X28tnjcPxk/00sp5KRdvOuNujkZCwAxCUSTGOvM1l3MAhIZp9Rwob7NdDlrdHXiZsmRwyRMY5U4Xegt/ypPS0kVEW8F6uIzFobzSuPsDPUxR99C0JSNHoyOGk6AjxqJy4H8EAq8y44g90r6DtQEty/2RFdGVyt4lUk8KBPY1n1+UGVV/IiRRdKwfHnt70iYx2p1ZzzhKG1icb9nqaVqbJmh01aww7HRODB6zxGe0ZnC3SqB1bkkegnTN6WtBKGJWX7B+yHvzuoQpr+bF6NkQRdZSKnEHhllRWjBFw6FjC90q8RBurA3AVztZV7cMei/qNie15veO2IM38qQTu8cnAX6v99BMy0NfHo1FGSBSYiQDejTzl6V2zNhhDkDcYmm+Oe8fJD7lmvs8xS31RrRoJjO3QcEMB9MA5NY5h6uHH7WiP5A0Mqda4/LYu8l5t2n0WJxUYn6OUpn14KHR/LMpaRkpW+g==","cookiePreferences":"%7B%22experience%22%3Atrue%2C%22advertising%22%3Atrue%7D","_csrf":"aTbwWXB640Zsl-oEEe_2EEqO", "_ga_33B19D36CY":"GS1.1.1694941898.6.1.1694943294.32.0.0","_gcl_au":"1.1.890781053.1694613476","bm_sz":"7C114E1599596F0248A146B1F6664827~YAAQEkw5Fyv8aJuKAQAAISbooRUKHK3DwcVbZmb4IcZ9CHJm3X7uoK/biRX4NLkpQpJ/Y+5gHnlySkeISqHBdUq4ECamPUlWJe1ggBCjgjYDto69PZQsx/9odEDz1AKVcXLo/zxQVrsROWAqz7Dn3gUPI0aicJJOQJNIiRC+oztonUUtIx5+UNHzGc4XUccgxNOscbF7E/ffL+82bMEXsiY9NbpwnrM5/is8l2bip57yfUgWkr5kiOjTzkJxNYP7Op+mc8YdYonOB15neqlt68Qzu4YkrV+l90j4NTFRfOToRg==~4342326~4403764", "_ga_H653QXESTP":"GS1.1.1694942057.6.0.1694942063.0.0.0", "_uetvid":"6e02ecf0a8a211ed9f9f971d9c8fd036","akavpau_tesco_groceries":"1694943594~id=1229fc287962ff6e2b0ec97f48d977fd","trkid":"a85ad080-00fd-4f77-8d7d-d0f291a2572d"}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
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
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   "intro.middlewares.IntroSpiderMiddleware": 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "intro.middlewares.IntroDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "intro.pipelines.IntroPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
