#!/bin/bash
ERRORS=$(mypy . 2>&1)
RESULT=$?

if [ $RESULT -ne 0 ]; then
    # Красный заголовок
    echo -e "\e[31mMypy found type errors:\e[0m\n"
    # Жёлтый текст ошибок
    echo -e "\e[33m$ERRORS\e[0m"
    exit 1
fi

# Зелёный успешный вывод
#echo -e "\e[32mMypy test passed\e[0m"
exit 0
