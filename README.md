# celery-django-example
    
## 缘起
> 因为需要使用延时异步任务的功能，对比后选用celery。在跟随官方教程配置过程中，发现celery4.+开始官方放弃了对Windows的支持。
> 为了方便在Windows中进行开发和调试，寻找解决办法。


## 环境
    Microsoft Windows 10 专业版 x64-based PC
    Python 3.6.6
    Django 2.0.8
    Reids 3.2.100

## 参考
[using-celery-with-django][using-celery-with-django]

 
### requirements
    $ pip install -r requirements.txt

### Start Celery Worker
| OS | Command |
| --- | ----------- |
| Ubuntu   | $ celery -A proj worker -l info |
| Windows   | $ celery -A proj worker -l info --pool=solo |


### Start Celery Producer
    $ python task_producer.py

## Windows上遇见的异常
Windows上会报如下错误

    Traceback (most recent call last):
      File "task_producer.py", line 18, in <module>
        print(res.get())
      File "D:\Code\Work\Personal\celery-django-example\venv\lib\site-packages\celery\result.py", line 224, in get
        on_message=on_message,
      File "D:\Code\Work\Personal\celery-django-example\venv\lib\site-packages\celery\backends\async.py", line 190, in wait_for_pending
        return result.maybe_throw(callback=callback, propagate=propagate)
      File "D:\Code\Work\Personal\celery-django-example\venv\lib\site-packages\celery\result.py", line 329, in maybe_throw
        self.throw(value, self._to_remote_traceback(tb))
      File "D:\Code\Work\Personal\celery-django-example\venv\lib\site-packages\celery\result.py", line 322, in throw
        self.on_ready.throw(*args, **kwargs)
      File "D:\Code\Work\Personal\celery-django-example\venv\lib\site-packages\vine\promises.py", line 217, in throw
        reraise(type(exc), exc, tb)
      File "D:\Code\Work\Personal\celery-django-example\venv\lib\site-packages\vine\five.py", line 179, in reraise
        raise value
    ValueError: not enough values to unpack (expected 3, got 0)
根据搜索引擎查到以下资料[celery-github-issue][celery-github-issue]

Windows平台通用解决方案

    celery -A your_app_name worker --pool=solo -l info

### 修复后的Console Log


Worker

    $ celery -A proj worker --pool=solo -l info
    
    
    -------------- celery@DESKTOP-SINA8S9 v4.2.1 (windowlicker)
    ---- **** -----
    --- * ***  * -- Windows-10-10.0.17134-SP0 2018-08-24 15:02:48
    -- * - **** ---
    - ** ---------- [config]
    - ** ---------- .> app:         proj:0x3598b90
    - ** ---------- .> transport:   redis://127.0.0.1:6379/0
    - ** ---------- .> results:     redis://127.0.0.1:6379/0
    - *** --- * --- .> concurrency: 6 (solo)
    -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
    --- ***** -----
     -------------- [queues]
                    .> celery           exchange=celery(direct) key=celery
    
    
    [tasks]
      . demoapp.tasks.add
      . demoapp.tasks.mul
      . demoapp.tasks.xsum
      . proj.celery.debug_task
    
    [2018-08-24 15:02:48,469: INFO/MainProcess] Connected to redis://127.0.0.1:6379/0
    [2018-08-24 15:02:48,476: INFO/MainProcess] mingle: searching for neighbors
    [2018-08-24 15:02:49,491: INFO/MainProcess] mingle: all alone
    [2018-08-24 15:02:49,497: WARNING/MainProcess] d:\code\work\personal\celery-django-example\venv\lib\site-packages\celery\fixups\django.py:200: UserWarning: Using settings.DEBUG leads to a memory leak, never use this set
    ting in production environments!
      warnings.warn('Using settings.DEBUG leads to a memory leak, never '
    [2018-08-24 15:02:49,497: INFO/MainProcess] celery@DESKTOP-SINA8S9 ready.
    [2018-08-24 15:02:57,986: INFO/MainProcess] Received task: demoapp.tasks.add[c3a225b3-e76c-4e99-bff0-92207d2b6835]
    [2018-08-24 15:02:57,987: INFO/MainProcess] Task demoapp.tasks.add[c3a225b3-e76c-4e99-bff0-92207d2b6835] succeeded in 0.0s: 5
    [2018-08-24 15:02:57,990: INFO/MainProcess] Received task: demoapp.tasks.add[43549f0c-1256-40af-b9f0-85fed1d5aea0]  ETA:[2018-08-24 07:03:00.988404+00:00]
    [2018-08-24 15:03:00,987: INFO/MainProcess] Task demoapp.tasks.add[43549f0c-1256-40af-b9f0-85fed1d5aea0] succeeded in 0.0s: 5
Producer
    
    $ python task_producer.py

    实时任务
    2018-08-24T15:02:57.934548
    2018-08-24T15:02:57.985446
    result: 5
    2018-08-24T15:02:57.988404
    延时任务
    2018-08-24T15:02:57.989402
    result: 5
    2018-08-24T15:03:00.987967




[using-celery-with-django]: http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#using-celery-with-django
[celery-github-issue]: https://github.com/celery/celery/issues/4081
