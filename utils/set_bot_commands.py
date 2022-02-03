from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("qoshish", "Qo`shish amali"),
            types.BotCommand("ayirish", "Ayirish amali"),
            types.BotCommand("kopaytirish", "Ko'paytirish amali"),
            types.BotCommand("bolish", "Bo'lish amali"),

        ]
    )
