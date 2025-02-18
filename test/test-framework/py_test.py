from functions.functions import *
import pytest

new_section("pytest and test scripting")
print("""
   - тестовые файлы должны быть названы test_<something>.py или <something>_test.py;
   - методы и функции тестирования должны быть названы test_<something>;
   - тестовые классы должны быть названы Test<Something>.
   - папка, в которой вы будете хранить свои тесты, должна быть названа tests и находиться в корневом каталоге, потому что PyTest по умолчанию ищет тесты именно в ней.
""")

line("unittest")
print("""
Модульное тестирование, или юнит-тестирование (англ. unit testing) — это такой вид тестирования, 
который позволяет проверить небольшие куски кода (модули).
""")

print("""
                                     Manual Tests    
                                  -------------------  
                                     Acceptance tests      
                                  -------------------   
                                     Integration Tests      
                                  -------------------   
                                     Unit Tests               
""")





































