# -*- coding: utf-8 -*-
'''Views for mainRecycleApp'''
from __future__ import unicode_literals

from mainRecycleApp.models import RecyclingCenter
from django.shortcuts import render

# Create your views here.
def index(request):
    '''Index render method for mainrecycleApp/home'''
    return render(request, 'mainRecycleApp/home.html')

def about(request):
    '''About render method for mainRecycleApp/about.html'''
    return render(request, 'mainRecycleApp/about.html')

def contact(request):
    '''Contact render method for mainRecycleApp/contact.html'''
    return render(request, 'mainRecycleApp/contact.html')

def getBoroughFromZip(zipcode):
    '''Get user's rough location by borough'''
    BK = [10461, 10462, 10464, 10465, 10472, 10473, 11209, 11214, 11228, 11204, 11218, 11219, 11230, 11234, 11236, 11239, 11223, 11224, 11229, 11235, 11201, 11205, 11215, 11217, 11231, 11203, 11210, 11225, 11226, 11207, 11208, 11211, 11222, 11220, 11232, 11206, 11221, 11237]
    MH = [10026, 10027, 10030, 10037, 10039,10001, 10011, 10018, 10019, 10020, 10036, 10029, 10035, 10010, 10016, 10017, 10022, 10012, 10013, 10014, 10004, 10005, 10006, 10007, 10038, 10280, 10002, 10003, 10009, 10021, 10028, 10044, 10065, 10075, 10128, 10023, 10024, 10025, 10031, 10032, 10033, 10034, 10040]
    QN = [11361, 11362, 11363, 11364, 11354, 11355, 11356, 11357, 11358, 11359, 11360, 11365, 11366, 11367, 11412, 11423, 11432, 11433, 11434, 11435, 11436, 11101, 11102, 11103, 11104, 11105, 11106, 11374, 11375, 11379, 11385, 11691, 11692, 11693, 11694, 11695, 11697, 11004, 11005, 11411, 11413, 11422, 11426, 11427, 11428, 11429, 11414, 11415, 11416, 11417, 11418, 11419, 11420, 11421, 11368, 11369, 11370, 11372, 11373, 11377, 11378]
    SI = [10302, 10303, 10310, 10306, 10307, 10308, 10309, 10312, 10301, 10304, 10305, 10314]
    borough = ""
    if int(zipcode) in BK:
        borough = "Brooklyn"
    elif int(zipcode) in MH:
        borough = "Manhattan"
    elif int(zipcode) in QN:
        borough = "Queens"
    elif int(zipcode) in SI:
        borough = "Staten Island"    
    else:
        # Not a new york city zip code
        borough = "Unknown"
    return borough

def search_withQuery(request):
    '''Method to search with query from the database'''
    if request.method == 'GET':
        category = request.GET.getlist("gtype")
<<<<<<< HEAD
        day=request.GET.getlist("day")
        try:
            time = request.GET.getlist("dropdown")[0]
        except:
            time = '0,0'
=======
        day = request.GET.getlist("day")
        time = request.GET.getlist("dropdown")[0]
>>>>>>> 09c5c98a28060fae7b9d3de7f67f89f1a9a8cbb3
        zipcode = request.GET.getlist("zipcode")[0]
        borough = getBoroughFromZip(zipcode)
        '''Filter list by user selected categories determined borough'''
        result = list(RecyclingCenter.objects.filter(type__in=category).filter(borough=borough).values())
        '''Filter out closed facilties'''
        filter_day = []
        for e in result:
            for i in day:
                if e[i] != "closed":
                    filter_day.append(e)
        result = [dict(t) for t in set([tuple(d.items()) for d in filter_day])]
        '''Filter out facilities that don't match user's avaiable time'''
        checktime = []
        for d in day:
            temp = []
            for e in result:
                temp.append(e[d])
            checktime.append(temp)
        index = []
        for i in range(0,len(checktime[0])):
            for j in range(0,len(checktime)):
                if(checktime[j][i] == "closed"):
                    continue
                db_time = checktime[j][i].split(",")
                user_time = time.split(",")
                if int(db_time[0]) <= int(user_time[0]) and int(db_time[1]) >= int(user_time[1]):
                    index.append(i)
        '''Remove duplicates in the result'''
        index = list(set(index))
        result = [result[i] for i in index]
        return render(request,'mainRecycleApp/home.html', {"data": result})
