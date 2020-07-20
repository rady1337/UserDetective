from datetime import datetime


def Logger(content):
    try:
        with open('log/' + 'log_' + str(datetime.now()) + '.txt', 'w') as log:
            log.write(content)
    except:
        pass
