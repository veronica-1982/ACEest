PROGRAMS = {
    "Fat Loss (FL)": {
        "workout": """Goal: Reduce body fat while preserving lean muscle

Weekly Plan:
Monday: Strength + Conditioning
- Back Squats (5x5)
- Push-ups (4x15)
- 15 min HIIT (treadmill sprints)

Tuesday: Cardio
- 30–40 min brisk walking or cycling

Wednesday: Full Body Circuit
- Deadlifts (4x8)
- Kettlebell swings (4x15)
- Burpees (3x20)

Thursday: Active Recovery
- Yoga / Stretching / Mobility work

Friday: Metabolic Conditioning
- 20 min AMRAP (Jump rope, lunges, push-ups)

Saturday: Light Cardio
- Swimming / jogging / sports

Sunday: Rest""",

        "diet": """Calorie Target: ~1800–2200 kcal

Breakfast:
- Oats with skim milk + boiled eggs
OR Idli with sambar

Lunch:
- Grilled chicken / paneer
- Brown rice / millet
- Vegetables

Snack:
- Fruits + green tea
- Nuts (almonds/walnuts)

Dinner:
- Fish / dal / paneer
- Roti or light carbs
- Salad

Guidelines:
- High protein intake
- Avoid sugar & fried foods
- Drink 3–4L water daily""",

        "color": "#e74c3c",
        "factor": 20
    },

    "Muscle Gain (MG)": {
        "workout": """Goal: Build muscle mass and strength

Weekly Plan:
Monday: Chest + Triceps
- Bench Press (5x5)
- Incline Dumbbell Press (4x10)
- Tricep Dips (3x12)

Tuesday: Back + Biceps
- Deadlift (5x5)
- Pull-ups (4x10)
- Barbell curls (3x12)

Wednesday: Rest / Light Cardio

Thursday: Legs
- Squats (5x5)
- Lunges (4x12)
- Leg press (4x10)

Friday: Shoulders
- Overhead press (5x5)
- Lateral raises (4x12)

Saturday: Full Body Pump
- Light weights + high reps

Sunday: Rest""",

        "diet": """Calorie Target: ~2800–3500 kcal

Breakfast:
- 4–5 eggs + oats + peanut butter

Lunch:
- Chicken / mutton / paneer
- White rice / biryani
- Vegetables

Snack:
- Banana shake / protein shake
- Dry fruits

Dinner:
- Heavy protein meal
- Rice / roti
- Curd

Guidelines:
- High protein (1.5–2g per kg body weight)
- Eat every 3–4 hours
- Focus on calorie surplus
- Strength training is key""",

        "color": "#2ecc71",
        "factor": 35
    },

    "Beginner (BG)": {
        "workout": """Goal: Build basic fitness and consistency

Weekly Plan:
Monday: Full Body
- Bodyweight squats (3x15)
- Push-ups (3x10)
- Plank (3x30 sec)

Wednesday: Light Cardio
- Walking / cycling (20–30 min)

Friday: Basic Strength
- Resistance band exercises
- Light dumbbells

Saturday: Fun Activity
- Sports / yoga / stretching

Sunday: Rest""",

        "diet": """Calorie Target: ~2000–2500 kcal

Breakfast:
- Idli / dosa + sambar
OR bread + eggs

Lunch:
- Rice + dal + vegetables
- Chicken / paneer optional

Snack:
- Fruits / peanuts

Dinner:
- Light meal (roti + sabzi)

Guidelines:
- Balanced nutrition
- Avoid junk food
- Stay hydrated
- Focus on consistency over intensity""",

        "color": "#3498db",
        "factor": 25
    }
}


def calculate_bmi(client):
    if not client.height or not client.weight:
        return None
    return round(client.weight / ((client.height / 100) ** 2), 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "Low risk"
    elif bmi < 25:
        return "Normal", "Healthy"
    elif bmi < 30:
        return "Overweight", "Moderate risk"
    else:
        return "Obese", "High risk"