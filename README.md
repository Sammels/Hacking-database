# Hacking database
Скрипт позволяет заменять данные в базе данных.

**ЭТО УЧЕБНЫЙ ПРОЕКТ**

## Установка скрипта
Ссылка на репозиторий электронного дневника.
[Электронный дневник](https://github.com/devmanorg/e-diary)

Для установки, необходимо скачать репозиторий, установить скрипт на сервере,
и поместить его в папку `e-dairy/`.



## Запуск скрипта
Для начала надо запустить консольную оболочку, для работы со скриптом.
```shell
pytnon manage.py shell
```

После этого, нужно импортировать функции в эту оболочку.
```python
from hacking_database import fix_marks, remove_chastisements, create_commendation
```

### Изменение оценок

Чтобы изменить оценки, нужно использовать функцию `fix_marks`, добавив в неё имя для изменения.

```python
fix_marks("Фамилия Имя")
```
где `Фамилия Имя` указывается имя фамилия ученика.


### Удаление замечаний
```python
remove_chastisements("Фамилия Имя")
```
где `Фамилия Имя` указывается имя фамилия ученика.

### Создание благодарностей
```python
create_commendation("Фамилия Имя", "Предмет")
```
где `Фамилия Имя` - Фамилия Имя школьника,
`Предмет` - указать предмет в который будет добавлена благодарность.
