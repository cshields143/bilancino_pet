import netCDF4
import pandas as pd

df = pd.read_csv('bilancino.csv', index_col=0)
df.index = pd.to_datetime(df.index)

# chunk by month
df['Month'] = df.index.month
df['Year'] = df.index.year
df['AbsYear'] = df['Year'] - df['Year'].min()
df['AbsMonth'] = df['Month'] + 12 * df['AbsYear']
thats_what_i_want = df.groupby('AbsMonth')['Temperature_Le_Croci'].mean()

# isolate data we need
dates = thats_what_i_want.index * 10**9 # trick it into thinking this is a valid time :(
cels = thats_what_i_want.values
n = len(cels)

# create the netcdf dataset
with netCDF4.Dataset('bilancino.nc', 'w') as nc:
    nc.createDimension('lat', 1)
    nc.createDimension('lon', 1)
    nc.createDimension('time', n)
    lats = nc.createVariable('lat', 'f', ('lat',))
    lats.units = 'degrees_north'
    lons = nc.createVariable('lon', 'f', ('lon',))
    lons.units = 'degrees_east'
    times = nc.createVariable('time', 'f', ('time',))
    times.units = 'seconds'
    tmps = nc.createVariable('tmp', 'f', ('lat', 'lon', 'time'))
    tmps.units = 'celsius'
    lats[:] = [44.0500613757517]
    lons[:] = [11.195636134639]
    times[:] = dates
    tmps[:] = cels
