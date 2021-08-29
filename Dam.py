dm_cap,wat,rain,ground= 250e100,199.5e85,25e8,5/100
uless = rain*25/100 #625000000.0
rem = 25e8 - uless #1875000000.0
cur = wat + rem #1.995e+87
storm = cur*0.15 #(15% of cur level=1.995e+87*0.15=2.9925e+86)
cur = cur + storm
cur += ground #5% ground add to present
evap = cur * 0.5 #5% of present level
cur -= evap #5% evaporated
current_level = cur - 0.15 #15% for irrigation to arid regions
print('Current water level of reservoir is',current_level) 

#OUTPUT : 
#Current water level of reservoir is 1.147125e+87
