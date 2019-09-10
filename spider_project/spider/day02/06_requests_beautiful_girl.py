import requests

url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1565352243871&di=097e10aa0f49a642544f0839d404351c&imgtype=0&src=http%3A%2F%2Fimg3.duitang.com%2Fuploads%2Fitem%2F201511%2F25%2F20151125151708_CwPkR.jpeg'
headers={'user-agent':'mozilla/5.0'}
res=requests.get(url=url,headers=headers)
html=res.content
filename=url[-10]
with open('girl.jpg','wb') as f:
    f.write(html)