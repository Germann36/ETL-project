#Ставим на расписание: ежедневное выполнение в 10 утра
import schedule
import time

schedule.every().day.at("10:00").do(insert_row)
 
while True:
    schedule.run_pending()
    time.sleep(1)
