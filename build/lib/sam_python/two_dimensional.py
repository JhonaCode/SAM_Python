#from  Parameters_SAM_tupa import * 


import numpy as np

import cftime

import  matplotlib          as mpl

import  matplotlib.pyplot    as plt

# Python standard library datetime  module
import datetime as dt  

#path of the ncfile
from files_direction import * 

#import  campain_data  as cd
import source.data_own as down

import source.figure_own_2d as fown



def plot2d_im_ctn(exp,days,alt,explabel,explabel2,hours,contour,axis_on,show):

    print('_________________')
    print('Cloud Fraction 2d')
    print('_________________')

    #number of experiment
    nexp= len(exp)

    fig=[]
    
    i=0

    for ex in exp:

        nivel1  = 0.0
        
        nivel2  = alt[i]
        
        #Initial day
        idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 

        idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])
        
        var     = ex.CLD[:,:]*100   #%
        
        fn,ax   = fown.d2_plot_im_ctn(ex,days[i],ex.time,ex.data,var,ex.z[:]/1000.0,contour[i],idi,idf,nivel1,nivel2,explabel[i],explabel2[i],'lower','whbuyl',axis_on[i])
        
        ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

        ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )

        #ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
        
        #plt.ylabel(r'z [km]') 
        
        plt.xlabel(r'Local Time (UTC-4)') 
        
        plt.savefig('%scloudfraction_2d_%s.pdf'%(file_fig,explabel[i]), format='pdf',bbox_inches='tight', dpi=1000)
        plt.savefig('%scloudfraction_2d_%s.png'%(file_fig,explabel[i]), format='png',bbox_inches='tight', dpi=1000)
        
        fig.append(fn)
        
        i=i+1

        if show:
            plt.show()

def plot2d_im_wsup(exp,days,alt,explabel,explabel2,hours,contour,axis_on,show):

    print('_________________')
    print('WSUP ')
    print('_________________')

    #number of experiment
    nexp= len(exp)


    fig=[]
    
    i=0

    for ex in exp:

        nivel1=0.0
        
        nivel2=alt[i]
        
        idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 
        idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])
        
        #var= ex.WSUP[:,:]        
        var= ex.WCLD[:,:]        
        #var= ex.WCOR[:,:]        

        fn,ax=fown.d2_plot_im_ctn(ex,days[i],ex.time,ex.data,var,ex.z[:]/1000.0,contour[i],idi,idf,nivel1,nivel2,explabel[i],explabel2[i],'lower','whbuyl',axis_on[i])

        ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )
        
        ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
        #plt.ylabel(r'z [km]') 
        plt.xlabel(r'Local Time (UTC-4)') 
        
        plt.savefig('%swcloud_2d_%s.pdf'%(file_fig,explabel[i]), format='pdf',bbox_inches='tight', dpi=1000)
        
        fig.append(fn)
        
        i=i+1

        if show:
            plt.show()

def plot2d_im_massflux_diff(exp,days,alt,explabel,explabel2,hours,contour,axis_on,show):

    print('_________________')
    print('MASSflux_diff')
    print('_________________')

    nivel1  = 0.0
    nivel2  = alt[0]
    
    idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 
    idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])
    
    var1     = exp[0].MCUP[:]
    var2     = exp[1].MCUP[:]

    var      = var2-var1
    
    fn,ax=fown.d2_plot_im_ctn(exp[0],days[0],exp[0].time,exp[0].data,var,exp[0].z[:]/1000.0,contour[0],idi,idf,nivel1,nivel2,explabel[0],explabel2[0],'lower','RdBu_r',axis_on[0])

    
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

    ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )

    plt.xlabel(r'Local Time (UTC-4)') 
    
    plt.savefig('%smassflux_2d_%s.pdf'%(file_fig,explabel[0]), format='pdf',bbox_inches='tight', dpi=1000)
    
    if show:
        plt.show()

def plot2d_im_wobs_diff(exp,days,alt,explabel,explabel2,hours,contour,axis_on,show):

    print('_________________')
    print('WOBS_diff')
    print('_________________')

    nivel1  = 0.0
    nivel2  = alt[0]
    
    idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 
    idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])
    
    var1     = exp[0].WOBS[:]*100.0
    var2     = exp[1].WOBS[:]*100.0

    var      = var2-var1
    
    fn,ax=fown.d2_plot_im_ctn(exp[0],days[0],exp[0].time,exp[0].data,var,exp[0].z[:]/1000.0,contour[0],idi,idf,nivel1,nivel2,explabel[0],explabel2[0],'lower','RdBu_r',axis_on[0])

    
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

    ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )

    plt.xlabel(r'Local Time (UTC-4)') 
    
    plt.savefig('%swobs_2d_%s.pdf'%(file_fig,explabel[0]), format='pdf',bbox_inches='tight', dpi=1000)
    
    if show:
        plt.show()

