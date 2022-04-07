def add_time(init_time, dur, day=None):

    ampm_table = {'1' : 'AM',
                  '2' : 'PM'}
    week_table = {'1' : 'Monday',
                  '2' : 'Tuesday',
                  '3' : 'Wednesday',
                  '4' : 'Thursday',
                  '5' : 'Friday',
                  '6' : 'Saturday',
                  '7' : 'Sunday'}

    in_time = init_time.split()[0]

    in_ampm = 0

    if init_time.split()[1] == 'AM':
        in_ampm = 1
    elif init_time.split()[1] == 'PM':
        in_ampm = 2

    in_hrs = in_time.split(':')[0]
    in_min = in_time.split(':')[1]

    dur_hrs = dur.split(':')[0]
    dur_min = dur.split(':')[1]

    new_hrs_int = (int(in_hrs) + int(dur_hrs))
    new_min_int = (int(in_min) + int(dur_min))
    new_hrs = (new_hrs_int + new_min_int)




    print()

add_time("11:06 PM", "2:02")