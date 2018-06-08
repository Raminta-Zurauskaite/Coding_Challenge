package components;

    public ToDoList() {
        super(new BorderLayout());
 
        listModel = new DefaultListModel();
        listModel.addElement("Go to the grocery store");
        listModel.addElement("Clean the house");