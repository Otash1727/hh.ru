from Bot.import_all_methods import *

router=Router()
logger=logger_name()

@router.message(Command('start'))
async def start_bot_command(message:Message,is_user:bool):
    try:
        user_id=message.from_user.id
        profile_name=message.from_user.full_name
        username=message.from_user.username
        print(is_user)
        if is_user:
            pass
        else:
            await create_user_record(user_id,username,profile_name)
        await message.answer(text='<b>Нажмите кнопку, чтобы получить информацию</b>',parse_mode=ParseMode.HTML,reply_markup=article_button())

    except Exception as e:
        logger.warning(e)
        await send_loggingFile()
    await logging_info(user_id=user_id,text='start_bot_command',handler='start_bot_command')




@router.callback_query(F.data=='get_article')
async def get_information_acticle(callback:CallbackQuery,state:FSMContext):
    try:
        user_id=callback.from_user.id
        await state.set_state(ProductInfo.request)
        await callback.answer(text='')
        await callback.message.answer(text='<b>Введите код артикула для получения информации о продукте</b>',parse_mode=ParseMode.HTML)

    except Exception as e:
        logger.warning(e)
        await send_loggingFile()
    await logging_info(user_id=user_id,text=f"{callback.data}",handler='get_information_acticle')

