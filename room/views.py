from rest_framework import viewsets, status
from room.models import User, Meeting
from room.serializers import UserSerializer, MeetingSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

@csrf_exempt
def getMeetingInfo_month(request):
    # 初始化該月份的 meeting info (default = [])
    result = {}
    for i in range(1,32):
        tmp = {}
        tmp["date"] = i
        tmp["meeting"] = []
        result[i] = tmp
    
    def add_dict(tmp_dict,index,data):
        return tmp_dict
    # 取 meeting table 的所有資料
    data = Meeting.objects.all()
    for i in range(len(data)):
        # 抓該年份以及該月份的 meeting 資料 
        if(data[i].start[0:4] == request.POST['year'] and data[i].start[5:7] == request.POST['month']):
            # 抓日期資料
            if(data[i].start[8:10] == "01"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room            
                result[1]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "02"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[2]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "03"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[3]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "04"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[4]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "05"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[5]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "06"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[6]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "07"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[7]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "08"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[8]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "09"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
            elif(data[i].start[8:10] == "10"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[10]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "11"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[11]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "12"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[12]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "13"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[13]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "14"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[14]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "15"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[15]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "16"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[16]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "17"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[17]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "18"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[18]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "19"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[19]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "20"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[20]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "21"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[21]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "22"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[22]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "23"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[23]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "24"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[24]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "25"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[25]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "26"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[26]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "27"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[27]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "28"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[28]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "29"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[29]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "30"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room 
                result[30]["meeting"].append(tmp_dict)
            elif(data[i].start[8:10] == "31"):
                tmp_dict = {}
                tmp_dict["topic"] = data[i].topic
                tmp_dict["host"] = data[i].host
                tmp_dict["start"] = data[i].start
                tmp_dict["end"] = data[i].end
                tmp_dict["attendee"] = data[i].attendee
                tmp_dict["room"] = data[i].room
                result[31]["meeting"].append(tmp_dict)

    return JsonResponse(result, safe=False)
@csrf_exempt
def getMeetingInfo_week(request):
    return JsonResponse({'result':1}, safe=False)

@csrf_exempt
def createReminder(request):
    return JsonResponse({'result':1}, safe=False)
@csrf_exempt
def create_meeting(request):
    topic = request.POST['topic']
    host = request.POST['host']
    start= request.POST['start']
    end = request.POST['end']
    attendee = request.POST['attendee']
    room = request.POST['room']
    meeting = Meeting(topic=topic,
                      host=host,
                      start=start,
                      end=end,
                      attendee=attendee,
                      room=room,
                      )
    meeting.save()
    return JsonResponse({"result":1}, safe=False)


@csrf_exempt
def meeting_update_view(request):
    meeting = Meeting.objects.get(pk=request.POST['id'])
    meeting.update(topic=request.POST["topic"],
                   host=request.POST["host"],
                   start=request.POST["start"],
                   end=request.POST["end"],
                   attendee=request.POST["attendee"],
                   room=request.POST["room"]
                   )
    return Response(meeting, status=status.HTTP_200_OK)

@csrf_exempt
def meeting_delete_view(request):
    meeting = Meeting.objects.get(pk=request.POST['id'])
    meeting.delete()
    return JsonResponse({'result':1})