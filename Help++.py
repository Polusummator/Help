import sys
from termcolor import colored


def all():
    for i in range(len(list_com)):
        if i != len(list_com) - 1:
            print(list_com[i], end='\n')
        else:
            print(list_com[i])
    return ''


def numbers():
    return ('Числа\n'
            '\n'
            'ЦЕЛЫЕ ЧИСЛА\n'
            '\n'
            'Целые числа в C++ представлены типами:\n'
            'char      (8 бит)\n'
            'short     (16 бит)\n'
            'int       (24 бита)\n'
            'long      (32 бита)\n'
            'long long (64 бита)\n'
            '\n'
            'Размеры типов могут варьироваться в зависимости от системы\n'
            '(максимальные и минимальные значения можно посмотреть в константах заголовочного файла climits)\n'
            'Также можно узнать кол-во байт, выделенных на тип или переменную с помощью sizeof:\n'
            'sizeof(int) для типов\n'
            'sizeof num  для переменных\n'
            '\n'
            'Также существуют unsigned-типы (целочисленные типы без отрицательных чисел). Их верхняя граница в 2 раза больше, чем у обычных типов\n'
            'например:\n'
            'unsigned n1 (тип int)\n'
            'ungigned long long n2\n'
            '\n'
            'СИСТЕМЫ СЧИСЛЕНИЯ:\n'
            'Целочисленные литералы могут хранится в трёх видах:\n'
            '1. Десятеричная с.с.      Обычная запись чисел в десятеричной с.с. Пример: -1, 0, 1323\n'
            '2. Восьмеричная с.с.      Первый символ - 0.                       Пример: 0425, 01\n'
            '3. Шестнадцатеричная с.с. Первый символ - 0, второй - x.           Пример: 0x1234a, 0xABBA\n'
            '\n'
            'Числа в этих с.с. можно выводить с помощью манипуляторов dec, oct и hex в cout:\n'
            'cout << oct; - замена вывода на восьмеричный формат\n'
            'По умолчанию стоит dec\n'
            '\n'
            'СУФФИКСЫ:\n'
            'Константы, наподобие cout << 24;, хранятся по умолчанию в типе int, но это можно изменить добавлением суффиксов (в любом регистре):\n'
            'l  - long\n'
            'll - long long\n'
            'u  - unsigned (можно добавлять к другим суффиксам: ul, ull)\n'
            'Примеры: 220ll, 30UL, 10u\n'
            '\n'
            'CHAR:\n'
            'char обозначает одиночный символ (из таблицы ASCII)\n'
            'Если использовать cin и cout, то при вводе char cin переведёт его в код символа (число), а cout переведёт его обратно в символ\n'
            'В основной программе char хранится в виде числа\n'
            'Если же присвоить значение char переменной типа int (или другого целочисленного типа), то при выводе этой переменной число не будет переводиться в символ\n'
            '\n'
            'Также отобразить одиночный символ можно функцией cout.put()\n'
            '\n'
            'ЭКРАНИРОВАННЫЕ ПОСЛЕДОВАТЕЛЬНОСТИ'
            'Говоря о символах, нельзя не упомянуть управляющие последовательности (экранированные последовательности)\n'
            'В языке C++ они почти полностью совпадают с последовательностями в языке Python\n'
            'Последовательности можно записывать не только в виде символов, но и в числовой записи (в разных с.с.):\n'
            '\\b = \\10 = \\12 = \\0x8\n'
            '\n'
            'CHAR: ДОПОЛНИТЕЛЬНО\n'
            'По умолчанию char не является типом со знаком или беззнаковым типом, но это можно исправить:\n'
            'signed char   - char со знаком\n'
            'unsigned char - char без знака\n'
            '\n'
            'Размер char можно увеличить другими типами:\n'
            '1. wchar_t (16 бит)\n'
            'Перед значением переменной ставится префикс L: wchar_t one = L\'K\'\n'
            'cin и cout не подходят для работы с эти типом, но есть wcin и wcout\n'
            '2. char16_t (16 бит)\n'
            'является беззнаковым\n'
            'Перед значением ставится префикс u\n'
            '3. char32_t (32 бита)\n'
            'является беззнаковым\n'
            'Перед значением ставится префикс U\n'
            '\n'
            'BOOL\n'
            'bool - это логический тип\n'
            'принимает значения true и false\n'
            'true = 1, false = 0, поэтому можно присваивать переменным другич числовых типов\n'
            'Также любая нулевая переменная равна false, ненулевая - true\n'
            '\n'
            'ЧИСЛА С ПЛАВАЮЩЕЙ ТОЧКОЙ\n'
            'Примеры:\n'
            '1.0\n'
            '0.111\n'
            '3.45E6\n'
            '2.52e+8\n'
            '5.11E-1\n'
            '7E5 (=7.0E+05, знак точки можно опускать)\n'
            'Типы с плавающей точкой в C++:\n'
            'float       (32 бита)\n'
            'double      (64 бита)\n'
            'long double (128 бит)\n'
            'Размеры типов могут варьироваться в зависимости от системы\n'
            'Ограничения можно найти в файле cfloat\n'
            '\n'
            'Исключить вывод экспоненциальной записи можно при помощи cout.setf(ios_base::fixed, ios_base::floatfield)\n'
            'также этот метод сделает фиксированное кол-во знаков после точки - 6\n'
            '\n'
            'КОНСТАНТЫ С ПЛАВАЮЩЕЙ ТОЧКОЙ:\n'
            'По умолчанию стоит тип double, но это можно изменить с помощью суффиксов (в любом регистре):\n'
            'f - float\n'
            'l - long double\n'
            'Примеры: 1.23f, 2.44E+28F, 1.111e20l\n')


