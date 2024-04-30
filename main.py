import pandas as pd
from riskquant.simpleloss import SimpleLoss

df = pd.read_csv("incidents_history.csv")


ddos_attacks = df[df['Type of Incident'] == 'DDoS Attack']

print(ddos_attacks)

DDoS_loss = ddos_attacks['Financial cost'].mean()

print("Mean loss for DDoS Attacks: $", DDoS_loss)



label = "DDoS"
name = "DDoS Attack"
frequency = df[df['Type of Incident'] == 'DDoS Attack'].shape[0] / df['Year'].nunique()
low_loss = ddos_attacks['Financial cost'].min()  # Highest financial loss of DDoS attacks
high_loss = ddos_attacks['Financial cost'].max()



s = SimpleLoss(label="DDoS", name="DDoS Attack", frequency=frequency, low_loss=low_loss, high_loss=high_loss)
risk_ddos = s.annualized_loss()
print("Risk of DDoS Attack:", risk_ddos)



