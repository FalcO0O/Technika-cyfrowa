import csv
import pandas as pd

def q0_prim(s, q1, q0, b1, b0):
    return (not q0) and b1 or q0 and (not b1)

def q1_prim(s, q1, q0, b1, b0):
    return (not q1 and not q0 and b1 and b0) or \
        (not q1 and q0 and b1 and not b0) or \
        (q1 and not q0 and not b0) or \
        (q1 and q0 and b0) or \
        (q1 and not b1)

def s_prim(s, q1, q0, b1, b0):
    return (not b1 and b0) or (s and b1)


def minimized_function_test(real_data, test_func):
    flag = True
    print("S Q1 Q0 B1 B0 | Expected | Got")
    print("-" * 30)
    
    # Read the input combinations from CSV directly
    df = pd.read_csv("Book(Arkusz2).csv", sep=";")
    
    for index, row in df.iterrows():
        s = row['S']
        q1 = row['Q1']
        q0 = row['Q0']
        b1 = row['B1']
        b0 = row['B0']
        
        test_data = int(test_func(s, q1, q0, b1, b0))
        expected = int(real_data[index])
        
        if expected != test_data:
            flag = False
            print(f"{s}  {q1}  {q0}  {b1}  {b0} |    {expected}    |  {test_data}  <- ERROR")

        else:
            print(f"{s}  {q1}  {q0}  {b1}  {b0} |    {expected}    |  {test_data}")


    
    if flag:
        print("All tests passed!")
    return flag

def load_real_data_from_csv(filename, column_name):
    df = pd.read_csv(filename, sep=";")
    if column_name not in df.columns:
        print("Available columns:", list(df.columns))
        raise KeyError(f"Column '{column_name}' not found in the CSV file.")
    return df[column_name].to_numpy()

if __name__ == "__main__":
    q0_prim_data = load_real_data_from_csv("Book(Arkusz2).csv", "Q0?")
    print("Testowanie q0_prim:")
    minimized_function_test(q0_prim_data, q0_prim)

    q1_prim_data = load_real_data_from_csv("Book(Arkusz2).csv", "Q1?")
    print("\nTestowanie q1_prim:")
    minimized_function_test(q1_prim_data, q1_prim)

    s_next_data = load_real_data_from_csv("Book(Arkusz2).csv", "S?")
    print("\nTestowanie s_next:")
    minimized_function_test(s_next_data, s_prim)