#####################
#####################
#####################
import  numpy as np

import  matplotlib.pyplot as plt

#shaded plot
import  seaborn as sns

from    netCDF4         import num2date, date2num

import  pandas as pd 

import  pylab

#To work with date in plots 
import matplotlib.dates as mdates

#Color map
from   matplotlib.colors import LinearSegmentedColormap

import matplotlib as mpl

import source.data_own as down

# To change the plot parameter 
from   source.plotparameters 		import 	*


#Color map
#########
#cmap = LinearSegmentedColormap.from_list('mycmap', ['skyblue','blue','navy','steelblue','lightskyblue','white'])
cmap = LinearSegmentedColormap.from_list('mycmap', ['white','lightblue','skyblue','RoyalBlue','blue','darkblue'])
cmap3 = LinearSegmentedColormap.from_list('mycmap', ['white','blue','green','yellow'], N=256, gamma=1.0)

#used user parameter to plot(plotparameter.py
#mpl.rcParams.update(params)

#cmap2 = LinearSegmentedColormap.from_list('mycmap', ['white','red','OrangeRed','yellow','Lime','cyan','steelblue','blue'])


def figure_sam():
    parameters={
 	    'legend.fontsize': 'medium',
 	    'axes.labelsize' : 'medium',
 	    'xtick.labelsize': 'medium',
 	    'ytick.labelsize': 'medium',
            }

    mpl.rcParams.update(parameters)


    ######################################################
    fig = plt.figure()

    fig.set_size_inches(6, 3)
    ###New axis
    ax  = plt.axes()

    # This simply sets the x-axis data to diagonal so it fits better.
    #fig.autofmt_xdate()

    plt.axis(aspect='image')

    #With legends 
    #plt.legend()
    ax.legend(frameon=False)

    #Legent out of the figure
    #box = ax.get_position()
    #ax.set_position([box.x0, box.y0, box.width * 0.80, box.height])
    #ax.legend(loc='left', bbox_to_anchor=(1.0, 1.0),frameon=False)

    #Grid
    #ax.grid(True)

    #Ticks of the axisss
    #locatormax = mdates.HourLocator(interval=1)
    #locatormin = mdates.MinuteLocator(interval=30)
    #ax.xaxis.set_minor_locator(locatormin)
    #ax.xaxis.set_major_locator(locatormax )

    majorFormatter = mpl.dates.DateFormatter('%H') #majorFormatter = mpl.dates.DateFormatter('%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(majorFormatter)

    #Autoscale ticks
    #plt.gcf().autofmt_xdate()
    #ax.autoscale_view()

    return fig,ax

def figure_sam_spatial():
    ######################################################
    fig = plt.figure()
    ###New axis
    ax  = plt.axes()

    fig.set_size_inches(4.5, 6)

    #With legends 
    #plt.legend()
    plt.legend(frameon=False)

    #Legent out of the figure
    #box = ax.get_position()
    #ax.set_position([box.x0, box.y0, box.width * 0.80, box.height])
    #ax.legend(loc='left', bbox_to_anchor=(1.0, 1.0),frameon=False)
# get current axis gca
    #plt.gca().invert_yaxis()
    #ax.invert_yaxis()

    #Grid
    ax.grid(True)


    return fig,ax

def figure_sam_spatial_inv():
    ######################################################
    fig = plt.figure()
    ###New axis
    ax  = plt.axes()

    fig.set_size_inches(4.5, 6)

    #With legends 
    #plt.legend()
    plt.legend(frameon=False)

    #Legent out of the figure
    #box = ax.get_position()
    #ax.set_position([box.x0, box.y0, box.width * 0.80, box.height])
    #ax.legend(loc='left', bbox_to_anchor=(1.0, 1.0),frameon=False)
# get current axis gca
    #plt.gca().invert_yaxis()
    ax.invert_yaxis()

    #Grid
    ax.grid(True)


    return fig,ax

