<?php
$successMessage = "";
$errorMessage = "";
$name = "";
$email = "";
$message = "";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = trim($_POST["name"] ?? "");
    $email = trim($_POST["email"] ?? "");
    $message = trim($_POST["message"] ?? "");

    if ($name === "" || $email === "" || $message === "") {
        $errorMessage = "Все поля должны быть заполнены.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errorMessage = "Введён некорректный email.";
    } else {
        $successMessage = "Сообщение успешно отправлено.";
        $name = "";
        $email = "";
        $message = "";
    }
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Форма обратной связи</title>
</head>
<body>
    <div id="feedback-status" name="feedback-status">
        <?php if ($successMessage): ?>
            <div id="success-message" name="success-message">
                <?= htmlspecialchars($successMessage) ?>
            </div>
        <?php endif; ?>
        <?php if ($errorMessage): ?>
            <div id="error-message" name="error-message">
                <?= htmlspecialchars($errorMessage) ?>
            </div>
        <?php endif; ?>
    </div>
    <form id="feedback-form" name="feedback-form" method="post">
        <div id="field-name-wrapper" name="field-name-wrapper">
            <label for="name-input" id="name-label">Имя:</label><br>
            <input type="text" id="name-input" name="name" value="<?= htmlspecialchars($name) ?>">
        </div>
        <br>
        <div id="field-email-wrapper" name="field-email-wrapper">
            <label for="email-input" id="email-label">Email:</label><br>
            <input type="text" id="email-input" name="email" value="<?= htmlspecialchars($email) ?>">
        </div>
        <br>
        <div id="field-message-wrapper" name="field-message-wrapper">
            <label for="message-textarea" id="message-label">Сообщение:</label><br>
            <textarea id="message-textarea" name="message" rows="5" cols="40"><?= htmlspecialchars($message) ?></textarea>
        </div>
        <br>
        <div id="submit-wrapper" name="submit-wrapper">
            <button type="submit" id="submit-button" name="submit-button">Отправить</button>
        </div>
    </form>
</body>
</html>
