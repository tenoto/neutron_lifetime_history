#!/usr/bin/env python

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("data/neutron_lifetime - neutron_lifetime.csv")
data = df[df['flag']=='use']
data['error'] = np.sqrt(data['stat']**2+data['sys']**2)
print(data['year'])

###################
# Plot 
###################
plt.style.use('script/default.mplstyle')

fig = plt.figure(figsize=(10.6,6))
fig.patch.set_alpha(0.0)
ax1 = fig.add_subplot(111)


ax1.axhspan(888.0+2.0,888.0-2.0,color="tab:blue",alpha=0.3)
ax1.errorbar(
	data['year'][data['method']=='Beam'],
	data['lifetime (s)'][data['method']=='Beam'],
	yerr=data['error'][data['method']=='Beam'],
	fmt='s',markersize=9,linewidth=2,markeredgecolor='k',
	color='tab:blue',label='Beam')

ax1.axhspan(879.6+0.6,879.6-0.6,color="orange",alpha=0.3)
ax1.errorbar(
	data['year'][data['method']=='UCN'],
	data['lifetime (s)'][data['method']=='UCN'],
	yerr=data['error'][data['method']=='UCN'],	
	fmt='o',markersize=10,linewidth=3,markeredgecolor='k',
	color='orange',label='Bottle')

ax1.errorbar(
	data['year'][data['method']=='Theory'],
	data['lifetime (s)'][data['method']=='Theory'],
	yerr=data['error'][data['method']=='Theory'],	
	fmt='^',markersize=10,linewidth=2,markeredgecolor='k',
	color='orange',label='QCD')

ax1.errorbar(
	data['year'][data['method']=='Planet'],
	data['lifetime (s)'][data['method']=='Planet'],
	yerr=data['error'][data['method']=='Planet'],	
	fmt='*',markersize=20,linewidth=2,markeredgecolor='k',
	color='tab:red',label='Planet')

ax1.set_xlim(1990,2030)
ax1.set_ylim(870,900)
ax1.set_xlabel("Year",labelpad=14)
ax1.set_ylabel('Lifetime (seconds)',labelpad=14)
plt.setp([ax1], xscale="linear", yscale="linear")
ax1.legend(loc='upper right',fontsize=13)
plt.tight_layout()
#ax1.patch.set_alpha(0.0)  
#ax2.patch.set_alpha(0.0)  
fig.savefig("out/neutron_lifetime_history.pdf")

