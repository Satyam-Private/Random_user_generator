import requests 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random_user', methods=['GET', 'POST'])
def get_random_user():
    # If the request method is POST, proceed to fetch the random user
    if request.method == "POST":
        url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
        response = requests.get(url)
        data = response.json()
        if data.get("success") and "data" in data:
            user_data = data["data"]
            user_name = user_data["login"]["username"]
            user_country = user_data["location"]["country"]
            user_mail = user_data["email"]
            user_phone = user_data["phone"]
            user_photo = user_data["picture"]["large"]

            final_data = {
                "name": user_name,
                "country": user_country,
                "email": user_mail,
                "phone": user_phone,
                "photo": user_photo
            }
            return render_template('results.html', user=final_data)
        else:
            return "Failed to fetch data", 500
    # If the request is GET, you could redirect or inform the user to use the form.
    return "Please submit the form to get a random user."

if __name__ == "__main__":
    app.run(debug=True)
