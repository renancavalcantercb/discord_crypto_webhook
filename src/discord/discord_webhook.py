import requests
import json
from utils.utils import convert_datetime_to_string


def send_embed(webhook_url, crypto_data):
    brl_price = crypto_data.get("values")[-1]
    datetime = convert_datetime_to_string(crypto_data.get("timestamps")[-1])
    emoji_id = "964375496257306634"
    emoji_name = "bcoin"
    title_emoji = f"<:{emoji_name}:{emoji_id}>"

    embed = {
        "title": f"{title_emoji} Preço do BCOIN: R$ {brl_price:.5f}",
        "description": f"Informações do site CoinGecko às {datetime}",
        "color": 0x0099FF,
        "fields": [
            {"name": "Quantidade", "value": "1", "inline": True},
            {
                "name": "Valor em R$",
                "value": f"R$ {brl_price:.5f}",
                "inline": True,
            },
        ],
        "footer": {"text": "Feito por CuTGurArDiAn"},
    }

    headers = {"Content-Type": "application/json"}

    data = {"embeds": [embed], "username": "CryptoBot"}

    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

    if response.status_code == 204:
        print("Embed sent successfully")
    else:
        print(f"Error sending embed: {response.status_code}")
        print(response.text)
