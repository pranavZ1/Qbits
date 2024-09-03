import numpy as np
import pandas as pd
np.random.seed(42)
phoneNumbers=[''.join(np.random.choice(list('0123456789'),10))for i in range(50)]
alphas = [''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'),10))for j in range(50)]
df = pd.DataFrame({
    "Names":alphas,
    "phoneNumbers":phoneNumbers
})
df.to_csv('support_leads.csv',index=False)