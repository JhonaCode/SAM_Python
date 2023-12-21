import  numpy as np

import  matplotlib.pyplot as plt

#Color map
from    matplotlib.colors import LinearSegmentedColormap

#To work with date in plots 
import  matplotlib.dates as mdates

import  matplotlib as mpl

from datetime import datetime, timedelta

import  sam_python.data_own as down

import  sam_python.plotparameters as pn 

#Filter the function, more smothy
from scipy.signal import lfilter

import scipy.ndimage as ndimage


# To change the plot parameter 
#from   sam_python  import  plotparameters_new as pn

#Color map
#########
#cmap = LinearSegmentedColormap.from_list('mycmap', ['skyblue','blue','navy','steelblue','lightskyblue','white'])
cmap = LinearSegmentedColormap.from_list('mycmap', ['white','lightblue','skyblue','RoyalBlue','blue','darkblue'])
cmap3 = LinearSegmentedColormap.from_list('mycmap', ['white','silver','blue','green','yellow'], N=256, gamma=0.5)
cmap4 = LinearSegmentedColormap.from_list('mycmap', ['white','grey','lightblue','blue','green','yellow'], N=256, gamma=1.0)

def d2_plot_im_diff(ex,time,z,var,contour,label,origin,colors,axis_on):

    #Data to plot 
    #used user parameter to plot(plotparameter.py
    #mpl.rcParams.update(params_2d)

    wf=axis_on[4]
    hf=1.0
    cmmais=axis_on[5]

    #plot size of the figures
    #cmmais are the cm to put the cbbar  without modified the size of the fig 
    pn.plotsize(wf,hf,cmmais,'2d')

    ################################3
    fig = plt.figure()
    ###New axis
    ax  = plt.axes()

    sx= time.shape[0]
    sy= z.shape[0]
    
    x=np.zeros(sx)
    y=np.zeros(sy)
    MF=np.zeros((sx,sy))
    
    # with the data and no time
    x       =   time[:]
    y       =   z[:]
    #Variable to plot
    MF      =   var[:,:]


    if colors=='cloud':
        colors=cmap

    if colors=='whbuyl':
        colors=cmap3

    X,Y= np.meshgrid(x,y)

    levels= np.linspace(contour[0],contour[1],contour[2],endpoint=True)

    Z = ndimage.gaussian_filter(MF.T, sigma=1.0, order=0)


    #CU=ax.contourf(X,Y,MF.T,levels=levels, interpolation='bilinear',origin='lower',cmap=colors,aspect='auto',extend='both');
    CU=ax.contourf(X,Y,Z,levels=levels,origin='lower',cmap=colors);


    #CU=ax.imshow(MF.T, interpolation='bilinear',origin='lower',cmap=colors,aspect='auto');

    # Set all level lines to black
    #line_colors = ['black' for l in CU.levels]
    line_colors = ['darkgrey' for l in CU.levels]

    #Contour plot 
    CS=plt.contour(X,Y,Z,levels=levels[1:len(levels):2],colors=line_colors,linewidths=0.1 );


    #plot_bar
    if(axis_on[3]):

        fig,ax=base_top_cloud(fig,ax,ex)

    #cbarlabels = np.linspace(contour[0],contour[1]+contour[0],contour[2],endpoint=True)
    #cbarlabels=cbarlabels[0::]-contour[0]
    #print(cbarlabels)
    #exit()

    #plot_bar
    if(axis_on[0]):

        #CB = fig.colorbar(CU, shrink=1.0, extend='both')
        CB = fig.colorbar(CU, shrink=1.0, extend='neither')

        if(contour[0]>contour[1]):

            kk= np.linspace(contour[0],0,11,endpoint=True,)
            cbarlabels=kk

        elif(contour[0]<0):

            cbarlabels = np.linspace(contour[0],contour[1] ,contour[2],endpoint=True)
            #cbarlabels=cbarlabels[1::]-contour[0]
            CB.set_ticks(cbarlabels[0::4])
            #print(cbarlabels)
            #exit()

        else:
            cbarlabels = np.linspace(contour[0],contour[1]+contour[0],contour[2],endpoint=True)
            cbarlabels=cbarlabels[1::]-contour[0]
            CB.set_ticks(cbarlabels[1::4])
            print(cbarlabels)


        #CB.set_ticks(cbarlabels[1::4])
        CB.ax.set_title(r'%s'%contour[3])


    ax.xaxis_date()

    date_form = mdates.DateFormatter("%H" )
    ax.xaxis.set_major_formatter(date_form)

    #ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
    #loc=mpl.ticker.MultipleLocator(0.5)
    #ax.yaxis.set_major_locator(loc)

    locatormax = mdates.HourLocator(interval=2)
    locatormin = mdates.HourLocator(interval=1)
    ax.xaxis.set_minor_locator(locatormin)
    ax.xaxis.set_major_locator(locatormax)

    ax.set_xlim(time[0],time[len(time)-1])
    ax.set_ylim([z[0],z[len(z)-1]])
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

    ax.text(time[0+1], z[len(z)-1]-0.5, r' %s'%(label), fontsize=7, color='black')


    return fig,ax    

