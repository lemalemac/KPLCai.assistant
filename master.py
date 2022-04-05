import projecthuman
import response_module
import whatsapp_api
master_list = []



while 1:
    temp = whatsapp_api.scan()
    temp2 = [i.id for i in temp]
    temp3 = [i.id for i in master_list]
    for t in temp2:
        if t in temp3:
            master_list[temp3.index(t)].latest_message = temp[temp2.index(t)].latest_message
            master_list[temp3.index(t)].replied = False
        else:
            master_list.append( temp[temp2.index(t)])

    for v in master_list:
        if v.active_state is False:
            master_list.remove(v)

        elif v.replied is False:
            v.active_state = True
            print(v.id)
            print('Query: ' + v.latest_message)
            v.response = projecthuman.think(v.latest_message)
            try:
                v.incident_type = v.response['intents'][0]['name']
            except:
                v.incident_type = 'unknown'
            if v.incident_type == 'meter_number':
                v.meter_number = v.response['entities']['wit$phone_number:phone_number'][0]['body']
                v.topic_mem = v.incident_type
            elif v.incident_type == 'money':
                v.money = v.latest_message
                v.topic_mem = v.incident_type
            elif v.incident_type == 'agree' or v.incident_type == 'disagree':
                v.sentiment = v.incident_type
            else:
                v.topic_mem = v.incident_type
            u = response_module.reply(v)
            print('Response: ' + u)
            v.send_message(u)
            v.replied = True










