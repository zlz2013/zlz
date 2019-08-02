import base64
import copy
import json
import hmac
import time


class JWT():
    def __init__(self):
        pass

    @staticmethod
    def encode(payload,key,exp=300):
        header={'alg':'HS256','typ':'JWT'}
        #sort_keys:将无序列表，有序排列
        #separators:制定序列化后的JSON串格式，第一个参数，指每个键值对之间的连接符号，
        # 第二个参数，指的是每一个键值对中建和值的连接符号
        header_json=json.dumps(header,sort_keys=True,separators=(',',':'))
        # header_bs=base64.urlsafe_b64encode(header_json.encode())
        header_bs=JWT.b64encode(header_json.encode())
        print(header_bs)

        payload=copy.deepcopy(payload)
        #添加共有声明-exp 且值为未来时间戳
        payload['exp']=int(time.time())+exp
        payload_json=json.dumps(payload,separators=(',',':'),sort_keys=True)
        # payload_bs=base64.urlsafe_b64encode(payload_json.encode())
        payload_bs=JWT.b64encode(payload_json.encode())
        print(payload_bs)

        #签名
        #判断传入的key的类型
        if isinstance(key,str):
            key=key.encode()
        hm = hmac.new(key,header_bs+b'.'+payload_bs, digestmod='SHA256')
        # hm_bs=base64.urlsafe_b64encode(hm.digest())
        hm_bs=JWT.b64encode(hm.digest())
        print(hm_bs)

        jwt=header_bs + b'.' +payload_bs+b'.'+hm_bs
        return jwt

    @staticmethod
    def b64encode(j_s):
        #替换生成出来的b64串中的占位符 =
        return base64.urlsafe_b64encode(j_s.replace(b'=',b''))

    @staticmethod
    def b64decode(b64_s):
        rem=len(b64_s)%4
        if rem>0:
            b64_s+=b'='*(4-rem)
        return base64.urlsafe_b64decode(b64_s)

    @staticmethod
    def decode(token,key):
        #校验两次hmac结果
        #检查exp公有声明的有效性
        #注意b64 = 要补全
        #校验成功 返回 payload字典对象
        header_b,payload_b,sign=token.split(b'.')
        if isinstance(key,str):
            key=key.encode()
        #比较两次HMAC结果
        hm=hmac.new(key,header_b+b'.'+payload_b,digestmod='SHA256')
        if sign != JWT.b64encode(hm.digest()):
            raise JwtSignError('---sign error!!!')
        #获取payload
        payload_json=JWT.b64decode(payload_b)
        payload=json.loads(payload_json.decode())
        #校验exp是否过期
        exp=payload['exp']
        now=time.time()
        if now>exp:
            #过期
            raise JwtExpireError('---The token is expire!!!')
        return payload

class JwtSignError(Exception):
    def __init__(self,error_msg):
        self.error_msg=error_msg

    def __str__(self):
        return '<JwtSignError is %s>'%(self.error_msg)

class JwtExpireError(Exception):
    def __init__(self,error_msg):
        self.error_msg=error_msg
    def __str__(self):
        return '<JwtExpireError is %s>'%(self.error_msg)

if __name__=='__main__':


    payload={'username':'lz'}
    key='lz'
    a=JWT()
    b=a.encode(payload,'lz')
    c=JWT.b64encode(b)
    print(b)
    print(c)

    res=JWT.decode(b,'lz')
    print(res)
