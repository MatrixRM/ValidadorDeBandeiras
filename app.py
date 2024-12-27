import re

def validar_bandeira_cartao(numero_cartao):
    bandeiras = {
        'Visa': r'^4[0-9]{12}(?:[0-9]{3})?$',
        'MasterCard': r'^5[1-5][0-9]{14}$',
        'American Express': r'^3[47][0-9]{13}$',
        'Diners Club': r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
        'Discover': r'^6(?:011|5[0-9]{2})[0-9]{12}$',
        'JCB': r'^(?:2131|1800|35\d{3})\d{11}$'
    }

    for bandeira, padrao in bandeiras.items():
        if re.match(padrao, numero_cartao):
            return bandeira
    return 'Bandeira desconhecida'

# Exemplo de uso
numero_cartao = '373954175316618'
bandeira = validar_bandeira_cartao(numero_cartao)
print(f'Bandeira do cartão: {bandeira}')