<?php
//  表单提交后...
$posts = $_POST;
$DB = new mysqli("localhost", "visitor", "visit2000", "userpwd");
//  清除一些空白符号
foreach ($posts as $key => $value) {
    $posts[$key] = trim($value);
}
$password = md5($posts["password"]);
$username = $posts["username"]; 

echo $password;
echo $username;

$query = "SELECT `username` FROM `tier0` WHERE `password` = '$password' AND `username` = '$username'";
//  取得查询结果
$userInfo = $DB->query($query)->fetch_assoc()['username'];
echo($userInfo);

if (!empty($userInfo)) {
    //  当验证通过后，启动 Session
    session_start();
    //  注册登陆成功的 admin 变量，并赋值 true
    $_SESSION["admin"] = true;
    echo("你登录了");
    ?>
        <meta http-equiv="refresh" content="1;url=webpage1.php">
    <?php
} else {
    session_start();
    $_SESSION["admin"] = null;
    die("用户名密码错误");
}
?>