app = Flask(__name__, static_folder='public', static_url_path='')
# CORS(app)

# genai.configure(api_key='AIzaSyAhCLD7xS06LV2pSkKMEEo_uLE1K3wbDuE')
# model = genai.GenerativeModel('gemini-1.0-pro-latest')

# def serve_app():
#     return send_from_directory(app.static_folder, 'index.html')

# @app.route('/generate', methods=['POST'])