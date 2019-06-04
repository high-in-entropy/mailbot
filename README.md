# mailbot
This is a mass marketing python mail bot with a huge mailing capacity.
Actually one can add as many emails in the `./emails/sender_emails.xlsx` as they want to,
to increase the bot's capacity.

Note that gmail has a limit of 200 emails per day per account. To be on a safer side bot assumes this figure to be 150. In other words, 
the bot's capacity is 150 times the number of emails in `./emails/sender_emails.xlsx`.

Edit the `./message/html.txt` and `./message/text.txt` with the email message that needs to be sent. Keep the content of text and html the same. Make sure to update both because in case if HTML message isn't rendered at the receiver's end, the text message of the same can be displayed.
Emails' Subject should be added to `./message/subject.txt`

Like what I do? Follow me on [Twitter](https://twitter.com/high_in_entropy) or connect with me on [LinkedIn](https://www.linkedin.com/in/viraj-mohile-70560b157/)!