def figure_sam_2d():

    ######################################################
    fig = plt.figure()
    ###New axis
    ax  = plt.axes()

    fig.set_size_inches(8, 5)

    #plt.imshow(sam1.MC, extent=extent1, origin='upper',cmap='RdGy')
    #plt.imshow(sam1.MC[:,:], origin='lower',cmap='RdGy')
    plt.axis(aspect='image')

    fig.autofmt_xdate()
    # into a nice datetime string.
    #ax.xaxis_date()
    
    # We can use a DateFormatter to choose how this datetime string will look.
    # I have chosen HH:MM:SS though you could add DD/MM/YY if you had data
    # over different days.
    #date_format = mdates.DateFormatter('%Y-%M-%d-%H')
    #date_format = mdates.DateFormatter('%Y-%m-%d')
    #ax.xaxis.set_major_formatter(date_format)

    #plt.colorbar(extend='both')
    
    majorFormatter = mpl.dates.DateFormatter('%d-%H') #majorFormatter = mpl.dates.DateFormatter('%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(majorFormatter)
    #ax.autoscale_view()
    
    # This simply sets the x-axis data to diagonal so it fits better.
    #fig.autofmt_xdate()
    
    plt.axis(aspect='image')
    #majorFormatter = mpl.dates.DateFormatter('%m-%d') #majorFormatter = mpl.dates.DateFormatter('%m-%d %H:%M:%S')
    #ax.xaxis.set_major_formatter(majorFormatter)
    #ax.autoscale_view()
    
    #plt.clabel(contours, inline=True, fontsize=8)
    
    #plt.imshow(pblt, extent=[-0.0012,0.0012,-0.0012,0.0012], origin='lower',cmap='RdGy', alpha=0.5)
    
    return fig,ax

def figure_sam_two_ax():

    #fig, ax1 = plt.subplots(fign)
    fig =   plt.figure()
    ###New axis
    ax1  =   plt.axes()

    color1 = 'tab:red'

    # instantiate a second axes that shares the same x-axis
    ax2 = ax1.twiny() 
    
    color2 = 'tab:blue'
    
    return fig,ax1,ax2,color1,color2 

def  splot_own(fig,ax,DATA,z,time,cor,label):


    #size of the data
    shapsam     =   DATA.shape

    data        =   np.zeros((shapsam[0],shapsam[1]))
        
    #rearrange the data, eliminit the ncformat
    for i in range(0,shapsam[0]):
    
        data[i,:] =DATA[i][:]

    #my own plot  
    fig,ax = shade_plot(fig,ax,data,z,time,cor,label)

    #tsplot only python 2.7
    #axis     = []
    #fig,ax = plot_function_tsplot(data,z,time,cor,axis,label)


    return fig,ax


def shade_plot(fig,ax,DATA,z,time,cor,label,**kw):

    #fig =   plt.figure(fign)

    ###New axis
    #ax =   plt.axes()

    #size of the data
    shapsam     =   DATA.shape

    data       =   np.zeros((shapsam[0],shapsam[1]))

    #rearrange the data, eliminit the ncformat
    for i in range(0,shapsam[0]):
    
        data[i,:] = DATA[i][:]

    am  = np.amax(data,axis=0)

    ax  = lplot(ax,data,z,cor,label)

    return fig,ax 

def lplot(ax,data,z,cor,label,**kw):

    #fmri   =   sns.load_dataset("fmri")
    #ax     = sns.lineplot( data=data,dashes=False)

    ####################################
    est =   np.mean(data, axis=0)
    sd  =   np.std(data, axis=0)

    #cis =   (est - sd/1.0, est + sd/1.0)
    #cis =   (est - sd, est + sd)
    cis =   (est*0.90, est*1.10)

    ax.fill_betweenx(z,cis[0],cis[1],alpha=0.3,color=cor)# **kw)

    if label[1]:

        ax.plot(est,z,color=cor,label=label[0])
    else:
        ax.plot(est,z,color=cor)

    #ax.set_title("sns.tsplot")
    #ax.set_title("custom tsplot")

    return ax