def const():
    return ('const\n'
            '\n'
            'const - это квалификатор, позволяющий создавать символический константы\n'
            'Пример: const int N = 10;\n'
            'Теперь в программе N будет заменять 10\n'
            '\n'
            'Константа инициализируется в объявлении. Такой пример недопустим:\n'
            'const int N;\n'
            'N = 10;\n')


def arithmetic_operations():
    return ('Арифметические операции\n'
            '\n'
            '+ - сложение\n'
            '- - вычитание\n'
            '* - умножение\n'
            '/ - деление\n'
            '% - остаток от деления\n'
            '\n'
            'C++ поддерживает такие операции, как +=, -=, *=, /=, %=\n'
            'b += 1; - эквивалент b = b + 1;\n'
            '\n'
            'ДЕЛЕНИЕ\n'
            'Поведение операции деления зависит от типов операндов\n'
            '\n'
            'Если операнды одинаковых типов, то и результат будет такого же типа\n'
            '(при целых операндах будет выполнена операция взятия целой части от деления)\n'
            '\n'
            'Если один из операндов имеет тип числа с плавающей точкой, то результат будет числом с плавающей точкой\n')


def type_conversion():
    return ('Преобразования типов\n'
            '\n'
            'C++ автоматически преобразует типы при:\n'
            '1. присваивании значения одной переменной другой переменной другого типа\n'
            '2. комбинировании разных типов в выражениях\n'
            '3. передаче аргументов функциям\n'
            '\n'
            'Пример:\n'
            'short a = 10;\n'
            'int c = a;   // преобразование short -> int\n'
            'int b = 2;\n'
            'a += b;      // преобразование int -> short\n'
            'int d = 3.3; // преобразование double -> int (усечение дробной части)\n'
            '\n'
            'С преобразованием типов могут появляться проблемы\n'
            'Например, значение большого типа передаётся переменной меньшего типа, в которую это значение "не влезает"\n'
            'Также могут быть проблемы с точностью (double -> float)\n'
            '\n'
            'Избежать такие проблемы можно, используя списковую инициализацию\n'
            'Списковая инициализация не допускает "сужения" (значение "не влезает" в тип)\n'
            '\n'
            'Такая инициализация будет работать, если значение - это константа, и это значение "влезает" в тип, или тип переменной, значение которой присваивается, имеет меньшие ограничения\n'
            'Пример:\n'
            'const int a = 260;\n'
            'int d = 10;\n'
            'int b = {a};   // можно\n'
            'short c = {a}; // можно\n'
            'short e = {d}; // нельзя, т.к. e - не константа\n'
            'long f = {d};  // можно, т.к. long > int\n'
            'char g {1000}; // нельзя\n'
            '\n'
            'ПРИВИДЕНИЕ ТИПОВ\n'
            'Типы могут быть преобразованы не автоматически, например, так:\n'
            'int a = int (b); // оба варианты равнозначны\n'
            'int a = (int) b;\n'
            'Такое приведение не меняет саму переменную, а возвращает значение переменной в другом типе\n'
            'Такой вариант не ограничивает переполнение типа\n'
            '\n'
            'Другим вариантом является static_cast<>\n'
            'Синтаксис: static_cast<тип>(значение)\n'
            'Пример:\n'
            'short b = 9;\n'
            'int a = static_cast<int>(b);\n'
            '\n'
            'Этот вариант также не проверяет переполнение типа\n'
            '\n'
            'AUTO\n'
            'auto позволяет компилятору самому выбрать тип, исходя из значения переменной\n'
            'Пример:\n'
            'auto n = 100;    // int\n'
            'auto x = 1.5;    // double\n'
            'auto y = 1.3e12L // long double\n')


