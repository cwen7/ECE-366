memory = [[]]
for i in range(1025):
    mem = hex(i)*4
    memory.append([mem, 0, 0, 0, 0])
    print(memory[i], end = " ")
"""
memory = [[0x2000,0,0,0,0],[0x2004,0,0,0,0],[0x2008,0,0,0,0],[0x200c,0,0,0,0],
         [[0x2010,0,0,0,0],[0x2014,0,0,0,0],[0x2018,0,0,0,0],[0x201c,0,0,0,0],
         [[0x2020,0,0,0,0],[0x2024,0,0,0,0],[0x2028,0,0,0,0],[0x202c,0,0,0,0],
         [[0x2030,0,0,0,0],[0x2034,0,0,0,0],[0x2038,0,0,0,0],[0x203c,0,0,0,0],
         [[0x2040,0,0,0,0],[0x2044,0,0,0,0],[0x2048,0,0,0,0],[0x204c,0,0,0,0],
         [[0x2050,0,0,0,0],[0x2054,0,0,0,0],[0x2058,0,0,0,0],[0x205c,0,0,0,0],
         [[0x2060,0,0,0,0],[0x2064,0,0,0,0],[0x2068,0,0,0,0],[0x206c,0,0,0,0],
         [[0x2070,0,0,0,0],[0x2074,0,0,0,0],[0x2078,0,0,0,0],[0x207c,0,0,0,0],
         [[0x2080,0,0,0,0],[0x2084,0,0,0,0],[0x2088,0,0,0,0],[0x208c,0,0,0,0],
         [[0x2090,0,0,0,0],[0x2094,0,0,0,0],[0x2098,0,0,0,0],[0x209c,0,0,0,0],
         [[0x20a0,0,0,0,0],[0x20a4,0,0,0,0],[0x20a8,0,0,0,0],[0x20ac,0,0,0,0],
         [[0x20b0,0,0,0,0],[0x20b4,0,0,0,0],[0x20b8,0,0,0,0],[0x20bc,0,0,0,0],
         [[0x20c0,0,0,0,0],[0x20c4,0,0,0,0],[0x20c8,0,0,0,0],[0x20cc,0,0,0,0],
         [[0x20d0,0,0,0,0],[0x20d4,0,0,0,0],[0x20d8,0,0,0,0],[0x20dc,0,0,0,0],
         [[0x20e0,0,0,0,0],[0x20e4,0,0,0,0],[0x20e8,0,0,0,0],[0x20ec,0,0,0,0],
         [[0x20f0,0,0,0,0],[0x20f4,0,0,0,0],[0x20f8,0,0,0,0],[0x20fc,0,0,0,0],
         [[0x2100,0,0,0,0],[0x2104,0,0,0,0],[0x2108,0,0,0,0],[0x210c,0,0,0,0],
         [[0x2110,0,0,0,0],[0x2114,0,0,0,0],[0x2218,0,0,0,0],[0x221c,0,0,0,0],
         [[0x2120,0,0,0,0],[0x2124,0,0,0,0],[0x2328,0,0,0,0],[0x232c,0,0,0,0],
         [[0x2130,0,0,0,0],[0x2134,0,0,0,0],[0x2138,0,0,0,0],[0x213c,0,0,0,0],
         [[0x2140,0,0,0,0],[0x2144,0,0,0,0],[0x2148,0,0,0,0],[0x214c,0,0,0,0],
         [[0x2150,0,0,0,0],[0x2154,0,0,0,0],[0x2158,0,0,0,0],[0x215c,0,0,0,0],
         [[0x2160,0,0,0,0],[0x2164,0,0,0,0],[0x2168,0,0,0,0],[0x216c,0,0,0,0],
         [[0x2170,0,0,0,0],[0x2174,0,0,0,0],[0x2878,0,0,0,0],[0x217c,0,0,0,0],
         [[0x2180,0,0,0,0],[0x2184,0,0,0,0],[0x2188,0,0,0,0],[0x218c,0,0,0,0],
         [[0x2190,0,0,0,0],[0x2194,0,0,0,0],[0x2198,0,0,0,0],[0x219c,0,0,0,0],
         [[0x21a0,0,0,0,0],[0x21a4,0,0,0,0],[0x21a8,0,0,0,0],[0x21ac,0,0,0,0],
         [[0x21b0,0,0,0,0],[0x21b4,0,0,0,0],[0x21b8,0,0,0,0],[0x21bc,0,0,0,0],
         [[0x21c0,0,0,0,0],[0x21c4,0,0,0,0],[0x21c8,0,0,0,0],[0x21cc,0,0,0,0],
         [[0x21d0,0,0,0,0],[0x21d4,0,0,0,0],[0x21d8,0,0,0,0],[0x21dc,0,0,0,0],
         [[0x21e0,0,0,0,0],[0x20e4,0,0,0,0],[0x20e8,0,0,0,0],[0x21ec,0,0,0,0],
         [[0x21f0,0,0,0,0],[0x21f4,0,0,0,0],[0x21f8,0,0,0,0],[0x21fc,0,0,0,0],
         [[0x2000,0,0,0,0],[0x2004,0,0,0,0],[0x2008,0,0,0,0],[0x200c,0,0,0,0],
         [[0x2010,0,0,0,0],[0x2014,0,0,0,0],[0x2018,0,0,0,0],[0x201c,0,0,0,0],
         [[0x2020,0,0,0,0],[0x2024,0,0,0,0],[0x2028,0,0,0,0],[0x202c,0,0,0,0],
         [[0x2030,0,0,0,0],[0x2034,0,0,0,0],[0x2038,0,0,0,0],[0x203c,0,0,0,0],
         [[0x2040,0,0,0,0],[0x2044,0,0,0,0],[0x2048,0,0,0,0],[0x204c,0,0,0,0],
         [[0x2050,0,0,0,0],[0x2054,0,0,0,0],[0x2058,0,0,0,0],[0x205c,0,0,0,0],
         [[0x2060,0,0,0,0],[0x2064,0,0,0,0],[0x2068,0,0,0,0],[0x206c,0,0,0,0],
         [[0x2070,0,0,0,0],[0x2074,0,0,0,0],[0x2078,0,0,0,0],[0x207c,0,0,0,0],
         [[0x2080,0,0,0,0],[0x2084,0,0,0,0],[0x2088,0,0,0,0],[0x208c,0,0,0,0],
         [[0x2090,0,0,0,0],[0x2094,0,0,0,0],[0x2098,0,0,0,0],[0x209c,0,0,0,0],
         [[0x20a0,0,0,0,0],[0x20a4,0,0,0,0],[0x20a8,0,0,0,0],[0x20ac,0,0,0,0],
         [[0x20b0,0,0,0,0],[0x20b4,0,0,0,0],[0x20b8,0,0,0,0],[0x20bc,0,0,0,0],
         [[0x20c0,0,0,0,0],[0x20c4,0,0,0,0],[0x20c8,0,0,0,0],[0x20cc,0,0,0,0],
         [[0x20d0,0,0,0,0],[0x20d4,0,0,0,0],[0x20d8,0,0,0,0],[0x20dc,0,0,0,0],
         [[0x20e0,0,0,0,0],[0x20e4,0,0,0,0],[0x20e8,0,0,0,0],[0x20ec,0,0,0,0],
         [[0x20f0,0,0,0,0],[0x20f4,0,0,0,0],[0x20f8,0,0,0,0],[0x20fc,0,0,0,0],
         [[0x2100,0,0,0,0],[0x2104,0,0,0,0],[0x2108,0,0,0,0],[0x210c,0,0,0,0],
         [[0x2110,0,0,0,0],[0x2114,0,0,0,0],[0x2218,0,0,0,0],[0x221c,0,0,0,0],
         [[0x2120,0,0,0,0],[0x2124,0,0,0,0],[0x2328,0,0,0,0],[0x232c,0,0,0,0],
         [[0x2130,0,0,0,0],[0x2134,0,0,0,0],[0x2138,0,0,0,0],[0x213c,0,0,0,0],
         [[0x2140,0,0,0,0],[0x2144,0,0,0,0],[0x2148,0,0,0,0],[0x214c,0,0,0,0],
         [[0x2150,0,0,0,0],[0x2154,0,0,0,0],[0x2158,0,0,0,0],[0x215c,0,0,0,0],
         [[0x2160,0,0,0,0],[0x2164,0,0,0,0],[0x2168,0,0,0,0],[0x216c,0,0,0,0],
         [[0x2170,0,0,0,0],[0x2174,0,0,0,0],[0x2878,0,0,0,0],[0x217c,0,0,0,0],
         [[0x2180,0,0,0,0],[0x2184,0,0,0,0],[0x2188,0,0,0,0],[0x218c,0,0,0,0],
         [[0x2190,0,0,0,0],[0x2194,0,0,0,0],[0x2198,0,0,0,0],[0x219c,0,0,0,0],
         [[0x21a0,0,0,0,0],[0x21a4,0,0,0,0],[0x21a8,0,0,0,0],[0x21ac,0,0,0,0],
         [[0x21b0,0,0,0,0],[0x21b4,0,0,0,0],[0x21b8,0,0,0,0],[0x21bc,0,0,0,0],
         [[0x21c0,0,0,0,0],[0x21c4,0,0,0,0],[0x21c8,0,0,0,0],[0x21cc,0,0,0,0],
         [[0x21d0,0,0,0,0],[0x21d4,0,0,0,0],[0x21d8,0,0,0,0],[0x21dc,0,0,0,0],
         [[0x21e0,0,0,0,0],[0x20e4,0,0,0,0],[0x20e8,0,0,0,0],[0x21ec,0,0,0,0],
         [[0x21f0,0,0,0,0],[0x21f4,0,0,0,0],[0x21f8,0,0,0,0],[0x21fc,0,0,0,0]]
"""