def plot2d_im_relh_diff(exp,days,alt,explabel,explabel2,hours,contour,axis_on,show):

    print('_________________')
    print('RH_diff')
    print('_________________')

    nivel1  = 0.0
    nivel2  = alt[0]
    
    idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 
    idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])
    
    var1     = exp[0].RELH[:]
    var2     = exp[1].RELH[:]

    var      = var2-var1
    
    fn,ax=fown.d2_plot_im_ctn(exp[1],days[1],exp[1].time,exp[1].data,var,exp[1].z[:]/1000.0,contour[0],idi,idf,nivel1,nivel2,explabel[0],explabel2[0],'lower','RdBu_r',axis_on[0])

    
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

    ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )

    plt.xlabel(r'Local Time (UTC-4)') 
    
    plt.savefig('%srelh_2d_%s.pdf'%(file_fig,explabel[0]), format='pdf',bbox_inches='tight', dpi=1000)
    
    if show:
        plt.show()

def plot2d_im_relh(exp,days,alt,explabel,explabel2,hours,contour,axis_on,show):

    print('_________________')
    print('RH')
    print('_________________')

    #number of experiment
    nexp= len(exp)

    fig=[]
    
    i=0

    for ex in exp:

        nivel1  = 0.0
        
        nivel2  = alt[i]
        
        
        idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 
        idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])

        var     = ex.RELH
        
        fn,ax=fown.d2_plot_im_ctn(ex,days[i],ex.time,ex.data,var,ex.z[:]/1000.0,contour[i],idi,idf,nivel1,nivel2,explabel[i],explabel2[i],'lower','RdBu_r',axis_on[i])

        
        ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

        ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )

        
        #plt.ylabel(r'z [km]') 
        
        plt.xlabel(r'Local Time (UTC-4)') 
        
        plt.savefig('%srelh_2d_%s.pdf'%(file_fig,explabel[i]), format='pdf',bbox_inches='tight', dpi=1000)
        
        fig.append(fn)
        
        i=i+1

        if show:
            plt.show()

def plot2d_im_wobs(exp,days,alt,explabel,explabel2,hours,contour,axis_on,show):

    print('_________________')
    print('W_obs')
    print('_________________')

    #number of experiment
    nexp= len(exp)

    fig=[]
    
    i=0

    for ex in exp:

        nivel1  = 0.0
        
        nivel2  = alt[i]
        
        idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 
        idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])
        
        var     = ex.WOBS[:]*100.0  #100to cm/s  #%
        
        fn,ax=fown.d2_plot_im_ctn(ex,days[i],ex.time,ex.data,var,ex.z[:]/1000.0,contour[i],idi,idf,nivel1,nivel2,explabel[i],explabel2[i],'lower','RdBu_r',axis_on[i])

        
        ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

        ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )

        
        #plt.ylabel(r'z [km]') 
        
        plt.xlabel(r'Local Time (UTC-4)') 
        
        plt.savefig('%swobs_2d_%s.pdf'%(file_fig,explabel[i]), format='pdf',bbox_inches='tight', dpi=1000)
        
        fig.append(fn)
        
        i=i+1

        if show:
            plt.show()
def plot2d_im_wsup_down(exp,days,alt,explabel,explabel2,hours,contour,axis_on,show):

    print('_________________')
    print('WSUP ')
    print('_________________')

    #number of experiment
    nexp= len(exp)


    fig=[]
    
    i=0

    for ex in exp:

        nivel1=0.0
        
        nivel2=alt[i]
        
        idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 
        idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])
        
        var= ex.WSDN[:,:]
        
        fn,ax=fown.d2_plot_im_ctn(ex,days[i],ex.time,ex.data,var,ex.z[:]/1000.0,contour[i],idi,idf,nivel1,nivel2,explabel[i],explabel2[i],'lower','whbuyl',axis_on[i])

        ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )
        
        ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
        #plt.ylabel(r'z [km]') 
        plt.xlabel(r'Local Time (UTC-4)') 
        
        plt.savefig('%swdowndraf_2d_%s.pdf'%(file_fig,explabel[i]), format='pdf',bbox_inches='tight', dpi=1000)
        
        fig.append(fn)

        i=i+1

        if show:
            plt.show()
        

