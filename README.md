# country-coordinates

This package provides longitude and latitude coordinates for countries.
It can be use together with xarray to extract data.

## Installation

```sh
pip install country-coordinates

```

## Usage

```python
import xarray as xr
from country_coord import lonlat

lon, lat = lonlat.get_coordinates('Ghana')

ds = xr.open_dataset('data.nc')

ds = ds.sel(time=slice('2000','2010'),lat=slice(*lon),lon=slice(*lat))<br>


```
