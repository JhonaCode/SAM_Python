import  numpy as np
import  matplotlib.pyplot as plt

from    netCDF4         import num2date, date2num

#Color map
from    matplotlib.colors import LinearSegmentedColormap

#To work with date in plots 
import matplotlib.dates as mdates

import matplotlib as mpl

import source.data_own as down

# To change the plot parameter 
from   source    import  plotparameters_new as pn

#Color map
#########
#cmap = LinearSegmentedColormap.from_list('mycmap', ['skyblue','blue','navy','steelblue','lightskyblue','white'])
cmap = LinearSegmentedColormap.from_list('mycmap', ['white','lightblue','skyblue','RoyalBlue','blue','darkblue'])
cmap3 = LinearSegmentedColormap.from_list('mycmap', ['white','blue','green','yellow'], N=256, gamma=1.0)


def d2_plot_im_ctn(time,data,var,z,contour,idi,idf,nv1,nv2,label1,label2,origin,colors):

    #used user parameter to plot(plotparameter.py
    #mpl.rcParams.update(params_2d)

    wf=0.4
    hf=0.7
    cmmais=0.0

    #plot size of the figures
    #cmmais are the cm to put the cbbar  without modified the size of the fig 
    pn.plotsize(wf,hf,cmmais,'2d')

    if(label1=='ca_sh' or label1=='ca_sh_wg' or label1=='large'):

        cmmais =1.0
        pn.plotsize(wf,hf,cmmais,'2d')

    if(label1=='iop1' or label1=='small' ):

        cmmais=0.3
        pn.plotsize(wf,hf,cmmais,'2d')

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
    li,lf= down.level_nr(nv1,nv2,z[:])

    sx= data.shape[0]
    sy= z.shape[0]
    
    x=np.zeros(sx)
    y=np.zeros(sy)
    
    MF=np.zeros((sx,sy))
    
    #THe only way to time to be reconize by the imshow and contour is 
    # with the data and no time
    x       =   data[:]
    y       =   z[:]


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


    #extent2= [exp.time[0],exp.time[sx-1],0,z[sy-1]]
    #x_lims = mdates.date2num(data[:])
    #extent2= [x_lims[0],x_lims[sx-1],z[0],z[sy-1]] 
    #CU=plt.imshow(MF.T,extent=extent2, interpolation='gaussian',origin='lower' ,cmap=colors,aspect='auto') 
    #ax.set_xlim([x_lims[ni],x_lims[nf]])

    # Levels to plot, in number. 

    levels= np.linspace(contour[0],contour[1],contour[2])


    CU=ax.contourf(X,Y,MF.T,levels=levels, interpolation='bilinear',origin='lower',cmap=colors,aspect='auto');
    #CU=ax.contourf(X,Y,MF.T);


    # Set all level lines to black
    line_colors = ['black' for l in CU.levels]

    #Contour plot 
    CS=plt.contour(X,Y,MF.T,levels=levels[::10],colors=line_colors,linewidths=0.1);

    #plt.clabel(CS, levels=levels[::20], fontsize=8.0)


    if(label1=='ca_sh' or label1=='ca_sh_wg' or label1=='large'):

        ###make a colorbar for the contourf 
        CB = fig.colorbar(CU, shrink=1.0, extend='max')

        cbarlabels = np.linspace(0.0, contour[1],11,endpoint=True)
        
        CB.set_ticks(cbarlabels[::2])

    if(label1=='iop1' or label1=='small' ):
        plt.ylabel(r'z [km]') 

    ax.xaxis_date()

    date_form = mdates.DateFormatter("%H" )

    ax.xaxis.set_major_formatter(date_form)
    
    ax.set_xlim(data[ni],data[nf])

    ax.set_ylim([nv1,nv2])
    
    ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))

    ######ax.text(x_lims[ni+5], nv2-1.0, r' %s'%(label), fontsize=5, color='black')
    ax.text(data[ni+1], nv2-0.5, r' %s'%(label2), fontsize=7, color='black')

    #plt.clim(contour[0], contour[1])

    #plt.tight_layout()

    #l, b, w, h = ax.get_position().bounds

    #ll, bb, ww, hh = CB.ax.get_position().bounds

    #CB.ax.set_position([ll, b + 0.01*h, ww, h*0.8])

    return fig,ax    

######################################################



def d2_goa(exp,var,z,idi,idf,nv1,nv2,orig):

    #to LIMIT THE VECTOR IN A INTERVAL TO MAKE 
    # THE MEAN 
    ni,nf= down.data_n(idi,idf,exp.data[:])


    li,lf= down.level_n(nv1,nv2,z[ni,:]/1000.0)

    print(li,lf)

    tu = "days  since 2013-12-31"
    tc = "gregorian"
    
    idin=date2num(idi,units=tu,calendar=tc)
    idfn=date2num(idf,units=tu,calendar=tc)

    x=np.zeros(exp.time[ni:nf].shape[0])
    y=np.zeros(z[ni,li:lf].shape[0])
    
    MF=np.zeros((exp.time[ni:nf].shape[0],z[ni,li:lf].shape[0]))
    
    x[:]=exp.time[ni:nf]
    y[:]=z[ni,li:lf]/1000.0
    
    MF[:,:]=var[ni:nf,li:lf]
    
    X,Y= np.meshgrid(x,y)

    
    def calculate_aspect(shape, extent,orig):
        dx = (extent[1] - extent[0]) / float(shape[1])
        dy = (extent[3] - extent[2]) / float(shape[0])
        return dx / dy

    fig, ax = plt.subplots()
    fig.set_size_inches(7.5, 2)
    
    #To use date in the x axis
    ax.xaxis_date()
    #plt.colorbar(extend='both')
    
    majorFormatter = mpl.dates.DateFormatter('%d %H') #majorFormatter = mpl.dates.DateFormatter('%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(majorFormatter)
    #ax.autoscale_view()
    ax.set_ylabel('z [km]')


    extent2= [idin,idfn,nv1,nv2]

    #plt.imshow(MF.T,extent=extent, interpolation='gaussian',origin='lower' ,cmap='RdBu',aspect=0.2) 
    #plt.imshow(MF.T,extent=extent2, interpolation='gaussian',origin='lower' ,cmap=cmap,aspect='auto') 
    plt.imshow(MF.T,extent=extent2, interpolation='gaussian',origin=orig ,cmap='RdBu_r',aspect='auto') 
    #plt.imshow(MF.T,extent=extent2, interpolation='gaussian',origin=orig ,cmap=cmap,aspect='auto') 

    #ax.set_xlim([idin,idfn])
    #ax.set_ylim([nv1,nv2])

    #fig.autofmt_xdate()
    plt.colorbar()

    return 

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
