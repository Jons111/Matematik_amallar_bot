from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.qoshish import Qoshish_javoblar
from random import randint

togri_javoblar = []
savollar = []
javoblar = []

@dp.message_handler(commands="qoshish")
async def bot_echo(message: types.Message):
    await message.answer(text="Qoshish amali.")
    son1, son2 = randint(1, 100), randint(1, 100)
    while son1 + son2 >= 100:
        son1, son2 = randint(1, 100), randint(1, 100)
    nat = son1 + son2
    label = f"{son1} + {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Qoshish_javoblar.javob_holat1.set()

@dp.message_handler(state=Qoshish_javoblar.javob_holat1)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(100, 200), randint(100, 200)
    while son1 + son2 >= 300:
        son1, son2 = randint(100, 200), randint(100, 200)
    nat = son1 + son2
    label = f"{son1} + {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Qoshish_javoblar.javob_holat2.set()


@dp.message_handler(state=Qoshish_javoblar.javob_holat2)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(200, 300), randint(200, 300)
    while son1 + son2 >=500:
        son1, son2 = randint(200, 300), randint(200, 300)
    nat = son1 + son2
    label = f"{son1} + {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Qoshish_javoblar.javob_holat3.set()


@dp.message_handler(state=Qoshish_javoblar.javob_holat3)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(200, 300), randint(200, 300)
    while son1 + son2 >=500:
        son1, son2 = randint(200, 300), randint(200, 300)
    nat = son1 + son2
    label = f"{son1} + {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Qoshish_javoblar.javob_holat4.set()

@dp.message_handler(state=Qoshish_javoblar.javob_holat4)
async def bot_echo(message: types.Message):
    javob = message.text
    javoblar.append(javob)
    son1, son2 = randint(200, 300), randint(200, 300)
    while son1 + son2 >=500:
        son1, son2 = randint(200, 300), randint(200, 300)
    nat = son1 + son2
    label = f"{son1} + {son2} = ?"
    savollar.append(label)
    togri_javoblar.append(nat)

    await message.answer(text=label)
    await Qoshish_javoblar.javob_holat5.set()

@dp.message_handler(state=Qoshish_javoblar.javob_holat5)
async def bot_echo(message: types.Message, state: FSMContext):
    javob = message.text
    javoblar.append(javob)

    await state.finish()