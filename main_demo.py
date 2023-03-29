import lists_lib
test = [2,4,6,9]
print(f'test: {test}')
print(f'is even2(test):{lists_lib.is_even2(test)}')
print(f"any_even1(test) : {lists_lib.any_even(test)}")
print(f"any_even2(test) : {lists_lib.any_even2(test)}")

print(f"sqtotal(test) : {lists_lib.sqtotal(test)}")
print("------------------------")
print(test)
print("------------------------")
print(f"Is it all number even? \nAnswer: {lists_lib.all_evenf(test)}")
print(f"Is it all number even? \nAnswer: {lists_lib.all_evenP(test)}")