def array():
    return ('Массивы\n'
            '\n'
            'Массив - это структура данных, которая содержит множество значений одного типа\n'
            'Создание массива: тип имяМассива[кол-во элементов]\n'
            'Кол-во элементов должно быть вычислено на момент компиляции (не может быть переменной, значение которой получается в процессе выполнения программы)\n'
            '\n'
            'Индексация: array[index], индексы начинаются с 0\n'
            '\n'
            'ИНИЦИАЛИЗАЦИЯ\n'
            'Инициализировать массив можно, прописав значения всех элементов так:\n'
            'int n[2];\n'
            'n[0] = 1;\n'
            'n[1] = 2;\n'
            'или так:\n'
            'int n[2] = {1, 2}\n'
            '\n'
            'Значение в квадратных скобках можно не писать, тогда компилятор сам подсчитает размер массива\n'
            'Можно писать не все элементы в кргулых скобках, тогда компилятор присвоит значения только первым элементам\n'
            'По умолчанию все элементы массива нулевые (при пустых фигурных скобках)\n'
            'Знак = может быть опущен\n'
            '\n'
            'Также в момент инициализации может произойти преобразование типов, но сужение не допускается, т.е. 2000 нельязя будет перевести в char\n')


def string():
    return ('Строки\n'
            '\n'
            'Строка - это серия символов\n'
            'Есть жва способа представления строки\n'
            '1. МАССИВ CHAR\n'
            'Характерная черта такой строки - нулевой символ в конце (\\0)\n'
            'char one[2] = {\'1\', \'a\'};       // не строка\n'
            'char two[3] = {\'1\', \'a\', \'\\0\'}; // строка\n'
            '\n'
            'Строки записываются в двойных кавычках\n'
            'char two[3] = "1a"; // \\0 подразумевается\n'
            'Можно дать компилятору самому подсчитать кол-во символов\n'
            'char two[] = "1a";\n'
            '\n'
            'Можно дать массиву больший размер, чем длина строки, тогда все остальные элементы будут заполнены \\0\n'
            '\n'
            'Строки можно конкатенировать (складывать)\n'
            'Если две строки записаны чере пробел, символ табуляции и символ новой строки, то они объединятся\n'
            'cout << "one " "and"\n'
            '" two";\n'
            'Этот код выведет one and two\n'
            '\n'
            'Строка - это массив, поэтому можно обращаться к элементам по индексам, изменять их\n'
            'Если присвоить элементу \\0, то строка оборвётся на этом месте (символы дальше выводиться не будут)\n'
            '\n'
            'Длину строки (строки, а не массива) можно найти с помощью функции strlen (из cstring)\n'
            '\n'
            'По умолчанию cin заканчивает строку, когда введён пробел, имвол табуляции или символ новой строки\n'
            'Поэтому не получится прото так ввести строку с прорбелом внутри\n'
            'Для построчного ввода строк используется get и getline (get оставляет символ новой строки в очереди, getline - нет)\n'
            'Синтаксис: cin.getline(name, size);\n'
            'name - имя переменной, значение которой нужно ввести\n'
            'size - максимальный размер строки, после достижения которого getline не будет читать строку\n'
            '\n'
            'Может возникнуть проблема с двумя последовательными вводами строки через get, т.к. get оставляет символ новой строки\n'
            'Исправить можно так:\n'
            'cin.get(one, size);\n'
            'cin.get();\n'
            'cin.get(two, size);\n'
            'или так:\n'
            'cin.get(one, size).get();\n'
            'cin.get(two, size);\n'
            '\n'
            'cin.get() читает символ новой строки\n'
            '\n'
            'Если введена пустая строка, то get отключает последующий ввод (failbit)\n'
            'Если введена слишком длиннная строка (больше, чем size), то getline отключает последующий ввод\n'
            'Исправить можно, написав cin.clear();'
            '\n'
            'В cstring есть функции strcpy и strcat\n'
            'strcpy(char1, char2); // копирование char2 в char1\n'
            'strcat(char1, char2); // добавление char2 к char1 (конкатенация)\n'
            'Однако эти функции не очень удобны (как и массив char), они могут вызывать переполнение памяти массива\n'
            '\n'
            'Можно создать не только массив char, но и массив, wchar_t, char16_t, char32_t\n'
            'Нужно не забыть поставить префиксы перед строками (описаны в numbers)\n'
            'Для того, чтобы создать строку UTF-8, нужно поставить префикс u8\n'
            '\n'
            '2. КЛАСС STRING\n'
            'Класс string удобнее, чем массив char\n'
            'Для того, чтобы использовать string, нужно написать include <string>;\n'
            'Инициализация:\n'
            'string one = "some";\n'
            'Можно использовать списковую инициализацию\n'
            '\n'
            'string позоляет конкатенировать строки, используя + и +=\n'
            'Можно присвоить значение одной переменной другой (массив char позволяет делать такое с импортированными функциями)\n'
            '\n'
            'Ввод можно осуществлять при помощи cin, но опять же будет проблема с пробелами, поэтому нужно использовать getline (другой синтаксис):\n'
            'getline(cin, name), где name - название переменной\n'
            'Спецификатор длины не требуется, потому что string автоматически изменяет размер\n'
            '\n'
            'Длину строки можно узнать так:\n'
            'int len = str.size();\n'
            '\n'
            'В строках могут встречаться экранированные последовательности. Чтобы вывести их в иде символов, можно добавить префикс R\n'
            'Пример: string b = R"(some\\nstring\\"wow\\")";\n'
            'Если вывести b, то получится some\\nstring\\"wow\\"\n'
            'Если же в строке есть последовательность )", которую нужно вывести, то между " и ( можно вставить символы\n'
            'Главное, чтобы эти символы повторялись в конце\n'
            'Пример: string b = R"+("(\\lol\\)")+";\n'
            'Здесь вместо "( и )" используются "+( и )+", но можно вставлять любые символы\n'
            'Префикс R может стоять в сочетании с другими префиксами (например UR"some\\n")\n')