def d2_plot_ctn(time,z,var,contour,ni,nf,nv1,nv2,label,origin,colors):

    #Data to plot 
    #used user parameter to plot(plotparameter.py
    #mpl.rcParams.update(params_2d)

    wf=0.4
    hf=0.7
    cmmais=0.0

    #plot size of the figures
    #cmmais are the cm to put the cbbar  without modified the size of the fig 
    pn.plotsize(wf,hf,cmmais,'2d')

    ################################3
    fig = plt.figure()
    ###New axis
    ax  = plt.axes()

    sx= time.shape[0]
    sy= z.shape[0]
    
    x=np.zeros(sx)
    y=np.zeros(sy)
    MF=np.zeros((sx,sy))
    
    # with the data and no time
    x       =   time[:]
    y       =   z[:]
    #Variable to plot
    MF      =   var[:,:]


    if colors=='cloud':
        colors=cmap

    if colors=='whbuyl':
        colors=cmap3

    X,Y= np.meshgrid(x,y)

    levels= np.linspace(contour[0],contour[1],contour[2])

    CU=ax.contourf(X,Y,MF.T,levels=levels, interpolation='bilinear',origin='lower',cmap=colors,aspect='auto');

    # Set all level lines to black
    line_colors = ['black' for l in CU.levels]

    #Contour plot 
    CS=plt.contour(X,Y,MF.T,levels=levels[::10],colors=line_colors,linewidths=0.1);

    ax.xaxis_date()
    date_form = mdates.DateFormatter("%H" )
    ax.xaxis.set_major_formatter(date_form)
    ax.set_xlim(time[ni],time[nf])
    ax.set_ylim([z[nv1],z[nv2]])
    ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))


    ax.text(time[ni+1], z[nv2]-0.5, r' %s'%(label), fontsize=7, color='black')


    return fig,ax    

