<h1 align="center">Telegram Бот для Подготовки к ЕГЭ по Математике 📚🤖</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11.8-blue" alt="Python Version"/>
  <img src="https://img.shields.io/badge/aiogram-3.1.1-orange" alt="aiogram"/>
  <img src="https://img.shields.io/badge/SQL-SQLite3-red" alt="aiogram"/>
  <img src="https://img.shields.io/badge/SdamGia-Api-yellow" alt="aiogram"/>
  <img src="https://img.shields.io/badge/license-Apache-green" alt="License"/>
</p>

<p align="center">
  <a href="https://github.com/Really-Fun/EgeBot" target="_blank" rel="noreferrer">
    <img src="https://img.shields.io/badge/GitHub-Repo-black" alt="GitHub Repo"/>
  </a>
</p>

---

### 📖 Описание

Этот бот разработан для помощи ученикам в подготовке к ЕГЭ по математике. Он генерирует случайные задания из тестовой части профильного экзамена с сайта [sdam-gia](https://sdamgia.ru/), предоставляет ответы и решения с этого же сайта, а также содержит справочные материалы. На данный момент у них имеется собственный телеграм бот, которым вы можете успешно пользоваться.

---


### ⚠️ Внимание

<p align="center">
  <b>Этот проект был создан исключительно в учебных целях.</b><br>
  <i>Он не предназначен для публичного использования или коммерческого распространения.</i><br>
  <i>Все материалы и решения, предоставленные ботом, предназначены для помощи в подготовке к ЕГЭ и взяты из общедоступного источника [Sdam-Gia](https://sdamgia.ru/)</i><br>
</p>

---

### 🛠️ Используемые технологии

- **Python 3.11.8**
- **Aiogram 3.1.1** - фреймворк для разработки Telegram-ботов.
- **SdamGIA API 0.1.7** - источник задач и решений.
- **SQLite** - база данных для хранения статистики пользователей.

---

### 🚀 Основные команды

- **/start**: Начало работы с ботом. Приветственное сообщение и клавиатура для выбора действий.
- **/help**: Получение справки по командам и функциональности бота.
- **/material**: Доступ к справочным материалам по математике.
- **/stats**: Статистика пользователя по выполненным заданиям.
- **задания**: Дает на выбор 12 разных типов заданий, выбираете тип, генерируется случайное задание этого типа.

---

### 📂 Основные модули

#### **Handlers**
- **default_handlers**: Обработчики базовых команд, таких как /start, /help, /leave.
- **tasks_handlers**: Логика для генерации и проверки заданий, предоставления ответов и решений.

#### **Services**
- **sdamgia_utils**: Взаимодействие с API SdamGIA для получения задач и решений.
- **tasks**: Модули с наборами математических задач для ЕГЭ.

#### **Database**
- **base**: Обеспечение работы с базой данных, включая сохранение статистики и управление пользовательскими данными.

---

### 🧪 Тестирование и отладка

<1. **Тестирование функциональности**:
   - Проверка работы основных команд и корректности выдаваемых данных.
   - Обработка разных сценариев взаимодействия пользователя с ботом (в разработке).

2. **Отладка и логирование**:
   - Ведение логов работы бота для выявления и исправления ошибок.

---

### 📄 Лицензия

Проект распространяется под лицензией Apache 2.0. Подробности смотрите в [LICENSE](https://github.com/Really-Fun/EgeBot?tab=Apache-2.0-1-ov-file).

---
![image](https://github.com/user-attachments/assets/4366577e-b4b9-47c0-9913-dd8229e83bab)

<p align="center">
  Сделано с ❤️ для студентов, готовящихся к ЕГЭ.
</p>
