from apscheduler.schedulers.background import BackgroundScheduler
from .views import update_all_products
from Bot.config.config import INTERVAL_MINUTES

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.start()

    # Запуск задачи обновления всех продуктов каждые 30 минут
    scheduler.add_job(update_all_products, 'interval', minutes=int(INTERVAL_MINUTES))
