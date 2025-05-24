import pandas as pd
import logicmin

df = pd.read_csv("Book(Arkusz2).csv", sep=';')

t = logicmin.TT(5, 3)

input_columns = ['S', 'Q1', 'Q0', 'B1', 'B0']
output_columns = ['S?', 'Q1?', 'Q0?']

elevator_input = df[input_columns].to_numpy().tolist()
elevator_output = df[output_columns].to_numpy().tolist()

ei = ["".join(str(el) for el in element) for element in elevator_input]
eo = ["".join(str(el) for el in element) for element in elevator_output]

for i in range(len(ei)):
    t.add(ei[i], eo[i])

sols = t.solve()
print(sols.printN(
    xnames=['S', 'Q1', 'Q0', 'B1', 'B0'],
    ynames=['S?', 'Q1?', 'Q0?']
))