def plot_function_tsplot(data,z,time,cor,axis,label):

    fig =   plt.figure()
    ###New axis
    ax =   plt.axes()

    #Shade plot 
    #ax  =   sns.tsplot(time=z,data=data,ci=95)
    #ax  =   sns.tsplot(time=z,data=data,ci='sd')
    ax  =   sns.tsplot(time=z,data=data,ci=90)
    
    ################################
    ################################

    #CREATED DATA FRAME
    #d={}
    #lev=[]
    #count=0

    #for j in range(0,data.shape[1]):
    #    d[count]=data[:,j]
    #    count+=1

    #time_df={'time':time}

    #df=pd.DataFrame(data=d[0])

    #for j in range(0,data.shape[1]):
    #    df.insert(j+1,j+1,d[j])

    #df.insert(0,'time',time)

    #df=pd.DataFrame(data,columns=z,index=time)
    #df=pd.DataFrame(data,columns=z,index=time)
    #print(df.head())

    #ax  =   sns.lineplot(data=df)

    #x = np.linspace(0, 15, 31)
    #df = pd.DataFrame(data).melt()
    #df = pd.DataFrame(data).melt()

    ################################
    ################################
    
    #get the line and the shape from the tsplot
    x,y =   ax.lines[0].get_data()

    c = ax.collections[0].get_paths()[0].vertices
    
    #Clear the current plot
    ax.clear()
    plt.close()

    fig =   plt.figure()
    ###New axis
    ax =   plt.axes()

    ax.fill_between(c[:,1], c[:,0], alpha=0.25,color=cor)


    if label[1]:

        ax.plot(y,x,color=cor,label=label[0])
    else:
        ax.plot(y,x,color=cor)

    #plt.axis(axis)

    # create new plot on the axes, inverting x and y
    #axn.fill_between(c[:,1], c[:,0], alpha=0.5,color=color)
    #axn.legend(loc='left',frameon=False)

    return fig,ax 


def  splot_own_ax(fig,ax,DATA,z,cor):

    #size of the data
    shapsam     =   DATA.shape

    data        =   np.zeros((shapsam[0],shapsam[1]))
        
    #rearrange the data, eliminit the ncformat
    for i in range(0,shapsam[0]):
    
        data[i,:] =DATA[i][:]
    
    #First axis
    axis     = []
    x1,y1,c1 = plot_function(data,z,cor,axis)

    
    ax.fill_between(c1[:,1], c1[:,0], alpha=0.3,color=cor)

    ax.plot(y1,x1,color=cor)
    
    return fig

def  steady(THETA,QT,z):

    #size of the data
    shapsam     =   THETA.shape

    Theta       =   np.zeros((shapsam[0],shapsam[1]))
    Qt          =   np.zeros((shapsam[0],shapsam[1]))
        
    #rearrange the data, eliminit the ncformat
    for i in range(0,shapsam[0]):
    
        Theta[i,:] =THETA[i][:]
        Qt[i,:]    =QT[i][:]
    
    #here subroutine
    fig,ax1,ax2,cor1,cor2  =   figure_sam_two_ax()
    
    axis     = [290,330,0.00, 8500]
    
    #First axis
    x1,y1,c1 = plot_function(Theta,z,'red',axis)
    
    axis    = [0,20,0.00, 8500]
    
    #Second axis
    x2,y2,c2 = plot_function(Qt,z,'blue',axis)

    
    ax1.fill_between(c1[:,1], c1[:,0], alpha=0.5,color=cor1)
    ax2.fill_between(c2[:,1], c2[:,0], alpha=0.5,color=cor2)
    
    ax1.set_xlabel(r'$\mathrm{\theta\ [K]}$', color=cor1)
    ax1.set_ylabel('Height [m]')
    ax1.axis([290,330,0,8000])

    plot1=ax1.plot(y1,x1,color='red')
    
    ax2.axis([0,20,0,8000])
    ax2.set_xlabel(r'q [g/kg]', color=cor2)
    plot1=ax2.plot(y2,x2,color='blue')

    return plot1,ax1,ax2 
    
    
def plot_temp(fign,data,time,color,axis,label):

    #used user parameter to plot(plotparameter.py
    mpl.rcparams.update(params)

    #new figure
    fig =   plt.figure(fign)
    ###new axis
    ax  =   plt.axes()

    #plot domain 
    plt.axis(axis)
    #plot label
    plt.xlabel(r"%s"%(label[0])) 
    plt.ylabel(r"%s"%(label[1])) 

    #box = ax.get_position()
    #ax.set_position([box.x0, box.y0, box.width * 1.0, box.height])
    #ax.legend(loc='left', bbox_to_anchor=(1.0, 1.0),frameon=false)

    ax.legend(loc='left',frameon=false)
    #ax.grid(true)
    
    locatormax = mdates.hourlocator(interval=1)
    locatormin = mdates.minutelocator(interval=30)
    
    #locator.maxticks = 5 
    
    ax.xaxis.set_minor_locator(locatormin)
    ax.xaxis.set_major_locator(locatormax )
    
    majorformatter = mpl.dates.dateformatter('%h') #majorformatter = mpl.dates.dateformatter('%m-%d %h:%m:%s')
    ax.xaxis.set_major_formatter(majorformatter)

    #subplots
    #fig,ax = plt.subplots(fign)

    plot= plt.plot(time,data,color=color)
    

    return plot,fig 

