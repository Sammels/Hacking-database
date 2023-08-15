from random import choice

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid, Subject)

COMMENDATIONS = ["Молодец!", "Отлично!", "Хорошо!", "Гораздо лучше, чем я ожидал!",
                 "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!",
                 "Именно этого я давно ждал от тебя!", "Сказано здорово – просто и ясно!", "Ты, как всегда, точен!",
                 "Очень хороший ответ!",
                 "Талантливо!", "Ты сегодня прыгнул выше головы!", "Я поражен!", "Уже существенно лучше!",
                 "Потрясающе!", "Замечательно!", "Прекрасное начало!", "Так держать!",
                 "Ты на верном пути!", "Здорово!", "Это как раз то, что нужно!", "Я тобой горжусь!",
                 "С каждым разом у тебя получается всё лучше!", "Мы с тобой не зря поработали!",
                 "Я вижу, как ты стараешься!", "Ты растешь над собой!",
                 "Ты многое сделал, я это вижу!", "Теперь у тебя точно все получится!", ]


def exception_decorator(func):
    """Декоратор принимает в себя функцию, и оборачивает её исключениями"""

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Schoolkid.DoesNotExist:
            print("Такого имени не существует")
        except Schoolkid.MultipleObjectsReturned:
            print("Найдено несколько учеников")

    return wrapper


@exception_decorator
def fix_marks(schoolkid: str):
    """Функция изменяет оценки."""
    schoolkid_name = Schoolkid.objects.get(full_name__contains=f"{schoolkid}")
    Mark.objects.filter(schoolkid_id=schoolkid_name.id, points__lte=3).update(points=5)
    print("Работа окончена. You are HACKERMAN...")


@exception_decorator
def remove_chastisements(schoolkid: str):
    """Функция удаляет замечания ученику"""
    Chastisement.objects.filter(schoolkid__full_name__contains=f"{schoolkid}").delete()
    print("Работа окончена. You are BAD...")


def create_commendation(schoolkid: str, subject: str) -> str:
    """Функция принимает ФИО ученика и предмет. Создает похвальное сообщение"""
    choice_commendation = choice(COMMENDATIONS)

    schoolkid_check = Schoolkid.objects.get(full_name__contains=f"{schoolkid}")
    schoolkid_year = schoolkid_check.year_of_study
    schoolkid_id = schoolkid_check.id

    subject_ = Subject.objects.filter(title__contains=f"{subject}",
                                      year_of_study__contains=schoolkid_year).first()
    subject_id = subject_.id

    lesson_identification = Lesson.objects.order_by('subject_id', 'group_letter', 'year_of_study').first()



    teacher_id = lesson_identification.teacher_id
    lesson_date = lesson_identification.date

    Commendation.objects.create(teacher_id=teacher_id, subject_id=subject_id, schoolkid_id=schoolkid_id,
                                text=choice_commendation, created=lesson_date)

    print("Ты очень ПЛОХОЙ.")


print("Knock-knock. KGB open up!!!!!")

if __name__ == "__main__":
    fix_marks("Васильева Полина")
    remove_chastisements("Голубеве Феофане")
