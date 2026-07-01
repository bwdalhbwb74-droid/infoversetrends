"""
InfoVerse Hub V2
Daily Scheduler
"""

import schedule
import time

from topics import collect_topics


class Scheduler:

    def __init__(self):

        pass


    def daily_job(self):
        """
        Daily topics collection.
        """

        print("Collecting today's topics...")

        collect_topics()

        print("Done.")


    def start(self):
        """
        Start scheduler.
        """

        schedule.every().day.at("00:00").do(
            self.daily_job
        )

        print("Scheduler Started.")

        while True:

            schedule.run_pending()

            time.sleep(30)


scheduler = Scheduler()
