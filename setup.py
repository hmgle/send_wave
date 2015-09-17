from setuptools import setup

requirements = ['requests', 'requests_oauthlib']

setup(
    name = "send_wave",
    version = "1.0",
    author = "hmgle",
    author_email = "dustgle@gmail.com",
    description = (
        """send msg via weibo, fanfou, .etc."""
    ),
    license = "GPLv2",
    url = "https://github.com/hmgle/send_wave",
    install_requires = requirements,
    scripts = [
        'request_token.py', 'fanfou_config.py',
        'fanfouphoto.py', 'fanfousender.py',
        'tqq_msg.py', 'tqq_pic.py',
        'weibo_msg.py', 'weibo_pic.py'
    ]
)
