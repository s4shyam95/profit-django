from django.views.decorators.csrf import csrf_exempt
from profit.models import Category,SubCat,Goal,FitUser,Activity,WeightLog,Suggestions,Session,SessionActivity
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
import logging
from gcm import GCM
import requests
import json
import random
import string
# Create your views here.

@csrf_exempt
def register(request):
    u = FitUser()
    u.uuid = request.POST['uuid'].strip()
    u.save()
    return HttpResponse("Done")

@csrf_exempt
def updateGCM(request):
    u = FitUser.objects.get(uuid=request.POST['uuid'].strip())
    u.gcm = request.POST['gcm'].strip()
    u.save()
    return HttpResponse("Done")

def sendGCM(to, type, data1, sid, qid):
    logging.log(logging.ERROR, 2)
    gcm = GCM('AIzaSyD6-BUFptIOpKNrFv-Lz-6EHuHv07Hwg90')
    data = {'type': type, 'data': data1, 'sid': sid, 'qid': qid}
    reg_id = to
    gcm.plaintext_request(registration_id=reg_id, data=data)