def plot_temp(fign,data,time,color,axis,label):

    #used user parameter to plot(plotparameter.py
    mpl.rcparams.update(params)

    #new figure
    fig =   plt.figure(fign)
    ###new axis
    ax  =   plt.axes()

    #plot domain 
    plt.axis(axis)
    #plot label
    plt.xlabel(r"%s"%(label[0])) 
    plt.ylabel(r"%s"%(label[1])) 

    #box = ax.get_position()
    #ax.set_position([box.x0, box.y0, box.width * 1.0, box.height])
    #ax.legend(loc='left', bbox_to_anchor=(1.0, 1.0),frameon=false)

    ax.legend(loc='left',frameon=false)
    #ax.grid(true)
    
    locatormax = mdates.hourlocator(interval=1)
    locatormin = mdates.minutelocator(interval=30)
    
    #locator.maxticks = 5 
    
    ax.xaxis.set_minor_locator(locatormin)
    ax.xaxis.set_major_locator(locatormax )
    
    majorformatter = mpl.dates.dateformatter('%h') #majorformatter = mpl.dates.dateformatter('%m-%d %h:%m:%s')
    ax.xaxis.set_major_formatter(majorformatter)

    #subplots
    #fig,ax = plt.subplots(fign)

    plot= plt.plot(time,data,color=color)
    

    return plot,fig 


def plot_mean(fign,data,time,cor,**kw):

    ######################################################
    fig =   plt.figure(fign)
    ###New axis
    ax  =   plt.axes()

    #With legends 
    ax.legend(frameon=False)

    ####################################
    est =   np.mean(data, axis=0)

    ax.plot(est,time,cor)


    return fig,ax

def plot_std(fign,data,time,cor,**kw):

    ######################################################
    fig =   plt.figure(fign)
    ###New axis
    ax  =   plt.axes()

    #With legends 
    ax.legend(frameon=False)

    ####################################
    est =   np.std(data, axis=0)

    ax.plot(est,time,cor)


    return fig,ax

def rp(DATA,z,ax,cor):

######################################################
    level=np.zeros(DATA.shape[0]*DATA.shape[1])

    #Total Dimesion 
    lz= level.shape[0]

    #Level dimension
    kk= z.shape[0]

    ct1=0
    ct2=0

    #Created the level array 
    for i  in range(0,lz):

        level[i]= z[ct2]
            
        ct1=ct1+1

        if ct1==kk:

            ct1=0
            ct2=ct2+1

    Thetapa     =   pd.DataFrame({'x':level,'y':np.reshape(DATA, lz, order='F')})


    #Thetapa.head()

    #fmri    =   sns.load_dataset("fmri")
    #fmi      =     sns.relplot(data=Theta, dashes=False)
    #fmi      =     sns.relplot('x','y',data=Thetapa,ci='sd',kind='line',dashes=False, markers=True,err_style='bars'   )

    sns.relplot('x','y',data=Thetapa,ci='sd',kind='line', markers=True,ax=ax )
    #sns.relplot('x','y',data=Thetapa,ci='sd',kind='line', markers=True,ax=ax )
    #sns.relplot('x','y',data=Thetapa,kind='line',ax=ax )

    #sns.lineplot('x','y',data=Thetapa,ci=None,ax=ax )
    #sns.relplot('x','y',data=Thetapa,ci=None,ax=ax )

    #plt.show()

    #get the line and the shape from the tsplot
    xx,yy =   ax.lines[0].get_data()

    c = ax.collections[0].get_paths()[0].vertices

    #Clear the current plot
    ax.clear()
    plt.close()

    ax.fill_between(c[:,1], c[:,0], alpha=0.5,color=cor)

    ax.plot(yy,xx,color=cor)


    return ax

