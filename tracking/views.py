# from ast import Store
# import io, csv, pandas as pd
import os
from exqship.settings import BASE_DIR
import pandas as pd
# from django.dispatch import receiver
# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework import generics, status, mixins
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
import json
# from rest_framework.authtoken.views import ObtainAuthToken
# from turtle import width
from .serializer import (
    PriorityTrackingSerializer, 
    FileUploadSerializer, 
    FileUploadSerializer1, 
    FileUploadSerializer2, 
    FileUploadSerializer3, 
    FileUploadSerializer4,
    UserListSerializer, 
    ExpressPriorityTrackingSerializer, 
    SigPriorityTrackingSerializer, 
    SigExpressTrackingSerializer,
    FirstClassSerializer,
    # LabelDataSerializer,
    # GeeksSerializer
    )
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import (
    User,
    PriorityTracking,  
    ExpressPriorityTracking, 
    PriorityWithSigTracking, 
    ExpressWithSigPriorityTracking,
    FirstClassTracking,
    # LabelData
    )
from django.db import IntegrityError
from rest_framework.authentication import (
    SessionAuthentication, 
    BasicAuthentication, 
    TokenAuthentication)                                                            
from rest_framework.pagination import PageNumberPagination
from fpdf import FPDF, HTMLMixin
from django.http import FileResponse
from rest_framework.exceptions import ParseError


# Write to a file 
def write_to_file(user_id, incomingData):
    dir = os.path.join(BASE_DIR, 'notepad')

    if user_id == 1:
        user_id = 'f0af8242-ddaf-4fc1-8013-18642a1d71e5'
        file = open(dir + "/note_one.txt", 'w', encoding='utf-8')
        for dic in incomingData:
            json.dump(dic, file) 
            file.write('\n')
        file.close()
        return user_id

    elif user_id == 2:
        user_id = '5154acba-18ca-4f02-b00c-34e1cb9cc04e'
        file = open(dir + "/note_two.txt", 'w', encoding='utf-8')
        for dic in incomingData:
            json.dump(dic, file) 
            file.write('\n')
        file.close()
        return user_id

    elif user_id == 3:
        user_id = 'ac120371-6b1b-40e4-a956-d70ad44dd41f'
        file = open(dir + "/note_three.txt", 'w', encoding='utf-8')
        for dic in incomingData:
            json.dump(dic, file) 
            file.write('\n')
        file.close()
        return user_id
    
    elif user_id == 4:
        user_id = '10c36fd7-9beb-4374-a945-fb3786fbae4b'
        file = open(dir + "/note_four.txt", 'w', encoding='utf-8')
        for dic in incomingData:
            json.dump(dic, file) 
            file.write('\n')
        file.close()
        return user_id

    elif user_id == 5:
        user_id = 'af841f9d-f3be-48bb-b154-7f7e85d86b31'
        file = open(dir + "/note_five.txt", 'w', encoding='utf-8')
        for dic in incomingData:
            json.dump(dic, file) 
            file.write('\n')
        file.close()
        return user_id

    elif user_id == 6:
        user_id = '0d733d63-a016-4131-94d8-80d963df4e1a'
        file = open(dir + "/note_six.txt", 'w', encoding='utf-8')
        for dic in incomingData:
            json.dump(dic, file) 
            file.write('\n')
        file.close()
        return user_id

    elif user_id == 7:
        user_id = '44816688-342b-4fc1-a4c8-6ffa196b8122'
        file = open(dir + "/note_seven.txt", 'w', encoding='utf-8')
        for dic in incomingData:
            json.dump(dic, file)
            file.write('\n')
        file.close()
        return user_id


def write_fc(id):
    dir = os.path.join(BASE_DIR, 'notepad')

    if id == 'f0af8242-ddaf-4fc1-8013-18642a1d71e5':
        get_stored_data = []
        with open(dir + "/note_one.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info = list(map(lambda x:{x[0]:x[1]},senders_data.items()))
        receivers_info = list(map(lambda x:{x[0]:x[1]},receiver_data.items()))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/f.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/f2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')
        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} oz".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 10.5)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))

        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == '5154acba-18ca-4f02-b00c-34e1cb9cc04e':
        get_stored_data = []
        with open(dir + "/note_two.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/f.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/f2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')
        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} oz".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 10.5)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))

        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == 'ac120371-6b1b-40e4-a956-d70ad44dd41f':
        get_stored_data = []
        with open(dir + "/note_three.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/f.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/f2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')
        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} oz".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 10.5)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))

        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == '10c36fd7-9beb-4374-a945-fb3786fbae4b':
        get_stored_data = []
        with open(dir + "/note_four.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/f.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/f2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')
        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} oz".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 10.5)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))

        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == 'af841f9d-f3be-48bb-b154-7f7e85d86b31':
        get_stored_data = []
        with open(dir + "/note_five.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/f.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/f2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')
        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} oz".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 10.5)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))

        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == '0d733d63-a016-4131-94d8-80d963df4e1a':
        get_stored_data = []
        with open(dir + "/note_six.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/f.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/f2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')
        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} oz".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 10.5)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))

        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == '44816688-342b-4fc1-a4c8-6ffa196b8122':
        get_stored_data = []
        with open(dir + "/note_seven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/f.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/f2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')
        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} oz".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 10.5)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))

        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name
            

