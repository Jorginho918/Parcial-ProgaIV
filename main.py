from API import api
from UI import ui

dataset_identifier = "ch4u-f3i5"


def manage_data():
    params = ui.get_params()
    api.normalize_params(params)
    result = api.get_data(dataset_identifier=dataset_identifier, **params)
    
    try:
        result_df = api.convert_dataset_to_df(result)
        
    except ValueError as error:
        print(f"\n\tError: {error}\n")
        return
    
    relevant_info = api.get_relevant_info(result_df)
    medians = api.calculate_median(relevant_info)
    ui.print_table(relevant_info, medians)



def main():
    while True:
        ui.menu()
        op = ui.get_option()

        if op == 1:
            manage_data()

        elif op == 2:
            return
            
        input("\n\tOprima enter para volver al menu...")
        ui.clean_terminal()


if "__main__" == __name__:
    main()