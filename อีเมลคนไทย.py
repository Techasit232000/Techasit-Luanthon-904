Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ("pub type Error = Box<dyn std::error::Error + Send + Sync>;
pub type Result<T> = std::result::Result<T, Error>;

use async_smtp::{
    ClientSecurity, Envelope, SendableEmail, SmtpClient, Transport,
};

async fn smtp_transport_simple() -> Result<()> {
    let email = SendableEmail::new(
        Envelope::new(
            Some("user@localhost".parse().unwrap()),
            vec!["root@localhost".parse().unwrap()],
        )?,
        "id",
        "Hello world",
    );

    // Create a client
    let mut smtp = SmtpClient::new("127.0.0.1:2525").await?.into_transport();

    // Connect and send the email.
    smtp.send(email).await?;

    Ok(())
}")
       
SyntaxError: EOL while scanning string literal
>>> (" EOL while scanning string literal")
' EOL while scanning string literal'
>>> 