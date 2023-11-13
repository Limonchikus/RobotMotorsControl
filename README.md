# RobotMotorsControl

## Project Description
RobotMotorsControl is a Python-based project aimed at providing a basic framework for controlling motor movements in robotic projects. The initial steps taken in this project lay the foundation for more complex functionalities.

## Progress Overview

1. **Initial Setup**: Created `README.md` and a draft Python script (`motors_control.py`) directly on GitHub.
2. **Credential Caching**: Implemented a mechanism to cache credentials for 15 minutes to streamline the development process.
3. **Script Implementation**: Developed and pushed the initial version of the `motors_control.py` script, which includes basic motor control functionalities.
4. **Adding motor features**: Debeloped more enhanced speed control script in `motors_control.py`.

## Usage
(Examples of how to use the project...)

## Contributing
(Guidelines for contributing to the project...)

## License
(Information about the license...)

### Отчет о Проекте RobotMotorsControl

Общее Описание Проекта

RobotMotorsControl - это проект, направленный на разработку программного обеспечения для управления моторами робота. Цель проекта - тренировка по работе с репозиториями на GitHub.

#### Описание Работы с Git

#### Создание и Клонирование Репозитория

Репозиторий был создан на GitHub, после чего я клонировал его на локальный компьютер для дальнейшей разработки с помощью команды git clone.

#### Процесс Сохранения Изменений

Для сохранения изменений использовались стандартные команды Git:

    git add . - для добавления изменений в индекс.
    git commit -m "комментарий" - для фиксации изменений.
    git push - для отправки изменений на сервер.

В процессе работы над проектом возникла проблема с учетными данными для входа в систему и работы с репозиторием - постоянно требовался ввод токена - пароля, открытого в настройках GitHub. Это вызвало трудности с доступом и отправкой изменений. Однако, я смог решить эту проблему, настроив кэширование учетных данных на 15 минут после каждого push (git config --global credential.helper 'cache --timeout=900'), что значительно упростило процесс работы.

В результате были созданы два файла: Readme и *.py (содержащи базовый код управления моторами робота).

#### Взаимодействие с Ветками, Пул-реквесты, Основные Изменения и Улучшения в Коде.

Далее была создана ветка enhanced-speed-regulation для разработки новых функций. В проект были добавлены ключевые функции для плавного управления скоростью моторов. После внесения улучшений ветка была успешно замерджена с основной веткой через Pull Request на GitHub (автоматическое слияние).

#### Заключение

Работа с Git оказалась продуктивной и обучающей. В будущем планирую продолжить изучение возможностей Git для более эффективной самостоятельной и командной работы.

