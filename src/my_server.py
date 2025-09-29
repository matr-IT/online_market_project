from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = 'localhost'
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа
        r = read_html('/Users/rybin/PycharmProjects/online_market_project/pages/contacts.html')
        self.wfile.write(r.encode('utf-8')) # Тело ответа


def read_html(current_file):
    """Функция чтения шаблона html"""
    with open(current_file, 'r', encoding="UTF-8") as f:
        result = f.read()
    return result


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Сервер запущен http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Сервер остановлен")
