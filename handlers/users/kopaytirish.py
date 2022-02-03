from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.kopaytirish import Kopaytirish_javoblar
from random import randint

togri_javoblar = []
savollar = []
javoblar = []

@dp.message_handler(commands="kopaytirish")
async def bot_echo(message: types.Message):
    await message.answer(text="Ko'paytirish amali.")
    son1, son2 = randint(1, 10), randint(1, 10)
    nat = son1 * son2
    label = f"{son1} * {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Kopaytirish_javoblar.javob_holat1.set()

@dp.message_handler(state=Kopaytirish_javoblar.javob_holat1)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(1, 15), randint(1, 15)
    while son1 * son2 <= 50:
        son1, son2 = randint(1, 15), randint(1, 15)
    nat = son1 * son2
    label = f"{son1} * {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Kopaytirish_javoblar.javob_holat2.set()


@dp.message_handler(state=Kopaytirish_javoblar.javob_holat2)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(1, 20), randint(1, 20)
    while son1 * son2 <= 100:
        son1, son2 = randint(1, 20), randint(1, 20)
    nat = son1 * son2
    label = f"{son1} * {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Kopaytirish_javoblar.javob_holat3.set()


@dp.message_handler(state=Kopaytirish_javoblar.javob_holat3)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(1, 25), randint(1, 25)
    while son1 * son2 <= 200:
        son1, son2 = randint(1, 25), randint(1, 25)
    nat = son1 * son2
    label = f"{son1} * {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Kopaytirish_javoblar.javob_holat4.set()

@dp.message_handler(state=Kopaytirish_javoblar.javob_holat4)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(1, 30), randint(1, 30)
    while son1 * son2 <= 400:
        son1, son2 = randint(1, 30), randint(1, 30)
    nat = son1 * son2
    label = f"{son1} * {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Kopaytirish_javoblar.javob_holat5.set()

@dp.message_handler(state=Kopaytirish_javoblar.javob_holat5)
async def bot_echo(message: types.Message, state: FSMContext):
    javob = message.text
    javoblar.append(javob)

    await state.finish()