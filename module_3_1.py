calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    tuple_ = len(string), string.upper(), string.lower()
    print(tuple_)
def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].upper()
    if string.upper() in list_to_search:
        print(True)
    else:
        print(False)
string_info('Capybara')
string_info('Armageddon')
string_info('AbRakadabra')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
is_contains('one', ['two', 'three', 'five','oNe'])
print(calls)