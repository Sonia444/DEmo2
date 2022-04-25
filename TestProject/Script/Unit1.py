def Test1():
    #Runs the "Orders" tested application.
    TestedApps.Orders.Run()
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|New order...")
    #Clicks the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Click(38, 14)
    #Enters the text 'sonia' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("sonia")
    #Clicks the 'Street' object.
    Aliases.Orders.OrderForm.Group.Street.Click(9, 12)
    #Enters the text 'str1' in the 'Street' text editor.
    Aliases.Orders.OrderForm.Group.Street.SetText("str1")
    #Clicks the 'City' object.
    Aliases.Orders.OrderForm.Group.City.Click(26, 7)
    #Enters '[Caps]' in the 'City' object.
    Aliases.Orders.OrderForm.Group.City.Keys("[Caps]")
    #Enters the text 'H' in the 'City' text editor.
    Aliases.Orders.OrderForm.Group.City.SetText("H")
    #Enters '[Caps]' in the 'City' object.
    Aliases.Orders.OrderForm.Group.City.Keys("[Caps]")
    #Enters the text 'Hyd' in the 'City' text editor.
    Aliases.Orders.OrderForm.Group.City.SetText("Hyd")
    #Clicks the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Click(100, 3)
    #Enters the text 'ap' in the 'State' text editor.
    Aliases.Orders.OrderForm.Group.State.SetText("ap")
    #Clicks the 'Zip' object.
    Aliases.Orders.OrderForm.Group.Zip.Click(74, 14)
    #Enters the text '5635617' in the 'Zip' text editor.
    Aliases.Orders.OrderForm.Group.Zip.SetText("5635617")
    #Clicks the 'CardNo' object.
    Aliases.Orders.OrderForm.Group.CardNo.Click(106, 10)
    #Enters the text '76467898' in the 'CardNo' text editor.
    Aliases.Orders.OrderForm.Group.CardNo.SetText("76467898")
    #Clicks the 'ButtonOK' button.
    Aliases.Orders.OrderForm.ButtonOK.ClickButton()
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|New order...")
    #Clicks the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Click(25, 14)
    #Enters '[Caps]' in the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Keys("[Caps]")
    #Enters the text 'S' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("S")
    #Enters '[Caps]' in the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Keys("[Caps]")
    #Enters the text 'Si' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("Si")
    #Clicks the 'Street' object.
    Aliases.Orders.OrderForm.Group.Street.Click(31, 11)
    #Enters the text 'st1' in the 'Street' text editor.
    Aliases.Orders.OrderForm.Group.Street.SetText("st1")
    #Clicks the 'City' object.
    Aliases.Orders.OrderForm.Group.City.Click(58, 11)
    #Enters the text 'tpd' in the 'City' text editor.
    Aliases.Orders.OrderForm.Group.City.SetText("tpd")
    #Clicks the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Click(103, 8)
    #Enters the text 'ts' in the 'State' text editor.
    Aliases.Orders.OrderForm.Group.State.SetText("ts")
    #Clicks the 'Zip' object.
    Aliases.Orders.OrderForm.Group.Zip.Click(19, 12)
    #Enters the text '54674' in the 'Zip' text editor.
    Aliases.Orders.OrderForm.Group.Zip.SetText("54674")
    #Clicks the 'CardNo' object.
    Aliases.Orders.OrderForm.Group.CardNo.Click(138, 16)
    #Enters the text '7656589' in the 'CardNo' text editor.
    Aliases.Orders.OrderForm.Group.CardNo.SetText("7656589")
    #Clicks the 'ButtonOK' button.
    Aliases.Orders.OrderForm.ButtonOK.ClickButton()
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|Edit order...")
    #Selects the 'FamilyAlbum' item of the 'ProductNames' combo box.
    Aliases.Orders.OrderForm.Group.ProductNames.ClickItem("FamilyAlbum")
    #Clicks the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Click(70, 5)
    #Enters the text 'parimi' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("parimi")
    #Clicks the 'ButtonOK' button.
    Aliases.Orders.OrderForm.ButtonOK.ClickButton()
    #Double-clicks the 'MyMoney' subitem of the 'sonia' item of the 'OrdersView' list view.
    Aliases.Orders.MainForm.OrdersView.DblClickItem("sonia", "MyMoney")
    #Clicks the 'ButtonCancel' button.
    Aliases.Orders.OrderForm.ButtonCancel.ClickButton()
    #Double-clicks the 'FamilyAlbum' subitem of the 'parimi' item of the 'OrdersView' list view.
    Aliases.Orders.MainForm.OrdersView.DblClickItem("parimi", "FamilyAlbum")
    #Clicks the 'ButtonCancel' button.
    Aliases.Orders.OrderForm.ButtonCancel.ClickButton()
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|Delete order")
    #Clicks the 'btnYes' button.
    Aliases.Orders.dlgConfirmation.btnYes.ClickButton()
    #Closes the 'MainForm' window.
    Aliases.Orders.MainForm.Close()
    #Clicks the 'btnNo' button.
    Aliases.Orders.dlgConfirmation.btnNo.ClickButton()
