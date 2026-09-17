"""Локальный сервер для 3D-галереи. Запуск: py -3 serve.py (открой http://localhost:8000).

Обычный `http.server` отдаёт .webp как application/octet-stream и без CORS-заголовков,
из-за чего загрузчик текстур A-Frame/three.js (crossOrigin='anonymous') бракует картинки.
Здесь чиним MIME-типы и добавляем Access-Control-Allow-Origin: *.
"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

class GalleryHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        '.webp': 'image/webp',
        '.mp4': 'video/mp4',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.mp3': 'audio/mpeg',
    }

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, *args):
        pass  # тихий режим

if __name__ == '__main__':
    srv = ThreadingHTTPServer(('127.0.0.1', 8000), GalleryHandler)
    print('Галерея: http://localhost:8000  (остановка: Ctrl+C)')
    srv.serve_forever()
