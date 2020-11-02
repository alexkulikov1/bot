from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.test import Test


# Сделаем фильтр на комманду /test, где не будет указано никакого состояния
# @dp.message_handler(Command("form"), state=None)
# async def enter_test(message: types.Message):
#     await message.answer("Введите ваше имя:")

@dp.message_handler(Text(equals=["Сантехник"]))
async def get_service(message: Message):
    await message.answer("Заполните заявку и я направлю её всем профессионалам\n", reply_markup=ReplyKeyboardRemove())
    await message.answer("----------------------------------------------------")
    await message.answer("Введите ваше имя:")


    # Вариант 1 - с помощью функции сет
    await Test.Q1.set()

    # Вариант 2 - с помощью first
    # await Test.first()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    # Ваирант 2 получения state
    # state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

    # Вариант 1 сохранения переменных - записываем через key=var
    # Если у вас запись идет какого-то параметра (например email) то записывайте не answer,
    # а email, чтобы потом было понятно что именно доставать
    await state.update_data(answer1=answer)

    # Вариант 2 - передаем как словарь
    await state.update_data(
        {"answer1": answer}
    )

    # Вариант 3 - через state.proxy
    async with state.proxy() as data:
        data["answer1"] = answer
        # Удобно, если нужно сделать data["some_digit"] += 1
        # Или data["some_list"].append(1), т.к. не нужно сначала доставать из стейта, А потом задавать

    await message.answer("Введите ваш Email:")

    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    # Достаем переменные
    # data = await state.get_data()
    # answer1 = data.get("answer1")
    answer2 = message.text
    await state.update_data(
        {"answer2": answer2}
    )

    await message.answer("Введите ваш номер телефона:")

    await Test.next()


@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    answer3 = message.text
    await state.update_data(
        {"answer3": answer3}
    )

    await message.answer("Ближайшее метро:")

    await Test.next()


@dp.message_handler(state=Test.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    answer4 = message.text
    await state.update_data(
        {"answer4": answer4}
    )

    await message.answer("Удобная дата:")

    await Test.next()


@dp.message_handler(state=Test.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    answer5 = message.text
    await state.update_data(
        {"answer5": answer5}
    )

    await message.answer("Удобное время (с - по):")

    await Test.next()


@dp.message_handler(state=Test.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    answer6 = message.text
    await state.update_data(
        {"answer6": answer6}
    )

    await message.answer("Название улицы:")

    await Test.next()


@dp.message_handler(state=Test.Q7)
async def answer_q3(message: types.Message, state: FSMContext):
    answer7 = message.text
    await state.update_data(
        {"answer7": answer7}
    )

    await message.answer("Номер дома:")

    await Test.next()


@dp.message_handler(state=Test.Q8)
async def answer_q8(message: types.Message, state: FSMContext):
    answer8 = message.text
    await state.update_data(
        {"answer8": answer8}
    )

    await message.answer("Номер квартиры:")

    await Test.next()


@dp.message_handler(state=Test.Q9)
async def answer_q9(message: types.Message, state: FSMContext):
    answer9 = message.text
    await state.update_data(
        {"answer9": answer9}
    )

    await message.answer("Цена:")

    await Test.next()


@dp.message_handler(state=Test.Q10)
async def answer_q4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = data.get("answer3")
    answer4 = data.get("answer4")
    answer5 = data.get("answer5")
    answer6 = data.get("answer6")
    answer7 = data.get("answer7")
    answer8 = data.get("answer8")
    answer9 = data.get("answer9")
    answer10 = message.text

    await message.answer("Твоя заявка:\n"
                         f"Имя - {answer1}\n"
                         f"Email - {answer2}\n"
                         f"Телефон: - {answer3}\n"
                         f"Метро - {answer4}\n"
                         f"Дата: - {answer5}\n"
                         f"Время: - {answer6}\n"
                         f"Улица - {answer7}\n"
                         f"Дом - {answer8}\n"
                         f"Квартира - {answer9}\n"
                         f"Цена - {answer10}")

    # Вариант 1
    await state.finish()

    # Вариант завершения 2
    # await state.reset_state()

    # Вариант завершения 3 - без стирания данных в data
    # await state.reset_state(with_data=False)