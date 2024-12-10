import sys
import os
from dotenv import load_dotenv

load_dotenv(override=True)

ENV_INCOME_RATE = os.getenv("INCOME_RATE")
ENV_HOURS_RATE = os.getenv("HOURS_RATE")
ENV_PER_HOUR_VALUE = os.getenv("PER_HOUR_VALUE")


if len(sys.argv) >= 2:
    labor_hours = round(float(sys.argv[1]), 1)
    hours_rate = int(ENV_HOURS_RATE)
    income_rate = int(ENV_INCOME_RATE)
    per_hour_value = int(ENV_PER_HOUR_VALUE)

    total_hours = labor_hours + (labor_hours * (hours_rate / 100))
    labor_value = total_hours * per_hour_value
    total_value = labor_value + (labor_value * (income_rate / 100))

    print(f"\nHoras de trabalho: {labor_hours}\nTotal: R${round(total_value, 2)}")
else:
    print("ERROR: LABOR_HOURS ARGUMENT IS MISSING")
