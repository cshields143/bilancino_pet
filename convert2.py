import netCDF4
import pandas as pd

nc = netCDF4.Dataset('urgh_pet_thornthwaite.nc', 'r')
vals = list(nc.variables['pet_thornthwaite'][:][0][0])
valsd = {'pet':vals}
df = pd.DataFrame(valsd)
df.to_csv('bilancino_pet.csv')
