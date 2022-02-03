from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.ayirish import Ayirish_javoblar
from random import randint

togri_javoblar = []
savollar = []
javoblar = []

@dp.message_handler(commands="ayirish")
async def bot_echo(message: types.Message):
    await message.answer(text="Ayirish amali.")
    son1, son2 = randint(1, 100), randint(1, 100)
    while son1 - son2 <= 50 and son1 - son2 >= 0:
        son1, son2 = randint(1, 100), randint(1, 100)
    nat = son1 - son2
    label = f"{son1} - {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Ayirish_javoblar.javob_holat1.set()

@dp.message_handler(state=Ayirish_javoblar.javob_holat1)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(1, 200), randint(1, 200)
    while son1 - son2 <= 150 and son1 - son2 >= 50:
        son1, son2 = randint(1, 200), randint(1, 200)
    nat = son1 - son2
    label = f"{son1} - {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Ayirish_javoblar.javob_holat2.set()


@dp.message_handler(state=Ayirish_javoblar.javob_holat2)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(1, 300), randint(1, 300)
    while son1 - son2 <= 250 and son1 - son2 >= 150:
        son1, son2 = randint(1, 300), randint(1, 300)
    nat = son1 - son2
    label = f"{son1} - {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Ayirish_javoblar.javob_holat3.set()


@dp.message_handler(state=Ayirish_javoblar.javob_holat3)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(1, 400), randint(1, 400)
    while son1 - son2 <= 350 and son1 - son2 >= 250:
        son1, son2 = randint(1, 400), randint(1, 400)
    nat = son1 - son2
    label = f"{son1} - {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Ayirish_javoblar.javob_holat4.set()

@dp.message_handler(state=Ayirish_javoblar.javob_holat4)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(1, 500), randint(1, 500)
    while son1 - son2 <= 450 and son1 - son2 >= 450:
        son1, son2 = randint(1, 500), randint(1, 500)
    nat = son1 - son2
    label = f"{son1} - {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Ayirish_javoblar.javob_holat5.set()

@dp.message_handler(state=Ayirish_javoblar.javob_holat5)
async def bot_echo(message: types.Message, state: FSMContext):
    javob = message.text
    javoblar.append(javob)

    await state.finish()