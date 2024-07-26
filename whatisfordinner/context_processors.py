from datetime import datetime

# this allow calling of Current_date in the template without calling it in the view
def current_date(request): 
    return {
        'current_date': datetime.now().strftime("%B %d, %Y")
    }