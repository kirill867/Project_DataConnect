import os #работаем с операционными системами (программно видеть, что находится в какой-то конкретной папке
from string import Template

class SQLProvider:

    def __init__(self, file_path: str) -> None:#путь до папки со sql-скрпитами, которые мы хотим перпедать
        self._scripts = {}#контейнер, который будет знать имя скрипта и его содержимое

        for file in os.listdir(file_path): #итерируемся по какой-то папке+какие файлы в ней (в данном случае одна по user_by_login
            self._scripts[file] = Template(open(f'{file_path}/{file}', 'r').read())
            #необходимо параметризировать доллары, поэтому берем библиотеку string
            #open(f'{file_path}/{file}', 'r').read() полностью читаем файл - это значение ключа, но тут он не воспринимает доллар как какую-то пермеменную, вместо которйо нужно что-нибудь поставить
            #поэтмоу оборачиваем все это в Template, который использует символ $ по умолчанию в качестве обозначение переменной
            #если другой символ, то нужно переименовать парамер delimetr. к примеру, поменять на решетку или что-нибудь подобное
            #{file_path}/{file} - путь, чтобы правильно прочитать

    def get(self, name, **kwargs):
        #name - имя того файла, который хотим передать
        #чтобы после указания имени, можно было накидывать всевозможные параметры - **kwargs. пример
        #к примеру, get('user_by_login.sql', login = 'kek', password = 'lol')
        #substitute - чтобы все значения поставить в качестве этой строки
        return self._scripts[name].substitute(**kwargs)

    get_sql1