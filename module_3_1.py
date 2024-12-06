calls = int(0)
def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    count_calls()
    string = str(string)
    m = (len(string), string.upper(), string.lower())
    return m
def is_contains(string,is_contains):
    count_calls()
    string = str(string)
    for i in range(len(is_contains)):
        is_contains[i] = is_contains[i].lower()
    if string.lower() in is_contains:
        log = True
    else:
        log = False
    return log

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['UrBan', 'BaNaN', 'urAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(string_info(123435235115))
print(string_info('AINHFPUNfmdnmfns,nfipunapsndfmvcmompioaninasdpfn))afffffffdfasf@@#23m12312313   1231  12312'))
print(is_contains('GoloGoloGu',['gologolog','GologolOgu','gol','Glagol','Google']))
print('Вызвано функций: ',calls)
