def mins_added_to_time(min, time):
    time_mins = int(time[:2])
    time_hours = int(time[3:])
    new_time_mins = (time_mins + min) % 60
    new_time_hours = (((time_mins + min)//60) + time_hours) % 24
    new_time = str(new_time_hours) + ':' + str(new_time_mins)
    return new_time
    


class train:
    def __init__(self, destination, expected_time):
        self.destination = destination
        self.expected_time = expected_time
#    def mins_added_to_time(min, time):
#        time_mins = int(time[:2])
#        time_hours = int(time[3:])
#        new_time_mins = (time_mins + min) % 60
#        new_time_hours = (((time_mins + min)//60) + time_hours) % 24
#        new_time = str(new_time_hours) + ':' + str(new_time_mins)

print(mins_added_to_time(60,'13:04'))