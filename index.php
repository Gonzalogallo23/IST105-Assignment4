<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignment #4 - User Input</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; background-color:purple; }
        h1 { color: #333; }
        .form-container { width: 300px; margin: 0 auto; color:white; }
        .form-container input { width: 100%; padding: 10px; margin: 10px 0; }
        label {font-weight: bold; }
    </style>
</head>
<body>

<h1>Assignment #4</h1>

<div class="form-container">
    <form action="process.php" method="POST">
        <label for="x">Enter value for a:</label>
        <input type="number" id="a" name="a" required>

        <label for="y">Enter value for b:</label>
        <input type="number" id="b" name="b" required>

        <label for="z">Enter value for c:</label>
        <input type="number" id="c" name="c" required>

        <button type="submit" style="width: 100%; padding: 10px; background-color: #4CAF50; color: white; border: none;">Calculate</button>
    </form>
</div>

</body>
</html>
