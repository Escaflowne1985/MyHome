# coding:utf-8
import os
import sys
import datetime

# 文件应用路径文件夹配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# 密钥配置，默认
SECRET_KEY = 'm_cb9d+k+9sseu$tdtdb@t!z!o+94w6c&^72z49ik@(!axe%=#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 访问权限配置
ALLOWED_HOSTS = ['*']

# 应用配置
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'xadmin',  # xadmin主体
    'crispy_forms',  # 渲染表格模块
    'reversion',  # 为模型通过版本设置提供数据回滚功能
    'rest_framework',

    'Configuration',  # 环境&数据配置
    'MyHomePage',  # 我的个人主页
    'GameTool',  # 游戏功能
    'User',  # 游戏功能
]

# 中间件配置，默认
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 路由配置，默认
ROOT_URLCONF = 'MyHome.urls'

# Web服务器网关接口配置，默认
WSGI_APPLICATION = 'MyHome.wsgi.application'

# 配置用户表单继承关系
AUTH_USER_MODEL = "User.UserProfile"
# 渲染模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static',
            }
        },
    },
]

# 数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 密码验证配置，默认
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 全球化配置
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static静态文件配置
STATIC_URL = '/static/'
# STATIC_ROOT = 'static' # 配置云服务器使用
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media多媒体文件配置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 发送邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.qq.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "33034782@qq.com"
EMAIL_HOST_PASSWORD = "citvzqlnixmkbjcb"
EMAIL_USE_TLS = True
EMAIL_FROM = EMAIL_HOST_USER

# CK 富文本编辑器配置
CKEDITOR_CONFIGS = {
    # django-ckeditor默认使用default配置
    'default': {
        # 编辑器宽度自适应
        'width': 'auto',
        'height': '250px',
        # tab键转换空格数
        'tabSpaces': 4,
        # 工具栏风格
        'toolbar': 'Custom',
        # 工具栏按钮
        'toolbar_Custom': [
            # 表情 代码块
            ['Smiley', 'CodeSnippet'],
            # 字体风格
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            # 字体颜色
            ['TextColor', 'BGColor'],
            # 链接
            ['Link', 'Unlink'],
            # 列表
            ['NumberedList', 'BulletedList'],
            # 最大化
            ['Maximize']
        ],
        # 插件
        'extraPlugins': ','.join(['codesnippet', 'prism', 'widget', 'lineutils']),
    }
}
CKEDITOR_JQUERY_URL = 'https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_UPLOAD_PATH = "uploads/"

# 缓存配置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',  # 指定缓存使用的引擎
        'LOCATION': os.path.join(BASE_DIR, 'caches'),  # 指定缓存的路径
        'TIMEOUT': 300,  # 缓存超时时间(默认为300秒,None表示永不过期)
        'OPTIONS': {
            'MAX_ENTRIES': 300,  # 最大缓存记录的数量
            'CULL_FREQUENCY': 3,  # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY
        }
    }
}

# rest framework 配置选项
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',            # IsAuthenticated 仅通过认证的用户
        # 'rest_framework.permissions.AllowAny',                   # AllowAny 允许所有用户
        # 'rest_framework.permissions.IsAdminUser',                # IsAdminUser 仅管理员用户
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',  # IsAuthenticatedOrReadOnly 认证的用户可以完全操作，否则只能get读取
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # 在 DRF中配置JWT认证
        'rest_framework.authentication.BasicAuthentication',  # 在 DRF中基础认证信息，特定认证修改使用
        # 'rest_framework.authentication.TokenAuthentication',  # 全局Token认证
        # 'rest_framework.authentication.SessionAuthentication',  # 全局Session认证
        # 'article.auth.MyTokenAuthentication',  # 自定义的带过期的认证
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 新版drf schema_class默认用的是rest_framework.schemas.openapi.AutoSchema
}

# 配置jwt载荷中的有效期设置
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),  # 设置Token有效期
    'JWT_AUTH_HEADER_PREFIX': 'DataYang',  # token前缀：headers中 Authorization 值的前缀
    'JWT_ALLOW_REFRESH': True,  # 刷新token：允许使用旧的token换新token
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(hours=24),  # token有效期：token在24小时内过期, 可续期token
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'User.utils.jwt_response_payload_handler',  # 5.自定义JWT载荷信息：自定义返回格式，需要手工创建
}

## SECURITY安全设置 - 支持http时建议开启
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# SECURE_SSL_REDIRECT = True  # 将所有非SSL请求永久重定向到SSL
# SESSION_COOKIE_SECURE = True  # 仅通过https传输cookie
# CSRF_COOKIE_SECURE = True  # 仅通过https传输cookie
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # 严格要求使用https协议传输
# SECURE_HSTS_PRELOAD = True  # HSTS为
# SECURE_HSTS_SECONDS = 60
# SECURE_CONTENT_TYPE_NOSNIFF = True  # 防止浏览器猜测资产的内容类型
