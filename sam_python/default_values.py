import  numpy               as np

######################3333
def default_values(ex,var,lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show): 

    #Getting the Defaul values
    maxv=np.max(ex.nc_f[var])
    minv=np.min(ex.nc_f[var])

    minh=np.min(ex.z[:]/1000.0)
    maxh=np.max(ex.z[:]/1000.0)
    name=ex.name

    lim.append([minv,maxv])
    alt.append([minh,maxh])                #[1]
    var_to.append(1)
    color.append('black')
    explabel1.append(name)
    explabel2.append('')
    leg_loc.append([(maxv-minv)/4.0+minv,maxh*0.85,True,True,True]) #[5] 
    diurnal.append(True)


    return lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show

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


def default(ex,var,lim,alt,var_to,color,explabel2,leg_loc,diurnal,show): 

    #Getting the Defaul values
    maxv=np.max(ex.nc_f[var])
    minv=np.min(ex.nc_f[var])
    maxh=np.max(ex.z[:]/1000.0)
    name=ex.name
    #To check if the list is empty
    if not lim:
        lim=[minv,maxv]         #[0]
    else:
        lim=lim

    if not alt:
        alt=maxh                #[1]
    else:
        alt=alt

    if not var_to:
        var_to=1                #[2]
    else:
        var_to=var_to

    if not color:
        color='red'            #[3]
    else:
        color=color

    if not explabel2:
        explabel2=name          #[4]
    else:
        explabel2=explabel2

    if not leg_loc:
        leg_loc=[(maxv-minv)/4.0+minv,maxh*0.85,True,True] #[5]
    else:
        leg_loc=leg_loc

    if not diurnal:
        diurnal=True           #[6]
    else:
        diurnal=diurnal

    if not show:
        show=True               #[7]
    else:
        show=show


    #lim=[minv,maxv]         #[0]
    #alt=maxh                #[1]
    #var_to=1                #[2]
    #color='red'             #[3]
    #explabel2=name          #[4]
    #leg_loc=[(maxv-minv)/4.0+minv,maxh*0.85,True,True] #[5]
    ##leg_loc.append([maxv*0.3,maxh*0.85,True,True]) #[5]
    #diurnal=True            #[6]
    #show=True               #[7]

    defaul=[lim,alt,var_to,color,explabel2,leg_loc,diurnal,show]


    return defaul