def base_top_cloud(fig,ax,ex):

    size= ex.date.shape[0]
    tam = ex.MCUP.shape[0]

    #max heigh points
    #ex: resolution (50m)*30
    maxl=30

    ctop  =[]
    ctop2 =[]
    cbase =[]
    cbase2=[]
    pblh  =[]

    for i in range(0,tam):

        index1  =  np.argmin(ex.TVFLUX[i][0:maxl])
        indexc  =  np.argmax(   ex.CLD[i][0:maxl])

        #for j in range(1,10):
        for j in range(1,5):

            index2=index1+j

            if ex.TVFLUX[i][index2]>0 and index1>3:

                indexmin=index2

                break

            else:
                    indexmin=index1

        for i1 in range(0,70):

             index3=indexmin+i1

             if ex.QC[i][index3]<0.001 :

                 indexmax=index3

                 break
        #for i2 in range(0,70):

        #         index4=indexmin+i1

        #         if ex.CLD[i][index4]<0.001 :

        #             indexmax2=index4

        #             break

        #for i1 in range(0,70):

        #    index3=indexmin+i1

        #    if ex.CLD[i][index3]<0.0005:

        #        indexmax=index3

        #        break

        ##for i1 in range(0,70):

        ##    index3=indexmin+i1

        ##    if ex.MCUP[i][index3]<0.001:

        ##        indexmax=index3

        ##        break


        pblh.append(ex.z[index1]/1000.0)
        cbase.append(ex.z[indexmin]/1000.0)
        cbase2.append(ex.z[indexc]/1000.0)
        ctop.append(ex.z[indexmax]/1000.0)

    step=1
    
    #Limits of time date
    idi2     = datetime(ex.datei.year,ex.datei.month,ex.datei.day,10)#dt.datetime(2014, days[2] ,days[0], 10)
    idf2     = datetime(ex.datef.year,ex.datef.month,ex.datef.day,18)#dt.datetime(2014, days[2] ,days[0], 10)
    #idf2     = ex.datef#dt.datetime(2014, days[3] ,days[0], 18)

    ni2,nf2= down.data_n(idi2,idf2,ex.date[:])


    n = 3#nf2-ni2  # the larger n is, the smoother curve will be
    b = [1.0 / n] * n
    a = 1

    text1='LFC'
    text2='$\mathrm{Z_i}$'
    text3='$\mathrm{h_{top}}$'
    text4='$\mathrm{h_{base}}$'

    cbasef = lfilter(b, a, cbase)

    pblhf = lfilter(b, a, pblh)

    ctopf = lfilter(b, a, ctop)

    ax.plot( ex.date[ni2:nf2:step]     , cbasef[ni2:nf2:step] ,color='indigo' ,dashes=[2,1]  ,linewidth=1.0,alpha=1.0,marker='')

    ax.plot( ex.date[ni2:nf2:step]     , pblhf[ni2:nf2:step]  ,color='black'     ,linewidth=2.0,alpha=1.0,marker='')

    ax.plot( ex.date[ni2:nf2:step]     , ctopf[ni2:nf2:step]  ,color='grey' ,  dashes=[2,1]  ,linewidth=1.0,alpha=1.0,marker='')

    ax.plot( ex.date[ni2:nf2:step]     , cbase2[ni2:nf2:step]  ,color='red' ,  dashes=[2,1]  ,linewidth=1.0,alpha=1.0,marker='')

    idtex0    = idf2-timedelta(hours=8, minutes=0)#dt.datetime(2014, days[2] ,days[0], 17)
    idtex1    = idf2-timedelta(hours=3, minutes=0)#dt.datetime(2014, days[2] ,days[0], 18)
    idtex2    = idf2-timedelta(hours=0, minutes=0)#dt.datetime(2014, days[2] ,days[0], 17)
    idtex3    = idf2-timedelta(hours=1, minutes=0)#dt.datetime(2014, days[2] ,days[0], 17)

    ytex,ytex2= down.data_n(idtex1,idtex2,ex.date[:])

    ax.text(idtex2,cbasef[ytex]+0.1 , r' %s'%(text1), fontsize=7, color='indigo')
    ax.text(idtex1,pblhf[ytex] -0.2 , r' %s'%(text2), fontsize=7, color='black')
    ax.text(idtex0, pblhf[ytex]-0.2 , r' %s'%(text4), fontsize=7, color='red')

    if ex.name=='m_w_l' or  ex.name=='large':
        ax.text(idtex3,ctopf[ytex2]-0.4 , r' %s'%(text3), fontsize=7, color='black')
    else :
        ax.text(idtex3,ctopf[ytex2]+0.1 , r' %s'%(text3), fontsize=7, color='black')

    return fig,ax


