# calibre wide preferences

### Begin group: DEFAULT
 
# database path
# Путь к базе данных в которой хранятся книги
database_path = 'C:\\Users\\User/library1.db'
 
# filename pattern
# Шаблон для получения метаданных из имени файла
filename_pattern = u'(?P<title>.+) - (?P<author>[^_]+)'
 
# isbndb com key
# Ключ доступа к isbndb.com
isbndb_com_key = ''
 
# network timeout
# Таймаут для сетевых операций по умолчанию (сек)
network_timeout = 5
 
# library path
# Путь к директории в которой хранятся книги
library_path = u'C:\\Users\\User\\Desktop\\Calibre Portable\\Calibre Library'
 
# language
# Язык для отображения пользовательского интерфейса
language = 'ru'
 
# output format
# Умолчальный формат вывода для преобразования электронных книг.
output_format = 'epub'
 
# input format order
# Упорядоченный список предпочитаемых форматов
input_format_order = cPickle.loads('\x80\x02]q\x01(U\x04EPUBq\x02U\x04AZW3q\x03U\x04MOBIq\x04U\x03LITq\x05U\x03PRCq\x06U\x03FB2q\x07U\x04HTMLq\x08U\x03HTMq\tU\x04XHTMq\nU\x05SHTMLq\x0bU\x05XHTMLq\x0cU\x03ZIPq\rU\x04DOCXq\x0eU\x03ODTq\x0fU\x03RTFq\x10U\x03PDFq\x11U\x03TXTq\x12e.')
 
# read file metadata
# Читать метаданные из файлов
read_file_metadata = True
 
# worker process priority
# Приоритет работы процесса. Более высокий приоритет означает более быструю работу и более высокое потребление ресурсов. Большинство задач вроде конвертации/новых загрузок/добавления книг/и т.д. зависят от этого параметра.
worker_process_priority = 'normal'
 
# swap author names
# Поменять местами имя и фамилию автора при чтении метаданных
swap_author_names = False
 
# add formats to existing
# Добавить новые форматы к существующим записям книг
add_formats_to_existing = False
 
# check for dupes on ctl
# Проверьте на наличие дубликатов перед копированием в другую библиотеку
check_for_dupes_on_ctl = False
 
# installation uuid
# Installation UUID
installation_uuid = '3dbb797c-919f-4b95-8e06-2f8094d95596'
 
# new book tags
# Теги, добавляемые к книгам в библиотеке
new_book_tags = cPickle.loads('\x80\x02]q\x01.')
 
# mark new books
# Пометить недавно добавленные книги. Отметки временные и автоматически удаляются после перезагрузки calibre.
mark_new_books = False
 
# saved searches
# Список сохраненных поисковых запросов
saved_searches = cPickle.loads('\x80\x02}q\x01.')
 
# user categories
# Пользовательские категории в браузере тегов
user_categories = cPickle.loads('\x80\x02}q\x01.')
 
# manage device metadata
# Как и когда calibre обновляет метаданные на устройстве.
manage_device_metadata = 'manual'
 
# limit search columns
# При поиске в тексте без использования поисковых префиксов, например, Red (красный) вместо title:Red (название:красный), ограничить столбцы поиска указанными ниже.
limit_search_columns = False
 
# limit search columns to
# Выберите столбцы для поиска, когда не используется префикс, например Red вместо title:Red. Введите список названий поиска разделённых запятой. Будет полезно только если вы установите ограничение столбцов поиска выше.
limit_search_columns_to = cPickle.loads('\x80\x02]q\x01(U\x05titleq\x02U\x07authorsq\x03U\x04tagsq\x04U\x06seriesq\x05U\tpublisherq\x06e.')
 
# use primary find in search
# Символы, набранные в поисковой строке будут соответствовать их акцентированным версиям, основываясь на выбранном для интерфейса Calibre языке. Для примера, на английском, поиску для n будет соответствовать ñ и n, но если ваш язык - Испанский, ему будет соответствовать только n. Заметьте, что это гораздо медленнее, чем простой поиск в очень больших библиотеках. Также учтите, что эта опция не будет работать, если вы включили регистрозависимый поиск.
use_primary_find_in_search = True
 
# case sensitive
# Сделать поиск регистрозависимым
case_sensitive = False
 
# migrated
# For Internal use. Don't modify.
migrated = False
 


