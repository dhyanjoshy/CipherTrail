from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def game():
    return render_template('game.html')

@app.route('/rAcIp')
def index():
    return render_template('index.html')

@app.route('/show_user_id', methods=['POST'])
def show_user_id():
    user_id = request.form['user_id']
    user_clue = {
        "CT001":"In the heart of the fest's technological hub, where bytes converge and insights abound, lies a cornerstone of innovation. Follow the data trail to the laboratory where the future unfolds in ones and zeros. Nearby, where footsteps echo with the rhythm of discovery, the shoe rack stands sentinel. Amidst the footwear flurry, your clue awaits, a digital breadcrumb amidst the analog world.",
        "CT002":"In the heart of the fest's technological hub, where bytes converge and insights abound, lies a cornerstone of innovation. Follow the data trail to the laboratory where the future unfolds in ones and zeros. Nearby, where footsteps echo with the rhythm of discovery, the shoe rack stands sentinel. Amidst the footwear flurry, your clue awaits, a digital breadcrumb amidst the analog world.",
        "CT003":"In the heart of the fest's technological hub, where bytes converge and insights abound, lies a cornerstone of innovation. Follow the data trail to the laboratory where the future unfolds in ones and zeros. Nearby, where footsteps echo with the rhythm of discovery, the shoe rack stands sentinel. Amidst the footwear flurry, your clue awaits, a digital breadcrumb amidst the analog world.",
        "CT004":"In the heart of the fest's technological hub, where bytes converge and insights abound, lies a cornerstone of innovation. Follow the data trail to the laboratory where the future unfolds in ones and zeros. Nearby, where footsteps echo with the rhythm of discovery, the shoe rack stands sentinel. Amidst the footwear flurry, your clue awaits, a digital breadcrumb amidst the analog world.",
        "CT005":"As the final revelation of our grand event unfurls, heed this ultimate clue: Traverse the corridors of our campus, where innovation intertwines with mystery. Amidst the labyrinthine paths, discover the sanctum of Big Data Analytics. Crack the digital code, for within its depths lies the culmination of our journey—where insights merge with analytics, beckoning those bold enough to unlock its enigmatic embrace. Embark now, and let the pursuit of knowledge guide you to the pinnacle of discovery",
        "CT006":"In the heart of the fest's technological hub, where bytes converge and insights abound, lies a cornerstone of innovation. Follow the data trail to the laboratory where the future unfolds in ones and zeros. Nearby, where footsteps echo with the rhythm of discovery, the shoe rack stands sentinel. Amidst the footwear flurry, your clue awaits, a digital breadcrumb amidst the analog world.",
        "CT007":"In the heart of the fest's technological hub, where bytes converge and insights abound, lies a cornerstone of innovation. Follow the data trail to the laboratory where the future unfolds in ones and zeros. Nearby, where footsteps echo with the rhythm of discovery, the shoe rack stands sentinel. Amidst the footwear flurry, your clue awaits, a digital breadcrumb amidst the analog world.",
    }
    if user_id in user_clue:
        clue = user_clue[user_id]
    else:
        clue = "Check the User ID"
    return render_template('show_user_id1.html', clue=clue)

if __name__ == '__main__':
    app.run(debug=True)