def struct():
    return ('Структуры\n'
            '\n'
            'Структуры позволяют хранить в себе элементы различных типов\n'
            'Структура - это своеобразный тип данных, создаваемый пользователем\n'
            '\n'
            'Создание:\n'
            'struct name {\n'
            '   int one;\n'
            '   char two;\n'
            '   string three;\n'
            '};\n'
            '\n'
            'После создания структуры можно создавать переменные этого типа\n'
            'name some_variable; - some_variable имеет тип name\n'
            'Теперь можно обратится к членам структуры:\n'
            'some_variable.one\n'
            'some_variable.two\n'
            '\n'
            'ИНИЦИАЛИЗАЦИЯ\n'
            'Инициализировать переменные созданного типа можно так:\n'
            'name var = {1, \'t\', "th"};\n'
            'Т.е. инициализация похожа на массив\n'
            'Знак = может быть опущен\n'
            'Пустые фигурные скобки обратят все байты членов в 0\n'
            '\n'
            'или так:\n'
            'name var;\n'
            'var.one = 1;\n'
            'var.two = \'t\'\n'
            'var.three = "th"\n'
            'Если какому-то члену не будет присвоено значение, то он не будет ничему равен (но исклюсение не будет выдано даже при обращении к этому члену)\n'
            '\n'
            'Можно сделать множественную инициализацию\n'
            'struct some {\n'
            '   int one;\n'
            '   int two;\n'
            '} var1, var2;\n'
            '\n'
            'struct some {\n'
            '   int one;\n'
            '   int two;\n'
            '} var1 {1, 2}, var2 {3, 4};\n'
            '\n'
            'Можно сделать структуру без имени, но тогда в программе будет только одна переменная такого типа\n'
            'struct {'
            '   int x;\n'
            '   int y;\n'
            '} position {-1, 20};'
            '\n'
            'Одну структуру можно присвоить другой, тогда все значения членов скопируются\n'
            '\n'
            'МАССИВЫ СТРУКТУР\n'
            'Структуры можно объединять в масиивы\n'
            'some vars[10]; - массив vars из 10 структур some\n'
            'Обращаться к членам структур следует так:\n'
            'vars[5].x\n'
            '\n'
            'Инициализировать структуры в массиве можно так:\n'
            'some vars[2] {\n'
            '   {10, 10},\n'
            '   {-2, 35},\n'
            '};\n'
            '\n'
            'БИТОВЫЕ ПОЛЯ\n'
            'Можно ограничить размер членов структуры\n'
            'struct some {'
            '   unsigned int rt : 4; - можно использовать только 4 бита\n'
            '};\n'
            '\n'
            'Можно создать указатель на структуру\n'
            'Тогда к членам структуры нужно будет обращаться через ->\n'
            '\n'
            'Можно создать конструктор структуры\n'
            'struct Man {\n'
            '    int height, weight;\n'
            '    string name;'
            '    Man() { // конструктор по умолчанию, обязан быть\n'
            '        height = 170;\n'
            '        weight = 75;\n'
            '    }\n'
            '    Man(string name_): height(170), weight(75), name(name_){}\n'
            '};\n'
            '\n'
            'Если создаётся переменная в виде указателя, то нужно написать Man *c = new Man("Bob");\n'
            ''
            'МЕТОДЫ И ПЕРЕОПРЕДЕЛЕНИЕ ОПЕРАТОРОВ\n'
            'struct Triple {\n'
            '    int a, b, c;\n'
            '    Triple(){}\n'
            '    Triple(int a_, int b_, int c_): a(a_), b(b_), c(c_){}\n'
            '    int mult() { // метод\n'
            '        return a * b * c;\n'
            '    }\n'
            '    void add(int x) { // метод\n'
            '        a += x;\n'
            '        b += x;\n'
            '        c += x;\n'
            '    }\n'
            '};\n')


