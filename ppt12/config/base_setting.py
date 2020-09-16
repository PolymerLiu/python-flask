# 公共配置文件

# 为true会打印log
DEBUG = False

# 为true会打印sql语句
SQLALCHEMY_ECHO = False

SQLALCHEMY_ENCODING = 'utf8mb4'

# local-------------------------------------
# 初始化DB配置
SQLALCHEMY_DATABASE_URI = "mysql://root:python123456@127.0.0.1/movie_cat"

SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG_TB_INTERCEPT_REDIRECTS = False

SECRET_KEY = 'python'

DOMAIN = {
  'www': 'http://localhost:5000'
}

RELEASE_PATH = 'ppt9/9.1/release_version'

AUTH_COOKIE_NAME = 'movie_cat'