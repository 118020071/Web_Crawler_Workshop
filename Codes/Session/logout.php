<?php
session_start();
//  这种方法是将原来注册的某个变量销毁
// unset($_SESSION['admin']);
//  这种方法是销毁整个 Session 文件
session_destroy();
?>

<body>
    <p>
        你已经退出了，正在跳转至登录页面
    </p>
    <meta http-equiv="refresh" content="1;url=index.php">
</body>