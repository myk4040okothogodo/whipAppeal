from .models import Account

@app.task
def toggle_account_status(Account):
  "This celery task sets the 'is_premium' flag of the account object to false in   the database after the account balance goes below 10 dollar"  
  Account.is_premium = False
  Account.save()
