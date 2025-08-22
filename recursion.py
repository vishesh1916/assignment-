def print_numbers(cn):
    if cn > 5:
        return
    print(cn)
    print_numbers(cn+1)

print_numbers(1)
