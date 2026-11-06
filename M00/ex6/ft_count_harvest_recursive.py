def ft_count_harvest_recursive(days=None, counter=1) -> None:
    if days is None:
        days = int(input("Days until harvest: "))

    if counter > days:
        print("Harvest time!")
        return

    print(f"Day {counter}")
    ft_count_harvest_recursive(days, counter + 1)
