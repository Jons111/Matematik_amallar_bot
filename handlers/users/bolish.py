from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.bolish import Bolish_javoblar
from random import randint

togri_javoblar = []
savollar = []
javoblar = []

@dp.message_handler(commands="bolish")
async def bot_echo(message: types.Message):
    await message.answer(text="Bo'lish amali.")
    son1, son2 = randint(1, 50), randint(1, 50)
    while son1 % son2 > 0:
        son1, son2 = randint(1, 50), randint(1, 50)
    nat = son1 / son2
    label = f"{son1} / {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Bolish_javoblar.javob_holat1.set()

@dp.message_handler(state=Bolish_javoblar.javob_holat1)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(1, 80), randint(1, 80)
    while son1 % son2 > 0 and son1 / son2 <= 10:
        son1, son2 = randint(1, 80), randint(1, 80)
    nat = son1 / son2
    label = f"{son1} / {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Bolish_javoblar.javob_holat2.set()


@dp.message_handler(state=Bolish_javoblar.javob_holat2)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(1, 120), randint(1, 120)
    while son1 % son2 > 0 and son1 / son2 <= 20:
        son1, son2 = randint(1, 120), randint(1, 120)
    nat = son1 / son2
    label = f"{son1} / {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Bolish_javoblar.javob_holat3.set()


@dp.message_handler(state=Bolish_javoblar.javob_holat3)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(1, 180), randint(1, 180)
    while son1 % son2 > 0 and son1 / son2 <= 40:
        son1, son2 = randint(1, 180), randint(1, 180)
    nat = son1 / son2
    label = f"{son1} / {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Bolish_javoblar.javob_holat4.set()

@dp.message_handler(state=Bolish_javoblar.javob_holat4)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(1, 240), randint(1, 240)
    while son1 % son2 > 0 and son1 / son2 <= 50:
        son1, son2 = randint(1, 240), randint(1, 240)
    nat = son1 / son2
    label = f"{son1} / {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Bolish_javoblar.javob_holat5.set()

@dp.message_handler(state=Bolish_javoblar.javob_holat5)
async def bot_echo(message: types.Message, state: FSMContext):
    javob = message.text
    javoblar.append(javob)

    await state.finish()