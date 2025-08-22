# syntax_fixer
 
Сборщик для прроверки синтаксиса на основе: ruff, mypy

#Использвание: 
1. Даем права на чтение `chmod +r pre_commit_script.bash`
2. Установить зависимости `pip install -r requiremets.txt`
3. Установить pre-commit 
`pre-commit install`
4. Используем гит через терминал, скрипт срабатывает на уровне `commit`

#Возможные ошибки:
Возможно скрипт будет косячить, необходимо добавить пустые хуки для прекоммита из корня проекта
```
mkdir .git
mkdir .git/hooks
```
P.S. Надеюсь, мы понимаем, что папка .git - скрытая и если что не отобразится в проводнике по-умоланию, для просмотра используем консоль

#Суть работы
Прогоняется `ruff format` исправляющий синтаксис, а затем `mypy` проверяющие репозиторий.
#Вариант 1:
Если мы видим такой вывод в консоли: 
```
[INFO] Stashing unstaged files to /home/???/.var/app/com.visualstudio.code/cache/pre-commit/???.
ruff format..............................................................Failed
- hook id: ruff-format
- files were modified by this hook
1 file reformatted
ruff (legacy alias)......................................................Passed
Run mypy-check and stop if find errors...................................Passed
[WARNING] Stashed changes conflicted with hook auto-fixes... Rolling back fixes...
[INFO] Restored changes from /home/???/.var/app/com.visualstudio.code/cache/pre-commit/???.
```
Сработало автоисправление, и необходимо заново сделать `add`
```
((venv) ) ???/???$ git add .
((venv) ) ???/???$ git commit -m 'test_bash'
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /home/???/.var/app/com.visualstudio.code/cache/pre-commit/???.
ruff format..............................................................Passed
ruff (legacy alias)......................................................Passed
Run mypy-check and stop if find errors...................................Passed
[INFO] Restored changes from /home/???/.var/app/com.visualstudio.code/cache/pre-commit/???.
[main a6ea6a1e] test_bash
```
#Вариант 2:
Видим такой вывод: 
```
((venv) ) ???/???$ git commit -m 'test_bash'
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /home/???/.var/app/com.visualstudio.code/cache/pre-commit/???.
ruff format..............................................................Failed
- hook id: ruff-format
- files were modified by this hook
1 file reformatted
ruff (legacy alias)......................................................Passe
Run mypy-check and stop if find errors...................................Failed
- hook id: mypy-custom
- exit code: 1

Mypy found type errors:

projects/syntax_fixer/test_2.py:12: error: Incompatible return value type (got "int", expected "str")  [return-value]
Found 1 error in 1 file (checked 1 source file)

[WARNING] Stashed changes conflicted with hook auto-fixes... Rolling back fixes...
[INFO] Restored changes from /home/???/.var/app/com.visualstudio.code/cache/pre-commit/???.
```
Сработал `ruff` и найденны ошибки в аннотациях типов `mypy`. Сначала исправляем ошибки `mypy`(выделяются желтым), затем заново `add` и крутим до победного. !Без исправления ошибок `mypy` коммита не произойдет, для обхода в `.yaml` в цикле на выход ставим `0`
