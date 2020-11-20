	protected void Page_Load(object sender, EventArgs e)
        {
 
        }
 
        protected void Button1_Click(object sender, EventArgs e)
        {
            string name = TextBox1.Text.Trim();
            string pwd = TextBox2.Text.Trim();
            if(name=="")
            {
                Response.Write("<font color='red'>用户名不能为空</font>");
                TextBox1.Focus();//获取焦点，光标会位于此处
                return;
            }
            if(pwd=="")
            {
                Response.Write("<font color='red'>密码不能为空</font>");
                TextBox2.Focus();
                return ;
            }
            if(name=="winycg"&&pwd=="123")
            {
                Session["username"] = name;
                Response.Redirect("view.aspx");
            }
            else
            {
                Response.Write("<font color='red'>用户名或密码不正确</font>");
            }
        }

