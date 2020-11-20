protected void Page_Load(object sender, EventArgs e)
        {
            if(Session["username"]==null)
            {
                Response.Write("<b><font color='red'>您不是合法用户！</font></b>");
                Response.Write("<p><a href='index.aspx'>进入主页面</a>");
            }
            else
            {
                Response.Write("<b>恭喜登陆成功</b>");
            }
        }