def union():
    return ('Объединения\n'
            '\n'
            'Объединение - это формат данных, похожий на структуру, но позволяющий в момент времени использовать только один член\n'
            '\n'
            'union some_u {\n'
            '   int i_val;\n'
            '   double d_val;\n'
            '};\n'
            '\n'
            'some_u var;\n'
            'var.i_val = 20;\n'
            'var.d_val = 1.1; - значения int уже нет\n'
            '\n'
            'Объединения можно использовать внутри структур\n'
            'struct one {\n'
            '   int val;\n'
            '   int type;\n'
            '   union id {\n'
            '       long id_l;\n'
            '       int id_i;\n'
            '   } id_val;\n'
            '};\n'
            '\n'
            '...\n'
            'one var;\n'
            '...\n'
            'if (var.type == 1)\n'
            '   cin >> var.id_val.id_l;\n'
            'else\n'
            '   cin >> var.id_val.id_i;\n'
            '\n'
            'Можно не указывать название объединения и имя переменной после него, тогда члены объединения будут принадлежать структуре (но условие их использования не меняется)\n')


def enum():
    return('Перечисления\n'
           '\n'
           'Перечисления - это способ создания символических констант\n'
           'enum some {one, two, three}; - создание типа some\n'
           'some var; - создание переменной типа\n'
           'Переменной var можно присвоить только one, two или three\n'
           '\n'
           'По умолчанию one = 0, two = 1, three = 2\n'
           '\n'
           'Перечисления могут переходить в int\n'
           'int i_am_int = one;\n'
           'но int не переходит в тип перечисления\n'
           'var = 1; - НЕВЕРНО\n'
           'Но можно перевести так:\n'
           'var = some(1);\n'
           'Если значение недопустимо, то результат будет неопределённым\n'
           '\n'
           'Перечисления поддерживают ТОЛЬКО присваивание\n'
           '\n'
           'Можно опустить имя после enum, тогда можно будет использовать константы, но нельзя будет создавать переменные перечислимого типа\n'
           '\n'
           'Есть возможность устанавливать свои значения перечислителей\n'
           'enum some {nUlL, zero = 0, one, dva}\n'
           'если не указано значение, то оно равно предудущий+1\n'
           'nUlL = 0, zero = 0, one = 1, dva = 2\n'
           '\n'
           'Можно присваивать значения, которых нет среди перечислителей\n'
           'enum some {one = 3, two = -5}\n'
           'some var;\n'
           'var = some(2);\n'
           'Присваивание производится в пределах диапазона\n'
           'Верхняя граница: первая степень двойки, которая больше наиб. перечислителя\n'
           'Нижняя граница: если наим. перечислитель >= 0, то 0\n'
           '                иначе то же самое, что с верхней границей, только со знаком минус\n')


def pointers():
    pass


