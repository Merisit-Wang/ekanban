import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

type_list = [('1', '开发-需求分析'),
('2', '开发-代码开发'),
('3', '开发-FT开发'),
('4', '测试-用例开发'),
('5', '测试-手工执行'),
('6', '测试-RF开发'),
('7', '故障'),
('8', '故障-定位'),
('9', '质量改进'),
('10', '质量改进-自动化用例'),
('11', '质量改进-业务分析'),
('12', '培训分享'),
('13', '专项支持'),
('14', '其他')]

priority_list = [('1', '必须完成'),
                 ('2', '尽量完成'),
                 ('3', '尝试完成'),
                 ('4', '无优先级')]

expect_days_list = [('0', '0'),
                    ('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('5', '5')]

actual_days_list = [('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4'),
                    ('5', '5')]

author_list = [("aaaaaaa", "aaaaaaa"),
               ("bbbbbbb", "bbbbbbb")]