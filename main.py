import requests
from urllib.parse import urlparse

def validate_url(url):
    """Valida se a URL fornecida é acessível e tem o formato correto."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def main():
    print("Bem-vindo ao Web Vulnerability Scanner!")
    
    # Solicita a URL ao usuário
    url = input("Por favor, insira a URL do site para escanear: ").strip()
    
    # Valida a URL
    if not validate_url(url):
        print("URL inválida. Certifique-se de incluir http:// ou https://")
        return
    
    # Verifica se a URL está acessível
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Erro ao acessar a URL: Status Code {response.status_code}")
            return
    except requests.RequestException as e:
        print(f"Erro ao conectar à URL: {e}")
        return
    
    print(f"Iniciando escaneamento de vulnerabilidades para: {url}")
    
    # Aqui é onde vamos chamar os módulos específicos
    # Exemplo:
    # sql_injection_scanner.scan(url)
    # xss_scanner.scan(url)
    # configuration_checker.scan(url)
    
    print("Escaneamento completo! Gerando relatório...")

    # Chama a função para gerar o relatório
    # report_generator.generate_report(results)

if __name__ == "__main__":
    main()
