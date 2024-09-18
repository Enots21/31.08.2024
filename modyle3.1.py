calls = 0


# #
#
def string_info(string):
    return len(string), string.upper(), string.lower()


print(string_info('Capybara'))
calls += 1
print(string_info('Armageddon'))
calls += 1


#
# #
def is_contains(string, list_to_search):
    for lst in list_to_search:
        if lst in string:
            return True
        else:
            return False


calls += 1

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches


def count_calls():
    return calls


calls += 1
print(calls)
