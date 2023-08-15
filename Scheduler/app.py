from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.executors.pool import ProcessPoolExecutor
import time
from config.db import database

scheduler = AsyncIOScheduler(executors={
    'default': ProcessPoolExecutor(4)  # Use 4 processes in the pool
})

# ... Add your jobs to the scheduler ...



# Create a background scheduler
scheduler = AsyncIOScheduler()

# Define the task you want to schedule
def my_task():
    message = {'msg': f'Scheduled task executed at: {time.strftime("%Y-%m-%d %H:%M:%S")}'}
    database.put(message)
# trigger
trigger = CronTrigger(second=3)
# Schedule the asynchronous task
scheduler.add_job(my_task, trigger)

# Start the scheduler
scheduler.start()

