import calendar 

def month(date):
    """
    Enter the date from which you want to extract the Month.
    This function takes the last two digits frome the entered data and transforded in month 
    """
    return calendar.month_name[(int(date[-2:]))] 

def year(date):
    """
    Enter the Date from which you want to extract the year.
    This function takes the first four digits frome the entered data 
    """
    return int(date[:4])  