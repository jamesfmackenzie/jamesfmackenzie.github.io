

  

#blog/ideas #twitter/ideas

  

How to Snooze items in real Outlook

  

I wrote some VBA to do it and learned a bunch about Outlook properties along the way

  

Public Sub UpdateSnoozeDates()

  Dim mailboxFolder As Folder

  Set mailboxFolder = Application.Session.GetDefaultFolder(olFolderInbox).Parent

  Dim snoozedFolder As Folder

  Set snoozedFolder = mailboxFolder.Folders("Snoozed")

  Dim PropName As String

  'Snoozed Until

  PropName = "[http://schemas.microsoft.com/mapi/proptag/0x0F070040](http://schemas.microsoft.com/mapi/proptag/0x0F070040)"

  For i = 1 To snoozedFolder.Items.Count

    Dim oMail As Outlook.MailItem

    Dim myUserProperty As Outlook.UserProperty

    Dim PropertyValue As String

    Dim AdjustedPropertyValue As String

    Set oMail = snoozedFolder.Items(i)

    Set oPA = oMail.PropertyAccessor

    PropertyValue = oPA.GetProperty(PropName)

    AdjustedPropertyValue = DateAdd("h", -4, PropertyValue)

    Set myUserProperty = oMail.UserProperties.Add("Snooze Until", olDateTime, True)

    myUserProperty.Value = AdjustedPropertyValue

    oMail.Save

  Next i

End Sub



![[Pasted image 20250315231905.png]]

  

  

  

The MAPI property for Snoozed emails is 0x0F070040

It is UTC. You can use VBA to get it (code attached)

Current code will iterate everything in the Snoozed folder and then update those values onto a custom attribute (“Snooze Until”) which is visible in Outlook

Can be added as a Macro to the Ribbon or Quick Action toolbar and then launched on demand

In the longer run, consider:

1. Adding to the Outlook context menu (right click)
2. Auto-running on a schedule