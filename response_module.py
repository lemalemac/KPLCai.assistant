def reply(x):
    #power_outage
    if x.incident_type == 'power_outage' and x.active_state is True:
        x.prompt = True
        x.sentiment = 'power_outage'
        return 'Hi, We apologize for the inconveniences, kindly provide your account number and exact location for assistance.'
    elif x.prompt is True and x.sentiment == 'power_outage' and x.incident_type == 'meter_number' or x.incident_type == 'location':
        x.prompt = False
        x.sentiment = ''
        return 'Thank you. Your issue is being resolved under reference number {insert_number}'
    #greeting
    elif x.incident_type == 'greeting' and x.active_state is True:
        return 'Hi☺\nHow may I help you?'
    #identity
    elif x.incident_type == 'identity' and x.active_state is True:
        return 'I am an AI assistant from KPLC.'
    #gratitude
    elif x.incident_type == 'gratitude' or x.incident_type == 'disagree' and x.active_state is True:
        return 'Happy to help☺'
    #general_problem
    elif x.incident_type == 'general_problem' and x.active_state is True:
        return 'Please describe your problem for assistance...'
    #customer_name
    elif x.incident_type == 'customer_name' and x.active_state is True:
        return 'Nice to meet you.'
    #location
    elif x.prompt is True and x.incident_type == 'location' and x.active_state is True:
        x.prompt = False
        return 'This function will be added later.'
    elif x.sentiment == 'agree' and x.prompt is True and x.topic_mem == 'service' and x.active_state is True:
        x.prompt = False
        return 'You can report incidences like power outages, staff misconduct, transaction failure. You can also buy tokens, pay or get a bill and verify staff IDs.'
    #buy_token
    elif x.incident_type == 'buy_token' and x.active_state is True:
        x.prompt = True
        x.sentiment = 'buy_token'
        return 'What is your meter number?'
    elif x.prompt is True and x.incident_type == 'meter_number' and x.sentiment == 'buy_token' and x.active_state is True:
        return 'Please enter a valid amount.'
    elif x.prompt is True and x.incident_type == 'money' and x.sentiment == 'buy_token' and x.active_state is True:
        return 'Are you sure you want to purchase tokens worth Ksh.{} '.format(x.money) + 'for account {}?'.format(x.meter_number)
    elif x.prompt is True and x.topic_mem == 'money' and x.sentiment == 'agree' and x.active_state is True:
        return 'Tokens purchased. Please await a confirmation message.'
    #query_bill
    elif x.incident_type == 'query_bill' and x.active_state is True:
        x.prompt = True
        x.sentiment = 'query_bill'
        return 'What is your meter number?'
    elif x.prompt is True and x.incident_type == 'meter_number' and x.sentiment == 'query_bill' and x.active_state is True:
        x.sentiment = ''
        return 'I can not fetch your bills at the moment.'
    #pay_bill
    elif x.incident_type == 'pay_bill' and x.active_state is True:
        x.prompt = True
        x.sentiment = 'pay_bill'
        return 'What is your meter number?'
    elif x.prompt is True and x.incident_type == 'meter_number' and x.sentiment == 'pay_bill' and x.active_state is True:
        x.sentiment = ''
        return 'You can not pay your bills through me at the moment.'
    #transaction_failure
    elif x.incident_type == 'transaction_failure' and x.active_state is True:
        x.prompt = True
        x.sentiment = 'transaction_failure'
        return 'What is your meter number?'
    elif x.prompt is True and x.incident_type == 'meter_number' and x.sentiment == 'transaction_failure' and x.active_state is True:
        x.sentiment = ''
        return 'I can not resolve transaction failure at the moment.'
    else:
        x.topic_mem = 'service'
        x.prompt = True
        return 'Sorry, I do not understand that.\n Do you want to see a list of my services?'
