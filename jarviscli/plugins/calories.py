from plugin import plugin


@plugin("calories")
class Calories:
    """
    Tells the recommended daily calorie intake, also recommends
    calories for weight add and loss.(Source 1)
    It is based on gender, age, height and weight.
    Uses the Miffin-St Jeor Equation as it is considered the
    most accurate when we don't know our body fat percentage(Source 2).
    Add gender(man/woman), age(15 - 80 recommended), metric height(cm),
    weight(kg), workout level(1-4). No decimal weight for now.
    Workout Levels:
        [1] Little or no exercise
        [2] Light 1-3 per week
        [3] Moderate 4-5 per week
        [4] Active daily exercise or physical job
    #Example: health calories woman 27 164 60 3
    ^Sources:
            1) https://en.wikipedia.org/wiki/Basal_metabolic_rate
            2) https://jandonline.org/article/S0002-8223(05)00149-5/fulltext
    """

    def __call__(self, jarvis, s):
        jarvis.say("Welcome!")
        info = input("Please enter the information about you following this order(gender age height(cms) weight(kg) workout level(1-4)): ").split()
        self.calories(jarvis, info)

    def calories(self, jarvis, strings):
        if len(strings) == 5:
            gender = strings[0].lower()
            age = int(strings[1])
            height = int(strings[2])
            weight = float(strings[3])
            level = int(strings[4])
        else:
            print("You wrote less or more arguments than it needed.")
            return None

        gender_no = 0
        if gender == "male" or gender == "man" or gender == "m":
            gender_no = 5
        elif gender == "female" or gender == 'woman' or gender == "f":
            gender_no = -161

        if gender_no != 0 and age > 14 and height > 0.0 and weight > 0.0 and level > 0 and level < 5:
            brm = int(float(10 * weight + 6.25 * height - 5 * age + gender_no) * self.exercise_level(level)*100)
            brm = float(brm)/100
            
            print("Daily caloric intake :    ", str(brm))
            print("Loss weight calories :    ", str(brm-500))
            print("Put on  weight calories : ", str(brm+500))
            return brm
        else:
            print("Please add correct input!")
            return None

    def exercise_level(self, level):
        multipliers = {1: 1.2, 2: 1.4, 3: 1.6, 4: 1.95}
        multiplier = multipliers.get(level, 1)
        return multiplier
