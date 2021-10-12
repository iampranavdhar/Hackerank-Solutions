time = input().split(':')
if 'AM' in time[2]:
    if int(time[0]) != 12: 
        time[2] = time[2][:2]
        print(':'.join(time))
    if int(time[0]) == 12:
        time[0] = '00'
        time[2] = time[2][:2]
        print(':'.join(time))
if 'PM' in time[2]:
    if int(time[0]) >= 12:
        time[2] = time[2][:2]
        print(':'.join(time))
    elif int(time[0]) < 12:
        time[0] = int(time[0])+12
        time[0] = str(time[0])
        time[2] = time[2][:2]
        print(':'.join(time))

        