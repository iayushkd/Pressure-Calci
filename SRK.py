import pandas as pd
data = pd.read_excel('Assignment.csv')

data['bi'] = 0.07796*8.314*data['Tc(K)']/(data['Pc(Mpa)']*(10**6))
data['xi*bi'] = data['Composition']*data['bi']
data['Tr'] = 373.15/data['Tc(K)']
data['ac'] = 0.457235*(8.314*data['Tc(K)'])**2/(data['Pc(Mpa)']*(10**6))

data['alpha'] = (1+(0.3676+1.54226*data['Wi']-0.26992*data['Wi']**2)*(1-data['Tr']**(1/2)))**2
data['ai'] = data['ac']*data['alpha']

kij = pd.read_excel('kij.csv',index_col=False)
T = 373 # Kelvin
v = 0.0005 #m3
mole = 0.5
R = 8.314 # J/mol.k
Vm = v/mole
b = data['xi*bi'].sum()
a=0
for i in range(1,11):
    for j in range(i,11):
        tmp = (data['Composition'][i]*data['Composition'][j])*((data['ai'][i]*data['ai'][j])**0.5)*(1-kij.iloc[j][i])
        a += tmp

p = (R*T)/(Vm-b)-a/(Vm*(Vm+b)+b*(Vm-b))
print(p)
# P = 2138433.3662314564 Pa