def d2_plot_contour(exp,var,idi,idf,nv1,nv2,orig,colors):

    #to LIMIT THE VECTOR IN A INTERVAL TO MAKE 
    # THE MEAN 
    ni,nf= down.data_n(idi,idf,exp.data[:])

    li,lf= down.level_n(nv1,nv2,exp.z[:]/1000.0)

    tu = "days  since 2013-12-31"
    tc = "gregorian"
    
    idin=date2num(idi,units=tu,calendar=tc)
    idfn=date2num(idf,units=tu,calendar=tc)

    x=np.zeros(exp.time[ni:nf].shape[0])
    y=np.zeros(exp.z[li:lf].shape[0])
    
    MF=np.zeros((exp.time[ni:nf].shape[0],exp.z[li:lf].shape[0]))
    
    x[:]=exp.time[ni:nf]
    y[:]=exp.z[li:lf]/1000.0
    
    MF[:,:]=var[ni:nf,li:lf]
    
    X,Y= np.meshgrid(x,y)

    #zz,date = np.meshgrid(y,x)

    ################################3
    fig, ax = plt.subplots()
    fig.set_size_inches(7.5, 2)
    #To use date in the x axis
    ax.xaxis_date()
    #plt.colorbar(extend='both')
    
    majorFormatter = mpl.dates.DateFormatter('%d %H') #majorFormatter = mpl.dates.DateFormatter('%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(majorFormatter)
    #ax.autoscale_view()
    ax.set_ylabel('z [km]')

    if colors=='cloud':
        colors=cmap

    #contours = plt.contourf(date, zz, MF, 100 ,cmap='coolwarm');
    #plt.contourf(X, Y, MF.T, 100 ,cmap=cmap,interpolation='gaussian',vmin=0.0,vmax=0.5 );
    #plt.contourf(X, Y, MF.T, 100 ,cmap=cmap,interpolation='gaussian',levels=[0,0.1,0.2,0.3,0.4,0.5]);

    levels= np.linspace(0.0, 0.5, 11) #  11=n+1

    #contorns number in plot


    CS=plt.contourf(X, Y, MF.T, 100 ,cmap=cmap,interpolation='gaussian',levels=levels);
    #CS=plt.contourf(X, Y, MF.T,cmap='flag',levels=levels,linewidths=2);

    #ax.clabel(CS, levels[1::2],  # label every second level
    #      inline=1, fmt='%1.1f', fontsize=14)

    # make a colorbar for the contour lines
    CB = fig.colorbar(CS, shrink=0.8, extend='both')



    return fig,ax    

######################################################

def d2_plot(exp,var,idi,idf,nv1,nv2,orig,colors):

    #to LIMIT THE VECTOR IN A INTERVAL TO MAKE 
    # THE MEAN 
    ni,nf= down.data_n(idi,idf,exp.data[:])

    li,lf= down.level_n(nv1,nv2,exp.z[:]/1000.0)

    tu = "days  since 2013-12-31"
    tc = "gregorian"
    
    idin=date2num(idi,units=tu,calendar=tc)
    idfn=date2num(idf,units=tu,calendar=tc)

    x=np.zeros(exp.time[ni:nf].shape[0])
    y=np.zeros(exp.z[li:lf].shape[0])
    
    MF=np.zeros((exp.time[ni:nf].shape[0],exp.z[li:lf].shape[0]))
    
    x[:]=exp.time[ni:nf]
    y[:]=exp.z[li:lf]/1000.0
    
    MF[:,:]=var[ni:nf,li:lf]
    
    X,Y= np.meshgrid(x,y)

    
    def calculate_aspect(shape, extent):
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

    if colors=='cloud':
        colors=cmap

    #plt.imshow(MF.T,extent=extent, interpolation='gaussian',origin='lower' ,cmap='RdBu',aspect=0.2) 
    #plt.imshow(MF.T,extent=extent2, interpolation='gaussian',origin='lower' ,cmap=cmap,aspect='auto') 
    plt.imshow(MF.T[:,:],extent=extent2, interpolation='gaussian',origin=orig ,cmap=colors,aspect='auto') 
    #plt.imshow(MF,extent=extent2,origin='lower',cmap='RdBu_r') 

    #ax.set_xlim([idin,idfn])
    #ax.set_ylim([nv1,nv2])

    #def calculate_aspect(shape, extent):
    #    dx = (extent[1] - extent[0]) / float(shape[1])
    #    dy = (extent[3] - extent[2]) / float(shape[0])
    #    return dx / dy

    #aspect=calculate_aspect(MF.T.shape,extent2) 

    #fig.autofmt_xdate()
    plt.colorbar()

    return fig,ax    

