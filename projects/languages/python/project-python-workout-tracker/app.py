class Workout():

    def __init__(self):
        self.workouts = []

    def add_workout(self,workout_dict):
        '''Add workout to a database IOT track exercise,
        number of reps and sets completed, and lbs'''
        sets = workout_dict.get('sets', 0)
        reps = workout_dict.get('reps', 0)
        weight = workout_dict.get('lbs', 0)

        total_reps = sets * reps
        total_weight = total_reps * weight

        return f'{workout_dict['name']}: total reps: {total_reps}, total weight: {total_weight}lbs'

    def sum_workout(self):
        pass
        
new_workout = Workout()
workout_dict = {'name':'hammer curls','reps':15,'sets':3,'lbs':30}
workout_dict1 = {'name':'bench press','reps':10,'sets':3,'lbs':135}

print(new_workout.add_workout(workout_dict))
print(new_workout.add_workout(workout_dict1))

print(new_workout.sum_workout())

