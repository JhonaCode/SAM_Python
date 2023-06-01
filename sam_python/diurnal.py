#Python standard library datetime  module

import  numpy               as np

import  datetime            as dt

import  cftime              as cf

import  matplotlib.pyplot   as plt

import  matplotlib          as mpl

from    matplotlib.ticker   import MultipleLocator, FormatStrFormatter

import  sam_python.data_own            as down

import  sam_python.figure_own          as fown

import  sam_python.campain_data        as cd

from    sam_python.plotparameters      import *

from    files_direction     import file_fig 


def color_hours(hour):
    line=[1,0]
    color='k'

    if hour==9:
          #line=[3,2,1,2]
          line=[1,0]
          color='darkcyan'

    elif  hour==10:

          line=[2,2,1,2]
          color='blue'

    elif  hour==11:
          #line=[2, 1]
          line=[1,0]
          color='cyan'

    elif  hour==12:

          line=[3, 1]
          color='green'

    elif  hour==13:

          color='r'

    elif  hour==14:

          color='tab:orange'

    elif  hour==15:

          line=[1,2,1,2]
          color='tab:brown'

    elif  hour==16:

          line=[2,1,1,3]
          color='m'

    elif  hour==17:

          line=[2,1,5,3]
          color='tab:purple'

    elif  hour==18:

          #line=[4,2,1,2]
          line=[1,0]
          color='y'

    elif  hour==19:

          line=[1,2,4,2]
          color='peru'
    
    return line,color

def defaul_values(lim,maxv,minv,alt,maxh,var_to,name,color,explabel2,leg_loc,diurnal,show): 


        lim.append([minv,maxv])         #[0]
        alt.append(maxh)                #[1]
        var_to.append(1)                #[2]
        color.append('red')             #[3]
        explabel2.append(name)            #[4]
        leg_loc.append([(maxv-minv)/4.0+minv,maxh*0.85,True,True]) #[5]
        #leg_loc.append([maxv*0.3,maxh*0.85,True,True]) #[5]
        diurnal.append(True)            #[6]
        show.append(True)               #[7]

        defaul=[lim,alt,var_to,color,explabel2,leg_loc,diurnal,show]


        return defaul


def label_plots(ax,legend,explabel): 

###Text position x
#legend[0]=0.0
###Text position y
#legend[1]=0.0
###Z label
#legend[2]=True
###hours label
#legend[3]=True

    ax.text(legend[0], legend[1], r' %s'%(explabel[1]), fontsize=8, color='black')

    if( legend[2]==True):
        plt.ylabel(r'z [km]') 

    if( legend[3]==True):
    	plt.legend(frameon=False,loc=legend[2])

    return ax


def diurnal_hours(exp,name_ex,exp_var,days,alt=[],lim=[],var_to=[],color=[],explabel2=[],leg_loc=[],diurnal=[],show=[]): 


    for ex in exp:

        print("___________________")
        print("________%s___"%(exp))
        print("___________________")

        #Function to defined the defaul values
        k=0
        for var in exp_var:

            maxh=np.max(ex.z)/1000.0
            maxv=np.max(var)
            minv=np.min(var)

            name=var.name

            defaul=defaul_values(lim,maxv,minv,alt,maxh,var_to,name,color,explabel2,leg_loc,diurnal,show)



            print("___________________")
            print("%s"%(var.long_name))
            print("___________________")

            figs,axis = main_plot_diurnal_new(var[:]*defaul[2][k],ex.data,ex.z,days[k],defaul[1][k],defaul[0][k],defaul[3][k],name_ex[0]+'_'+name,defaul[4][k],defaul[5][k],defaul[6][k])

            #print(defaul )
            if defaul[7][k]:

                plt.show()

            k+=1

    plt.close('all')

    return 


