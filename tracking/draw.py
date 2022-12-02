import json
from fpdf import FPDF, HTMLMixin


class MyFPDF(FPDF, HTMLMixin):
	pass


def draw_fc(stored_data):
    get_stored_data = stored_data
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
    pdf.image("http://barcode.design/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    pdf.set_font('helvetica', 'B', 13.5)  
    pdf.text(137.5, 196, "{}".format(number_data))

    pdf.line(98.55, 197.10, 252.45, 197.10)
    pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
    pdf.output('./files/{}.pdf'.format(sender_name), 'F')
    return sender_name


def draw_es(stored_data):
    get_stored_data = stored_data
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

    pdf.image("http://barcode.design/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
    # pdf.image("http://barcode.design/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 162.95, w = 140.45, h = 26.4, type = '', link = '')
    pdf.set_font('helvetica', 'B', 13.5)  
    pdf.text(137.5, 196, "{}".format(number_data))
    pdf.line(98.55, 197.10, 252.45, 197.10)
    pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
    pdf.output('./files/{}.pdf'.format(sender_name), 'F')
    return sender_name


def draw_e(stored_data):
    get_stored_data = stored_data
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

    pdf.image("http://barcode.design/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 163.2, w = 140.45, h = 26.4, type = '', link = '')
    pdf.set_font('helvetica', 'B', 13.5)  
    pdf.text(137.5, 196, "{}".format(number_data))
    pdf.line(98.55, 197.10, 252.45, 197.10)
    pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
    pdf.output('./files/{}.pdf'.format(sender_name), 'F')
    return sender_name


def draw_ps(stored_data):
    get_stored_data = stored_data
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
    pdf.image("http://barcode.design/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    pdf.set_font('helvetica', 'B', 13.5)  
    pdf.text(137.5, 197, "{}".format(number_data))
    # pdf.text(137.5, 197, '9210 3564 7281 3047 3532 7281 31')
    pdf.line(98.55, 198.55, 252.45, 198.55)
    pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')

    pdf.output('./files/{}.pdf'.format(sender_name), 'F')  
    return sender_name 


def draw_p(stored_data):
    get_stored_data = stored_data
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
    pdf.image("http://barcode.design/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    pdf.set_font('helvetica', 'B', 13.5)  
    pdf.text(137.5, 197, "{}".format(number_data))
    pdf.line(98.55, 198.55, 252.45, 198.55)
    pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    pdf.output('./files/{}.pdf'.format(sender_name), 'F')
    return sender_name


def draw_bp(stored_data):
    get_stored_data = stored_data
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
    pdf.image("http://barcode.design/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    pdf.set_font('helvetica', 'B', 13.5)  
    pdf.text(137.5, 197, "{}".format(number_data))
    pdf.line(98.55, 198.55, 252.45, 198.55)
    pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    pdf.output('./files/{}.pdf'.format(sender_name), 'F')
    return sender_name