def d2_plot_im_xy(exp,var,lcmax,nlines,x1,x2,y1,y2,origin,colors):

    ################################3
    fig, ax = plt.subplots()

    fig.set_size_inches(7.5, 2)

    # Variables to make the grid to contourplot
    x       =   np.zeros(exp.x[:].shape[0])
    y       =   np.zeros(exp.y[:].shape[0])

    x       =   exp.x[:]/1000.0
    y       =   exp.y[:]/1000.0

    #Variable to plot
    MF=np.zeros((exp.x.shape[0],exp.y.shape[0]))
    MF=var[:,:]


    if colors=='cloud':
        colors=cmap


    #Y axis label 
    ax.set_xlabel('x [km]')
    ax.set_ylabel('y [km]')


    X,Y= np.meshgrid(x,y)

    # Levels to plot, in number. 
    levels= np.linspace(0.0, lcmax,nlines) #  11=n+1

    #Contour plot 

    #CS= plt.contour(X,Y,MF.T,cmap='flag',levels=levels,linewidths=1);
    #CD=plt.contourf(X,Y,MF.T,cmap=colors,levels=levels,linewidths=1);
    CD=plt.contourf(X,Y,MF.T,cmap='RdBu');


    # To control the color bar, lcmax is the maximum Z value
    #plt.clim(0, lcmax)

    # Limits of the plot for both IM AN CS
    ax.set_xlim([x1,x2])
    ax.set_ylim([y1,y2])

    # Thicken the zero contour.
    #zc = CS.collections[5]
    #plt.setp(zc, linewidth=0.01)
    
    #ax.clabel(CS, levels[1::1],  # label every second level
    #          inline=1, fmt='%1.2f', fontsize=8)
    
    #make a colorbar for the contour lines
    CB = fig.colorbar(CD, shrink=0.8, extend='both')
    
    #ax.set_title('Lines with colorbar')
    
    return fig,ax    

def d3_plot_im_xyz(exp,var,lcmax,nlines,x1,x2,y1,y2,origin,colors):

    ################################3
    fig, ax = plt.subplots()

    fig.set_size_inches(7.5, 2)

    # Variables to make the grid to contourplot
    x       =   np.zeros(exp.x[:].shape[0])
    y       =   np.zeros(exp.y[:].shape[0])
    z       =   np.zeros(exp.z[:].shape[0])

    x       =   exp.x[:]/1000.0
    y       =   exp.y[:]/1000.0
    z       =   exp.z[:]/1000.0

    #Variable to plot
    MF=np.zeros((exp.x.shape[0],exp.z.shape[0]))
    MF=var[:,:]


    if colors=='cloud':
        colors=cmap


    #Y axis label 
    ax.set_xlabel('x [km]')
    ax.set_ylabel('z [km]')


    X,Y= np.meshgrid(x,z)

    # Levels to plot, in number. 
    levels= np.linspace(0.0, lcmax,nlines) #  11=n+1

    #Contour plot 

    #CS= plt.contour(X,Y,MF.T,cmap='flag',levels=levels,linewidths=1);
    #CD=plt.contourf(X,Y,MF.T,cmap=colors,levels=levels,linewidths=1);
    CD=plt.contourf(X,Y,MF,cmap='RdBu');


    # To control the color bar, lcmax is the maximum Z value
    #plt.clim(0, lcmax)

    # Limits of the plot for both IM AN CS
    ax.set_xlim([x1,x2])
    ax.set_ylim([y1,y2])

    # Thicken the zero contour.
    #zc = CS.collections[5]
    #plt.setp(zc, linewidth=0.01)
    
    #ax.clabel(CS, levels[1::1],  # label every second level
    #          inline=1, fmt='%1.2f', fontsize=8)
    
    #make a colorbar for the contour lines
    CB = fig.colorbar(CD, shrink=0.8, extend='both')
    
    #ax.set_title('Lines with colorbar')
    
    return fig,ax    

