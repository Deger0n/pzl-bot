# [pzl-bot](https://t.me/lapzlbot)
## 📕 Описание
* Телеграм бот, помогающий ставить цели, и добиваться их.
* Подробности можете прочесть в [Руководстве](https://telegra.ph/CHto-takoe-pzl-bot-08-23).
* Кликните на заголовок, если хотите использовать бота.

## 🔧 Технология
### Общий индекс
Пожалуй, опишу здесь как у меня получилось избежать повторяющегося кода для очень похожих функций, и каким образом **work_handler.py** вообще работает. 
Если хотите узнать как сократить N похожих функций в одну - почитайте **work** файлы.<br><br>

В **general_lists.py** лежат списки, в них каждый похожий по смыслу элемент лежит под определённым индексом. Объясню на простом примере. <br>
У нас есть список инлайн-кнопок: Заработок-Редактировать; Заработок-Добавить; Товары-Редактировать; Товары-Добавить, в коде это **work_list**.
А также список текстов, для сообщений, которые отправляются при нажатии на эти кнопку. Мы храним кнопку и ответ на неё под одним и тем же индексом, иначе говоря, общим.

```python
edit_text = "Старый текст будет полностью заменён на новый, который вы, сейчас, отправите боту.\n"\
            "Ниже ваш нынешний текст со всеми тегами, вы можете его скопировать, внести правки, и отправить боту."
add_text = "Написанное вами добавится в конце основного текста, с новой строчки."

text_list = ['Напишите, за что вы хотите получать очки?\n' + edit_text,
             'Напишите, на что вы хотите тратить очки?\n' + edit_text,
             'Напишите, что хотите добавить в "Заработок"?\n' + add_text,
             'Напишите, что хотите добавить в "Товары"?\n' + add_text]

work_list = ["receive_edit", "spend_edit", "receive_add", "spend_add"]
```

Зная, какую кнопку нажал пользователь, мы можем получить текст, который ему необходимо отправить: <br>
```python
pressed button = "receive_edit"
text_list[work_list.index(pressed_button)] 
``` 
Это поиск индекса кнопки в списке кнопок, а далее поиск элемента по этому индексу в списке сообщений. <br><br>

Если вы всё поняли - поздравляю, теперь вы можете писать похожии функции, используя списки, и выглядеть это будет как что-то гениальное и волшебное: "Каким образом он регbстрирует 4 кнопки одновременно, вызывает одну функцию, и у него всё работает?"
