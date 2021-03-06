"""
Источник: https://habr.com/ru/post/448782/

Установка библиотеки:
pip install pytest

Запустить тесты из данного файла:
>pytest test_PyTest.py

Запустить тесты с остановкой на первом файле:
pytest -x

Останавливаемся после 2го фейла, отключаем трассировку ошибок:
pytest --maxfail=2 --tb=no

Рассчитывает локальные переменные в провалившемся тесте:
pytest -l/--showlocals

Если вы хотите видеть больше точек для прохождения тестов, используйте опцию -v или --verbose.
pytest -v test_PyTest.py
-q - если хотим меньше инфы

Выводит самые медленные тесты:
--durations=N


Все опции:
pytest --help

Для запуска pytest у вас есть возможность указать файлы и каталоги.
Если вы не укажете какие-либо файлы или каталоги, pytest будет искать тесты в текущем рабочем каталоге и подкаталогах.
Он ищет файлы, начинающиеся с test_ или заканчивающиеся на _test.

Тестовые файлы должны быть названы test_<something>.py или <something>_test.py.
Методы и функции тестирования должны быть названы test_<something>.
Тестовые классы должны быть названы Test<Something>.

В выводе. Точки предназначены только для прохождения тестов.
Failures (сбоев), errors (ошибок), skips (пропусков), xfails, и xpasses обозначаются с F, E, s, x, и Х, соответственно.

PASSED (.): Тест выполнен успешно.
FAILED (F): Тест не выполнен успешно (или XPASS + strict).
SKIPPED (s): Тест был пропущен. Вы можете заставить pytest пропустить тест, используя декораторы @pytest.mark.skip()
или pytest.mark.skipif(), обсуждаемые в разделе пропуск тестов, на стр. 34.
xfail (x): Тест не должен был пройти, был запущен и провалился.
Вы можете принудительно указать pytest, что тест должен завершиться неудачей, используя декоратор @pytest.mark.xfail(),
описанный в маркировках тестов как ожидающий неудачу, на стр. 37.
XPASS (X): Тест не должен был пройти, был запущен и прошел!..
ERROR (E): Исключение произошло за пределами функции тестирования, либо в фикстуре, обсуждается в главе 3,
pytest Фикстуры, на стр. 49, или в hook function, обсуждается в главе 5, Плагины, на странице 95.
"""
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

def test_failing():
    a=1
    assert (1, 2, 3) == (3, 2, 1)

def test_passing2():
    assert (1, 2, 3) == (1, 2, 3)
