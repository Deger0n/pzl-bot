from create_bot import FSMgame
import keyboard

edit_text = "Старый текст будет полностью заменён на новый, который вы, сейчас, отправите боту.\n"\
            "Ниже ваш нынешний текст со всеми тегами, вы можете его скопировать, внести правки, и отправить боту."
add_text = "Написанное вами добавится в конце основного текста, с новой строчки."

text_list = ['Напишите, за что вы хотите получать очки?\n' + edit_text,
             'Напишите, на что вы хотите тратить очки?\n' + edit_text,
             'Напишите, что хотите добавить в "Заработок"?\n' + add_text,
             'Напишите, что хотите добавить в "Товары"?\n' + add_text]

work_list = ["receive_edit", "spend_edit", "receive_add", "spend_add"]
columns_list = ["receive", "spend"]

set_state_list = [FSMgame.receive_edit_state, FSMgame.spend_edit_state, FSMgame.receive_add_state,
                  FSMgame.spend_add_state]
keyboard_list = [keyboard.receive, keyboard.spend]