def d2_plot_im_ctn_n(exp,var,z,lcmax,nlines,idi,idf,nv1,nv2,origin,colors):

    ################################3
    fig, ax = plt.subplots()
    fig.set_size_inches(7.5, 2)
    #Y axis label 
    ax.set_ylabel('z [km]')



    #Limits of time date
    ni,nf= down.data_n(idi,idf,exp.data[:])

    # To found the maximum date, even 
    #that required date not exists
    if nf==0:
        nf=exp.data.shape[0]-1

    #Limits of high date
    li,lf= down.level_n(nv1,nv2,z[:])

    sx= exp.time.shape[0]
    sy= z.shape[0]
    
    x=np.zeros(sx)
    y=np.zeros(sy)
    
    MF=np.zeros((sx,sy))
    
    x       =   exp.data[:]
    y       =   z[:]

    MF=np.zeros((sx,sy))
    #Variable to plot
    MF=var[:,:]


    if colors=='cloud':
        colors=cmap

    if colors=='whbuyl':
        colors=cmap3

    #Differently to the countour in thje imshow the 
    #other coodinates for the two dimensinal plot 
    #are not expecified in X Y with the meshgrid. 
    #For this reazon it is necessary to 
    #specified this coorindates in the extendt, for the minimum to 
    #maximum in x and y. To control the extent of the plot, the 
    #must be use set_xlim and set_ylim

    #pq /2, sei la mas funcionou 
    #extent2= [exp.time[ni],exp.time[nf],y[0],y[ln-1]]
    #extent2= [exp.time[0],exp.time[exp.time.shape[0]-1],z[0],z[z.shape[0]-1]]

    #ax.autoscale(False)

    #Imagen plot, color plot 
    #IM=plt.imshow(MF.T,extent=extent2,interpolation='gaussian',cmap='gray',origin='lower',aspect='auto') 
    #IM=ax.imshow(MF.T[:,:],interpolation='gaussian',extent=extent2,cmap=colors,origin=origin,aspect='auto') 
    #IM=ax.imshow(MF.T[:,:],interpolation='gaussian',extent=extent2,cmap=colors,origin=origin,aspect='auto') 
    #IM=ax.imshow(exp.CLD[:,:].T,interpolation='gaussian',extent=extent2,cmap=colors,origin=origin,aspect='auto') 



    X,Y= np.meshgrid(x,y)

    def calculate_aspect(shape, extent):
        dx = (extent[1] - extent[0]) / float(shape[1])
        dy = (extent[3] - extent[2]) / float(shape[0])
        return dx / dy

    #extent2= [ni,nf,li,lf]
    extent2= [exp.time[0],exp.time[sx-1],0,z[sy-1]]
    #x_lims = mdates.date2num(exp.data[:])
    #extent2= [x_lims[0],x_lims[sx-1],li,lf] 



    # Levels to plot, in number. 
    levels= np.linspace(0.0, lcmax,nlines) #  11=n+1

    #Contour plot 

    CS=plt.contour(X,Y,MF.T,cmap=colors,interpolation='gaussian',levels=levels[0::1],linewidths=1);

    colormapi=plt.imshow(MF.T,extent=extent2, interpolation='nearest',origin='lower' ,cmap=colors,aspect='auto') 

    #CD=plt.imshow(MF.T,extent=extent2, interpolation='gaussian',origin=origin,cmap=colors,aspect='auto') 

    cbair = plt.colorbar(colormapi)

    ax.xaxis_date()
    date_form = mdates.DateFormatter("%H" )
    ax.xaxis.set_major_formatter(date_form)
    
    ax.set_xlim([exp.data[ni],exp.data[nf]])
    ax.set_ylim([0., 4.0])
    
    ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
    
    plt.clim(0, 20)




    #CD=plt.contourf(X,Y,MF.T,cmap='BuPu',levels=levels,linewidths=1); 
    #### To control the color bar, lcmax is the maximum Z value
    ###plt.clim(0, lcmax)

    ####To puts dates in the x axis
    ###ax.xaxis_date()
    ###majorFormatter = mpl.dates.DateFormatter(' %H') #majorFormatter = mpl.dates.DateFormatter('%m-%d %H:%M:%S')
    ###ax.xaxis.set_major_formatter(majorFormatter)


    #### Limits of the plot for both IM AN CS
    ###ax.set_xlim([exp.data[ni],exp.data[nf]])
    ###ax.set_ylim([0,nv2])

    #### Thicken the zero contour.
    ####zc = CS.collections[5]
    ####plt.setp(zc, linewidth=0.01)
    ###
    ####ax.clabel(CS, levels=levels[0::2],  # label every second level
    ####          inline=1, fmt='%1.4f', fontsize=8)
    ###
    ####make a colorbar for the contour lines
    ####CB = fig.colorbar(CD, shrink=0.8, extend='both')
    ###
    ####ax.set_title('Lines with colorbar')
    ###
    #### We can still add a colorbar for the image, too.
    ####CBI = fig.colorbar(CD, orientation='horizontal', shrink=0.8)
    ####CBI = fig.colorbar(IM, orientation='vertical', shrink=1.0,drawedges=True)
    ####CBI = fig.colorbar(IM, orientation='vertical', shrink=1.0)

    ####l, b, w, h = ax.get_position().bounds

    ####ll, bb, ww, hh = CB.ax.get_position().bounds

    ####CB.ax.set_position([ll, b + 0.1*h, ww, h*0.8])

    ####plt.show()
    ####computer=''
    ####file_fig = "%s/repositories/posdoc/fig/goamazon/les/diurnal_v8_pgi/2d/"%(computer)  
    ####plt.savefig('%scloud_clf.pdf'%(file_fig), format='pdf', dpi=1000)

    ####exit() 
    return fig,ax    

