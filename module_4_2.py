# "Пространство имен"
def test_function():
    print("Во внешней функции!")
    def inner_function():
        return 'Я в области видимости функции test_function'
    d = inner_function()
    print(d)

test_function()
p = inner_function()
print(p)