def d2_plot_im_ctn(ex,days,time,data,var,z,contour,idi,idf,nv1,nv2,label1,label2,origin,colors,axis_on):

    #used user parameter to plot(plotparameter.py
    #mpl.rcParams.update(params_2d)

    wf=axis_on[3]
    hf=1.0

    #cmmais=0.0
    #plot size of the figures
    #cmmais are the cm to put the cbbar  without modified the size of the fig
    plotsize(wf,hf,axis_on[4],'2d')

    ################################3
    fig = plt.figure()
    ###New axis
    ax  = plt.axes()

    #Limits of time date
    ni,nf= down.data_n(idi,idf,data[:])

    # To found the maximum date, even
    # that required date not exists
    if nf==0:

        nf=data.shape[0]-1

    #Limits of high date
    li,lf= down.level_n(nv1,nv2,z[:])


    sx= data.shape[0]
    sy= z.shape[0]

    x=np.zeros(sx)
    y=np.zeros(sy)

    MF=np.zeros((sx,sy))

    #THe only way to time to be reconize by the imshow and contour is
    # with the data and no time
    x       =   data[:]
    y       =      z[:]

    #Variable to plot
    MF      =   var[:,:]


    if colors=='cloud':
        colors=cmap

    if colors=='whbuyl':
        colors=cmap3

    X,Y= np.meshgrid(x,y)

    def calculate_aspect(shape, extent):

        dx = (extent[1] - extent[0]) / float(shape[1])
        dy = (extent[3] - extent[2]) / float(shape[0])

        return dx / dy


    # Levels to plot, in number.

    levels= np.linspace(contour[0],contour[1],contour[2],endpoint=True)

    CU=ax.contourf(X,Y,MF.T,levels=levels, interpolation='bilinear',origin='lower',cmap=colors,aspect='auto');

    # Set all level lines to black
    #line_colors = ['white' for l in CU.levels]
    #line_colors = ['lightgrey' for l in CU.levels]
    #line_colors[0]='white'
    line_colors = ['darkgrey' for l in CU.levels]

    CS=plt.contour(X,Y,MF.T,levels=levels[1:len(levels):2],colors=line_colors,linewidths=0.1);

    #plot_cloud
    if(axis_on[0]):

        fig,ax=base_top_cloud(fig,ax,ex)

    #plot_bar
    if(axis_on[1]):
        plt.ylabel(r'z [km]')

    ax.xaxis_date()

    date_form = mdates.DateFormatter("%H" )
    ax.xaxis.set_major_formatter(date_form)

    #ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
    #loc=mpl.ticker.MultipleLocator(0.5)
    #ax.yaxis.set_major_locator(loc)

    locatormax = mdates.HourLocator(interval=2)
    locatormin = mdates.HourLocator(interval=1)
    ax.xaxis.set_minor_locator(locatormin)
    ax.xaxis.set_major_locator(locatormax)

    ax.set_ylim([nv1,nv2])
    ax.set_xlim(data[ni],data[nf])

    #plt.axis( [data[ni],data[nf],nv1,nv2])

    ax.text(data[ni+1] , nv2-0.5, r' %s'%(label2), fontsize=7, color='black')
    #ax.text(data[ni+1] , nv2-0.5, r' %s'%(label2[0:3]), fontsize=9, color='black')
    #ax.text(data[ni+10], nv2-0.5, r' %s'%(label2[3:17]), fontsize=7, color='black')

    #plt.clim(contour[0], contour[1])
    #plt.tight_layout()
    #l, b, w, h = ax.get_position().bounds
    #ll, bb, ww, hh = CB.ax.get_position().bounds
    #CB.ax.set_position([ll, b + 0.01*h, ww, h*0.8])

    return fig,ax



def get_figsize(columnwidth, wf=0.5, hf=(5.**0.5-1.0)/2.0, ):

      """Parameters:
        - wf [float]:  width fraction in columnwidth units
        - hf [float]:  height fraction in columnwidth units.
                       Set by default to golden ratio.
        - columnwidth [float]: width of the column in latex. Get this from LaTeX
                               using \showthe\columnwidth
      Returns:  [fig_width,fig_height]: that should be given to matplotlib

      """

      fig_width_pt  = columnwidth*wf
      #1pt=0.3515
      inches_per_pt = 1.0/72.27               # Convert pt to inch
      fig_width     = fig_width_pt*inches_per_pt  # width in inches
      fig_height    = fig_width*hf           # height in inches

      #print('Fig size in',fig_width,fig_height)
      #print('Fig size mm',fig_width*2.54*2.0,fig_height*2.54*2.0,wf,hf)

      return [fig_width, fig_height]
