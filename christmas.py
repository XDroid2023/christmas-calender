import datetime

# Define the advent calendar as a list of messages for each day
advent_calendar = [
    "🎄 December 1st: Put up your Christmas decorations!",
    "🎅 December 2nd: Watch your favorite Christmas movie.",
    "🍪 December 3rd: Bake some Christmas cookies.",
    "📜 December 4th: Write your Christmas cards.",
    "🛍️ December 5th: Do some Christmas shopping.",
    "🎶 December 6th: Listen to Christmas music.",
    "📚 December 7th: Read a Christmas story.",
    "🕯️ December 8th: Light a candle and relax.",
    "🌟 December 9th: Go stargazing and make a wish.",
    "🎁 December 10th: Wrap Christmas presents.",
    "📷 December 11th: Take a festive photo.",
    "🌺 December 12th: Make a Christmas wreath.",
    "🎨 December 13th: Create a holiday craft.",
    "🌌 December 14th: Go to a neighborhood full of Christmas lights.",
    "🍴 December 15th: Cook a special dinner.",
    "✉️ December 16th: Deliver Christmas cards to your neighbors.",
    "🎁 December 17th: Donate a gift to charity.",
    "🖋️ December 18th: Write a list of things you're grateful for.",
    "🚶 December 19th: Take a winter walk.",
    "🌰 December 20th: Roast chestnuts on an open fire.",
    "❄️ December 21st: Make paper snowflakes.",
    "🥂 December 22nd: Plan your Christmas Eve dinner.",
    "🎻 December 23rd: Attend a Christmas concert or event.",
    "🌟 December 24th: Spend time with loved ones and enjoy Christmas Eve."
]

# Function to display the activity for a given day
def get_activity(day):
    if 1 <= day <= len(advent_calendar):
        return advent_calendar[day-1]
    else:
        return "🎉 Merry Christmas! Enjoy your day!"

# Get today's date
today = datetime.date.today()

# Calculate day of December
if today.month == 12:
    activity = get_activity(today.day)
    print(activity)
else:
    print("It's not December yet! Wait for the festivities to begin.")
