import os
from exqship.settings import BASE_DIR
import json

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
