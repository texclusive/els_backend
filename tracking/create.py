import os
from exqship.settings import BASE_DIR
# import json
# from fpdf import FPDF, HTMLMixin
from tracking.draw import draw_fc, draw_es, draw_e, draw_ps, draw_p, draw_bp


# class MyFPDF(FPDF, HTMLMixin):
# 	pass


def write_fc(id):
    dir = os.path.join(BASE_DIR, 'notepad')

    if id == 'f0af8242-ddaf-4fc1-8013-18642a1d71e5':
        get_stored_data = []
        with open(dir + "/note_one.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
        
        sender_name = draw_fc(get_stored_data)
        return sender_name

    elif id == '5154acba-18ca-4f02-b00c-34e1cb9cc04e':
        get_stored_data = []
        with open(dir + "/note_two.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_fc(get_stored_data)
        return sender_name

    elif id == 'ac120371-6b1b-40e4-a956-d70ad44dd41f':
        get_stored_data = []
        with open(dir + "/note_three.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_fc(get_stored_data)
        return sender_name

    elif id == '10c36fd7-9beb-4374-a945-fb3786fbae4b':
        get_stored_data = []
        with open(dir + "/note_four.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_fc(get_stored_data)
        return sender_name

    elif id == 'af841f9d-f3be-48bb-b154-7f7e85d86b31':
        get_stored_data = []
        with open(dir + "/note_five.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
        
        sender_name = draw_fc(get_stored_data)
        return sender_name

    elif id == '0d733d63-a016-4131-94d8-80d963df4e1a':
        get_stored_data = []
        with open(dir + "/note_six.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_fc(get_stored_data)
        return sender_name

    elif id == '44816688-342b-4fc1-a4c8-6ffa196b8122':
        get_stored_data = []
        with open(dir + "/note_seven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_fc(get_stored_data)
        return sender_name

    elif id == '2fe6c32e-9eb5-4c88-ae05-e7d41725d562':
        get_stored_data = []
        with open(dir + "/note_eight.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_fc(get_stored_data)
        return sender_name

    elif id == 'a15219a4-735c-4990-af86-f3eccae97d93':
        get_stored_data = []
        with open(dir + "/note_nine.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_fc(get_stored_data)
        return sender_name

    elif id == '52688593-9479-4b38-a8ae-3aeff96df687':
        get_stored_data = []
        with open(dir + "/note_ten.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_fc(get_stored_data)
        return sender_name

    elif id == '55582345-9da5-4eb8-9dc9-5f03fdea0dda':
        get_stored_data = []
        with open(dir + "/note_eleven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_fc(get_stored_data)
        return sender_name

    elif id == '15f22fd9-173f-4c55-a026-6e5bab8d0c3c':
        get_stored_data = []
        with open(dir + "/note_twelve.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_fc(get_stored_data)
        return sender_name

    elif id == '2db2f956-9ccd-46b8-90af-56ed54dc4328':
        get_stored_data = []
        with open(dir + "/note_thirteen.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_fc(get_stored_data)
        return sender_name

    elif id == 'dfdbb5d1-7b1d-4fe0-adb1-d697e11b02a7':
        get_stored_data = []
        with open(dir + "/note_fourteen.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_fc(get_stored_data)
        return sender_name


def write_es(id):
    dir = os.path.join(BASE_DIR, 'notepad')

    if id == 'f0af8242-ddaf-4fc1-8013-18642a1d71e5':
        get_stored_data = []
        with open(dir + "/note_one.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name   

    elif id == '5154acba-18ca-4f02-b00c-34e1cb9cc04e':
        get_stored_data = []
        with open(dir + "/note_two.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name

    elif id == 'ac120371-6b1b-40e4-a956-d70ad44dd41f':
        get_stored_data = []
        with open(dir + "/note_three.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name

    elif id == '10c36fd7-9beb-4374-a945-fb3786fbae4b':
        get_stored_data = []
        with open(dir + "/note_four.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name
    
    elif id == 'af841f9d-f3be-48bb-b154-7f7e85d86b31':
        get_stored_data = []
        with open(dir + "/note_five.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name
     
    elif id == '0d733d63-a016-4131-94d8-80d963df4e1a':
        get_stored_data = []
        with open(dir + "/note_six.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name
    
    elif id == '44816688-342b-4fc1-a4c8-6ffa196b8122':
        get_stored_data = []
        with open(dir + "/note_seven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name

    elif id == '2fe6c32e-9eb5-4c88-ae05-e7d41725d562':
        get_stored_data = []
        with open(dir + "/note_eight.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name

    elif id == 'a15219a4-735c-4990-af86-f3eccae97d93':
        get_stored_data = []
        with open(dir + "/note_nine.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name

    elif id == '52688593-9479-4b38-a8ae-3aeff96df687':
        get_stored_data = []
        with open(dir + "/note_ten.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name

    elif id == '55582345-9da5-4eb8-9dc9-5f03fdea0dda':
        get_stored_data = []
        with open(dir + "/note_eleven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name

    elif id == '15f22fd9-173f-4c55-a026-6e5bab8d0c3c':
        get_stored_data = []
        with open(dir + "/note_twelve.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name

    elif id == '2db2f956-9ccd-46b8-90af-56ed54dc4328':
        get_stored_data = []
        with open(dir + "/note_thirteen.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name

    elif id == 'dfdbb5d1-7b1d-4fe0-adb1-d697e11b02a7':
        get_stored_data = []
        with open(dir + "/note_fourteen.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_es(get_stored_data)
        return sender_name


def write_e(id):
    dir = os.path.join(BASE_DIR, 'notepad')

    if id == 'f0af8242-ddaf-4fc1-8013-18642a1d71e5':
        get_stored_data = []
        with open(dir + "/note_one.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
        
        sender_name = draw_e(get_stored_data)
        return sender_name
    
    elif id == '5154acba-18ca-4f02-b00c-34e1cb9cc04e':
        get_stored_data = []
        with open(dir + "/note_two.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_e(get_stored_data)
        return sender_name

    elif id == 'ac120371-6b1b-40e4-a956-d70ad44dd41f':
        get_stored_data = []
        with open(dir + "/note_three.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_e(get_stored_data)
        return sender_name

    elif id == '10c36fd7-9beb-4374-a945-fb3786fbae4b':
        get_stored_data = []
        with open(dir + "/note_four.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_e(get_stored_data)
        return sender_name

    elif id == 'af841f9d-f3be-48bb-b154-7f7e85d86b31':
        get_stored_data = []
        with open(dir + "/note_five.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_e(get_stored_data)
        return sender_name
    
    elif id == '0d733d63-a016-4131-94d8-80d963df4e1a':
        get_stored_data = []
        with open(dir + "/note_six.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_e(get_stored_data)
        return sender_name

    elif id == '44816688-342b-4fc1-a4c8-6ffa196b8122':
        get_stored_data = []

        with open(dir + "/note_seven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_e(get_stored_data)
        return sender_name

    elif id == '2fe6c32e-9eb5-4c88-ae05-e7d41725d562':
        get_stored_data = []

        with open(dir + "/note_eight.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_e(get_stored_data)
        return sender_name

    elif id == 'a15219a4-735c-4990-af86-f3eccae97d93':
        get_stored_data = []

        with open(dir + "/note_nine.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_e(get_stored_data)
        return sender_name

    elif id == '52688593-9479-4b38-a8ae-3aeff96df687':
        get_stored_data = []

        with open(dir + "/note_ten.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_e(get_stored_data)
        return sender_name

    elif id == '55582345-9da5-4eb8-9dc9-5f03fdea0dda':
        get_stored_data = []

        with open(dir + "/note_eleven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_e(get_stored_data)
        return sender_name

    elif id == '15f22fd9-173f-4c55-a026-6e5bab8d0c3c':
        get_stored_data = []

        with open(dir + "/note_twelve.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_e(get_stored_data)
        return sender_name

    elif id == '2db2f956-9ccd-46b8-90af-56ed54dc4328':
        get_stored_data = []

        with open(dir + "/note_thirteen.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_e(get_stored_data)
        return sender_name

    elif id == 'dfdbb5d1-7b1d-4fe0-adb1-d697e11b02a7':
        get_stored_data = []

        with open(dir + "/note_fourteen.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_e(get_stored_data)
        return sender_name


def write_ps(id):
    dir = os.path.join(BASE_DIR, 'notepad')

    if id == 'f0af8242-ddaf-4fc1-8013-18642a1d71e5':
        get_stored_data = []

        with open(dir + "/note_one.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_ps(get_stored_data)
        return sender_name

    elif id == '5154acba-18ca-4f02-b00c-34e1cb9cc04e':
        get_stored_data = []
        with open(dir + "/note_two.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_ps(get_stored_data)
        return sender_name

    elif id == 'ac120371-6b1b-40e4-a956-d70ad44dd41f':
        get_stored_data = []
        with open(dir + "/note_three.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
        
        sender_name = draw_ps(get_stored_data)
        return sender_name

    elif id == '10c36fd7-9beb-4374-a945-fb3786fbae4b':
        get_stored_data = []
        with open(dir + "/note_four.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
        
        sender_name = draw_ps(get_stored_data)
        return sender_name

    elif id == 'af841f9d-f3be-48bb-b154-7f7e85d86b31':
        get_stored_data = []
        with open(dir + "/note_five.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
        
        sender_name = draw_ps(get_stored_data)
        return sender_name

    elif id == '0d733d63-a016-4131-94d8-80d963df4e1a':
        get_stored_data = []
        with open(dir + "/note_six.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_ps(get_stored_data)
        return sender_name

    elif id == '44816688-342b-4fc1-a4c8-6ffa196b8122':
        get_stored_data = []
        with open(dir + "/note_seven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_ps(get_stored_data)
        return sender_name

    elif id == '2fe6c32e-9eb5-4c88-ae05-e7d41725d562':
        get_stored_data = []
        with open(dir + "/note_eight.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_ps(get_stored_data)
        return sender_name

    elif id == 'a15219a4-735c-4990-af86-f3eccae97d93':
        get_stored_data = []
        with open(dir + "/note_nine.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_ps(get_stored_data)
        return sender_name

    elif id == '52688593-9479-4b38-a8ae-3aeff96df687':
        get_stored_data = []
        with open(dir + "/note_ten.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_ps(get_stored_data)
        return sender_name

    elif id == '55582345-9da5-4eb8-9dc9-5f03fdea0dda':
        get_stored_data = []
        with open(dir + "/note_eleven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_ps(get_stored_data)
        return sender_name

    elif id == '15f22fd9-173f-4c55-a026-6e5bab8d0c3c':
        get_stored_data = []
        with open(dir + "/note_twelve.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_ps(get_stored_data)
        return sender_name

    elif id == '2db2f956-9ccd-46b8-90af-56ed54dc4328':
        get_stored_data = []
        with open(dir + "/note_thirteen.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_ps(get_stored_data)
        return sender_name

    elif id == 'dfdbb5d1-7b1d-4fe0-adb1-d697e11b02a7':
        get_stored_data = []
        with open(dir + "/note_fourteen.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_ps(get_stored_data)
        return sender_name



def write_p(id):
    dir = os.path.join(BASE_DIR, 'notepad')

    if id == 'f0af8242-ddaf-4fc1-8013-18642a1d71e5':
        get_stored_data = []

        with open(dir + "/note_one.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
        
        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == '5154acba-18ca-4f02-b00c-34e1cb9cc04e':
        get_stored_data = []

        with open(dir + "/note_two.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == 'ac120371-6b1b-40e4-a956-d70ad44dd41f':
        get_stored_data = []

        with open(dir + "/note_three.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == '10c36fd7-9beb-4374-a945-fb3786fbae4b':
        get_stored_data = []

        with open(dir + "/note_four.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
        
        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == 'af841f9d-f3be-48bb-b154-7f7e85d86b31':
        get_stored_data = []

        with open(dir + "/note_five.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == '0d733d63-a016-4131-94d8-80d963df4e1a':
        get_stored_data = []

        with open(dir + "/note_six.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == '44816688-342b-4fc1-a4c8-6ffa196b8122':
        get_stored_data = []

        with open(dir + "/note_seven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == '2fe6c32e-9eb5-4c88-ae05-e7d41725d562':
        get_stored_data = []

        with open(dir + "/note_eight.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == 'a15219a4-735c-4990-af86-f3eccae97d93':
        get_stored_data = []

        with open(dir + "/note_nine.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == '52688593-9479-4b38-a8ae-3aeff96df687':
        get_stored_data = []

        with open(dir + "/note_ten.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == '55582345-9da5-4eb8-9dc9-5f03fdea0dda':
        get_stored_data = []

        with open(dir + "/note_eleven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == '15f22fd9-173f-4c55-a026-6e5bab8d0c3c':
        get_stored_data = []

        with open(dir + "/note_twelve.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == '2db2f956-9ccd-46b8-90af-56ed54dc4328':
        get_stored_data = []

        with open(dir + "/note_thirteen.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == 'dfdbb5d1-7b1d-4fe0-adb1-d697e11b02a7':
        get_stored_data = []

        with open(dir + "/note_fourteen.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name


def write_bp(id):
    dir = os.path.join(BASE_DIR, 'bulkpad')

    if id == 'f0af8242-ddaf-4fc1-8013-18642a1d71e5':
        get_stored_data = []

        with open(dir + "/bulk_one.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
        
        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == '5154acba-18ca-4f02-b00c-34e1cb9cc04e':
        get_stored_data = []

        with open(dir + "/bulk_two.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
                print(get_stored_data)

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == 'ac120371-6b1b-40e4-a956-d70ad44dd41f':
        get_stored_data = []

        with open(dir + "/bulk_three.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == '10c36fd7-9beb-4374-a945-fb3786fbae4b':
        get_stored_data = []

        with open(dir + "/bulk_four.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())
        
        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == 'af841f9d-f3be-48bb-b154-7f7e85d86b31':
        get_stored_data = []

        with open(dir + "/bulk_five.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == '0d733d63-a016-4131-94d8-80d963df4e1a':
        get_stored_data = []

        with open(dir + "/bulk_six.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

    elif id == '44816688-342b-4fc1-a4c8-6ffa196b8122':
        get_stored_data = []

        with open(dir + "/bulk_seven.txt", 'r') as f:
            for line in f:
                get_stored_data.append(line.strip())

        sender_name = draw_p(get_stored_data)
        return sender_name

