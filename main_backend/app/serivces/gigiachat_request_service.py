import requests
import urllib3
import json
import spacy

from app import app

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def api_auth():
    auth_url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    auth_payload='scope=GIGACHAT_API_PERS'
    auth_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': f'{app.config["AI_API_RQUID"]}',
    'Authorization': f'Basic {app.config["AI_API_AUTHORIZATION"]}'
    }

    auth_response = requests.request("POST", auth_url, headers=auth_headers, data=auth_payload, verify=False)
    return auth_response.json()['access_token']

def api_text_generation(analyse_text: str, reference_text):

    nlp = spacy.load("xx_ent_wiki_sm")  
    doc = nlp(analyse_text)

    cleaned_text = analyse_text
    for ent in doc.ents:
        if ent.label_ in ['PERSON', 'DATE']:
            cleaned_text = cleaned_text.replace(ent.analyse_text, '')  
        access_token = api_auth()
        text_generation_url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

        text_ganaration_payload = json.dumps({
        "model": "GigaChat:latest",
        "messages": [
            {
            "role": "user",
            "content": f'От лица специалиста, расскажи о результатах анализа из первого текста - {cleaned_text} исходя из информации о значениях во втором - {reference_text}. расшифруй результаты таким образом, чтобы любой человек понял. В своём ответе не указывай, что ты опирался на какой-либо текст, а просто дай своё заключение'
            }
        ],
        "temperature": 0.5,
        "top_p": 0.1,
        "n": 1,
        "stream": False,
        "max_tokens": 1024,
        "repetition_penalty": 1
        })

        text_generation_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
        }

        text_generation_response = requests.request("POST", text_generation_url, headers=text_generation_headers, data=text_ganaration_payload, verify=False)

        print(text_generation_response.json()['choices'])
        return text_generation_response.json()['choices'][0]['message']['content']