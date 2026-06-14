<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Панель управления ботом</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .button { padding: 10px 20px; margin: 5px; font-size: 16px; cursor: pointer; }
        .info { margin-top: 20px; padding: 10px; background: #f0f0f0; }
    </style>
</head>
<body>
    <h1>Панель управления Telegram‑ботом</h1>

    <div>
        <button class="button" onclick="sendMessage('Привет!')">Приветствие</button>
        <button class="button" onclick="sendMessage('Статус системы')">Статус</button>
        <button class="button" onclick="sendMessage('Экстренное уведомление!')">Аварийный сигнал</button>
    </div>

    <div class="info">
        <h3>Логи отправки:</h3>
        <div id="log"></div>
    </div>

    <script>
        function sendMessage(text) {
            fetch('http://localhost:5000/send_message', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: text })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('log').innerHTML +=
                    `<p><strong>${new Date().toLocaleTimeString()}:</strong> Отправлено: "${text}"</p>`;
            })
            .catch(error => {
                console.error('Ошибка:', error);
                alert('Ошибка отправки!');
            });
        }
    </script>
</body>
</html>
