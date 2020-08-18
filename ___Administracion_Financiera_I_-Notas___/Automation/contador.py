from cuenta import cuenta 
from load_data import get_rows
from balance_general import balance_general
from yaml import full_load, dump

def main(db):
    data_rows = get_rows()
    master_cuentas,current = [],0
    for i in data_rows:

        instance = cuenta(
            str(data_rows[current][0]),
            data_rows[current][1],
            data_rows[current][3], db
        )
        instance.sort_category()
        instance.circulante()
        master_cuentas.append(instance)
        with open("accounting.yaml",encoding="UTF-8",mode="w") as file:
            dump(db,file) # default_flow_style=True
            file.close()
        current += 1
    print("balance general ... ")
    balance = balance_general(master_cuentas)
    balance.sort()
    balance.write_balance()
    

if __name__ == "__main__":
    with open("accounting.yaml",encoding="UTF-8",mode="r+") as file:
        db = full_load(file)
        file.close()
    main(db)

    


# Transform into dataframe
# import pandas as pd
# df = pd.DataFrame(data_rows)
# # to print everything
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(df)

