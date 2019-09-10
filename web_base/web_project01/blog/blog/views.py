
from django.http import HttpResponse

from user.models import UserProfile
import redis

def test(request):
    # u=UserProfile.objects.get(username='lz')
    # u.score+=1
    # u.save()

    pool=redis.ConnectionPool(host='127.0.0.1',port=6379,db=1)
    r=redis.Redis(connection_pool=pool)
    while True:
        try:
            with r.lock('lz',blocking_timeout=3) as lock:
                u = UserProfile.objects.get(username='lz')
                u.score+=1
                u.save()
            break
        except Exception as e:
            print('lock is failed')


    return HttpResponse('HI HI HI')