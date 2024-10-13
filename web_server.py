from flask import Flask, request, jsonify, render_template, session
from flask_session import Session
from flask_cors import CORS, cross_origin
from scraper import main, get_body_content, clean_body_content
from parser import get_llm_result

app = Flask(__name__)
## Custom session for storing large content
app.secret_key = "jahidllm"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
CORS(app, origins="*")

Session(app)


@app.route('/scraper', methods=['POST'])
async def scrape():
    try:
        url = request.json.get('url')
        print(request.json)
        content = await main(url)
        body_content = get_body_content(content)
        cleaned_content = clean_body_content(body_content)
        session['content'] = cleaned_content
        return jsonify({"content": cleaned_content})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/parse', methods=['POST'])
def parse_content():
    try:
        user_prompt = request.json.get('prompt')
        print(user_prompt)
        content = session.get('content')

        if content:
            result = get_llm_result(content, user_prompt)
            session.pop('content')
            return jsonify({"result": result})
        return jsonify({"error": "No content to parse"})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
