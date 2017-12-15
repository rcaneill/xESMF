"""
Standard test data for regridding benchmark.

Data field originally proposed by Jones (1999).
Ullrich et al. (2009) contain the figures.

Reference:
Jones, P. W. (1999). First-and second-order conservative remapping schemes for
grids in spherical coordinates. Monthly Weather Review, 127(9), 2204-2210.

Ullrich, P. A., Lauritzen, P. H., & Jablonowski, C. (2009). Geometrically exact
conservative remapping (GECoRe): regular latitude–longitude and cubed-sphere
grids. Monthly Weather Review, 137(6), 1721-1741.
"""

import numpy as np


def wave_smooth(lon, lat):
    '''
    Spherical harmonic with low frequency
    Y_2^2 = 2 + \cos^2(\theta) \cos(2 \phi)
    '''
    # degree to radius, make a copy
    lat = lat/180.0*np.pi
    lon = lon/180.0*np.pi

    f = 2 + np.cos(lat)**2 * np.cos(2*lon)
    return f
