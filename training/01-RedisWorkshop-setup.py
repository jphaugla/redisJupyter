import inspect
import json
import redis
import redisearch
import rejson
import pprint
import time

import workshop.strings
import workshop.hashes
import workshop.lists
import workshop.sets
import workshop.zsets

from workshop import redis_cloud

config = redis_cloud.load_redis_cloud_config()
r = redis_cloud.reset_redis_connection(config)

workshop.reset_redis_connection = lambda : redis_cloud.reset_redis_connection(config)

redis_workshop_loaded = True


