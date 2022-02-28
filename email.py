import win32com.client as w32

outlook = w32.Dispatch('outlook.application')

mail = outlook.CreateItem(0)
mail.To = 'jane.doe@outlook.com'
mail.Subject = 'my pythonic email'
mail.Body = 'Message body'
#mail.HTMLBody = 

# To attach a file to the email (optional):
attachment  = "C:\\Desktop\\MyAttachments\\Attachment.csv"
mail.Attachments.Add(attachment)

#mail.Display()
mail.Send()