def scanf_printf():
    return ('Scanf и printf\n'
            '\n'
            'scanf и printf - методы ввода/вывода\n'
            '\n'
            'Синтаксис:\n'
            'scanf("форматная строка", переменные)\n'
            'printf("форматная строка", переменные)\n'
            '\n'
            'В строке для ввода используются спецификаторы:\n'
            '%d   - int\n'
            '%hd  - short\n'
            '%ld  - long\n'
            '%lld - long long\n'
            '%s   - string (char*)\n'
            '%c   - char\n'
            '%f   - float\n'
            '%lf  - double\n'
            '%Lf  - long double\n'
            '%u   - unsigned int\n'
            '%lu  - unsigned long\n'
            '%llu - unsigned long long\n'
            '*вещественные числа в разных компиляторах имеют разные спецификаторы\n'
            '\n'
            'Переменные (кроме string) передаются в scanf адресом (&val)\n'
            'scanf игнорирует пробельные символы , поэтому два числа можно ввести так: scanf("%d%d", &a, &b) и так scanf("%d %d", &a, &b)\n'
            'Но char нужно указывать явно (пробелы тоже считаются)\n'
            '\n'
            'При вводе и выводе string (не char*) нужно указывать s.data() или &s[0]\n'
            'Если нужно ввести определённые кол-во символов в string, то можно написать так: %5s\n'
            'Но если мы вводим две строки, то следующая начинает вводиться сразу после окончания предыдущей (там, где мы хакончили считывать)\n'
            'Поэтому таким способом нельзя вводить строку и число после неё\n'
            '\n'
            'Можно ввести определённый промежуток символов\n'
            'Например, пропуск символов от a до c: %*s[a-c]\n'
            '\n'
            'Чтобы вывести символ % нужно написать %%\n'
            '\n'
            'Можно пропустить ввод одной переменной. Для этого нужно написать %*спецификатор\n'
            '\n'
            'scanf возвращает число, равное кол-ву введённых полей, поэтому мржно сделать ввод без указания кол-ва вводмиых объектов:\n'
            'while (scanf("%d", &x)) {\n'
            '   ...\n'
            '}\n'
            '\n'
            'При выводе можно указывать точность вещественного числа:\n'
            'printf("%.10lf", val)\n'
            '\n'
            'НЕ ПО ТЕМЕ:\n'
            'Можно переопредеить ввод и вывод для других типов и своих структур. Например, пример ввода/вывода массива:\n'
            'template <class T>\n'
            'istream& operator >>(istream& in, vector<T>& arr) {\n'
            '    for (T& i: arr)\n'
            '        in >> i;\n'
            '    return in;\n'
            '}\n'
            'template <class T>\n'
            'ostream& operator <<(ostream& out, const vector<T>& arr) {\n'
            '    for (const T& i: arr)\n'
            '        out << i << \' \';\n'
            '    return out;\n'
            '}\n')


def files():
    return ('Работа с файлами\n'
            '\n'
            '1. freopen\n'
            'Синтаксис:\n'
            'freopen("file", "mode", thread)\n'
            'file   - путь к файлу (название, файл должен быть в текущей директории)\n'
            'mode   - способ открытия (r или w)\n'
            'thread - переопределяемый поток (обычно stdin/stdout)\n'
            '\n'
            'r стирает всё, что было в файле\n'
            '\n'
            'в конце можно (необязательно) закрыть потоки: fclose(stdin)\n'
            '\n'
            '2. ifstream/ofstream\n'
            'fstream позволяет создавть новые потоки\n'
            'создание потока ввода и вывода:\n'
            'ifstream in("file");\n'
            'ofstream out("file");\n'
            '\n'
            'ввод/вывод будет с этими потками:\n'
            'in >> x;\n'
            'out << x << endl;\n'
            '\n'
            'Можно закрыть потки:\n'
            'in.close();\n')

def no(a):
    global list_com
    list_com = ['all', 'numbers, const', 'arithmetic_operations', 'type_conversion', 'array', 'string', 'struct', 'union', 'enum', 'pointers', 'scanf_printf', 'files']
    if a not in list_com:
        return False
    else:
        return True


a = '1'
print(colored('Help of C++\n', 'green'))
print(colored('Это программа-тетрадь о языке C++\n'
              'Программа разделена на разделы. Чтобы прочитать документацию по одной теме, напишите её название\n'
              'Чтобы увидеть список всех тем, напишите all\n'
              'Чтобы выйти из программы, напишите exit\n', 'blue'))
while a != 'exit':
    a = input(colored('>>>', 'green'))
    if a == 'exit':
        sys.exit('Завершение работы...')
    else:
        if not no(a):
            print('Такого раздела не существует!')
        else:
            a += '()'
            print(eval(a))