def diurnal_hours_se(exp,days,alt,lim,color,explabel,explabel2,leg_loc,show,diurnal): 

    print("__________")
    print("Static Energy")
    print("__________")

    var1 =[]
    var2 =[]
    var3 =[]
    data=[]
    z=[]

    name='se'

    for ex in exp:

        var1.append(ex.DSE[:])
        var2.append(ex.MSE[:])
        var3.append(ex.SSE[:])
        data.append(ex.data)
        z.append(ex.z)
    
    figs,axis= main_plot_diurnal_3var(var1,var2,var3,data,z,days,alt,lim,color,name,explabel,explabel2,leg_loc,diurnal)

    if show:
        plt.show()

    plt.close('all')

    return 

def diurnal_hours_uv(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 


    print("__________")
    print("U_V"       )
    print("__________")

    var1 =[]
    var2 =[]
    data=[]
    z=[]

    name='u_v'

    for ex in exp:

        var1.append(ex.U[:])
        var2.append(ex.V[:])
        data.append(ex.data)
        z.append(ex.z)
    
    figs,axis = main_plot_diurnal_2var(var1,var2,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

    k=0


    if show:

        plt.show()

    plt.close('all')

    return 


def diurnal_hours_tq(exp,days,alt,lim1,lim2,cor1,cor2,explabel,explabel2,leg_loc,show,diurnal): 


    print("__________"          )
    print("Temperature Humidity")
    print("__________"          )

    var1 =[]
    var2 =[]
    data=[]
    z=[]

    name='tq'

    for ex in exp:

        var1.append(ex.THETA[:])
        var2.append(ex.QT[:])
        data.append(ex.data)
        z.append(ex.z)
    
    figs,axis1,axis2 = main_plot_diurnal_2axis(var1,var2,data,z,days,alt,lim1,lim2,cor1,cor2,name,explabel,explabel2,leg_loc,diurnal)

    if show:

        plt.show()

    plt.close('all')
    return 



def d_time(data,days):

    #Inicial hour
    hi= days[3]    
    #Final hour
    hf= days[7] 

                         #ano	    #me  	#dia	#Hour
    #Initial day
    idi     = dt.datetime(days[0], days[1] ,days[2], days[3]) 
    idf     = dt.datetime(days[4], days[5] ,days[6], days[7])

    #print("Data", idi, ' to ', idf) 
    ni,nf = down.data_n(idi,idf,data)

    return idi, idf,ni, nf,hi,hf


def diurnal_tke_budget(exp,days,alt,hour_step,lim,color,explabel,explabel2,leg_loc,show,diurnal): 


    print("__________")
    print("   TKE    ")
    print("__________")

    
    k=0
    nfig=0

    for ex in exp:

        size_wg = 0.33
        size_hf = 1.50
        if (explabel=='small'):
            plotsize(size_wg,size_hf, 1.0,'diurnal')
        else:
            plotsize(size_wg,size_hf, 0.0,'diurnal')

        #To plot 
        fn  = plt.figure(nfig)
        ax  = plt.axes()

        
        #Data and heigh index for the vectors
        idi,idf,ni,nf,hi,hf   =   d_time(ex.data,days[k][:])

        ##interval hour
        ch=hour_step

        #Falta dividir pelo tempo, derivada temporal no budget
        #var1=ex.TKE[:]  +ex.TKES[:]

        var2=ex.SHEAR[:]#+ex.SHEARS[:]
        var3=ex.BUOYA[:]#+ex.BUOYAS[:]
        var4=ex.ADVTR[:]#+ex.ADVTRS[:]
        var5=ex.PRESSTR[:]
        var6=ex.DISSIP[:]#+ex.DISSIPS[:]

        var1=var2+var3+var4+var5+var6

        #mean diurnal function 
        meanvar1,hour = diurnal_main(ex.data,ex.z[:]/1000.0,var1,idi,idf,k,hi,hf,ch)
        meanvar2,hour = diurnal_main(ex.data,ex.z[:]/1000.0,var2,idi,idf,k,hi,hf,ch)
        meanvar3,hour = diurnal_main(ex.data,ex.z[:]/1000.0,var3,idi,idf,k,hi,hf,ch)
        meanvar4,hour = diurnal_main(ex.data,ex.z[:]/1000.0,var4,idi,idf,k,hi,hf,ch)
        meanvar5,hour = diurnal_main(ex.data,ex.z[:]/1000.0,var5,idi,idf,k,hi,hf,ch)
        meanvar6,hour = diurnal_main(ex.data,ex.z[:]/1000.0,var6,idi,idf,k,hi,hf,ch)


        fn,ax=fown.splot_own_label(nfig,var2[ni:nf,:],ex.z[:]/1000.0,'blue'   , 'S'  )
        fn,ax=fown.splot_own_label(nfig,var3[ni:nf,:],ex.z[:]/1000.0,'red'    , 'B'  )
        fn,ax=fown.splot_own_label(nfig,var4[ni:nf,:],ex.z[:]/1000.0,'magenta', 'P'  )
        fn,ax=fown.splot_own_label(nfig,var5[ni:nf,:],ex.z[:]/1000.0,'cyan'   , 'T'  )
        fn,ax=fown.splot_own_label(nfig,var6[ni:nf,:],ex.z[:]/1000.0,'green'  , 'D'  )

        if diurnal==True:

            jj=0

            for j in range(0,hf-hi+ch,ch):
    
                line,col =color_hours(hour[j])

                plt.plot(meanvar2[j,:] ,ex.z[:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.0,alpha=1.0,dashes=line)
                plt.plot(meanvar3[j,:] ,ex.z[:]/1000.0,color=col,linewidth=1.0,alpha=1.0,dashes=line)
                plt.plot(meanvar4[j,:] ,ex.z[:]/1000.0,color=col,linewidth=1.0,alpha=1.0,dashes=line)
                plt.plot(meanvar5[j,:] ,ex.z[:]/1000.0,color=col,linewidth=1.0,alpha=1.0,dashes=line)

                jj=jj+1



        plt.axis([lim[k][0],lim[k][1],0,alt[k]])

        ax=label_plots(ax,leg_loc[k],[explabel[k],explabel2[k]])

        plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
        plt.legend(frameon=False)
        plt.ylabel(r'z[km]') 

        plt.xlabel(r'TKE BUDGET $\mathrm{[m^{2}s^{-3}]}$') 

        plt.savefig('%sdiurnal_tke_budget_%s.pdf'%(file_fig,explabel[k]),bbox_inches='tight',dpi=1000, format='pdf')

        nfig=nfig+1

        k=k+1

    if show:
        plt.show()

    plt.close('all')

    return fig 

def main_plot_deep(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal):

    f=open('cloud_deep_%s.dat'%(explabel[0][0:3]),'w+')
    f.write('Case\t\ttop\t\tbase\t\tDeep\n')


    k=0
    for vartoplot in var:

        #Initial day
        idi     = dt.datetime(days[k][0], days[k][1] ,days[k][2], days[k][3],00) 
        idf     = dt.datetime(days[k][4], days[k][5] ,days[k][6], days[k][7],00)
        #initial hour
        hi=days[k][3]
        #final hour
        hf=days[k][7]

        ni,nf= down.data_n(idi,idf,data[k][:])


        mean=   np.mean(vartoplot[ni:nf,:], axis=0)

        band=0
        for nn in range(0,len(z[k][:])):

            if ( mean[nn]>0.0010 and band==0):
                band=1
                base=z[k][nn]/1000.0
                print(base)
            if ( mean[nn]<0.0010 and band==1):
            
                top=z[k][nn]/1000.0
                print(top)
                break
        deep=top-base

        f.write('%s\t%f\t%f\t%f\n'%(explabel[k],top,base,deep))
        print('DEEP',top-base,explabel[k])
        k=k+1

    f.close()


    return 


def main_plot_diurnal_new(vartoplot,data,z,days,alt,lim,color,name,explabel2,leg_loc,diurnal):

    #Initial day
    idi     = dt.datetime(days[0], days[1] ,days[2], days[3]) 
    idf     = dt.datetime(days[4], days[5] ,days[6], days[7])

    #initial hour
    hi=days[3]
    #final hour
    hf=days[7]

    ni,nf= down.data_n(idi,idf,data[:])

    ##interval hour
    ch      = 1

    #mean diurnal function 
    meanvar,hour = diurnal_main(data,z,vartoplot,idi,idf,hi,hf,ch)

    size_wg = 0.28
    size_wg = 0.33
    size_hf = 1.50

    plotsize(size_wg,size_hf, 0.0,'diurnal')

    #To plot 
    fig  = plt.figure()
    ax   = plt.axes()

    jj=0

    if diurnal:

        for j in range(0,hf-hi+ch,ch):
    
            line,col =color_hours(hour[j])

            plt.plot(meanvar[j,:] ,z[:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.0,alpha=1.0,dashes=line)
    
            jj=jj+1


    if( name=='buoyancyflux'):

        ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
        ax.xaxis.get_offset_text().set_visible(False)


    elif( name=='relh' or name=='cld' or name=='qtflux'or name=='thetalflux'):
        xFormatter = FormatStrFormatter('%.f')
        ax.xaxis.set_major_formatter(xFormatter)


    label=['mean',False]

    fn,ax=fown.splot_own(fig,ax,vartoplot[ni:nf,:],z[:]/1000.0,data,color,label)

    plt.axis([lim[0],lim[1],0,alt])

    ax=label_plots(ax,leg_loc,[name,explabel2])

    label="%s"%(name)

    plt.savefig('%sdiurnal_%s.pdf'%(file_fig,label),bbox_inches='tight',dpi=1000, format='pdf')

    return fig,ax

def main_plot_diurnal_2var(var1,var2,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal):

    fig =[]
    axis=[]

    nfig=0
    k   =0

    for vartoplot in var1:

        idi     = dt.datetime(days[k][0], days[k][1] ,days[k][2], days[k][3]) 
        idf     = dt.datetime(days[k][4], days[k][5] ,days[k][6], days[k][7])

        hi=days[k][3]
        hf=days[k][7]

        ni,nf= down.data_n(idi,idf,data[k][:])

        ##interval hour
        ch      = 1

        #mean diurnal function 
        meanvar1,hour = diurnal_main(data[k],z[k],var1[k],idi,idf,k,hi,hf,ch)
        meanvar2,hour = diurnal_main(data[k],z[k],var2[k],idi,idf,k,hi,hf,ch)

        size_wg=0.33
        size_hf=1.5

        plotsize(size_wg,size_hf, 0.0,'diurnal')

        fn  = plt.figure(nfig)
        ax  = plt.axes()

        jj=0

        if diurnal:
            for j in range(0,hf-hi+ch,ch):
    
                line,col =color_hours(hour[j])

                plt.plot(meanvar1[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.0,alpha=1.0,dashes=line)
    
                plt.plot(meanvar2[j,:] ,z[k][:]/1000.0,color=col,linewidth=1.0,alpha=1.0,dashes=line)

                jj=jj+1
    

        #fn,ax=fown.splot_own(nfig,var1[k][ni:nf,:],z[k][:]/1000.0,color[k])
        #fn,ax=fown.splot_own(nfig,var2[k][ni:nf,:],z[k][:]/1000.0,color[k])
        plt.axis([lim[k][0],lim[k][1],0,alt[k]])

        ax.text(lim[k][0], 0.1, r' %s'%(explabel2[k]), fontsize=8, color='black')

        label="%s_%s"%(name,explabel[k])

        if(name=='u_v'):
            ax.text(lim[k][0]+0.5, 2.5, r'u $\rightarrow$ ')
            ax.text(lim[k][1]-4, 2.5, r'$\leftarrow$ v')

        plt.savefig('%sdiurnal_%s.pdf'%(file_fig,label),bbox_inches='tight',dpi=1000, format='pdf')

        k=k+1
        nfig=nfig+1
        fig.append(fn)
        axis.append(ax)


    return fig,axis 

def main_plot_diurnal_2axis(var1,var2,data,z,days,alt,lim1,lim2,cor1,cor2,name,explabel,explabel2,leg_loc,diurnal):

    fig=[]
    axis1=[]
    axis2=[]

    nfig=0

    k=0

    for vartoplot in var1:

        #Initial day
        idi     = dt.datetime(days[k][0], days[k][1] ,days[k][2], days[k][3]) 
        idf     = dt.datetime(days[k][4], days[k][5] ,days[k][6], days[k][7])
        #initial hour
        hi=days[k][3]
        #final hour
        hf=days[k][7]

        ni,nf= down.data_n(idi,idf,data[k][:])

        ##interval hour
        ch      = 1

        #mean diurnal function 
        meanvar1,hour = diurnal_main(data[k],z[k],vartoplot,idi,idf,k,hi,hf,ch)
        meanvar2,hour = diurnal_main(data[k],z[k],var2[k],idi,idf,k,hi,hf,ch)

        size_wg = 0.28
        size_wg = 0.33
        size_hf = 1.50

        if (explabel=='small'):

            plotsize(size_wg,size_hf, 1.0,'diurnal')

        else:

            plotsize(size_wg,size_hf, 0.0,'diurnal')

        #To plot 
        fn  = plt.figure(nfig)
        ax1 = plt.axes()
        ax2 = ax1.twiny() 

        jj=0

        label=['mean',False]

        if diurnal:

            for j in range(0,hf-hi+ch,ch):
    
                line,col =color_hours(hour[j])

                ax1.plot(meanvar1[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.5,alpha=1.0,dashes=line)
    
                ax2.plot(meanvar2[j,:] ,z[k][:]/1000.0,color=col,linewidth=1.0,alpha=1.0,dashes=line)

                jj=jj+1

        fn,ax=fown.splot_own(fig,ax1,vartoplot[ni:nf,:],z[k][:]/1000.0,data[k],cor1[k],label)

        fn,ax=fown.splot_own(fig,ax2,var2[k][ni:nf,:],z[k][:]/1000.0,data[k],cor2[k],label)

        ax1.axis([lim1[k][0],lim1[k][1],0,alt[k]])
        ax2.axis([lim2[k][0],lim2[k][1],0,alt[k]])

        ax1=label_plots(ax1,leg_loc[k],[explabel[k],explabel2[k]])

        label="%s_%s"%(name,explabel[k])

        plt.savefig('%sdiurnal_%s.pdf'%(file_fig,label),bbox_inches='tight', format='pdf', dpi=1000)

        fig.append(fn)

        axis1.append(ax1)
        axis2.append(ax2)

        k=k+1

        nfig=nfig+1



    return fig,axis1,axis2 

def main_plot_diurnal_3var(var1,var2,var3,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal):

    fig=[]

    nfig=0

    k=0
    for vartoplot in var1:

        #Initial day
        idi     = dt.datetime(days[k][0], days[k][1] ,days[k][2], days[k][3]) 
        idf     = dt.datetime(days[k][4], days[k][5] ,days[k][6], days[k][7])
        #initial hour
        hi=days[k][3]
        #final hour
        hf=days[k][7]

        ni,nf= down.data_n(idi,idf,data[k][:])

        ##interval hour
        ch      = 1

        #mean diurnal function 
        meanvar1,hour = diurnal_main(data[k],z[k],vartoplot,idi,idf,k,hi,hf,ch)
        meanvar2,hour = diurnal_main(data[k],z[k],var2[k],idi,idf,k,hi,hf,ch)
        meanvar3,hour = diurnal_main(data[k],z[k],var3[k],idi,idf,k,hi,hf,ch)

        #To plot 
        fn  = plt.figure(nfig)
        ax  = plt.axes()

        jj=0

        if diurnal:
            for j in range(0,hf-hi+ch,ch):
    
                line,col =color_hours(hour[j])

                plt.plot(meanvar1[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.5,alpha=1.0,dashes=line)
    
                plt.plot(meanvar2[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.5,alpha=1.0,dashes=line)

                plt.plot(meanvar3[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.5,alpha=1.0,dashes=line)

                jj=jj+1
    

        fn,ax=fown.splot_own(nfig,vartoplot[ni:nf,:],z[k][:]/1000.0,color[k])
        fn,ax=fown.splot_own(nfig,var2[k][ni:nf,:],z[k][:]/1000.0,color[k])
        fn,ax=fown.splot_own(nfig,var3[k][ni:nf,:],z[k][:]/1000.0,color[k])
        plt.axis([lim[k][0],lim[k][1],0,alt[k]])

        ax=label_plots(ax,[lim[k][0],alt[k]],[explabel[k],explabel2[k]])
        fig.append(fn)


        label="%s_%s"%(name,explabel[k])

        plt.savefig('%sdiurnal_%s.pdf'%(file_fig,label),bbox_inches='tight', format='pdf', dpi=1000)

        k=k+1

        nfig=nfig+1


    return fig,ax 

def diurnal_main(data,z,var,idi,idf,hi,hf,ch): 

    ni,nf   = down.data_n(idi,idf,data)

    #number of levels
    nl      = z.shape[0]

    #Lengh of the time array to search
    ndtp        =   len(data) 

    #Hour array
    #+ch to reach the final hour in the loop
    hour    = np.zeros(hf-hi+ch)

    #Sum variable to the mean 
    varsum  = np.zeros([hf-hi+ch,nl])

    meanvar = np.zeros([hf-hi+ch,nl])

    #var     = np.zeros([nl])
    meanvar = np.zeros([hf-hi+ch,nl])

    #Number of  time thar variable was sum 
    cont    = np.zeros(hf-hi+ch)
    

    #nf+1 because for does arrive to n+1, but  n its necessary
    for i in range(ni,nf+1):
    
        for j in range(0,hf-hi+ch,ch):

            if int(data[i].hour)==j+hi: 

                hour[j]     =   j+hi

                varsum[j,:] =   varsum[j,:]+var[i,:]

                cont[j]     =   cont[j]+1


    for j in range(0,hf-hi+ch,ch):
        
        meanvar[j,:] = varsum[j,:]/cont[j]


    return meanvar,hour



def diurnal_function(time,variable): 


    #Number of hour
    ndh     = 24
    #Hour array
    hour    = np.zeros(ndh)
    #Sum variable to the mean 
    varsum   = np.zeros(ndh)
    #Number of  time thar variable was sum 
    cont    = np.zeros(ndh)

    
    #Lengh of the time array to search
    ndtp    = len(time) 
    
    for i in range(0,ndtp):
    
        for j in range(0,ndh):
    
            if int(time[i].hour)==j : 
    
                hour[j]=j
                varsum[j]=varsum[j]+variable[i]
                cont[j]=cont[j]+1

   
    meanvar = varsum/cont

    return meanvar,hour 

def diurnal_function_exp(time,variable): 

#print timed.datetime.hour

    #Number of hour
    ndh     = 24
#Hour array
    hour    = np.zeros(ndh)
    #Sum variable to the mean 
    varsum   = np.zeros(ndh)
    #Number of  time thar variable was sum 
    cont    = np.zeros(ndh)
    
    #Lengh of the time array to search
    ndtp    = len(time) 

    #defaul time
    timebefore=dt.datetime(2000,1,1,0,0)
    
    for i in range(0,ndtp):
    
        for j in range(0,ndh):
    
            #to fund in an hour 
            if int(time[i].hour)==j: 

                hour[j]=j

                #to found in the half of an hour on time  
                if int(time[i].minute)<30: 

                    #to no stay in the same hour 
                    if int(time[i].hour)!=timebefore.hour: 

                        varsum[j]=varsum[j]+variable[i]
                        cont[j]=cont[j]+1

                        #print time[i]
                        timebefore=time[i] 

                        continue

                
    
    meanvar = varsum/cont


    return meanvar,hour 

def get_figsize(columnwidth, wf=0.24, hf=(5.**0.5-1.0)/2.0, ):

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
