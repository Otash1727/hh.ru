from Bot.import_all_methods import *
from Bot.config.config import URL
import requests

router=Router()
logger=logger_name()

@router.message(ProductInfo.request)
async def client_request_api(message: Message, state: FSMContext):
    try:
        article = message.text.strip()
        if not article.isdigit():
            await message.reply(text='<b>Пожалуйста, пришлите действительный номер артикула.</b>',reply_markup=help_found_article(),parse_mode=ParseMode.HTML)
            return await state.set_state(ProductInfo.request)

        # Логируем URL для отладки
        print(f"Артикул: {article}")
        print(f"Запрос к URL: {URL.format(article=article)}")

        # Отправка запроса к Wildberries API
        response = requests.get(f"{URL}{article}")
        if response.status_code != 200:
            await message.reply(text='<b>Не удалось получить данные о продукте. Попробуйте позже.</b>',parse_mode=ParseMode.HTML)
            return await state.set_state(ProductInfo.request)

        data = response.json()

        # Проверка наличия данных о продуктах
        if not data.get('data') or not data['data'].get('products'):
            await message.reply(text=f'Товар с артикулом {article} не найден в базе Wildberries.',reply_markup=help_found_article())
            return 

        # Извлечение данных продукта
        product_data = data['data']['products'][0]
        name = product_data['name']
        price = product_data['salePriceU'] / 100
        article_product=product_data['id']
        rating = product_data['reviewRating']
        quantity =product_data['totalQuantity']
        await create_product(name,article_product,price,rating,quantity)
        # Формирование ответа пользователю
        await message.reply(
            f"Название: <b>{name}</b>\nАртикул: <b>{article_product}</b>\nЦена: <b>{price}</b> RUB\nРейтинг: <b>{rating} ⭐️</b>\nКоличество на складах: <b>{quantity}</b>",parse_mode=ParseMode.HTML,reply_markup=article_button())
        await state.clear()
    except requests.exceptions.RequestException as e:
        await message.reply(text=f'Ошибка при обращении к Wildberries API: {e}')
    except KeyError as e:
        await message.reply(text=f'Некорректный ответ от API: отсутствует ключ {e}')
    except Exception as e:
        await message.reply(text=f'Произошла ошибка: {e}')
   