def plot2d_im_ql(exp,days,alt,explabel,explabel2,hours,contour,axis_on,show):

    print('_________________')
    print('Liquid Water QC ')
    print('_________________')

    #number of experiment
    nexp= len(exp)


    fig=[]
    
    i=0

    for ex in exp:

        nivel1=0.0
        
        nivel2=alt[i]
        
        idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 
        idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])
        
        var= ex.QC[:,:]
        
        fn,ax=fown.d2_plot_im_ctn(ex,days[i],ex.time,ex.data,var,ex.z[:]/1000.0,contour[i],idi,idf,nivel1,nivel2,explabel[i],explabel2[i],'lower','whbuyl',axis_on[i])

        ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )
        
        ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
        #plt.ylabel(r'z [km]') 
        plt.xlabel(r'Local Time (UTC-4)') 
        
        plt.savefig('%sql_2d_%s.pdf'%(file_fig,explabel[i]), format='pdf',bbox_inches='tight', dpi=1000)
        
        fig.append(fn)
        
        i=i+1

        if show:
            plt.show()

def plot2d_im_mass_flux(exp,days,alt,explabel,explabel2,hours,contour,axis_on,show):

    print('_________________')
    print('Mass Flux')
    print('_________________')

    #number of experiment
    nexp= len(exp)


    fig=[]
    
    i=0

    for ex in exp:

        nivel1=0.0
        nivel2=alt[i]
        
        idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 
        idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])
        
        var= ex.MCUP[:,:]#%
        
        fn,ax=fown.d2_plot_im_ctn(ex,days[i],ex.time,ex.data,var,ex.z[:]/1000.0,contour[i],idi,idf,nivel1,nivel2,explabel[i],explabel2[i],'lower','whbuyl',axis_on[i])

        ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )

        #plt.ylabel(r'z [km]') 
        plt.xlabel(r'Local Time (UTC-4)') 
        
        plt.savefig('%smass_flux_2d_%s.pdf'%(file_fig,explabel[i]), format='pdf',bbox_inches='tight', dpi=1000)

        plt.savefig('%smass_flux_2d_%s.png'%(file_fig,explabel[i]), format='png',bbox_inches='tight', dpi=1000)
        
        fig.append(fn)
        
        i=i+1

        if show:
            plt.show()

def plot2d_media_ctn(exp,days,alt,explabel,hours,contour,axis_on,show):

    print('_________________')
    print('Cloud Fraction 2d')
    print('_____Mean________')

    #wherever day
    i=0

    nivel1=0.0
    nivel2=alt[i]

    var,time,data,lev= media(exp,days)


    idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 
    idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])

    var[:,:]= var[:,:]*100#%

    fn,ax=fown.d2_plot_im_ctn(ex,days[i],time[i],data[i],var,lev[i][:]/1000.0,contour[i][0],contour[i][1],idi,idf,nivel1,nivel2,'lower','whbuyl',axis_on[i])

    ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
    plt.ylabel(r'z [km]') 
    #plt.xlabel(r'$\mathrm{Cloud Fraction}$') 

    plt.savefig('%scloudfraction_6cases_mean.pdf'%(file_fig), format='pdf',bbox_inches='tight', dpi=1000)

    if show:
        plt.show()

def media(exp,days):
    
    clf_d=[]

    time=[]
    lev=[]
    data_p=[]

    k=0


    for ex in exp:

	#run begin 08 and end 19
        idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 
        idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])


        ni,nf   = down.data_n(idi,idf,ex.data[:])

        #number of levels
        nl      =  ex.z[:].shape[0]

        time.append(ex.time[ni:nf])
        data_p.append(ex.data[ni:nf])
        lev.append(ex.z[0:nl])

        #clf_d.append(ex.cld_frac_mpl[ni:nf,0:nl])
        clf_d.append(ex.CLD[ni:nf,0:nl])

        k+=1

    mean =np.mean(clf_d,axis=0)

    return mean,time,data_p,lev  

def get_figsize(columnwidth, wf=0.5, hf=(5.**0.5-1.0)/2.0, ):

      """Parameters:
        - wf [float]:  width fraction in columnwidth units
        - hf [float]:  height fraction in columnwidth units.
                       Set by default to golden ratio.
        - columnwidth [float]: width of the column in latex. Get this from LaTeX
                               using \showthe\columnwidth
      Returns:  [fig_width,fig_height]: that should be given to matplotlib
      """
      fig_width_pt = columnwidth*wf
      inches_per_pt = 1.0/72.27               # Convert pt to inch
      fig_width = fig_width_pt*inches_per_pt  # width in inches
      fig_height = fig_width*hf      # height in inches
      return [fig_width, fig_height]

