from datetime import datetime

time = datetime.now()

result = datetime.strftime(time, "%Y-%m-%d")

print(result)