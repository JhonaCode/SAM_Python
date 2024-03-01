import  numpy               as np

# Python standard library datetime  module
import  datetime as dt  
##################################

##################################
def default_values_2d(exp,varst,lim,alt,var_to,color,explabel1,explabel2,axis_on,show,k): 

    el=len(exp) 
    vl=len(varst)

    ex=exp[k]

    name=ex.name


    a1          =  [(True,True,True ,True,0.35,1.34)]

    lim1=[]
    alt1=[]
    var_to1=[]
    label1=[]
    label2=[]
    color1=[]
    ax1=[]
    show1=[]


    for i in range(0, vl):

        var=varst[i]
        #Getting the Defaul values
        maxv=np.max(ex.nc_f[var])
        minv=np.min(ex.nc_f[var])

        minh=np.min(ex.z[:]/1000.0)
        maxh=np.max(ex.z[:]/1000.0)

        lim1.append([minv,maxv])
        alt1.append([minh,maxh])         

        var_to1.append(1)

        color1.append('RdBu_r')

        label1.append(var+'_'+ex.name)
        label2.append('')

        ####bar ,x,y axis, top_lfc_pbl,size,cm a mais do grafico
        ax1.append(a1)

        show1.append('True')

    lim.append(lim1)
    var_to.append(var_to1)
    color1.append(color1)
    explabel1.append(label1)
    explabel2.append(label2)
    axis_on.append(ax1)
    show.append(show1)

    return lim,alt,var_to,color,explabel1,explabel2,axis_on,show

#######################

def default_values_diff(exp,varst,lim,alt,var_to,color,explabel1,explabel2,axis_on,show): 

    el=1#len(exp) 
    vl=len(varst)

    ex=exp

    name=ex.name


    a1          =  [(True,True,True ,True,0.35,1.34)]

    lim1=[]
    alt1=[]
    var_to1=[]
    label1=[]
    label2=[]
    color1=[]
    ax1=[]
    show1=[]


    for i in range(0, vl):

        var=varst[i]
        #Getting the Defaul values
        maxv=np.max(ex.nc_f[var])
        minv=np.min(ex.nc_f[var])

        minh=np.min(ex.z[:]/1000.0)
        maxh=np.max(ex.z[:]/1000.0)

        lim1.append([minv,maxv])
        alt1.append([minh,maxh])         

        var_to1.append(1)

        color1.append('RdBu_r')

        label1.append(var+'_'+ex.name)
        label2.append('')

        ####bar ,x,y axis, top_lfc_pbl,size,cm a mais do grafico
        ax1.append(a1)

        show1.append('True')

    lim.append(lim1)
    var_to.append(var_to1)
    color1.append(color1)
    explabel1.append(label1)
    explabel2.append(label2)
    axis_on.append(ax1)
    show.append(show1)

    return lim,alt,var_to,color,explabel1,explabel2,axis_on,show

def default_values_1d(exp,varst,lim,alt,var_to,color,explabel1,explabel2,plot_def,show,k): 

    el=len(exp) 
    vl=len(varst)

    ex=exp[k]

    name=ex.name

    X=''
    Y=''

    a1          =  ( [X,Y],[X,0,0],[False,'upper left'],[0.35,0])

    lim1=[]
    alt1=[]
    var_to1=[]
    label1=[]
    label2=[]
    color1=[]
    ax1=[]
    show1=[]


    interval_x=4


    for i in range(0, vl):

        var=varst[i]

        #Getting the Defaul values
        maxv=np.max(ex.nc_f[var])
        minv=np.min(ex.nc_f[var])
        interval_y=int(maxv/4)

        maxt=np.max(0)
        mint=np.min(len(ex.nc_f[var]))

        lim1.append([mint,maxt,interval_x])
        alt1.append([minv,maxv,interval_y])         


        var_to1.append([1])

        color1.append('blue')

        label1.append(var+'_'+ex.name)
        label2.append([''])

        ####bar ,x,y axis, top_lfc_pbl,size,cm a mais do grafico
        ax1.append([a1])

        show1.append('True')

    lim.append(lim1)
    alt.append(alt1)
    var_to.append(var_to1)
    color1.append(color1)
    explabel1.append(label1)
    explabel2.append(label2)
    plot_def.append(ax1)
    show.append(show1)

    return lim,alt,var_to,color,explabel1,explabel2,plot_def,show
    #return lim1,alt1,var_to1,color,label1,label2,ax1,show1