def d2_plot_im_ctn(time,data,var,z,lcmax,nlines,idi,idf,nv1,nv2,origin,colors):


    #used user parameter to plot(plotparameter.py
    mpl.rcParams.update(params_2d)
    ################################3
    fig, ax = plt.subplots()
    fig.set_size_inches(7.0, 2.0)

    #Y axis label 
    ax.set_ylabel('z [km]')

    #Limits of time date
    ni,nf= down.data_n(idi,idf,data[:])

    # To found the maximum date, even 
    #that required date not exists
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
    y       =   z[:]

    #Variable to plot
    MF=var[:,:]

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
    x_lims = mdates.date2num(data[:])
    extent2= [x_lims[0],x_lims[sx-1],z[0],z[sy-1]] 


    # Levels to plot, in number. 
    levels= np.linspace(0.0, lcmax,nlines) #  11=n+1

    #Contour plot 

    CS=ax.contour(X,Y,MF.T,cmap=colors,interpolation='gaussian',levels=levels[0::1],linewidths=1);

    CI=plt.imshow(MF.T,extent=extent2, interpolation='gaussian',origin='lower' ,cmap=colors,aspect='auto') 

    ####make a colorbar for the contour lines
    CB = fig.colorbar(CI, shrink=1.0, extend='max')

    cbarlabels = np.linspace(0.0, lcmax, 6, endpoint=True)
    CB.set_ticks(cbarlabels)


    ax.xaxis_date()
    date_form = mdates.DateFormatter("%H" )
    ax.xaxis.set_major_formatter(date_form)
    
    ax.set_xlim([x_lims[ni],x_lims[nf]])
    #ax.set_xlim(exp.data[ni],exp.data[nf])
    ax.set_ylim([nv1,nv2])
    
    ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
    
    plt.clim(0, lcmax)

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
    
def color_hours(hour):

    line=[1,0]
    color='k'

    if hour==9:

        line=[3,2,1,2]
        color='magenta'
        
    elif hour==10:
    
        line=[2,2,1,2]
        color='cyan'
    
    elif  hour==11:
    
    	line=[2, 1]
    	color='b'
    
    elif  hour==12:
    
        line=[3, 1]
        color='g'
    
    elif  hour==13:
    
        line=[4, 1]
        color='r'
    
    elif  hour==14:
    
        line=[1,1]
        color='tab:orange'
    
    elif  hour==15:
    
        line=[1,2,1,2]
        color='m'
    
    elif  hour==16:
    
        line=[2,1,1,3]
        color='tab:brown'
    
    elif  hour==17:
    
        line=[2,1,5,3]
        color='tab:purple'
    
    elif  hour==18:
    
        line=[4,2,1,2]
        color='y'
    
    elif  hour==19:

        line=[1,2,4,2]
        color='c'

    return line,color

