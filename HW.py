from datetime import datetime

time_now = datetime.now().year
# years_sinc_birth_date = time_now - 2001
# days_sinc_birth_date = years_sinc_birth_date * 365
# hours_sinc_birth_date = days_sinc_birth_date * 24
# minutes_sinc_birth_date = hours_sinc_birth_date * 60
# seconds_sinc_birth_date = minutes_sinc_birth_date * 60
# print(seconds_sinc_birth_date)
seconds_sinc_birthdate = (time_now - 2001) * 365 * 24 * 60 * 60
years_sinc_birthdate = seconds_sinc_birthdate / 355 / 24 / 60 / 60
# print(int(years_sinc_birthdate))
print(seconds_sinc_birthdate // (365 * 24 * 60 * 60))     # division without floating point