def write_es(id):
    dir = os.path.join(BASE_DIR, 'notepad')

    if id == 'f0af8242-ddaf-4fc1-8013-18642a1d71e5':
        get_stored_data = []
        with open(dir + "/note_one.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
    # get_stored_data = StoreData.my_store
    # senders_data = get_stored_data[0]
    # receiver_data = get_stored_data[1]
    # weight = get_stored_data[2]
    # barcode_target = get_stored_data[3]
    # number_data = get_stored_data[4]
    # today_date = get_stored_data[5]
    # sender_name = get_stored_data[6]
    # id = id
    # print('new id is: ',id)
    # get_stored_data = []

    # if id == '2':
    #     with open("sheetone.txt", 'r') as f:
    #         for line in f:
    #             get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        # pdf.set_xy(98.55, 72)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE REQUIRED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(142.4, 158, 'USPS SIGNATURE TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 162.95, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name
        # return FileResponse(open('./files/{}.pdf'.format(sender_name), 'rb'), as_attachment=True, content_type='application/pdf')
    elif id == '5154acba-18ca-4f02-b00c-34e1cb9cc04e':
        get_stored_data = []
        with open(dir + "/note_two.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
     
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        # pdf.set_xy(98.55, 72)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE REQUIRED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(142.4, 158, 'USPS SIGNATURE TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 162.95, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == 'ac120371-6b1b-40e4-a956-d70ad44dd41f':
        get_stored_data = []
        with open(dir + "/note_three.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
     
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        # pdf.set_xy(98.55, 72)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE REQUIRED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(142.4, 158, 'USPS SIGNATURE TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 162.95, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == '10c36fd7-9beb-4374-a945-fb3786fbae4b':
        get_stored_data = []
        with open(dir + "/note_four.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
     
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        # pdf.set_xy(98.55, 72)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE REQUIRED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(142.4, 158, 'USPS SIGNATURE TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 162.95, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name
    
    elif id == 'af841f9d-f3be-48bb-b154-7f7e85d86b31':
        get_stored_data = []
        with open(dir + "/note_five.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
     
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        # pdf.set_xy(98.55, 72)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE REQUIRED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(142.4, 158, 'USPS SIGNATURE TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 162.95, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == '0d733d63-a016-4131-94d8-80d963df4e1a':
        get_stored_data = []
        with open(dir + "/note_six.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
     
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        # pdf.set_xy(98.55, 72)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE REQUIRED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(142.4, 158, 'USPS SIGNATURE TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 162.95, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name
    
    elif id == '44816688-342b-4fc1-a4c8-6ffa196b8122':
        get_stored_data = []
        with open(dir + "/note_seven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
     
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        # pdf.set_xy(98.55, 72)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE REQUIRED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(142.4, 158, 'USPS SIGNATURE TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 162.95, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name


def write_e(id):
    dir = os.path.join(BASE_DIR, 'notepad')

    if id == 'f0af8242-ddaf-4fc1-8013-18642a1d71e5':
        get_stored_data = []
        with open(dir + "/note_one.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE WAIVED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name
        # return FileResponse(open('./files/{}.pdf'.format(sender_name), 'rb'), as_attachment=True, content_type='application/pdf')
    
    elif id == '5154acba-18ca-4f02-b00c-34e1cb9cc04e':
        get_stored_data = []
        with open(dir + "/note_two.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE WAIVED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == 'ac120371-6b1b-40e4-a956-d70ad44dd41f':
        get_stored_data = []
        with open(dir + "/note_three.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE WAIVED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == '10c36fd7-9beb-4374-a945-fb3786fbae4b':
        get_stored_data = []
        with open(dir + "/note_four.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE WAIVED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == 'af841f9d-f3be-48bb-b154-7f7e85d86b31':
        get_stored_data = []
        with open(dir + "/note_five.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE WAIVED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name
    
    elif id == '0d733d63-a016-4131-94d8-80d963df4e1a':
        get_stored_data = []
        with open(dir + "/note_six.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE WAIVED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == '44816688-342b-4fc1-a4c8-6ffa196b8122':
        get_stored_data = []
        with open(dir + "/note_seven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 14)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
        pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 54.3, 252.45, 54.3)
        pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 69.5, 252.45, 69.5)
        pdf.set_xy(207, 71.5)
        pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(211, 79)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 5.8
                incre = 71.5 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        pdf.set_font('helvetica', '', 13.7)
        pdf.text(100.1, 102, 'SIGNATURE WAIVED')

        pdf.set_font('helvetica', '', 14.8)
        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 15.4)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 151.5, 252.45, 151.5)
        pdf.set_font('helvetica', 'B', 11.2)  
        pdf.text(155.4, 158, 'USPS TRACKING #EP')

        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 196, "{}".format(number_data))
        pdf.line(98.55, 197.10, 252.45, 197.10)
        pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name


def write_ps(id):
    dir = os.path.join(BASE_DIR, 'notepad')

    if id == 'f0af8242-ddaf-4fc1-8013-18642a1d71e5':
        get_stored_data = []

        with open(dir + "/note_one.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')
        
        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)
        
        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        # for line in sales:
        #     pdf.cell(170, 6, f"{line['item'].ljust(30)} {line['amount'].rjust(15)}", 0, 1,'L')
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')
        # pdf.cell(50, 6, "Ship Date:07/29/22", 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')


        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(140.4, 159, 'USPS SIGNATURE TRACKING #EP')
        # pdf.image(image_url)
        # pdf.image("{}".format(image_url))
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        # pdf.text(137.5, 197, '9210 3564 7281 3047 3532 7281 31')
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')  
        return sender_name 

    elif id == '5154acba-18ca-4f02-b00c-34e1cb9cc04e':
        get_stored_data = []
        with open(dir + "/note_two.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')
        
        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)
        
        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        # for line in sales:
        #     pdf.cell(170, 6, f"{line['item'].ljust(30)} {line['amount'].rjust(15)}", 0, 1,'L')
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')
        # pdf.cell(50, 6, "Ship Date:07/29/22", 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')


        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(140.4, 159, 'USPS SIGNATURE TRACKING #EP')
        # pdf.image(image_url)
        # pdf.image("{}".format(image_url))
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        # pdf.text(137.5, 197, '9210 3564 7281 3047 3532 7281 31')
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')  
        return sender_name   

    elif id == 'ac120371-6b1b-40e4-a956-d70ad44dd41f':
        get_stored_data = []
        with open(dir + "/note_three.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')
        
        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)
        
        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        # for line in sales:
        #     pdf.cell(170, 6, f"{line['item'].ljust(30)} {line['amount'].rjust(15)}", 0, 1,'L')
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')
        # pdf.cell(50, 6, "Ship Date:07/29/22", 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')


        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(140.4, 159, 'USPS SIGNATURE TRACKING #EP')
        # pdf.image(image_url)
        # pdf.image("{}".format(image_url))
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        # pdf.text(137.5, 197, '9210 3564 7281 3047 3532 7281 31')
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')  
        return sender_name 

    elif id == '10c36fd7-9beb-4374-a945-fb3786fbae4b':
        get_stored_data = []
        with open(dir + "/note_four.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')
        
        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)
        
        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        # for line in sales:
        #     pdf.cell(170, 6, f"{line['item'].ljust(30)} {line['amount'].rjust(15)}", 0, 1,'L')
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')
        # pdf.cell(50, 6, "Ship Date:07/29/22", 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')


        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(140.4, 159, 'USPS SIGNATURE TRACKING #EP')
        # pdf.image(image_url)
        # pdf.image("{}".format(image_url))
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        # pdf.text(137.5, 197, '9210 3564 7281 3047 3532 7281 31')
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')  
        return sender_name 

    elif id == 'af841f9d-f3be-48bb-b154-7f7e85d86b31':
        get_stored_data = []
        with open(dir + "/note_five.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')
        
        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)
        
        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        # for line in sales:
        #     pdf.cell(170, 6, f"{line['item'].ljust(30)} {line['amount'].rjust(15)}", 0, 1,'L')
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')
        # pdf.cell(50, 6, "Ship Date:07/29/22", 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')


        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(140.4, 159, 'USPS SIGNATURE TRACKING #EP')
        # pdf.image(image_url)
        # pdf.image("{}".format(image_url))
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        # pdf.text(137.5, 197, '9210 3564 7281 3047 3532 7281 31')
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')  
        return sender_name 

    elif id == '0d733d63-a016-4131-94d8-80d963df4e1a':
        get_stored_data = []
        with open(dir + "/note_six.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')
        
        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)
        
        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        # for line in sales:
        #     pdf.cell(170, 6, f"{line['item'].ljust(30)} {line['amount'].rjust(15)}", 0, 1,'L')
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')
        # pdf.cell(50, 6, "Ship Date:07/29/22", 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')


        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(140.4, 159, 'USPS SIGNATURE TRACKING #EP')
        # pdf.image(image_url)
        # pdf.image("{}".format(image_url))
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        # pdf.text(137.5, 197, '9210 3564 7281 3047 3532 7281 31')
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')  
        return sender_name 

    elif id == '44816688-342b-4fc1-a4c8-6ffa196b8122':
        get_stored_data = []
        with open(dir + "/note_seven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

    
        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')
        
        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)
        
        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        # for line in sales:
        #     pdf.cell(170, 6, f"{line['item'].ljust(30)} {line['amount'].rjust(15)}", 0, 1,'L')
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')
        # pdf.cell(50, 6, "Ship Date:07/29/22", 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]:
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')


        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(140.4, 159, 'USPS SIGNATURE TRACKING #EP')
        # pdf.image(image_url)
        # pdf.image("{}".format(image_url))
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        # pdf.text(137.5, 197, '9210 3564 7281 3047 3532 7281 31')
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')  
        return sender_name 


def write_p(id):
    dir = os.path.join(BASE_DIR, 'notepad')

    if id == 'f0af8242-ddaf-4fc1-8013-18642a1d71e5':
        get_stored_data = []

        with open(dir + "/note_one.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]: 
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(155.4, 159, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == '5154acba-18ca-4f02-b00c-34e1cb9cc04e':
        get_stored_data = []

        with open(dir + "/note_two.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]: 
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(155.4, 159, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == 'ac120371-6b1b-40e4-a956-d70ad44dd41f':
        get_stored_data = []

        with open(dir + "/note_three.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]: 
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(155.4, 159, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == '10c36fd7-9beb-4374-a945-fb3786fbae4b':
        get_stored_data = []

        with open(dir + "/note_four.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]: 
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(155.4, 159, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == 'af841f9d-f3be-48bb-b154-7f7e85d86b31':
        get_stored_data = []

        with open(dir + "/note_five.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]: 
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(155.4, 159, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == '0d733d63-a016-4131-94d8-80d963df4e1a':
        get_stored_data = []

        with open(dir + "/note_six.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]: 
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(155.4, 159, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    elif id == '44816688-342b-4fc1-a4c8-6ffa196b8122':
        get_stored_data = []

        with open(dir + "/note_seven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        senders_data = get_stored_data[0]
        receiver_data = get_stored_data[1]
        weight = get_stored_data[2].replace('"', '')
        barcode_target = get_stored_data[3].replace('"', '')
        number_data = get_stored_data[4].replace('"', '')
        today_date = get_stored_data[5].replace('"', '')
        sender_name = get_stored_data[6].replace('"', '')

        senders_data = json.loads(senders_data)
        receiver_data = json.loads(receiver_data)

        senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
        receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

        pdf = MyFPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 15)
        pdf.set_line_width(0.8)
        pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
        pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 55.3, 252.45, 55.3)
        pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
        pdf.line(98.55, 70.5, 252.45, 70.5)
        pdf.set_xy(98.55, 73)
        pdf.set_xy(204.5, 72.5)
        pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')

        pdf.set_xy(212, 80)
        pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
        
        for index in range(len(senders_info)):
            for key in senders_info[index]: 
                incre_by_one = index * 6
                incre = 73 + incre_by_one
                pdf.set_xy(99, incre)
                pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

        for index in range(len(receivers_info)):
            for key in receivers_info[index]:
                incre_by_one = index * 6
                incre = 119.5 + incre_by_one
                pdf.set_xy(118.5, incre)
                pdf.set_font('helvetica', '', 14.8)
                pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

        pdf.line(98.55, 153, 252.45, 153)
        pdf.set_font('helvetica', 'B', 12)  
        pdf.text(155.4, 159, 'USPS TRACKING #EP')
        pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
        pdf.set_font('helvetica', 'B', 13.5)  
        pdf.text(137.5, 197, "{}".format(number_data))
        pdf.line(98.55, 198.55, 252.45, 198.55)
        pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
        pdf.output('./files/{}.pdf'.format(sender_name), 'F')
        return sender_name

    
    # return FileResponse(open('./files/{}.pdf'.format(sender_name), 'rb'), as_attachment=True, content_type='application/pdf')

# Pagination Class

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 50


class StoreData:
    my_store = 'red'

    def __init__(self, x):
        self.x = x

    def show(self):
        print(f"{self.x}")

class MyFPDF(FPDF, HTMLMixin):
	pass


# This  block contains FC
################################################################################
################################################################################


# Get number of fc count
class FirstClasTrackingCount(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = FirstClassTracking.objects.filter(user_id=request.user.id).count() 
        return Response({"fcount" : qs})


# Upload fc numbers
class UploadFirstClassTracking(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FileUploadSerializer4

    def post(self, request, *args, **kwargs):
        mydata = []
        # Get user trying to upload tracking
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                requested_user = ss.user

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
   
        if not file.name.endswith('.csv'):
            return Response({"status": "unsupported file"}, status.HTTP_406_NOT_ACCEPTABLE) 

        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = FirstClassTracking(
                       first_class = row[0],
                       user = requested_user
                       )
            mydata.append(new_file)
            if len(new_file.first_class) < 26:
                return Response({"status": "forbidden",
                                "incomplete_number": f"{new_file.first_class}"}, status.HTTP_403_FORBIDDEN)

        for number in mydata:
            if FirstClassTracking.objects.filter(first_class=number.first_class).exists():
                return Response({"existed_number": number.first_class})

        try:
            FirstClassTracking.objects.bulk_create(mydata)
            return Response({"success": "success"}, status.HTTP_201_CREATED)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)
                    
        return Response({"status": "success"}, status.HTTP_201_CREATED)


# Delete all first class numbers
class DeleteAllFirstClassNumber(APIView):
    def delete(self, request, *args, **kwargs):
        # incomplete....filter deletion by user
        qs = FirstClassTracking.objects.all()
        qs.delete()
        return Response('You have sucessfully deleted all fc numbers')


# Delete selected single first class numbers on select 
class DeleteSingleFirstClassNumber(APIView):
    def delete(self, request, selected=None):
        selectedNumber = selected.split(",") 
        for index in range(0, len(selectedNumber)):
            qs = FirstClassTracking.objects.filter(first_class=selectedNumber[index])
            qs.delete()
        return Response('Successfully deleted')


# Get first ten numbers by a user
class ListFirstClassTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = FirstClassTracking.objects.all()
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = FirstClassTracking.objects.filter(user_id=ss.user.pk)[:10]

        serializer = FirstClassSerializer(qs, many=True)
        if request.user:
            return Response(serializer.data)


# Get list of all fc numbers by user
class FirstClassTrackingSets(generics.ListAPIView):
    serializer_class = FirstClassSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user_id = self.request.user.id
        return FirstClassTracking.objects.filter(user_id=user_id)


# Delete Number to be used
class DeleteFirstClassTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, first_class=None):
        qs = FirstClassTracking.objects.filter(first_class=first_class)
        if qs.exists():
            qs.delete()
            return Response('number has been successfully deleted')
        else:
            raise ParseError('number has been used')


# Get required data
class GetDataFirstClass(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        incomingData = request.data
        user_id = request.user.id

        uuid = write_to_file(user_id, incomingData)
        # return Response('http://127.0.0.1:8000/download/fc/{}'.format(uuid))
        return Response('https://texclusive.herokuapp.com/download/fc/{}'.format(uuid))
        # return Response('https://texclusive.herokuapp.com/report/fc')




def download_fc(request, id):
    sender = write_fc(id)
    return FileResponse(open('./files/{}.pdf'.format(sender), 'rb'), as_attachment=True, content_type='application/pdf')
    # get_stored_data = StoreData.my_store
    # senders_data = get_stored_data[0]
    # receiver_data = get_stored_data[1]
    # weight = get_stored_data[2]
    # barcode_target = get_stored_data[3]
    # number_data = get_stored_data[4]
    # today_date = get_stored_data[5]
    # sender_name = get_stored_data[6]
    # print('new id is: ',id)
    # id = id
    # get_stored_data = []

    # if id == '2':
    #     with open("sheetone.txt", 'r') as f:
    #         for line in f:
    #             get_stored_data.append(line.strip())

    #     senders_data = get_stored_data[0]
    #     receiver_data = get_stored_data[1]
    #     weight = get_stored_data[2].replace('"', '')
    #     barcode_target = get_stored_data[3].replace('"', '')
    #     number_data = get_stored_data[4].replace('"', '')
    #     today_date = get_stored_data[5].replace('"', '')
    #     sender_name = get_stored_data[6].replace('"', '')

    #     senders_data = json.loads(senders_data)
    #     receiver_data = json.loads(receiver_data)

    #     senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
    #     receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

    #     pdf = MyFPDF('L', 'mm', 'letter')
    #     pdf.add_page()
    #     pdf.set_font('helvetica', '', 14)
    #     pdf.set_line_width(0.8)
    #     pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
    #     pdf.image("media/images/f.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
    #     pdf.line(98.55, 54.3, 252.45, 54.3)
    #     pdf.image("media/images/f2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
    #     pdf.line(98.55, 69.5, 252.45, 69.5)
    #     # pdf.set_xy(98.55, 72)
    #     pdf.set_xy(207, 71.5)
    #     pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

    #     pdf.set_xy(211, 79)
    #     pdf.cell(40, 3, "Weight: {} oz".format(weight), 0, 1,'R')

    #     for index in range(len(senders_info)):
    #         for key in senders_info[index]:
    #             incre_by_one = index * 5.8
    #             incre = 71.5 + incre_by_one
    #             pdf.set_xy(99, incre)
    #             pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

    #     pdf.set_font('helvetica', '', 14.8)
    #     for index in range(len(receivers_info)):
    #         for key in receivers_info[index]:
    #             incre_by_one = index * 6
    #             incre = 119 + incre_by_one
    #             pdf.set_xy(118.5, incre)
    #             pdf.set_font('helvetica', '', 15.4)
    #             pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

    #     pdf.line(98.55, 151.5, 252.45, 151.5)
    #     pdf.set_font('helvetica', 'B', 10.5)  
    #     pdf.text(155.4, 158, 'USPS TRACKING #EP')
    #     pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    #     pdf.set_font('helvetica', 'B', 13.5)  
    #     pdf.text(137.5, 196, "{}".format(number_data))

    #     pdf.line(98.55, 197.10, 252.45, 197.10)
    #     pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
    #     pdf.output('./files/{}.pdf'.format(sender_name), 'F')
    #     return FileResponse(open('./files/{}.pdf'.format(sender_name), 'rb'), as_attachment=True, content_type='application/pdf')


# End of FC section
##################################################################################################
##################################################################################################
##################################################################################################


# This block begins ES
##################################################################################################
##################################################################################################
##################################################################################################


# Get ES count by user
class SigExpressTrackingCount(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = ExpressWithSigPriorityTracking.objects.filter(user_id=request.user.id).count()
        return Response({"pcountexpsig" : qs})


class UploadSigExpressPriorityTracking(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = FileUploadSerializer3
   
    def post(self, request, *args, **kwargs):
        mydata = []
        # Get user trying to upload tracking
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                requested_user = ss.user
                
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
   
        if not file.name.endswith('.csv'):
            return Response({"status": "unsupported file"}, status.HTTP_406_NOT_ACCEPTABLE) 

        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = ExpressWithSigPriorityTracking(
                       express_priority_with_sig = row[0],
                       user = requested_user
                       )
            mydata.append(new_file)

            if len(new_file.express_priority_with_sig) < 26:
                return Response({"status": "forbidden",
                                "incomplete_number": f"{new_file.express_priority_with_sig}"})
        
                
            # elif ExpressWithSigPriorityTracking.objects.filter(express_priority_with_sig=new_file.express_priority_with_sig).exists():
            #     print(ExpressWithSigPriorityTracking.objects.filter(express_priority_with_sig=new_file.express_priority_with_sig).exists())
            #     return Response({"status": "Duplicate data found"}, status.HTTP_404_FORBIDDEN)

            # try:
            #     ExpressWithSigPriorityTracking.objects.bulk_create([new_file])
            #     # new_file.save()
            # except IntegrityError as e:
            #     if 'UNIQUE constraint' in str(e.args):
            #         return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)
        for number in mydata:
            # print(x.express_priority_with_sig)
            if ExpressWithSigPriorityTracking.objects.filter(express_priority_with_sig=number.express_priority_with_sig).exists():
                return Response({"status": "Duplicate data found",
                                 "existed_number": f"{number.express_priority_with_sig}"})

        try:
            ExpressWithSigPriorityTracking.objects.bulk_create(mydata)
            return Response({"success": "success"}, status.HTTP_201_CREATED)
            # new_file.save()
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)

        # return Response({"success": "success"}, status.HTTP_201_CREATED)


# Delete all express with sig numbers
class DeleteAllExpressWithSigNumber(APIView):
    def delete(self, request, *args, **kwargs):
        qs = ExpressWithSigPriorityTracking.objects.all()
        qs.delete()
        return Response('You have sucessfully deleted all express with sig numbers')


# Delete selected single es numbers
class DeleteFromExpressWithSigNumber(APIView):
    def delete(self, request, selected=None):
        selectedNumber = selected.split(",") 
        for index in range(0, len(selectedNumber)):
            qs = ExpressWithSigPriorityTracking.objects.filter(express_priority_with_sig=selectedNumber[index])
            qs.delete()
        return Response('Working.....now on express with sig numbers')


# get all es by user
class ExpressWithSigTrackingSets(generics.ListAPIView):
    # queryset = ExpressWithSigPriorityTracking.objects.all()
    serializer_class = SigExpressTrackingSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user_id = self.request.user.id
        return ExpressWithSigPriorityTracking.objects.filter(user_id=user_id)        


# get first es ten numbers
class ListSigExpressPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = ExpressPriorityTracking.objects.all()
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = ExpressWithSigPriorityTracking.objects.filter(user_id=ss.user.pk)[:10]

        serializer = SigExpressTrackingSerializer(qs, many=True)
        if request.user:
            return Response(serializer.data)


# delete number to be used
class DeleteSigExpressPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, express_priority_with_sig=None):
        qs = ExpressWithSigPriorityTracking.objects.filter(express_priority_with_sig=express_priority_with_sig)
        if qs.exists():
            qs.delete()
            return Response('number has been successfully deleted')
        else:
            raise ParseError('number has been used')


#Get data for express with sig  
class GetDataExpressSig(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        incomingData = request.data
        # StoreData.my_store = incomingData
        user_id = request.user.id
        uuid = write_to_file(user_id, incomingData)
        return Response('https://texclusive.herokuapp.com/download/es/{}'.format(uuid))
        # return Response('http://127.0.0.1:8000/download/es/{}'.format(uuid))
        
      
        # if request.user.id == 2:
        #     file = open("sheetone.txt", 'w', encoding='utf-8')
        #     for dic in incomingData:
        #         json.dump(dic, file) 
        #         file.write('\n')
        #     file.close()
    

        # file = open("sample.txt", 'w', encoding='utf-8')
        # for dic in incomingData:
        #     json.dump(dic, file) 
        #     file.write('\n')
        # file.close()
           
        # return Response('http://127.0.0.1:8000/download/es/{}'.format(request.user.id))
        # return Response('https://texclusive.herokuapp.com/download/es')


def download_es(request, id):
    sender = write_es(id)
    return FileResponse(open('./files/{}.pdf'.format(sender), 'rb'), as_attachment=True, content_type='application/pdf')
    # get_stored_data = StoreData.my_store
    # senders_data = get_stored_data[0]
    # receiver_data = get_stored_data[1]
    # weight = get_stored_data[2]
    # barcode_target = get_stored_data[3]
    # number_data = get_stored_data[4]
    # today_date = get_stored_data[5]
    # sender_name = get_stored_data[6]
    # id = id
    # print('new id is: ',id)
    # # get_stored_data = []

    # # if id == '2':
    # #     with open("sheetone.txt", 'r') as f:
    # #         for line in f:
    # #             get_stored_data.append(line.strip())

    # # senders_data = get_stored_data[0]
    # # receiver_data = get_stored_data[1]
    # # weight = get_stored_data[2].replace('"', '')
    # # barcode_target = get_stored_data[3].replace('"', '')
    # # number_data = get_stored_data[4].replace('"', '')
    # # today_date = get_stored_data[5].replace('"', '')
    # # sender_name = get_stored_data[6].replace('"', '')

    # # senders_data = json.loads(senders_data)
    # # receiver_data = json.loads(receiver_data)

    # senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
    # receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

    # pdf = MyFPDF('L', 'mm', 'letter')
    # pdf.add_page()
    # pdf.set_font('helvetica', '', 14)
    # pdf.set_line_width(0.8)
    # pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
    # pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
    # pdf.line(98.55, 54.3, 252.45, 54.3)
    # pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
    # pdf.line(98.55, 69.5, 252.45, 69.5)
    # # pdf.set_xy(98.55, 72)
    # pdf.set_xy(207, 71.5)
    # pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

    # pdf.set_xy(211, 79)
    # pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

    # for index in range(len(senders_info)):
    #     for key in senders_info[index]:
    #         incre_by_one = index * 5.8
    #         incre = 71.5 + incre_by_one
    #         pdf.set_xy(99, incre)
    #         pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

    # pdf.set_font('helvetica', '', 13.7)
    # pdf.text(100.1, 102, 'SIGNATURE REQUIRED')

    # pdf.set_font('helvetica', '', 14.8)
    # for index in range(len(receivers_info)):
    #     for key in receivers_info[index]:
    #         incre_by_one = index * 6
    #         incre = 119 + incre_by_one
    #         pdf.set_xy(118.5, incre)
    #         pdf.set_font('helvetica', '', 15.4)
    #         pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

    # pdf.line(98.55, 151.5, 252.45, 151.5)
    # pdf.set_font('helvetica', 'B', 11.2)  
    # pdf.text(142.4, 158, 'USPS SIGNATURE TRACKING #EP')

    # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
    # # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 162.95, w = 140.45, h = 26.4, type = '', link = '')
    # pdf.set_font('helvetica', 'B', 13.5)  
    # pdf.text(137.5, 196, "{}".format(number_data))
    # pdf.line(98.55, 197.10, 252.45, 197.10)
    # pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
    # pdf.output('./files/{}.pdf'.format(sender_name), 'F')
    # return FileResponse(open('./files/{}.pdf'.format(sender_name), 'rb'), as_attachment=True, content_type='application/pdf')

#End of ES
###############################################################################################
###############################################################################################
###############################################################################################
             

# This block is the  begining of E
###############################################################################################
###############################################################################################
###############################################################################################


# Get the count of express
class ExpressTrackingCount(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = ExpressPriorityTracking.objects.filter(user_id=request.user.id).count()
        return Response({"pcountexp" : qs})



class UploadExpressPriorityTracking(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FileUploadSerializer1
   
    def post(self, request, *args, **kwargs):
        mydata = []
        # Get user trying to upload tracking
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                requested_user = ss.user
                
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
   
        if not file.name.endswith('.csv'):
            return Response({"status": "unsupported file"}, status.HTTP_406_NOT_ACCEPTABLE) 

        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = ExpressPriorityTracking(
                       express_priority = row[0],
                    #    priority = row['priority'],
                       user = requested_user
                       )
            mydata.append(new_file)

            if len(new_file.express_priority) < 26:
                return Response({"status": "forbidden",
                                "incomplete_number": f"{new_file.express_priority}"}, status.HTTP_403_FORBIDDEN)

        for number in mydata:
            if ExpressPriorityTracking.objects.filter(express_priority=number.express_priority).exists():
                return Response({"existed_number": number.express_priority})

        try:
            ExpressPriorityTracking.objects.bulk_create(mydata)
            return Response({"success": "success"}, status.HTTP_201_CREATED)
            # new_file.save()
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)

        return Response({"status": "success"}, status.HTTP_201_CREATED)


#Delete all express numbers
class DeleteAllPriorityExpressNumber(APIView):
    def delete(self, request, *args, **kwargs):
        qs = ExpressPriorityTracking.objects.all()
        # qs.delete()
        print(qs)
        return Response('You have sucessfully deleted all express numbers')


#Delete selected express number
class DeleteFromPriorityExpressTrackingList(APIView):
    def delete(self, request, selected=None):
        selectedNumber = selected.split(",") 
        for index in range(0, len(selectedNumber)):
            qs = ExpressPriorityTracking.objects.filter(express_priority=selectedNumber[index])
            qs.delete()
            print(selectedNumber[index])
        return Response('Working.....now on express')


# Get all sets of e numbers 
class ExpressPriorityTrackingSets(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # queryset = ExpressPriorityTracking.objects.all()
    serializer_class = ExpressPriorityTrackingSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user_id = self.request.user.id
        return ExpressPriorityTracking.objects.filter(user_id=user_id)


# Delete the number to be used by user
class DeleteExpressPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, express_priority=None):
        qs = ExpressPriorityTracking.objects.filter(express_priority=express_priority)
        if qs.exists():
            qs.delete()
            return Response('number has been successfully deleted')
        else:
            raise ParseError('number has been used')
            # return Response('no match found')


# Get the first ten of e numbers
class ListExpressPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = ExpressPriorityTracking.objects.all()
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = ExpressPriorityTracking.objects.filter(user_id=ss.user.pk)[:10]

        serializer = ExpressPriorityTrackingSerializer(qs, many=True)
        if request.user:
            return Response(serializer.data)


# Get data for E
class GetDataExp(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        incomingData = request.data
        user_id = request.user.id
        # StoreData.my_store = incomingData
        uuid = write_to_file(user_id, incomingData)
        return Response('https://texclusive.herokuapp.com/download/e/{}'.format(uuid))
        # return Response('http://127.0.0.1:8000/download/e/{}'.format(uuid))
 
        # if request.user.id == 2:
        #     file = open("sheetone.txt", 'w', encoding='utf-8')
        #     for dic in incomingData:
        #         json.dump(dic, file) 
        #         file.write('\n')
        #     file.close()
    

        # file = open("sample.txt", 'w', encoding='utf-8')
        # for dic in incomingData:
        #     json.dump(dic, file) 
        #     file.write('\n')
        # file.close()
           
        # return Response('http://127.0.0.1:8000/download/e/{}'.format(request.user.id))

        # return Response('https://texclusive.herokuapp.com/report/exp')


def download_e(request, id):
    sender = write_e(id)
    return FileResponse(open('./files/{}.pdf'.format(sender), 'rb'), as_attachment=True, content_type='application/pdf')
    # get_stored_data = StoreData.my_store
    # senders_data = get_stored_data[0]
    # receiver_data = get_stored_data[1]
    # weight = get_stored_data[2]
    # barcode_target = get_stored_data[3]
    # number_data = get_stored_data[4]
    # today_date = get_stored_data[5]
    # sender_name = get_stored_data[6]
    
    # id = id
    # print('new id is: ',id)
    # get_stored_data = []

    # if id == '2':
    #     with open("sheetone.txt", 'r') as f:
    #         for line in f:
    #             get_stored_data.append(line.strip())

    # senders_data = get_stored_data[0]
    # receiver_data = get_stored_data[1]
    # weight = get_stored_data[2].replace('"', '')
    # barcode_target = get_stored_data[3].replace('"', '')
    # number_data = get_stored_data[4].replace('"', '')
    # today_date = get_stored_data[5].replace('"', '')
    # sender_name = get_stored_data[6].replace('"', '')

    # senders_data = json.loads(senders_data)
    # receiver_data = json.loads(receiver_data)

    # senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
    # receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

    # pdf = MyFPDF('L', 'mm', 'letter')
    # pdf.add_page()
    # pdf.set_font('helvetica', '', 14)
    # pdf.set_line_width(0.8)
    # pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
    # pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
    # pdf.line(98.55, 54.3, 252.45, 54.3)
    # pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
    # pdf.line(98.55, 69.5, 252.45, 69.5)
    # # pdf.set_xy(98.55, 72)
    # pdf.set_xy(207, 71.5)
    # pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

    # pdf.set_xy(211, 79)
    # pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')

    # for index in range(len(senders_info)):
    #     for key in senders_info[index]:
    #         incre_by_one = index * 5.8
    #         incre = 71.5 + incre_by_one
    #         pdf.set_xy(99, incre)
    #         pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

    # pdf.set_font('helvetica', '', 13.7)
    # pdf.text(100.1, 102, 'SIGNATURE WAIVED')

    # pdf.set_font('helvetica', '', 14.8)
    # for index in range(len(receivers_info)):
    #     for key in receivers_info[index]:
    #         incre_by_one = index * 6
    #         incre = 119 + incre_by_one
    #         pdf.set_xy(118.5, incre)
    #         pdf.set_font('helvetica', '', 15.4)
    #         pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

    # pdf.line(98.55, 151.5, 252.45, 151.5)
    # pdf.set_font('helvetica', 'B', 11.2)  
    # pdf.text(155.4, 158, 'USPS TRACKING #EP')

    # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
    # # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 162.95, w = 140.45, h = 26.4, type = '', link = '')
    # pdf.set_font('helvetica', 'B', 13.5)  
    # pdf.text(137.5, 196, "{}".format(number_data))
    # pdf.line(98.55, 197.10, 252.45, 197.10)
    # pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
    # pdf.output('./files/{}.pdf'.format(sender_name), 'F')
    # return FileResponse(open('./files/{}.pdf'.format(sender_name), 'rb'), as_attachment=True, content_type='application/pdf')


# End section of E
###################################################################################################
###################################################################################################
###################################################################################################


# PS blocks starts here
###################################################################################################
###################################################################################################
###################################################################################################



# Get the count of ps
class SigPriorityTrackingCount(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        # for user in User.objects.all():
        #     ss, token = Token.objects.get_or_create(user=user)
        #     if ss.user.pk == request.user.id:
        qs = PriorityWithSigTracking.objects.filter(user_id=request.user.id).count()
        return Response({"psigcount" : qs})


# Upload ps numbers
class UploadSigPriorityTracking(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = FileUploadSerializer2
   
    def post(self, request, *args, **kwargs):
        # Get user trying to upload tracking
        mydata = []

        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                requested_user = ss.user
                
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
   
        if not file.name.endswith('.csv'):
            return Response({"status": "unsupported file"}, status.HTTP_406_NOT_ACCEPTABLE) 

        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = PriorityWithSigTracking(
                       priority_with_sig = row[0],
                    #    priority = row['priority'],
                       user = requested_user
                       )
            mydata.append(new_file)
            if len(new_file.priority_with_sig) < 26:
                return Response({"status": "forbidden",
                                "incomplete_number": f"{new_file.priority_with_sig}"}, status.HTTP_403_FORBIDDEN)

        
        for number in mydata:
            if PriorityWithSigTracking.objects.filter(priority_with_sig=number.priority_with_sig).exists():
                return Response({"existed_number": number.priority_with_sig})
                 

        try:
            PriorityWithSigTracking.objects.bulk_create(mydata)
            return Response({"success": "success"}, status.HTTP_201_CREATED)
            # new_file.save()
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                return Response({"status": "duplicate found"})

        return Response({"status": "success"}, status.HTTP_201_CREATED)


# Delete all priority with sig numbers
class DeleteAllPriorityWithSigNumber(APIView):
    def delete(self, request, *args, **kwargs):
        qs = PriorityWithSigTracking.objects.all()
        qs.delete()
        return Response('You have sucessfully deleted all priority with sig numbers')


# Delete single selected priority with sig numbers
class DeleteFromPriorityWithSigNumber(APIView):
    def delete(self, request, selected=None):
        selectedNumber = selected.split(",") 
        for index in range(0, len(selectedNumber)):
            qs = PriorityWithSigTracking.objects.filter(priority_with_sig=selectedNumber[index])
            qs.delete()
            # print(selectedNumber[index])
        return Response('Working.....now on priority with sig numbers')


# Get PS numbers with pagination
class PriorityWithSigTrackingSets(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # queryset = PriorityWithSigTracking.objects.all()
    serializer_class = SigPriorityTrackingSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user_id = self.request.user.id
        return PriorityWithSigTracking.objects.filter(user_id=user_id)
  


# Delete PS number to used by user
class DeleteSigPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, priority_with_sig=None):
        qs = PriorityWithSigTracking.objects.filter(priority_with_sig=priority_with_sig)
        if qs.exists():
            qs.delete()
            return Response('number has been successfully deleted')
        else:
            raise ParseError('number has been used')


# Get first ten numbers of PS
class ListSigPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = PriorityWithSigTracking.objects.all()
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = PriorityWithSigTracking.objects.filter(user_id=ss.user.pk)[:10]

        serializer = SigPriorityTrackingSerializer(qs, many=True)
        if request.user:
            return Response(serializer.data)


# Get data to be process by user for PS
class GetDataSig(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        incomingData = request.data
        user_id = request.user.id
        # StoreData.my_store = incomingData
        uuid = write_to_file(user_id, incomingData)
        return Response('https://texclusive.herokuapp.com/download/ps/{}'.format(uuid))
        # return Response('http://127.0.0.1:8000/download/ps/{}'.format(uuid))


        # file = open("sample.txt", 'w', encoding='utf-8')
        # for dic in incomingData:
        #     json.dump(dic, file) 
        #     file.write('\n')
        # file.close()
            
        # return Response('http://127.0.0.1:8000/download/ps/{}'.format(request.user.id))
        # return Response('https://texclusive.herokuapp.com/report/sig')


def download_ps(request, id):
    sender = write_ps(id)
    return FileResponse(open('./files/{}.pdf'.format(sender), 'rb'), as_attachment=True, content_type='application/pdf')
    # get_stored_data = StoreData.my_store
    # # get_stored_data = []

    # # with open("sample.txt", 'r') as f:
    # #     for line in f:
    # #         get_stored_data.append(line.strip())
    # id = id
    # print('This is the new id: ', id)

    
    # senders_data = get_stored_data[0]
    # receiver_data = get_stored_data[1]
    # weight = get_stored_data[2]
    # barcode_target = get_stored_data[3] 
    # number_data = get_stored_data[4]
    # today_date = get_stored_data[5]
    # sender_name = get_stored_data[6]
    
    # # senders_data = json.loads(senders_data)
    # # receiver_data = json.loads(receiver_data)
    
    # senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
    # receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

    # pdf = MyFPDF('L', 'mm', 'letter')
    # pdf.add_page()
    # pdf.set_font('helvetica', '', 15)
    # pdf.set_line_width(0.8)
    # pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
    # pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
    # pdf.line(98.55, 55.3, 252.45, 55.3)
    # pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
    # pdf.line(98.55, 70.5, 252.45, 70.5)
    # pdf.set_xy(98.55, 73)
    # # for line in sales:
    # #     pdf.cell(170, 6, f"{line['item'].ljust(30)} {line['amount'].rjust(15)}", 0, 1,'L')
    # pdf.set_xy(204.5, 72.5)
    # pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')
    # # pdf.cell(50, 6, "Ship Date:07/29/22", 0, 1,'L')

    # pdf.set_xy(212, 80)
    # pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
    
    # for index in range(len(senders_info)):
    #     for key in senders_info[index]:
    #         incre_by_one = index * 6
    #         incre = 73 + incre_by_one
    #         pdf.set_xy(99, incre)
    #         pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

    # for index in range(len(receivers_info)):
    #     for key in receivers_info[index]:
    #         incre_by_one = index * 6
    #         incre = 119.5 + incre_by_one
    #         pdf.set_xy(118.5, incre)
    #         pdf.set_font('helvetica', '', 14.8)
    #         pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')


    # pdf.line(98.55, 153, 252.45, 153)
    # pdf.set_font('helvetica', 'B', 12)  
    # pdf.text(140.4, 159, 'USPS SIGNATURE TRACKING #EP')
    # # pdf.image(image_url)
    # # pdf.image("{}".format(image_url))
    # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    # pdf.set_font('helvetica', 'B', 13.5)  
    # pdf.text(137.5, 197, "{}".format(number_data))
    # # pdf.text(137.5, 197, '9210 3564 7281 3047 3532 7281 31')
    # pdf.line(98.55, 198.55, 252.45, 198.55)
    # pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
  
    # pdf.output('./files/{}.pdf'.format(sender_name), 'F')
    # return FileResponse(open('./files/{}.pdf'.format(sender_name), 'rb'), as_attachment=True, content_type='application/pdf')
    # pdf.output('barcode.pdf', 'F')
    # return FileResponse(open('barcode.pdf', 'rb'), as_attachment=True, content_type='application/pdf')


# End section for PS
##############################################################################################
#############################################################################################
#################################################################################################



# P block starts here
#################################################################################################
#################################################################################################
#################################################################################################


class TrackingCount(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = PriorityTracking.objects.filter(user_id=request.user.id).count()
            
        return Response({"pcount" : qs})


class UploadPriorityTracking(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FileUploadSerializer
   
    def post(self, request, *args, **kwargs):
        mydata = []
        # Get user trying to upload tracking
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                requested_user = ss.user
                
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
   
        if not file.name.endswith('.csv'):
            return Response({"status": "unsupported file"}, status.HTTP_406_NOT_ACCEPTABLE) 

        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = PriorityTracking(
                       priority = row[0],
                    #    priority = row['priority'],
                       user = requested_user
                       )
            mydata.append(new_file)
            if len(new_file.priority) < 26:
                return Response({"status": "forbidden",
                                "incomplete_number": f"{new_file.priority}"}, status.HTTP_403_FORBIDDEN)

        for number in mydata:
            if PriorityTracking.objects.filter(priority=number.priority).exists():
                return Response({"existed_number": number.priority})

        try:
            # new_file.save()
            PriorityTracking.objects.bulk_create(mydata)
            return Response({"success": "success"}, status.HTTP_201_CREATED)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)
                    
        return Response({"status": "success"}, status.HTTP_201_CREATED)


# Delete number to be used by user
class DeletePriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, priority=None):
        qs = PriorityTracking.objects.filter(priority=priority)
        if qs.exists():
            qs.delete()
            return Response('number has been successfully deleted')
        else:
            raise ParseError('number has been used')


        # qs = PriorityTracking.objects.get(priority=priority)
        # qs.delete()
        # return Response('Tracking deleted')
        # snippet = self.get_object(pk)
        # snippet.delete()


# Get first ten from P number
class ListPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = PriorityTracking.objects.all()
        # content = {
        #     'user': str(request.user),  # `django.contrib.auth.User` instance.
        #     'auth': str(request.auth),  # None
        # }
        # print(content)
        # token = Token.objects.get_or_create(user=user)
        # print(request.user.id)
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            # print(ss)
            if ss.user.pk == request.user.id:
                # print(ss.user.pk)
                qs = PriorityTracking.objects.filter(user_id=ss.user.pk)[:10]

        # y = User.objects.filter(id=request.user.id)
        # print(y)
        # ss, token = Token.objects.get_or_create(user=y)
        serializer = PriorityTrackingSerializer(qs, many=True)
        if request.user:
            return Response(serializer.data)
        # data = {
        #     'name': 'Paul',
        #     'age': 30
        # }
        # return Response(data)

    # def post(self, request, *args, **kwargs):
    #     serializer = PriorityTrackingSerializer(data=request.data)
    #     # print(serializer.data['priority'])
    #     if serializer.is_valid():
          
    #         sw = serializer.data['priority'] = "92055903419874465273204333"
    #         print(sw)
    #         # serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)


    # def get(self, request, format=None):
    #     content = {
    #         'user': str(request.user),  # `django.contrib.auth.User` instance.
    #         'auth': str(request.auth),  # None
    #     }
    #     return Response(content)




# class TestView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     permission_classes = (IsAuthenticated, )

#     serializer_class = PriorityTrackingSerializer
#     queryset = PriorityTracking.objects.filter(user=2)

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
        

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class Upload(APIView):
#     permission_classes = (IsAuthenticated, )

#     def get(self, request, *args, **kwargs):
#         qs = PriorityTracking.objects.all()
#         serializer = PriorityTrackingSerializer(qs, many=True)
#         return Response(serializer.data)
#         # data = {
#         #     'name': 'Paul',
#         #     'age': 30
#         # }
#         # return Response(data)

#     def post(self, request, *args, **kwargs):
#         serializer = PriorityTrackingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

 
# class CustomAuthToken(ObtainAuthToken):
#     def get(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })




#Delete all priority numbers
class DeleteAllPriorityNumber(APIView):
    def delete(self, request, *args, **kwargs):
        qs = PriorityTracking.objects.all()
        qs.delete()
        return Response('You have sucessfully deleted all numbers now now')


# Delete selected priority numbers
class DeleteFromPriorityTrackingList(APIView):
    def delete(self, request, selected=None):
        selectedNumber = selected.split(",") 
        for index in range(0, len(selectedNumber)):
            qs = PriorityTracking.objects.filter(priority=selectedNumber[index])
            qs.delete()
        return Response('Successfully deleted')


class PriorityTrackingSets(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # queryset = PriorityTracking.objects.all()
    serializer_class = PriorityTrackingSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user_id = self.request.user.id
        return PriorityTracking.objects.filter(user_id=user_id)


# Get data to be proceessed by user
class GetData(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        incomingData = request.data
        # StoreData.my_store = incomingData
        user_id = request.user.id
        uuid = write_to_file(user_id, incomingData)
        return Response('https://texclusive.herokuapp.com/download/p/{}'.format(uuid))
        # return Response('http://127.0.0.1:8000/download/p/{}'.format(uuid))
     

        # file = open("sample.txt", 'w', encoding='utf-8')
        # for dic in incomingData:
        #     json.dump(dic, file) 
        #     file.write('\n')
        # file.close()

        # return Response('http://127.0.0.1:8000/download/p/{}'.format(request.user.id))
        # return Response('https://texclusive.herokuapp.com/report')


def download_p(request, id):
    sender = write_p(id)
    dir = os.path.join(BASE_DIR, 'files')
    return FileResponse(open(dir + '{}.pdf'.format(sender), 'rb'), as_attachment=True, content_type='application/pdf')
    # get_stored_data = StoreData.my_store
    # senders_data = get_stored_data[0]
    # receiver_data = get_stored_data[1]
    # weight = get_stored_data[2]
    # barcode_target = get_stored_data[3]
    # number_data = get_stored_data[4]
    # today_date = get_stored_data[5]
    # sender_name = get_stored_data[6]

    # id = id
    # print('This is the new id: ', id)


    # # get_stored_data = []

    # # with open("sample.txt", 'r') as f:
    # #     for line in f:
    # #         get_stored_data.append(line.strip())
    

    # # senders_data = get_stored_data[0]
    # # receiver_data = get_stored_data[1]
    # # weight = get_stored_data[2].replace('"', '')
    # # barcode_target = get_stored_data[3].replace('"', '')
    # # number_data = get_stored_data[4].replace('"', '')
    # # today_date = get_stored_data[5].replace('"', '')
    # # sender_name = get_stored_data[6].replace('"', '')

    # # senders_data = json.loads(senders_data)
    # # receiver_data = json.loads(receiver_data)

    # senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
    # receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

    # pdf = MyFPDF('L', 'mm', 'letter')
    # pdf.add_page()
    # pdf.set_font('helvetica', '', 15)
    # pdf.set_line_width(0.8)
    # pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
    # pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
    # pdf.line(98.55, 55.3, 252.45, 55.3)
    # pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
    # pdf.line(98.55, 70.5, 252.45, 70.5)
    # pdf.set_xy(98.55, 73)
    # pdf.set_xy(204.5, 72.5)
    # pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')


    # pdf.set_xy(212, 80)
    # pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
    
    # for index in range(len(senders_info)):
    #     for key in senders_info[index]: 
    #         incre_by_one = index * 6
    #         incre = 73 + incre_by_one
    #         pdf.set_xy(99, incre)
    #         pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

    # for index in range(len(receivers_info)):
    #     for key in receivers_info[index]:
    #         incre_by_one = index * 6
    #         incre = 119.5 + incre_by_one
    #         pdf.set_xy(118.5, incre)
    #         pdf.set_font('helvetica', '', 14.8)
    #         pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

    # pdf.line(98.55, 153, 252.45, 153)
    # pdf.set_font('helvetica', 'B', 12)  
    # pdf.text(155.4, 159, 'USPS TRACKING #EP')
    # # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=12.2&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    # # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    # pdf.set_font('helvetica', 'B', 13.5)  
    # pdf.text(137.5, 197, "{}".format(number_data))
    # pdf.line(98.55, 198.55, 252.45, 198.55)
    # pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    # pdf.output('./files/{}.pdf'.format(sender_name), 'F')
    # return FileResponse(open('./files/{}.pdf'.format(sender_name), 'rb'), as_attachment=True, content_type='application/pdf')


# End of P section
###########################################################################################################
###########################################################################################################
###########################################################################################################


# User section begins here
########################################################################################################
########################################################################################################
########################################################################################################


# delete single user
class DeleteUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    def delete(self, request, user_id=None):
        try:
            qs = User.objects.filter(pk=user_id)
            print(qs)
            qs.delete()
            # # print(user_pk)
        
            return Response('User has been deleted')
        except PriorityTracking.DoesNotExist:
            return Response('User does not exist')


class UserList(APIView):
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializer = UserListSerializer(qs, many=True)
        return Response(serializer.data)


"""
    End of P section
"""

"""
    File clean up starts here
"""


class FileCleanUp(APIView):
    def delete(self, request, *args, **kwargs):
        dir = os.path.join(BASE_DIR, 'files')
        # print(dir)
        # dir = './files'
        # print('here', len(os.listdir(dir)))
        # print(os.listdir(dir).len())
        total_files = len(os.listdir(dir))
        if total_files > 0:
            for file in os.listdir(dir):
                os.remove(os.path.join(dir, file))
            return Response('{} file removed'.format(total_files))
        else:
            return Response('No file is present')


def download_p46(request):
    # get_stored_data = StoreData.my_store
    # senders_data = get_stored_data[0]
    # receiver_data = get_stored_data[1]
    # weight = get_stored_data[2]
    # barcode_target = get_stored_data[3]
    # number_data = get_stored_data[4]
    # today_date = get_stored_data[5]
    # sender_name = get_stored_data[6]

    # id = id
    # print('This is the new id: ', id)


    # # get_stored_data = []

    # # with open("sample.txt", 'r') as f:
    # #     for line in f:
    # #         get_stored_data.append(line.strip())
    

    # # senders_data = get_stored_data[0]
    # # receiver_data = get_stored_data[1]
    # # weight = get_stored_data[2].replace('"', '')
    # # barcode_target = get_stored_data[3].replace('"', '')
    # # number_data = get_stored_data[4].replace('"', '')
    # # today_date = get_stored_data[5].replace('"', '')
    # # sender_name = get_stored_data[6].replace('"', '')

    # # senders_data = json.loads(senders_data)
    # # receiver_data = json.loads(receiver_data)

    # senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
    # receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

    pdf = MyFPDF("p", "mm", [133.858 , 202.946])
    pdf.add_page()
    pdf.set_font('helvetica', '', 15)
    pdf.set_line_width(0.6)
    pdf.rect(0.7, 1, 131.9, 200.8, style = '')
    pdf.image("media/images/1p.jpg", x=1.3, y=1.4, w=130.4, h=34.8)
    pdf.line(1.3, 36, 132.5, 36)
    pdf.image("media/images/p3.jpg", x = 1.3, y = 36.88, w = 130.4, h = 0, type = '', link = '')
    pdf.line(1.3, 47.2, 132.5, 47.2)
    # pdf.set_xy(98.55, 73)
    # pdf.set_xy(204.5, 72.5)
    # pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')


    # pdf.set_xy(212, 80)
    # pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
    
    # for index in range(len(senders_info)):
    #     for key in senders_info[index]: 
    #         incre_by_one = index * 6
    #         incre = 73 + incre_by_one
    #         pdf.set_xy(99, incre)
    #         pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

    # for index in range(len(receivers_info)):
    #     for key in receivers_info[index]:
    #         incre_by_one = index * 6
    #         incre = 119.5 + incre_by_one
    #         pdf.set_xy(118.5, incre)
    #         pdf.set_font('helvetica', '', 14.8)
    #         pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

    # pdf.line(98.55, 153, 252.45, 153)
    # pdf.set_font('helvetica', 'B', 12)  
    # pdf.text(155.4, 159, 'USPS TRACKING #EP')
    # # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=12.2&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    # # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    # pdf.set_font('helvetica', 'B', 13.5)  
    # pdf.text(137.5, 197, "{}".format(number_data))
    # pdf.line(98.55, 198.55, 252.45, 198.55)
    # pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    pdf.output('barcode.pdf', 'F')
    return FileResponse(open('barcode.pdf', 'rb'), as_attachment=False, content_type='application/pdf')
           

# Notes


        # x = s[0]
        # print(x)
        # serializer = LabelDataSerializer(data=request.data)
        # if serializer.is_valid():
        #     print(serializer)
        #     # serializer.save()
        #     return Response('http://127.0.0.1:8000/report')
#             return Response(serializer.data)
        # y =list(map(lambda x:{x[0]:x[1]},x.items() ))
        # print(y)
           

# "p", "in", [5.27, 7.98]
      # if len(output) > row_height_lines:
        #     row_height_lines = len(output)
                
        # for tlines , datum in zip(lines_in_row, row):
        #     # here you can hack-in the
        #     text =datum.rstrip('\n') + (1 + row_height_lines - tlines) * '\n'
        #     pdf.multi_cell(col_width, line_height, text, border=0, ln=3)
        # pdf.ln(row_height_lines * line_height)

    # for row in data:
    #     row_height_lines = 1
    #     lines_in_row = []
    #     for datum in row: # determine height of highest cell
    #         output = pdf.multi_cell(col_width, line_height, datum, border=0, ln=3, split_only=True)
    #         print(len(output))
    #         lines_in_row.append(len(output))
    #         if len(output) > row_height_lines:
    #             row_height_lines = len(output)

    #     for tlines , datum in zip(lines_in_row, row):
    #         # here you can hack-in the
    #         text =datum.rstrip('\n') + (1 + row_height_lines - tlines) * '\n'
    #         pdf.multi_cell(col_width, line_height, text, border=0, ln=3)
    #     pdf.ln(row_height_lines * line_height)
    # index = 0
    # for line in salesd: 
    #     for key in line:
    #         print(index)
    #         pdf.set_xy(20, 105)
    #         pdf.cell(170, 6, f"{line[key].ljust(30)}", 0, 1, )
    # for line in salesd: 
    #     pdf.set_xy(20, 105)
    #     pdf.cell(170, 6, f"{line['item'].ljust(30)}", 0, 1, )
    # pdf.cell(10, 50, txt = 'John Do', border = 0, ln = 0, align = '', fill = False, link = '')
    # pdf.cell(10, 65, txt = '64 Ajegunle', border = 0, ln = 0, align = '', fill = False, link = '')
    # pdf.cell(10, 55, f"{'Item'} {'Amount'}", 0, 0)
    # pdf.text(10, 75, 'Barv')
    # pdf.cell(10, 100, 'This is what you have sold this month so far:',0,0)
    # pdf.cell(40, 10, '',0,1)
    # pdf.set_font('courier', '', 12)
    
    # pdf.line(10, 30, 150, 30)
    # pdf.line(10, 38, 150, 38)
    # for line in sales:
    #     pdf.cell(200, 8, f"{line['item'].ljust(30)} {line['amount'].rjust(20)}", 0, 1)


#  line_height = pdf.font_size * 1.5
#     col_width = pdf.epw /6   # distribute content evenly
#     row_height_lines = 1

#     # pdf.multi_cell(col_width, line_height, f"{datum['item']}", border=0, ln=3)
#     for datum in salesd:
#         pdf.multi_cell(col_width, line_height, datum['item'], border=0, ln=3)

   # pdf.set_font('arial', 'B', 20)
#     pdf.write_html("""
#    <table border="0" align="center" width="50%">
#         <thead>
#             <tr>
#                 <th width="100%"><img src="media/images/1p.jpg"/></th>            
#             </tr>
#         </thead>
#         <tbody>
#         <tbody>
#             <tr>
#                 <td><img src="media/images/p2.png"/></td> 
#             </tr>
            
#         </tbody>

        
#     </table>
# """)