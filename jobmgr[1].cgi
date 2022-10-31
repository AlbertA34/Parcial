<HTML>
	
	<HEAD><TITLE>WebMO Login</TITLE>
		<LINK REL="shortcut icon" HREF="/demoserver/webmo/images/webmo.ico" />
		<LINK REL="stylesheet" TYPE="text/css" HREF="/demoserver/webmo/webmo.css?v=22.0.009e" />
		<META NAME="apple-itunes-app" CONTENT="app-id=797898095, affiliate-data=at=1l3v7Lw">
	</HEAD>
	
	<SCRIPT LANGAUGE="JavaScript">
		function detectCookies(form)
		{
			document.cookie = "testcookie=testing";
			if (document.cookie.indexOf("testcookie") == -1)
				alert("You must enable cookies in your browser in order to login.");				
		}
	</SCRIPT>
	
	<BODY ONLOAD="document.form.username.focus()">
		<H1>WebMO Login</H1>
		<H3>Version: 22.0.009e<BR>
		Computational Chemistry on the WWW<P>Username: guest<BR>Password: guest</H3>
		<H3></H3>
		<!--	22.0.009e,1140324,1667233963,3903	-->
		
		<FORM NAME="form" METHOD="POST">
			<TABLE CLASS="tframe">
				<TD><IMG SRC="/demoserver/webmo/images/login.png"></TD>
				<TD HEIGHT=189 WIDTH=192 VALIGN=CENTER>
					<TABLE CLASS="tabpage">
						<TR>
							<TD>Username</TD>
							<TD><INPUT TYPE="text" NAME="username"></TD>
						</TR>
						<TR>
							<TD>Password</TD>
							<TD><INPUT TYPE="password" NAME="password"></TD>
						</TR>
						<TR>
							<TD COLSPAN=2></TD>
						</TR>
						<TR>
							<TD COLSPAN=2><A ID="app_connect_link">Connect using WebMO app</A></TD>
						</TR>
					</TABLE>
				</TD>
			</TABLE>
			
			<P>
			<INPUT TYPE="submit" value="Login" ONCLICK="detectCookies(document.form)">
		</FORM>
		<P>
		<A HREF="https://www.webmo.net" TARGET="_blank"><IMG SRC="/demoserver/webmo/images/webmo.png" BORDER=0 STYLE="margin-bottom: 4px; margin-right: 4px"></A>
		<A HREF="https://itunes.apple.com/us/app/webmo/id797898095?mt=8&uo=4&at=1l3v7Lw" TARGET="_blank"><IMG SRC="/demoserver/webmo/images/apple_app_store.png" BORDER=0 STYLE="margin-bottom: 4px"></A>
		<A HREF="https://play.google.com/store/apps/details?id=net.webmo.android.moledit&utm_source=global_co&utm_medium=prtnr&utm_content=Mar2515&utm_campaign=PartBadge&pcampaignid=MKT-AC-global-none-all-co-pr-py-PartBadges-Oct1515-1" TARGET="_blank"><img height="45px" alt="Get it on Google Play" src="/demoserver/webmo/images/en-play-badge-border.png" STYLE="margin-bottom: 1px" /></A>
	</BODY>
	
	<SCRIPT LANGAUGE="JavaScript">
		var link = document.getElementById('app_connect_link');
		link.href = "webmoapp://localhost/config?url=" + window.location;
	</SCRIPT>
	
</HTML>
