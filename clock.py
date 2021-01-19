from apscheduler.schedulers.blocking import BlockingScheduler

from temperature import temperaturefunction

sched = BlockingScheduler() 

sched.add_job(temperaturefunction, 'cron', hour=7, minute=30)
sched.add_job(temperaturefunction, 'cron', hour=15, minute=30)
    
sched.start()