#from  Parameters_SAM_tupa import * 


import  numpy as np

import  cftime

import  matplotlib          as mpl

import  matplotlib.pyplot   as plt

# Python standard library datetime  module
import  datetime as dt  

#path of the ncfile
from     files_direction import * 

#import  campain_data  as cd
import   sam_python.data_own       as down

import   sam_python.figure_own_2d  as fown


#def defaul_values(lim,maxv,minv,alt,maxh,var_to,name,color,explabel,leg_loc,diurnal,show): 

def default_values(ex,var,lim,alt,var_to,color,explabel,axis_on,show): 

        maxh  = np.max(ex.z[:]/1000.0)
        minv  = np.min(var)
        maxv  = np.max(var)
        name  = ex.name

        lim.append([minv,maxv,21])      #[0]
        alt.append(maxh)                #[1]
        var_to.append(1.0)              #[2]
        color.append('RdBu_r')          #[3]
        explabel.append(name)           #[4]
        axis_on.append((True,False,False,0.35,0.00))##[5]
        show.append(True)               #[6]

        #defaul=[lim,alt,var_to,color,explabel2,leg_loc,diurnal,show]
        default=[lim,alt,var_to,color,explabel,axis_on,show]


        return default


def plot2d_contour(ex,contour=[],alt=[],explabel=[],color=[],var_to=[],axis_on=[],show=[]):


    print('_________________')
    print('________%s_______'%(ex.name))
    print('_________________')

    exp_var=ex.var_to_plot
    days=ex.datei+ex.datef

    i=0

    for vtex in exp_var:

        var=getattr(ex, vtex)
        
        maxh  = np.max(ex.z[:]/1000.0)
        minv  = np.min(var)
        maxv  = np.max(var)

        name  = var.name

        defaul= default_values(ex,var,contour,alt,var_to,color,explabel,axis_on,show)

        print('')
        print('_________________')
        print("_______%s________"%(var.long_name) )
        print('_________________')

        days    = ex.datei+ex.datef

        idi     = dt.datetime(days[0], days[1] ,days[2], days[3]) 
        idf     = dt.datetime(days[4], days[5] ,days[6], days[7])
            
        #Limits of time date
        ni,nf= down.data_n(idi,idf,ex.data[:])

        # To found the maximum date, even 
        # that required date not exists
        if nf==0:

            nf=data.shape[0]-1

        li,lf= down.level_n(0.0,defaul[1][i],ex.z[:]/1000.0)

        #To scale de var
        var=var[:]*defaul[2][i]

        fn,ax   = fown.d2_plot_ctn(ex.data,ex.z[:]/1000.0,var,contour[i],ni,nf,li,lf,explabel[i],'lower',defaul[3][i])
        
        ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

        ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )

        #ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
        
        plt.ylabel(r'z [km]') 
        plt.xlabel(r'Local Time (UTC-4)') 

        plt.savefig('%s%s_2d_%s.pdf'%(file_fig,name,ex.name), format='pdf',bbox_inches='tight', dpi=1000)
        

        #print(defaul )
        if defaul[5][i]:

            plt.show()

        i+=1


    plt.close('all')

    return 

def plot2d_im_diff(ex1,ex2,variables,days=[],alt=[],color=[],explabel=[],var_to=[],contour=[],axis_on=[],show=[]):

    print("___________________")
    print("Difference %s-%s   "%(ex2.name,ex1.name))
    print("___________________")


    #Experimento base 
    ex=ex2

    j=0
    for var in variables:

        print("____Variable_______")
        print("       %s          "%(var))
        print("___________________")

        nivel1  = 0.0
        nivel2  = alt[0]

        
        if days:

            idi     = dt.datetime(days[j][0][0], days[j][0][1] ,days[j][0][2], days[j][0][3],5,0) 
            idf     = dt.datetime(days[j][1][0], days[j][1][1] ,days[j][1][2], days[j][1][3],5,0)

            #print(idi)

            h1i=days[j][0][3]
            h2i=days[j][1][3]

            n1i,n1f= down.data_n(idi,idf,ex1.date[:])
            n2i,n2f= down.data_n(idi,idf,ex2.date[:])

            if n1f-n1i!=n2f-n2i:

                print("The period os the date must be the same, with the same number os points. Use interpolation function to others cases ")
                exit()

        else:
            #initial hour
            h1i=ex1.datei.hour
            #final hour
            h1f=ex1.datef.hour

            n1i,n1f= down.data_n(ex1.datei,ex1.datef,ex1.date[:])


            h2i=ex2.datei.hour
            #final hour
            h2f=ex2.datef.hour
            n2i,n2f= down.data_n(ex2.datei,ex2.datef,ex2.date[:])

            n1i=n1i-1
            n1f=n1f+1
            n2i=n2i-1
            n2f=n2f+1



        var1     = ex1.nc_f[var][n1i:n1f,:]
        var2     = ex2.nc_f[var][n2i:n2f,:]

        diff     = var2-var1
        #mean     = (var2+var1)/2.0
        #dp       = np.sqrt(0.5*((var1-mean)**2+(var2-mean)**2))
        #diff     = (var2-var1)/dp

        default= default_values(ex,diff,contour,alt,var_to,color,explabel,axis_on,show)

        li,lf= down.level_n(0.0,default[1][j],ex.z[:]/1000.0)

        #To scale de var
        diff=diff[:,li:lf]*default[2][j]
        date=ex.date[n2i:n2f]
        z=ex.z[li:lf]/1000.0

        #fn,ax   = fown.d2_plot_ctn_diff(date,z,diff,contour[j],explabel[j],'lower',defaul[3][j])

        #defaul=[lim,alt,var_to,color,explabel,axin_on,show]

        fn,ax=fown.d2_plot_im_diff(ex,date,z,diff,default[0][j],default[4][j],'lower',default[3][j],default[5][j])
        
        #ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

        ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )

        plt.xlabel(r'Hours LT (UTC-4)') 

        plt.savefig('%s/diff_%s_2d_%s.pdf'%(file_fig,var,ex1.name+'_'+ex2.name), format='pdf',bbox_inches='tight', dpi=200)


        if default[6][j]:
            plt.show()

        plt.close()

        j+=1

    return
        


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

