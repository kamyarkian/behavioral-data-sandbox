import pandas as pd
import numpy as np
import random

# Setting a seed for reproducibility
np.random.seed(42)

def generate_mock_data(num_users=1000):
    """
    Simulates a behavioral experiment dataset.
    Group A: Control
    Group B: Nudge (Loss Aversion Tactics)
    """
    data = []
    
    for _ in range(num_users):
        user_id = random.randint(10000, 99999)
        group = random.choice(['A_Control', 'B_Nudge'])
        
        # Simulating higher conversion for Nudge group based on behavioral economics theory
        if group == 'B_Nudge':
            conversion_rate = 0.15  # 15% conversion (Higher engagement)
            time_on_page = np.random.normal(120, 30) # Average 120 seconds
        else:
            conversion_rate = 0.10  # 10% conversion
            time_on_page = np.random.normal(90, 20) # Average 90 seconds
            
        converted = 1 if random.random() < conversion_rate else 0
        
        data.append([user_id, group, time_on_page, converted])
    
    df = pd.DataFrame(data, columns=['User_ID', 'Group', 'Time_On_Page_Sec', 'Converted'])
    return df

if __name__ == "__main__":
    print("--- Behavioral Data Simulation ---")
    df = generate_mock_data()
    print(df.head())
    print("\nConversion Rate by Group:")
    print(df.groupby('Group')['Converted'].mean())
    print("\nData generated successfully.")
