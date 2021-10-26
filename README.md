## Тестовое задание для подаче резюме на позицию <a href='https://hh.ru/vacancy/48973633?from=vacancy_search_list'>Junior Game Analyst</a> в компанию <a href='https://lightmap.ru/'>LIGHTMAP</a>.

Проект состоит из следующих файлов:
<li><a href='https://github.com/KhurazovRuslan/lightmap_test-russian-/blob/main/lightmap.ipynb'>lightmap.ipynb</a> - ноутбук с решениями заданий</li>
<li><a href='https://github.com/KhurazovRuslan/lightmap_test-russian-/blob/main/lightmap2.csv'>lightmap2.csv</a> и <a href='https://github.com/KhurazovRuslan/lightmap_test-russian-/blob/main/lightmap3.csv'>lightmap3.csv</a> - .csv файлы с данными для второго и третьего задания</li>
<li><a href='https://github.com/KhurazovRuslan/lightmap_test-russian-/blob/main/lightmap_funcs.py'>lightmap_funcs.py</a> - функции, написанные на Python и используемые при решении заданий</li>
<li><a href='https://github.com/KhurazovRuslan/lightmap_test-russian-/blob/main/README.md'>Readme файл</a> с кратким описанием проекта</li>

<h2></h2>
<p>Задание состоит из трех частей:</p>
<ol>
<li>В специальной лотерее игрок выбирает 5 разных чисел из возможных 30. В этот же день случайным образом определяется победная комбинация из 7 разных чисел (из того же набора). Игрок считается победителем в случае, если совпадают любые 4 числа в выбранном им наборе и в победной комбинации.
Какова вероятность выигрыша? - <i>Это задача решалась в "лоб", рассуждением о вероятности победной комбинации.</i></li>
<li>В файле <a href='https://github.com/KhurazovRuslan/lightmap_test-russian-/blob/main/lightmap2.csv'>lightmap2.csv</a> построчно приведены записи событий установки приложения (install) и начала сессии (login). В столбце player_id указан уникальный id пользователя, в столбце event_timestamp - время события (unix timestamp UTC). Удержание первого дня определяется как доля уникальных пользователей, отправивших событие login на следующий календарный день, среди всех пользователей, отправивших событие install в текущий календарный день. Например, если 1 сентября 100 пользователей скачали приложение, и 50 из них совершили логин 2 сентября, удержание первого дня для 1 сентября составляет 50%.
Удержание первого дня для периода дат определяется как отношение общего числа уникальных пользователей, вернувшихся в приложение на следующий день после дня установки, к общему числу уникальных пользователей, совершивших установку в рамках заданного периода дат. Например, если 2 сентября 200 пользователей скачали приложение, и 75 из них совершили логин 3 сентября, удержание первого дня за период 1-2 сентября составляет: (50 + 75) / (100 + 200) ≈ 42%. Можно ли с уверенностью утверждать, что удержание первого дня за период с 15 по 18 сентября выше, чем удержание первого дня за период с 19 по 22 сентября? И почему? - <i>Для решения был создан новый датафрейм с количеством событий install и login на следущий день, а также удержанием первого дня по дням. Были построены графики для наглядности. Также были посчитаны удержания первого дня для групп пользователей с 15 по 18 сентября и с 19 по 22 сентября и p-значение для определия значимости полученных результатов.</i></li>
<li>В файле <a href='https://github.com/KhurazovRuslan/lightmap_test-russian-/blob/main/lightmap3.csv'>lightmap3.csv</a> построчно приведены записи транзакций, совершенных в приложении когортой пользователей. В столбце event_timestamp указано время транзакции (unix timestamp UTC), в столбце registration_timestamp - дата регистрации пользователя, в столбце inapp_size - размер соответствующего платежа (сумма $). Требуется построить кривую накопительной суммы платежей когорты по дням с момента регистрации (один день - одна точка на кривой). На основании полученных данных построить и отобразить в виде другой кривой на том же графике прогноз значений накопительной суммы для дней жизни с 90 по 180. - <i>Для решения этого задания трансакции были сгруппированы по дням, прошедшим с момента регистрации, посчитаны накопительные суммы платежей, построен график. Также было сделано и изображено на графике два прогноза: прогноз основанный на простой арифметической средней суммы платежей по дням и прогноз, построенный с помощью простого экспоненциального сглаживания средневзешенной средней суммы платежей по дням.</i></li>
</ol>

<p>Для решения использовались python 3.7.8, numpy 1.18.5, pandas 1.1.0, matplotlib 3.3.0 и statsmodels 0.11.1</p>
<p>Ссылка на репозитарий была отправлена вместе с откликом на вакансию.</p>
