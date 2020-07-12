import pandas as pd
from snownlp import SnowNLP

data = pd.read_csv("review.csv")
df = pd.DataFrame(data)
for i in df['review']:
    print(i)

    s = SnowNLP(i)
    print(s.words)