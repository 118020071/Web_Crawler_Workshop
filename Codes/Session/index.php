<!DOCTYPE html>
<?php
session_start();
$_SESSION["admin"] = null;
?>
<head></head>

<body>
    <form action="init.php" method="post">
        <div class="imgcontainer">
          <img src="img_avatar2.png" alt="Avatar" class="avatar">
        </div>
      
        <div class="container">
          <label for="username"><b>Username</b></label>
          <input type="text" placeholder="Enter Username" name="username" required>
      
          <label for="password"><b>Password</b></label>
          <input type="password" placeholder="Enter Password" name="password" required>
      
          <button type="submit">Login</button>
        </div>
    </form>

    <div class="container" style="background-color:#f1f1f1">
        <form action="logout.php" method="post">
          <button type="button" class="cancelbtn">Cancel</button>
        </form>
        <span class="psw">Forgot <a href="#">password?</a></span>
    </div>
</body>