# База знаний слушателя AI и Data

Практическая база знаний для слушателей курсов по анализу данных и машинному обучению. Помогает подготовить окружение, запустить первый ноутбук, отправить домашнюю работу и сформулировать вопрос куратору.

Материалы рассчитаны прежде всего на начинающего слушателя с Windows. Более опытные слушатели могут использовать разделы по воспроизводимости, Git и диагностике ошибок. Это самостоятельный проект для портфолио, не официальная база конкретной школы.

## Быстрый маршрут

1. [С чего начать обучение](guides/00_start.md).
2. [Установить Python на Windows](guides/01_python_windows.md).
3. [Запустить Jupyter Notebook](guides/02_jupyter.md).
4. [Выполнить первое задание](guides/03_first_assignment.md).
5. [Отправить работу через GitHub](guides/04_submit_homework.md).

Если что-то не работает: [типичные ошибки](guides/06_troubleshooting.md) → [как запросить помощь](guides/08_ask_for_help.md).

## Все материалы

| Раздел | Что внутри |
|---|---|
| [Старт курса](guides/00_start.md) | Доступы, расписание, материалы, первые действия |
| [Python на Windows](guides/01_python_windows.md) | Установка, проверка версии, виртуальное окружение |
| [Jupyter](guides/02_jupyter.md) | Запуск, ядро, сохранение и повторный запуск |
| [Первое задание](guides/03_first_assignment.md) | Анализ небольшого CSV и проверка результата |
| [Сдача задания](guides/04_submit_homework.md) | Состав работы, загрузка на GitHub, исправления |
| [Git](guides/05_git.md) | Локальные изменения, коммиты, push и частые затруднения |
| [Ошибки](guides/06_troubleshooting.md) | Ошибка → причина → действия → проверка |
| [Организационные вопросы](guides/07_faq.md) | Дедлайны, доступы, записи, обратная связь |
| [Запрос помощи](guides/08_ask_for_help.md) | Шаблон понятного обращения и маршрутизация |
| [Обратная связь](guides/09_feedback.md) | Короткая анкета после занятия и разбор ответов |
| [Вебинар](guides/10_webinar.md) | Чек-лист куратора до, во время и после занятия |
| [macOS и Linux](guides/11_macos_linux.md) | Альтернативные команды окружения |

## Примеры и шаблоны

- [Рабочий ноутбук](examples/first_analysis.ipynb) и [данные](examples/sales.csv).
- [Скрипт с тем же расчётом](examples/first_analysis.py).
- [Оформление домашней работы](templates/HOMEWORK_README.md).
- [Обращение за помощью](templates/HELP_REQUEST.md).
- [Журнал вопросов](templates/ISSUE_LOG.csv).
- [Форма обратной связи](templates/FEEDBACK_FORM.md).
- [Таблица ответов обратной связи](templates/feedback_responses.csv).
- [Карточка доступа к курсу](templates/COURSE_CARD.md).
- [Журнал изменений базы](CHANGELOG.md).

## Как читать

Распакуйте архив и откройте файлы `.md` в VS Code или другом Markdown-просмотрщике. При загрузке папки в GitHub страницы и относительные ссылки работают прямо в репозитории. Для простого чтения установка Python не нужна.

Для примера с расчётом нужен Python 3.11/3.12:

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe examples\first_analysis.py
.venv\Scripts\python.exe -m notebook
```

Проверка локальных ссылок и примеров:

```powershell
.venv\Scripts\python.exe scripts\check_docs.py
.venv\Scripts\python.exe scripts\check_examples.py
```

Результаты фактически выполненной проверки — [VERIFICATION.md](VERIFICATION.md). Источники технических инструкций — [SOURCES.md](SOURCES.md).

## Как развивать базу

Добавляйте вопрос в журнал с обезличенным описанием. Сначала воспроизведите проблему, затем обновите статью: причина, действия и ожидаемый результат. После изменения проверьте ссылки и рабочий пример. Порядок редактирования — [CONTRIBUTING.md](CONTRIBUTING.md).
