# Positive covariance yang menggambarkan dua feature yang berkorelasi positif atau bersesuaian.
# Negative covariance yang merepresentasikan dua feature yang berkorelasi negatif atau berlawanan.
# Zero covariance yang menandakan dua feature yang tidak berkorelasi satu sama lain.

import pandas as pd
    
sample_data = {
    'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
    'age': [24, 22, 23, 25, 28],  
    'communication_skill_score': [85, 70, 75, 90, 90],
    'quantitative_skill_score': [80, 90, 80, 75, 70]
}
    
df = pd.DataFrame(sample_data)
    
print(df.cov(numeric_only=True))