##################################
def default_values(exp,varst,lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show,k): 

    el=len(exp) 
    vl=len(varst)

    ex=exp[k]

    name=ex.name

    lim1=[]
    alt1=[]
    var_to1=[]
    label1=[]
    label2=[]
    color1=[]
    leg_loc1=[]
    diurnal1=[]
    show1=[]


    for i in range(0, vl):

        var=varst[i]
        #Getting the Defaul values
        maxv=np.max(ex.nc_f[var])
        minv=np.min(ex.nc_f[var])

        minh=np.min(ex.z[:]/1000.0)
        maxh=np.max(ex.z[:]/1000.0)

        lim1.append([minv,maxv])
        alt1.append([minh,maxh])         

        var_to1.append(1)

        color1.append('RdBu_r')

        label1.append(var+'_'+ex.name)
        label2.append('')

        #legent loc
        ll1        =  [[(maxv-minv)/4.0+minv,maxh*0.85,True,True,True]]
        ####bar ,x,y axis, top_lfc_pbl,size,cm a mais do grafico
        leg_loc.append(ll1)

        diurnal1.append('True')

        show1.append('True')

    lim.append(lim1)
    var_to.append(var_to1)
    color1.append(color1)
    explabel1.append(label1)
    explabel2.append(label2)
    leg_loc.append(leg_loc1)
    diurnal.append(diurnal1)
    show.append(show1)

    return lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show

def default_values_horizontal(ex,var,lim,xlim,ylim,var_to,color,explabel1,explabel2,axis_on,leg_loc,show): 

    #Getting the Defaul values
    maxv=np.max(var)
    minv=np.min(var)

    minx=np.min(ex.x[:])/1000.0
    maxx=np.max(ex.x[:])/1000.0
                               
    miny=np.min(ex.y[:])/1000.0
    maxy=np.max(ex.y[:])/1000.0

    name=ex.name


    try:
        units=var.units
    except AttributeError:
        units ='' 

    lim.append([[minv,maxv,20,'%s'%units]])
    xlim.append([[minx,maxx,10]])         
    ylim.append([[miny,maxy,10]])         

    var_to.append([1])

    color.append('RdBu_r')

    explabel1.append([name])
    explabel2.append([''])

    ####bar ,x,y axis, top_lfc_pbl,size,cm a mais do grafico
    a1          =  [(True,True,True,0.35,1.34)]
    axis_on.append([a1])

    dx=(ex.x[1]-ex.x[0])/1000.0
    dy=(ex.y[1]-ex.y[0])/1000.0

    l1  =[True,minx+100*dx,maxy-100*dy]
    leg_loc.append([l1])


    show.append(['True'])

    return lim,xlim,ylim,var_to,color,explabel1,explabel2,axis_on,leg_loc,show

##################################
def default_values_old(ex,var,lim,alt,var_to,color,explabel1,explabel2,explabel3,leg_loc,diurnal,show): 


    #Getting the Defaul values
    maxv=np.max(ex.nc_f[var])
    minv=np.min(ex.nc_f[var])

    minh=np.min(ex.z[:]/1000.0)
    maxh=np.max(ex.z[:]/1000.0)
    name=ex.name

    lim.append([minv,maxv])
    alt.append([minh,maxh])                #[1]
    var_to.append([1])
    color.append(['black'])
    explabel1.append([name])
    explabel2.append('')
    explabel3.append('')
    leg_loc.append([(maxv-minv)/4.0+minv,maxh*0.85,True,True,True]) #[5] 
    diurnal.append(True)


    return lim,alt,var_to,color,explabel1,explabel2,explabel3,leg_loc,diurnal,show

def check_list(default): 

    #Getting the Defaul values
    maxv=np.max(ex.nc_f[var])
    minv=np.min(ex.nc_f[var])
    maxh=np.max(ex.z[:]/1000.0)
    name=ex.name

    if j>0:

        #To check if the list is empty
        if lim:
            lim=lim[k][j]
        else: 
            lim=[minv,maxv]         #[0]
            
        if alt:
            alt=alt[k][j]
        else: 
            alt=maxh

        if var_to:
            var_to=var_to[k][j]
        else: 
            var_to=1

        if color:
            color=color[k][j]
        else: 
            color='red'

        if explabel:
            explabel=explabel[k][j]
        else:
            explabel=name

        if explabel2:
            explabel2=explabel2[j]
        else:
            explabel2=''

        if leg_loc:
            leg_loc=leg_loc[k][j]
        else:
            leg_loc=[(maxv-minv)/4.0+minv,maxh*0.85,True,True] #[5]

        if  diurnal:
            diurnal=diurnal[k][j]
        else:
            diurnal=True

        if show:
            show=show[k][j]
        else:
            show=True

    else:
    #To check if the list is empty

        if lim:
            lim=lim[k]
        else: 
            lim=[minv,maxv]         #[0]
            
        if alt:
            alt=alt[k]
        else: 
            alt=maxh

        if var_to:
            var_to=var_to[k]
        else: 
            var_to=1

        if color:
            color=color[k]
        else: 
            color='red'

        if explabel:
            explabel=explabel[k]
        else:
            explabel=name

        if explabel2:
            explabel2=explabel2[k]
        else:
            explabel2=''

        if leg_loc:
            leg_loc=leg_loc[k]
        else:
            leg_loc=[(maxv-minv)/4.0+minv,maxh*0.85,True,True] #[5]

        if  diurnal:
            diurnal=diurnal[k]
        else:
            diurnal=True

        if show:
            show=show[k]
        else:
            show=True

    default=[lim,alt,var_to,color,explabel,explabel2,leg_loc,diurnal,show]

    return default

