from random import choice

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid, Subject)

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def fix_marks(schoolkid: str):
    """Функция изменяет оценки."""
    user_name = Mark.objects.filter(schoolkid__full_name__contains=f"{schoolkid}", points__lte=3)
    ids = []
    for point in user_name:
        ids.append(point.id)

    for point in ids:
        work_process = Mark.objects.get(id=point)
        work_process.points = 5
        work_process.save()

    print("Work is over. You are HACKERMAN...")


def remove_chastisements(schoolkid: str):
    """Функция удаляет замечания ученику"""
    user_name = Chastisement.objects.filter(schoolkid__full_name__contains=f"{schoolkid}")
    ids = []
    for point in user_name:
        ids.append(point.id)

    for point in ids:
        work_process = Chastisement.objects.get(id=point)
        work_process.delete()

    print("Work is over. You are BAD...")


def create_commendation(schoolkid: str, subject: str) -> str:
    """Функция принимает ФИО ученика и предмет. Создает похвальное сообщение"""
    commendations = ["Молодец!", "Отлично!", "Хорошо!", "Гораздо лучше, чем я ожидал!",
                     "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!",
                     "Именно этого я давно ждал от тебя!", "Сказано здорово – просто и ясно!", "Ты, как всегда, точен!",
                     "Очень хороший ответ!",
                     "Талантливо!", "Ты сегодня прыгнул выше головы!", "Я поражен!", "Уже существенно лучше!",
                     "Потрясающе!", "Замечательно!", "Прекрасное начало!", "Так держать!",
                     "Ты на верном пути!", "Здорово!", "Это как раз то, что нужно!", "Я тобой горжусь!",
                     "С каждым разом у тебя получается всё лучше!", "Мы с тобой не зря поработали!",
                     "Я вижу, как ты стараешься!", "Ты растешь над собой!",
                     "Ты многое сделал, я это вижу!", "Теперь у тебя точно все получится!", ]
    choice_commendation = choice(commendations)

    try:
        schoolkid_check = Schoolkid.objects.get(full_name__contains=f"{schoolkid}")
        schoolkid_year = schoolkid_check.year_of_study
        schoolkid_group_letter = schoolkid_check.group_letter
        schoolkid_id = schoolkid_check.id

        subject_ = Subject.objects.filter(title__contains=f"{subject}",
                                          year_of_study__contains=schoolkid_year)
        subject_id = subject_[0].id

        teacher_identification = Lesson.objects.filter(subject_id=subject_id, group_letter=schoolkid_group_letter,
                                                       year_of_study=schoolkid_year)
        teacher_id = teacher_identification[0].teacher_id
        lesson_date = teacher_identification[0].date

        # Create inst
        Commendation.objects.create(teacher_id=teacher_id, subject_id=subject_id, schoolkid_id=schoolkid_id,
                                    text=choice_commendation, created=lesson_date)

        print("You are very BAD kid")

    except ObjectDoesNotExist:
        print("Такого имени не существует")
    except MultipleObjectsReturned:
        print("Найдено несколько учеников")


print("Knock-knock. KGB open up!!!!!")

if __name__ == "__main__":
    fix_marks("Васильева Полина")
    remove_chastisements("Голубеве Феофане")
