# # # a = 0
# # #
# # #
# # # def send_message():
# # #     global a
# # #     a = 1790
# # #     # session[key]=code
# # #
# # #
# # # def func2(p):
# # #     if p == a:
# # #         pass
# # #
# # #
# # # def func3():
# # #     pass
# # #
# # #
# # # class User:
# # #     pass
# # #
# # #
# # # user = User()
# # # user.username = 'zhangsan'
# # #
# # # filename= '1440w.jpg'
# # # result = filename.rsplit('.')
# # # print(result[-1])
# # # filename.endswith('jpg')
# #
# # # -*- coding: utf-8 -*-
# # # flake8: noqa
# import os
# #
# import time
#
# from qiniu import Auth, put_file, etag
# import qiniu.config
#
# # 需要填写你的 Access Key 和 Secret Key
# from settings import Config
#
# access_key = 'ak'
# secret_key = 'sk'
#
# # # 构建鉴权对象
# # q = Auth(access_key, secret_key)
# #
# # # 要上传的空间
# # bucket_name = 'myblog202005'
# #
# # # 上传后保存的文件名
# # key = 'my-python-logo.png'
# # policy={
# #  'callbackUrl':'http://qb2w77i8c.bkt.clouddn.com/callback.php',
# #  'callbackBody':'filename=$(fname)&filesize=$(fsize)'
# #  }
# #
# # # 生成上传 Token，可以指定过期时间等
# # token = q.upload_token(bucket_name, key, 3600)
# # print(token)
# #
# # # 要上传文件的本地路径
# # localfile = os.path.join(Config.UPLOAD_ICON_DIR, 'v2-b9a93719ecd1519f7bffc06f91cd8d45_r.jpg')
# #
# # ret, info = put_file(token, key, localfile)
# # print(info)
# # print(ret)
# # token = token.split('=:')[0]+'='
# # print(token)
# # e= str(time.time()).split('.')[0]
# # domain= 'http://qb2w77i8c.bkt.clouddn.com/'
# # url = domain+key+"?e="+e+'&attname=&token='+token
# # print(url)
#
#
#
# import requests
# from qiniu import Auth
# #AK、SK可在控制台的个人中心里面获取
# access_key = 'ak'
# secret_key = 'sk'
# q = Auth(access_key, secret_key)
# #有两种方式构造base_url的形式
# base_url = 'http://%s/%s' % ('qb2w79i8c.bkt.clouddn.com', 'my-python-logo.png')
# #或者直接输入url的方式下载
# # base_url = 'http://domain/key'
# #可以设置token过期时间
# private_url = q.private_download_url(base_url, expires=3600)
# print(private_url)
# r = requests.get(private_url)
# import random
#
# filename='xxx193.jpg'
# ran = random.randint(1, 1000)
# suffix = filename.rsplit('.')[-1]
# key = filename.rsplit('.')[0] + '_' + str(ran) + '.' + suffix
# print(key)


# -*- coding: utf-8 -*-
# flake8: noqa
import os

from qiniu import Auth, put_file, etag
import qiniu.config

#需要填写你的 Access Key 和 Secret Key
from settings import Config

# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth
from qiniu import BucketManager

access_key = '1fXvG9wkbN7AgRUG6usHDcRP5Bb85apcovRAIITP'
secret_key = 'Aqf1lPAmUG72EdZJ7PxKtWHfWDYNdUycZP1TaAIN'
# 构建鉴权对象
q = Auth(access_key, secret_key)
# 要上传的空间
bucket_name = 'myblog202006'

bucket = BucketManager(q)
# 要拉取的文件名
key = 'testname_351.png'
ret, info = bucket.prefetch(bucket_name, key)
print(info)
print(ret)


#删除bucket_name 中的文件 key
ret, info = bucket.delete(bucket_name, key)
print(info)
print(ret)

