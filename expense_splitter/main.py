def calculate_split(total_amount: float, no_of_people: int, currency: str) -> None:
    if no_of_people <= 1:
        raise ValueError("Number of people must be greater than one.")
    
    percentage_sharing = []

    for count in range(no_of_people):
        individual_percentage = int(input(f"Enter the share for the {count + 1} person: "))
        percentage_sharing.append(individual_percentage)


    share_per_person: list[float] = []

    for i in range(no_of_people):
        share = total_amount * (percentage_sharing[i] / 100)
        share_per_person.append(share)

    print(f"Total Expense : {currency}{total_amount:,.2f}")
    print(f"Number of people : {no_of_people}")
    for i in range(no_of_people):
        print(f"The share for {i + 1} person is {share_per_person[i]}")
    


def main() -> None:
    try:
        total_amount: float = float(input("Enter the total amount to be divided (€): "))
        no_of_persons: int = int(input("Enter the total number of people: "))
        
        calculate_split(total_amount, no_of_persons, currency="€")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()    